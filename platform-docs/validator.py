"""Validation for Monday.com generated configurations.

Validates board schemas and automation recipes before deployment.
Called by the Monday parser and usable standalone.
"""

from pathlib import Path
import json

from logger_config import get_logger

logger = get_logger("platforms.monday.validator")

# Column types supported by Monday.com GraphQL API
VALID_COLUMN_TYPES = {
    "auto_number", "button", "checkbox", "color_picker",
    "connect_boards", "country", "creation_log", "date", "dependency",
    "doc", "dropdown", "email", "file", "formula", "hour",
    "item_id", "last_updated", "link", "location", "long_text",
    "mirror", "name", "numbers", "people", "phone",
    "progress_tracking", "rating", "status", "subitems",
    "tags", "text", "time_tracking", "timeline", "vote",
    "week", "world_clock",
}

# Column types that require options
COLUMNS_REQUIRING_OPTIONS = {"dropdown", "status"}

# Column types that must NOT have options
COLUMNS_WITHOUT_OPTIONS = {"text", "date", "numbers", "long_text", "name", "people"}

# Valid trigger types for automations
VALID_TRIGGER_TYPES = {
    "item_created", "column_changed", "date_arrived",
    "webhook_received", "form_submitted", "chat_message",
    "schedule", "button_clicked",
}

# Valid action types for automations
VALID_ACTION_TYPES = {
    "create_item", "change_column_value", "move_item_to_group",
    "notify_user", "send_webhook", "assign_person",
}


def validate_board_schema(data: dict) -> list[str]:
    """Validate a Monday.com board schema dict.

    Returns list of error strings. Empty list means valid.
    """
    errors = []

    name = data.get("name", data.get("board", {}).get("name", ""))
    if not name:
        errors.append("Board is missing 'name' field")
    else:
        logger.debug("Validating board schema: name=%s", name)

    # Columns validation
    columns = data.get("columns", [])
    if not isinstance(columns, list):
        errors.append("'columns' must be an array")
        return errors

    if len(columns) == 0:
        errors.append("Board has no columns — at minimum a 'name' column is required")

    column_ids: set[str] = set()
    column_names: set[str] = set()

    for i, col in enumerate(columns):
        if not isinstance(col, dict):
            errors.append(f"Column {i}: must be an object, got {type(col).__name__}")
            continue

        col_id = col.get("id", col.get("column_id", f"col_{i}"))
        col_name = col.get("name", col.get("title", ""))
        col_type = col.get("type", "").lower()
        prefix = f"Column '{col_name}' ({col_id[:12]}...)"

        # ID uniqueness
        if col_id in column_ids:
            errors.append(f"{prefix}: duplicate ID")
        column_ids.add(col_id)

        # Name uniqueness
        if col_name and col_name in column_names:
            errors.append(f"{prefix}: duplicate name")
        if col_name:
            column_names.add(col_name)

        # Valid type
        if not col_type:
            errors.append(f"{prefix}: missing 'type' field")
        elif col_type not in VALID_COLUMN_TYPES:
            errors.append(
                f"{prefix}: invalid type '{col_type}'. "
                f"Must be one of {len(VALID_COLUMN_TYPES)} supported column types"
            )

        # Option value validation for dropdown columns
        if col_type == "dropdown":
            options = col.get("options", col.get("values", []))
            if not options:
                errors.append(f"{prefix}: dropdown column has no options")
            for j, opt in enumerate(options):
                if not isinstance(opt, dict):
                    errors.append(
                        f"{prefix}: option {j} must be an object, got {type(opt).__name__}"
                    )
                    continue
                value = opt.get("value", opt.get("name", ""))
                if value and not _is_valid_option_value(value):
                    errors.append(
                        f"{prefix}: option value '{value}' contains invalid "
                        "characters. Only letters, numbers, dashes, underscores allowed."
                    )
        elif col_type in COLUMNS_WITHOUT_OPTIONS:
            if "options" in col or "values" in col:
                logger.debug(
                    "%s: type '%s' should not have options — ignoring",
                    prefix,
                    col_type,
                )

    # Groups validation (optional but check structure)
    groups = data.get("groups", [])
    if not isinstance(groups, list):
        errors.append("'groups' must be an array")

    group_ids: set[str] = set()
    for i, group in enumerate(groups):
        if not isinstance(group, dict):
            errors.append(f"Group {i}: must be an object")
            continue
        gid = group.get("id", str(i))
        if gid in group_ids:
            errors.append(f"Group {i}: duplicate ID '{gid}'")
        group_ids.add(gid)

    logger.info(
        "Board validation: name=%s columns=%d groups=%d errors=%d",
        name,
        len(columns),
        len(groups),
        len(errors),
    )

    return errors


def validate_automation_recipes(data: dict) -> list[str]:
    """Validate automation recipes.

    Returns list of error strings. Empty list means valid.
    """
    errors = []

    automations = data.get("automations", data.get("recipes", []))
    if not isinstance(automations, list):
        errors.append("'automations' must be an array")
        return errors

    # Get column IDs for reference checking
    columns = data.get("columns", [])
    column_ids = {
        c.get("id", c.get("column_id", ""))
        for c in columns
        if isinstance(c, dict)
    }

    for i, recipe in enumerate(automations):
        if not isinstance(recipe, dict):
            errors.append(f"Automation {i}: must be an object")
            continue

        name = recipe.get("name", f"automation_{i}")
        trigger_type = recipe.get("trigger_type", "").lower()
        action_type = recipe.get("action_type", "").lower()
        prefix = f"Automation '{name}'"

        # Valid trigger type
        if trigger_type and trigger_type not in VALID_TRIGGER_TYPES:
            errors.append(
                f"{prefix}: invalid trigger type '{trigger_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_TRIGGER_TYPES))}"
            )

        # Valid action type
        if action_type and action_type not in VALID_ACTION_TYPES:
            errors.append(
                f"{prefix}: invalid action type '{action_type}'. "
                f"Must be one of: {', '.join(sorted(VALID_ACTION_TYPES))}"
            )

        # Column reference checks in trigger config
        trigger_config = recipe.get("trigger_config", recipe.get("trigger", {}))
        if isinstance(trigger_config, dict):
            trigger_col = trigger_config.get("column_id", "")
            if trigger_col and column_ids and trigger_col not in column_ids:
                errors.append(
                    f"{prefix}: trigger references unknown column '{trigger_col}'"
                )

        # Column reference checks in action config
        action_config = recipe.get("action_config", recipe.get("action", {}))
        if isinstance(action_config, dict):
            action_col = action_config.get("column_id", "")
            if action_col and column_ids and action_col not in column_ids:
                errors.append(
                    f"{prefix}: action references unknown column '{action_col}'"
                )

    logger.info(
        "Automation validation: recipes=%d errors=%d",
        len(automations),
        len(errors),
    )

    return errors


def validate_agent_config(data: dict) -> list[str]:
    """Validate an AI agent configuration for Monday.com.

    Returns list of error strings. Empty list means valid.
    """
    errors = []

    name = data.get("name", "")
    provider = data.get("provider", "").lower()

    if not name:
        errors.append("Agent config is missing 'name' field")

    if not provider:
        errors.append("Agent config is missing 'provider' field")
    elif provider not in {"managed_claude", "managed_gpt", "custom_webhook", "sidekick_tool"}:
        errors.append(
            f"Agent provider '{provider}' is not recognized. "
            "Valid: managed_claude, managed_gpt, custom_webhook, sidekick_tool"
        )

    if provider == "managed_claude" or provider == "managed_gpt":
        if "model" not in data.get("config", {}):
            errors.append(
                f"Managed provider '{provider}' requires a 'model' in config"
            )

    if provider == "custom_webhook":
        if "callback_url" not in data.get("config", {}):
            errors.append(
                "Custom webhook agent requires 'callback_url' in config"
            )

    logger.info(
        "Agent validation: name=%s provider=%s errors=%d",
        name,
        provider,
        len(errors),
    )

    return errors


def validate_monday_dict(data: dict) -> list[str]:
    """Validate any Monday.com configuration dict.

    Auto-detects type and runs the appropriate validator.
    Returns list of error strings. Empty list means valid.
    """
    errors = []

    # Detect type
    has_columns = "columns" in data and isinstance(data.get("columns"), list)
    has_automations = "automations" in data and isinstance(data.get("automations"), list)
    has_agent = "provider" in data and "name" in data

    if has_columns or has_automations:
        board_errors = validate_board_schema(data)
        errors.extend(board_errors)

    if has_automations:
        auto_errors = validate_automation_recipes(data)
        errors.extend(auto_errors)

    if has_agent and not has_columns:
        agent_errors = validate_agent_config(data)
        errors.extend(agent_errors)

    if not errors and not has_columns and not has_agent:
        errors.append(
            "Unrecognized config format — expected board schema (columns), "
            "automation recipes, or agent config (provider + name)"
        )

    logger.info(
        "validate_monday_dict: type=%s errors=%d",
        "board" if has_columns else ("agent" if has_agent else "unknown"),
        len(errors),
    )

    return errors


def validate_monday_json(json_path: Path) -> list[str]:
    """Validate a Monday.com configuration JSON file on disk.

    Returns list of error strings. Empty list means valid.
    """
    try:
        with open(json_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in %s: %s", json_path.name, e)
        return [f"Invalid JSON: {e}"]
    except FileNotFoundError:
        logger.error("File not found: %s", json_path)
        return [f"File not found: {json_path}"]

    return validate_monday_dict(data)


def format_validation_report(errors: list[str], source: str) -> str:
    """Format validation results as a readable report."""
    if not errors:
        return f"Validation PASSED: {source} — no errors found."

    lines = [
        f"Validation FAILED: {source} — {len(errors)} error(s):",
        "",
    ]
    for i, err in enumerate(errors, 1):
        lines.append(f"  {i}. {err}")

    return "\n".join(lines)


def _is_valid_option_value(value: str) -> bool:
    """Check if a dropdown option value follows Monday.com constraints."""
    import re
    return bool(re.match(r"^[a-zA-Z0-9\-_]+$", value))
