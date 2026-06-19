# Monday.com Forms

## Overview

Monday.com WorkForms capture structured data directly into a board. Every form submission creates an item on a backing board. Forms are managed via Platform MCP — there is no direct GraphQL API equivalent.

## Form Workflow

```
1. create_form            → Get formToken + board_id
2. form_questions_editor  → Add/update/delete questions
3. update_form            → Configure title, appearance, features, accessibility
4. get_form               → Inspect current form state
5. create_form_submission → Submit a response
```

## create_form

Creates a new WorkForm and simultaneously creates a backing board in the specified workspace.

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| destination_workspace_id | string | Yes | Workspace for form + backing board |
| destination_name | string | No | Custom name for backing board |
| board_kind | string | No | private, public, or share |
| destination_folder_id | string | No | Existing folder ID |
| destination_folder_name | string | No | New folder name |
| board_owner_ids | array | No | User IDs as board owners |
| board_owner_team_ids | array | No | Team IDs as board owners |
| board_subscriber_ids | array | No | User IDs for notifications |
| board_subscriber_teams_ids | array | No | Team IDs for notifications |

Returns: `formToken` and `board_id`. The form is immediately active.

## form_questions_editor

Add, update, or delete individual questions. Each call performs exactly one operation on one question.

### Supported Question Types (23 total)
`Boolean`, `ConnectedBoards`, `Country`, `DISPLAY_TEXT`, `Date`, `DateRange`, `Email`, `File`, `HOUR`, `Link`, `Location`, `LongText`, `MultiSelect`, `Name`, `Number`, `PAGE_BLOCK`, `People`, `Phone`, `Rating`, `ShortText`, `Signature`, `SingleSelect`, `Subitems`, `Updates`

### Parameters

| Parameter | Type | Required | Purpose |
|-----------|------|----------|---------|
| action | string | Yes | create, update, or delete |
| formToken | string | Yes | The form identifier |
| questionId | string | update/delete | Which question to modify |
| question | object | create/update | Question definition |

### question Object Fields

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| type | string | Yes | One of 23 types; immutable after creation |
| title | string | create | Question text shown to respondents |
| description | string | No | Help text beneath the question |
| visible | boolean | No | Defaults to true |
| required | boolean | No | Whether a response is mandatory |
| insert_after_question_id | string/null | No | Position; null = first position |
| page_block_id | string/null | No | Group within a page block |
| options | array | select types | [{label, value, visible}] |
| settings | object | No | Type-specific settings |
| show_if_rules | object | No | Conditional visibility (OR logic only) |

### Critical Rules
- Type is immutable after creation — always include existing type on updates
- For SingleSelect/MultiSelect updates, include every option you want to keep — omitted options are deleted
- Use get_form before updating select questions to see existing options

## update_form

Modifies form configuration via action-based calls.

| Parameter | Type | Required | Notes |
|-----------|------|----------|-------|
| formToken | string | Yes | The form identifier |
| action | string | Yes | Which operation to perform |
| form | object | Conditional | Patch semantics — only include fields to change |
| formPassword | string | Conditional | For setFormPassword |
| tag | object | Conditional | For tag CRUD |

### Supported Actions

| Action | Fields | Purpose |
|--------|--------|---------|
| activate | none | Make form publicly accessible |
| deactivate | none | Stop accepting responses |
| updateFormHeader | form.title, form.description | Title and description |
| updateAppearance | form.appearance | Background, layout, font, colors, branding |
| updateAccessibility | form.accessibility | Language, logo alt text |
| updateFeatures | form.features | Submission behavior, password, response limit, close date |
| updateQuestionOrder | form.questions | Must include all existing question IDs |
| setFormPassword | formPassword | Enable password protection |
| shortenFormUrl | none | Generate wkf.ms short URL |
| createTag | tag.name, tag.value | Add routing tag |
| updateTag | tag.id, tag.value | Update tag value |
| deleteTag | tag.id | Remove tag |

## get_form

Returns the complete form structure: all questions (IDs, types, options, conditional logic), appearance settings, feature flags, accessibility settings, and tags.

| Parameter | Type | Required |
|-----------|------|----------|
| formToken | string | Yes |

The formToken is extracted from the form URL: `https://forms.monday.com/forms/{formToken}?r=use1`

## create_form_submission

Submits a response to the form. Always call get_form first to retrieve the correct question IDs — especially for select-type questions.

Refer to get_form output for the expected question ID format for each question type.

## Intake Form Pattern (PMO Use Case)

For a PMO intake form, the typical structure:

1. Create form with `create_form` → get formToken
2. Add questions via `form_questions_editor`:
   - Name (ShortText) — Project request title
   - Description (LongText) — What's being requested
   - Department (SingleSelect) — IT, Operations, HR
   - Priority (SingleSelect) — High, Medium, Low
   - Requested By (People) — Who is asking
   - Estimated Budget (Number) — Dollar amount
   - Timeline (Date) — When needed
   - Scope Notes (LongText) — Additional context
3. Configure via `update_form` — title, description, appearance
4. Each submission creates an item on the Intake board
