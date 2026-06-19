# Monday.com Native AI Features (AI Columns)

## Overview

AI columns automate text analysis, categorization, translation, and content generation directly within monday.com boards. Each AI column is assigned a specific "block type" that determines what the AI does and which source columns it reads from.

Available in API version `2026-10` and later. Required scope: `boards:write`.

## AI Block Types (8)

### 1. Categorize (`configure_categorize_ai_column`)

Assigns labels/categories based on content analysis. AI picks from the target column's **existing labels** (must be status or dropdown column).

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target status/dropdown column |
| source_type | Yes | item_name, thread, column, or emails_and_activities |
| source_column_id | Conditional | Required when source_type is column |
| additional_instructions | No | Max 3000 chars; custom categorization rules |

Use case: Auto-categorize incoming project requests into departments (IT, Operations, HR) based on the request description.

### 2. Summarize (`configure_summarize_ai_column`)

Generates concise summaries from input text. Target must be text or long_text column.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target text/long_text column |
| source_type | Yes | item_name, thread, or column |
| source_column_id | Conditional | Required when source_type is column |

Use case: Auto-summarize lengthy project request descriptions into a one-line executive summary.

### 3. Translate (`configure_translate_ai_column`)

Translates text into a target language. Target must be text or long_text column.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target text/long_text column |
| source_type | Yes | item_name or column |
| source_column_id | Conditional | Required when source_type is column |
| target_language | Yes | One of 22 supported languages |

Supported languages: English, Spanish, French, German, Hebrew, Chinese, Korean, Arabic, Bengali, Danish, Dutch, Hindi, Indonesian, Italian, Japanese, Norwegian, Polish, Portuguese, Russian, Swedish, Thai, Turkish, Vietnamese.

### 4. Improve Text (`configure_improve_text_ai_column`)

Rewrites or enhances text quality. Target must be text or long_text column.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target text/long_text column |
| source_type | Yes | item_name, thread, or column |
| source_column_id | Conditional | Required when source_type is column |
| tone | No | empathic, promotional, confident, professional, natural, casual, friendly, same |
| length | No | same, shorter, longer |
| refinement_type | No | minimal_changes, moderate_changes, high_creativity |

### 5. Extract (`configure_extract_ai_column`)

Extracts structured information from text. Target can be text, long_text, date, email, phone, or link column.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target column |
| source_type | Yes | item_name or column |
| source_column_id | Conditional | Required when source_type is column |
| entity_type | Yes | 12 entity types (see below) |
| custom_instructions | Conditional | Required when entity_type is custom; max 3000 chars |

Entity types: `email_address`, `first_name`, `last_name`, `phone_number`, `company_name`, `domain_name`, `url`, `date`, `time`, `year`, `custom`

### 6. Open Block (`configure_open_block_ai_column`)

Flexible, general-purpose block for custom AI logic. Target can be text, long_text, numbers, date, status, or dropdown.

Uses inline `{pulse.column_id}` references instead of `source_type`/`source_column_id`. Also supports `{pulse.name}` for item name and `{pulse.subitem.column_id}` for subitem columns.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target column |
| ai_query | Yes | Natural language description of what to do; max 3000 chars |

Example ai_query: "Based on the priority ({pulse.priority}) and estimated budget ({pulse.budget}), recommend whether to approve or reject this project request."

### 7. Write Me (`configure_write_me_ai_column`)

Generates new text content from a prompt. Target can be text, long_text, or doc.

Also uses inline `{pulse.column_id}` references — no `source_type`/`source_column_id`.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target text/long_text/doc column |
| ai_query | Yes | What content to generate; max 3000 chars |
| tone | Yes | empathic, promotional, confident, professional, natural, casual, friendly, same |
| length | No | sentence, paragraph, brief, in_depth |

### 8. Person Assignment (`configure_person_assignment_ai_column`)

Assigns a person based on rules or context. Target must be a people column.

| Parameter | Required | Description |
|-----------|----------|-------------|
| board_id | Yes | Board identifier |
| column_id | Yes | Target people column |
| source_type | Yes | item_name, thread, or column |
| source_column_id | Conditional | Required when source_type is column |
| groups | Yes | Stringified JSON array of available people/team IDs |

All configure mutations accept `extra_settings: {run_backfill: Boolean}` — when true (default), AI applies to up to 200 existing items.

## Removing AI

```graphql
mutation {
  remove_ai_from_column(
    board_id: 1234567890
    column_id: "ai_categorize"
  ) {
    column_id
    success
  }
}
```

## Key Error Codes

| Code | Meaning |
|------|---------|
| INVALID_COLUMN_ID | column_id doesn't exist |
| INVALID_COLUMN_TYPE | Column type incompatible with block |
| SELF_REFERENCING_COLUMN | source_column_id equals column_id |
| MISSING_SOURCE_COLUMN_ID | source_type is column but no source_column_id |
| MISSING_CUSTOM_INSTRUCTIONS | entity_type is custom but no custom_instructions |
| INVALID_COLUMN_REFERENCE | {pulse.column_id} reference invalid |
| QUERY_TOO_LONG | ai_query > 3000 chars |
| INSTRUCTIONS_TOO_LONG | additional_instructions > 3000 chars |

## PMO Intake Automation Pattern

For Pepper's vague request problem:

```
1. Categorize AI Column → reads request description, assigns to department dropdown
   - source_type: column (long_text description)
   - target: Department (dropdown with IT, Operations, HR)
   
2. Summarize AI Column → reads request description, writes executive summary
   - source_type: column (long_text description)
   - target: Executive Summary (long_text)

3. Extract AI Column → reads request description, extracts dates
   - source_type: column (long_text description)
   - target: Requested Deadline (date)
   - entity_type: date

4. Write Me AI Column → generates approval recommendation
   - ai_query: "Review project {pulse.name} — scope: {pulse.description}. 
     Based on department {pulse.department}, priority {pulse.priority}, 
     and budget {pulse.budget}, provide a brief approval recommendation."
```

The Categorize + Summarize combination processes unstructured intake forms into structured, categorized, summarized board items — solving Pepper's "messy" request problem.
