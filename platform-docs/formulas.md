# Monday.com Formula Column

## Overview

The formula column calculates values using mathematical expressions, text functions, logical operations, and references to other columns. Formulas are computed server-side. Read and create only — no update, clear, or filter via API.

**Column type:** `formula`
**Implementation type:** `FormulaValue`

## Reading Formula Values

The computed result is returned in `display_value`. The `text` and `value` fields return empty/null.

```graphql
query {
  items(ids: [1234567890]) {
    column_values {
      ... on FormulaValue {
        id
        display_value
        type
        column { title }
      }
    }
  }
}
```

### Rate Limits
- Up to 10,000 formula values per minute
- Maximum 5 formula columns per request
- Does not support formulas referencing mirror or connect boards columns

## Creating a Formula Column

Use generic `create_column` with `column_type: formula`:

```graphql
mutation {
  create_column(
    board_id: 1234567890
    title: "SLA Status"
    column_type: formula
    defaults: "{\"settings\":{\"formula\":\"IF(DAYS({date_submitted}, TODAY()) > 5, \\\"BREACHED\\\", \\\"ON TRACK\\\")\"}}"
  ) {
    id
    title
    type
    settings
  }
}
```

The `defaults` argument is a JSON string with this structure:
```json
{"settings": {"formula": "expression using {column_id} references"}}
```

Column references use column IDs in curly braces: `{column_id}`. Example: `{numeric_col} * {rate_col}`

If you omit `defaults` or pass an empty formula, the column is created without a formula expression — it must be configured manually in the UI.

## Column References

Always use column IDs (not titles) wrapped in curly braces:
- `{numeric_col}` — references a Numbers column
- `{status_col}` — references a Status column
- `{text_col}` — references a Text column

Find column IDs via: `query { boards(ids: X) { columns { id title } } }`

Literal values can be used directly: `{numbers_col} + 5`, `"Text " & {text_col}`

## Formula Functions Reference

### Math Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| SUM | `SUM({col1}, {col2}, ...)` | Sum of values |
| AVERAGE | `AVERAGE({col1}, {col2}, ...)` | Average of values |
| MIN | `MIN({col1}, {col2}, ...)` | Minimum value |
| MAX | `MAX({col1}, {col2}, ...)` | Maximum value |
| ROUND | `ROUND({col}, N)` | Round to N decimal places |
| ROUNDUP | `ROUNDUP({col}, N)` | Round up to N decimals |
| ROUNDDOWN | `ROUNDDOWN({col}, N)` | Round down to N decimals |
| ABS | `ABS({col})` | Absolute value |
| POWER | `POWER({col}, N)` | Raise to power N |
| SQRT | `SQRT({col})` | Square root |
| MOD | `MOD({col1}, {col2})` | Remainder after division |

### Arithmetic Operators
`+`, `-`, `*`, `/`, `^` (exponent)

### Logical Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| IF | `IF(condition, value_if_true, value_if_false)` | Conditional logic |
| AND | `AND(cond1, cond2, ...)` | All conditions true |
| OR | `OR(cond1, cond2, ...)` | Any condition true |
| NOT | `NOT(condition)` | Negation |
| IFBLANK | `IFBLANK({col}, value_if_blank, value_if_not)` | Handle empty values |
| SWITCH | `SWITCH({col}, val1, result1, val2, result2, ..., default)` | Multi-condition |

### Comparison Operators
`=`, `<>`, `>`, `<`, `>=`, `<=`

### Date Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| TODAY | `TODAY()` | Current date |
| NOW | `NOW()` | Current date and time |
| DAYS | `DAYS({date1}, {date2})` | Days between two dates |
| YEAR | `YEAR({date})` | Extract year |
| MONTH | `MONTH({date})` | Extract month (1-12) |
| DAY | `DAY({date})` | Extract day of month |
| WEEKDAY | `WEEKDAY({date})` | Day of week (1-7) |
| WEEKNUM | `WEEKNUM({date})` | Week number |
| ADD_DAYS | `ADD_DAYS({date}, N)` | Add N days |
| ADD_MONTHS | `ADD_MONTHS({date}, N)` | Add N months |
| ADD_YEARS | `ADD_YEARS({date}, N)` | Add N years |
| WORKDAYS | `WORKDAYS({start}, {end})` | Count of workdays between dates |

### Text Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| CONCATENATE | `CONCATENATE("text", {col}, ...)` | Join text values |
| LEN | `LEN({col})` | Character count |
| LEFT | `LEFT({col}, N)` | First N characters |
| RIGHT | `RIGHT({col}, N)` | Last N characters |
| MID | `MID({col}, start, N)` | N characters from position |
| FIND | `FIND("text", {col})` | Position of text (0 if not found) |
| REPLACE | `REPLACE({col}, start, N, "new")` | Replace characters |
| TRIM | `TRIM({col})` | Remove leading/trailing spaces |
| UPPER | `UPPER({col})` | Uppercase |
| LOWER | `LOWER({col})` | Lowercase |
| TEXT | `TEXT({col})` | Convert number to text |
| `&` | `"text" & {col}` | Concatenation operator |

### Status Functions

| Function | Syntax | Description |
|----------|--------|-------------|
| STATUS_LABEL | `STATUS_LABEL({status_col})` | Get status label text |
| STATUS_INDEX | `STATUS_INDEX({status_col})` | Get status index number |

## SLA Tracking Formula Patterns

### 5-Day SLA Countdown
```
IF(DAYS({date_submitted}, TODAY()) > 5, "BREACHED", CONCATENATE(TEXT(5 - DAYS({date_submitted}, TODAY())), " days remaining"))
```

### SLA Status with Color Coding (for display_value)
```
IF(DAYS({date_submitted}, TODAY()) > 5, "BREACHED", IF(DAYS({date_submitted}, TODAY()) >= 3, "DUE SOON", "ON TRACK"))
```

### Days Since Submission
```
DAYS({date_submitted}, TODAY())
```

### Progress Percentage (with Progress column)
```
ROUND(MIN({progress_col}, 100), 0)
```

## Limitations

| Operation | Supported |
|-----------|-----------|
| Read via display_value | Yes |
| Filter in items_page | No — filter client-side |
| Create column | Yes (generic create_column) |
| Update column value | No — result is computed |
| Clear column value | No — clear source columns |
| Reference mirror columns | No |
| Reference connect boards columns | No |
| Max formula columns/request | 5 |
| Rate limit (display_value) | 10,000/minute |
