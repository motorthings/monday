<!--
  Source: https://developer.monday.com/api-reference/docs/importing-items-in-bulk
  Fetched: 2026-06-06T22:37:48.063969+00:00
  Platform: monday
-->

For AI agents: visit https://developer.monday.com/llms.txt for an index of all pages formatted in Markdown and endpoints in OpenAPI.

Jump to Content

[](https://developer.monday.com/)

[ __Home](https://developer.monday.com/api-reference/)[ __Guides](https://developer.monday.com/api-reference/docs)[ __API Reference](https://developer.monday.com/api-reference/reference)[ __Changelog](https://developer.monday.com/api-reference/changelog)[ Build with AI](https://developer.monday.com/api-reference/docs/build-on-monday-with-ai)[Playground](https://monday.com/developers/v2/try-it-yourself)

* * *

[Apps Docs](https://developer.monday.com/apps/docs/intro)[Community](https://developer-community.monday.com/)[Need Help?](https://developer.monday.com/api-reference/docs/get-help)[](https://developer.monday.com/)

__Guides

[Apps Docs](https://developer.monday.com/apps/docs/intro)[Community](https://developer-community.monday.com/)[Need Help?](https://developer.monday.com/api-reference/docs/get-help)

[__Home](https://developer.monday.com/api-reference/)[ __Guides](https://developer.monday.com/api-reference/docs)[ __API Reference](https://developer.monday.com/api-reference/reference)[ __Changelog](https://developer.monday.com/api-reference/changelog)[ Build with AI](https://developer.monday.com/api-reference/docs/build-on-monday-with-ai)[Playground](https://monday.com/developers/v2/try-it-yourself)

Importing items in bulk

## About the monday API

  * [The basics](https://developer.monday.com/api-reference/docs/basics)
  * [Authentication](https://developer.monday.com/api-reference/docs/authentication)
  * [Versioning](https://developer.monday.com/api-reference/docs/api-versioning)
  * [Rate limits](https://developer.monday.com/api-reference/docs/rate-limits)
  * [Idempotency](https://developer.monday.com/api-reference/docs/idempotency)
  * [Error handling](https://developer.monday.com/api-reference/docs/error-handling)
  * [Release notes __](https://developer.monday.com/api-reference/docs/release-notes)
    * [Migrating the User entity: 2026-04 → 2026-10](https://developer.monday.com/api-reference/docs/migrating-user-entity-to-2026-10)
    * [ Migrating to version 2025-04](https://developer.monday.com/api-reference/docs/migrating-to-version-2025-04)
  * [Platform MCP for monday.com ____](https://monday.com/w/mcp)
    * [Platform MCP overview](https://developer.monday.com/api-reference/docs/monday-mcp-overview)
    * [ Platform MCP tools __](https://developer.monday.com/api-reference/docs/platform-mcp-tools)
      * [Create Board (Platform MCP)](https://developer.monday.com/api-reference/docs/create-board)
      * [ Get Board Info (Platform MCP)](https://developer.monday.com/api-reference/docs/get-board-info)
      * [Get Board Items (Platform MCP)](https://developer.monday.com/api-reference/docs/get-board-items)
      * [Get Board Activity (Platform MCP)](https://developer.monday.com/api-reference/docs/get-board-activity)
      * [Board Insights (Platform MCP)](https://developer.monday.com/api-reference/docs/board-insights)
      * [Create Group (Platform MCP)](https://developer.monday.com/api-reference/docs/create-group)
      * [Create Column (Platform MCP)](https://developer.monday.com/api-reference/docs/create-column)
      * [Get Column Type Info (Platform MCP)](https://developer.monday.com/api-reference/docs/get-column-type-info)
      * [Create Item (Platform MCP)](https://developer.monday.com/api-reference/docs/create-item)
      * [Change Item Column Values (Platform MCP)](https://developer.monday.com/api-reference/docs/change-item-column-values)
      * [Create Workspace (Platform MCP)](https://developer.monday.com/api-reference/docs/create-workspace)
      * [Update Workspace (Platform MCP)](https://developer.monday.com/api-reference/docs/update-workspace)
      * [List Workspaces (Platform MCP)](https://developer.monday.com/api-reference/docs/list-workspaces)
      * [Workspace Info (Platform MCP)](https://developer.monday.com/api-reference/docs/workspace-info)
      * [Create Folder (Platform MCP)](https://developer.monday.com/api-reference/docs/create-folder)
      * [Update Folder (Platform MCP)](https://developer.monday.com/api-reference/docs/update-folder)
      * [Move Object (Platform MCP)](https://developer.monday.com/api-reference/docs/move-object)
      * [Create Doc (Platform MCP)](https://developer.monday.com/api-reference/docs/create-doc)
      * [Update Doc (Platform MCP)](https://developer.monday.com/api-reference/docs/update-doc)
      * [Read Docs (Platform MCP)](https://developer.monday.com/api-reference/docs/read-docs)
      * [Create Dashboard (Platform MCP)](https://developer.monday.com/api-reference/docs/create-dashboard)
      * [Create Widget (Platform MCP)](https://developer.monday.com/api-reference/docs/create-widget)
      * [All Widgets Schema (Platform MCP)](https://developer.monday.com/api-reference/docs/all-widgets-schema)
      * [Create Form (Platform MCP)](https://developer.monday.com/api-reference/docs/create-form)
      * [Get Form (Platform MCP)](https://developer.monday.com/api-reference/docs/get-form)
      * [Update Form (Platform MCP)](https://developer.monday.com/api-reference/docs/update-form)
      * [Form Questions Editor (Platform MCP)](https://developer.monday.com/api-reference/docs/form-questions-editor)
      * [Create Form Submission (Platform MCP)](https://developer.monday.com/api-reference/docs/create-form-submission)
      * [Get User Context (Platform MCP)](https://developer.monday.com/api-reference/docs/get-user-context)
      * [List Users and Teams (Platform MCP)](https://developer.monday.com/api-reference/docs/list-users-and-teams)
      * [Create Update (Platform MCP)](https://developer.monday.com/api-reference/docs/create-update)
      * [Get Updates (Platform MCP)](https://developer.monday.com/api-reference/docs/get-updates)
      * [Create Notification (Platform MCP)](https://developer.monday.com/api-reference/docs/create-notification)
      * [Search (Platform MCP)](https://developer.monday.com/api-reference/docs/mcp-search)
      * [Get Assets (Platform MCP)](https://developer.monday.com/api-reference/docs/get-assets)
      * [Create Agent (Platform MCP)](https://developer.monday.com/api-reference/docs/create-agent)
      * [Get Agent (Platform MCP)](https://developer.monday.com/api-reference/docs/get-agent)
      * [Delete Agent (Platform MCP)](https://developer.monday.com/api-reference/docs/delete-agent)
      * [Get Notetaker Meetings (Platform MCP)](https://developer.monday.com/api-reference/docs/get-notetaker-meetings)
      * [Get Sprints Boards (Platform MCP)](https://developer.monday.com/api-reference/docs/get-sprints-boards)
      * [Get Sprints Metadata (Platform MCP)](https://developer.monday.com/api-reference/docs/get-sprints-metadata)
      * [Get Sprint Summary (Platform MCP)](https://developer.monday.com/api-reference/docs/get-sprint-summary)
      * [Execute API Query (Platform MCP)](https://developer.monday.com/api-reference/docs/all-monday-api)
      * [Get GraphQL Schema (Platform MCP)](https://developer.monday.com/api-reference/docs/get-graphql-schema)
      * [Get Type Details (Platform MCP)](https://developer.monday.com/api-reference/docs/get-type-details)
      * [Show Table (Platform MCP UI)](https://developer.monday.com/api-reference/docs/show-table)
      * [Show Chart (Platform MCP UI)](https://developer.monday.com/api-reference/docs/show-chart)
      * [Show Battery (Platform MCP UI)](https://developer.monday.com/api-reference/docs/show-battery)
      * [Show Assign (Platform MCP UI)](https://developer.monday.com/api-reference/docs/show-assign)
    * [Platform MCP security](https://developer.monday.com/api-reference/docs/monday-mcp-security-overview)

## Guides

  * [GraphQL overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
  * [Making your first request](https://developer.monday.com/api-reference/docs/getting-started)
  * [Querying board items](https://developer.monday.com/api-reference/docs/querying-board-items)
  * [Working with multi-level boards](https://developer.monday.com/api-reference/docs/working-with-multi-level-boards)
  * [Changing column values](https://developer.monday.com/api-reference/docs/change-column-values)
  * [Searching across your account](https://developer.monday.com/api-reference/docs/searching-across-your-account)
  * [Optimizing API usage](https://developer.monday.com/api-reference/docs/optimizing-api-usage)
  * [Aggregating Board Data](https://developer.monday.com/api-reference/docs/aggregation-api-guide)
  * [Validation Rules](https://developer.monday.com/api-reference/docs/validation-rules-guide)
  * [Importing items in bulk](https://developer.monday.com/api-reference/docs/importing-items-in-bulk)
  * [Working with the dependency column](https://developer.monday.com/api-reference/docs/working-with-dependency-column)

## AI Skills

  * [Build on monday.com with AI](https://developer.monday.com/api-reference/docs/build-on-monday-with-ai)
  * [mcli — monday.com GraphQL CLI](https://developer.monday.com/api-reference/docs/mcli-cli-guide)
  * [Portfolio Agent Skills __](https://developer.monday.com/api-reference/docs/portfolio-agent-skills)
    * [Skill: Archive / Delete a Project](https://developer.monday.com/api-reference/docs/portfolio-skill-archive-delete-project)
    * [ Skill: Update Project Status](https://developer.monday.com/api-reference/docs/portfolio-skill-update-project-status)
    * [Skill: List All Projects in a Portfolio](https://developer.monday.com/api-reference/docs/portfolio-skill-list-portfolio-projects)
    * [Skill: Get Tasks Assigned to a Person Across Projects](https://developer.monday.com/api-reference/docs/portfolio-skill-get-tasks-by-person)
    * [Skill: Get Project Status / Health](https://developer.monday.com/api-reference/docs/portfolio-skill-get-project-status)
    * [Skill: Duplicate a Project](https://developer.monday.com/api-reference/docs/portfolio-skill-duplicate-project)
    * [Skill: Create a New Portfolio](https://developer.monday.com/api-reference/docs/portfolio-skill-create-portfolio)
    * [Skill: Connect a Project to a Portfolio](https://developer.monday.com/api-reference/docs/portfolio-skill-connect-project-to-portfolio)

## Tools

  * [The Developer Center](https://developer.monday.com/api-reference/docs/the-developer-center)
  * [API analytics dashboard](https://developer.monday.com/api-reference/docs/api-analytics)
  * [API playground](https://developer.monday.com/api-reference/docs/api-playground)
  * [Postman collection __](https://www.postman.com/matiasdavidson1/my-workspace/collection/dmzv0h4/queries-and-mutations-for-monday-com)
  * [External APIs](https://developer.monday.com/api-reference/docs/external-apis)
  * [ Developer AI assistant](https://developer.monday.com/api-reference/docs/developer-ai-assistant)

## SDKs

  * [JavaScript SDK](https://developer.monday.com/api-reference/docs/javascript-sdk)
  * [Python SDK](https://developer.monday.com/api-reference/docs/python-sdk)

## Resources

  * [Get help](https://developer.monday.com/api-reference/docs/get-help)
  * [Youtube __](https://www.youtube.com/@mondayappdeveloper)
  * [monday.com help center __](https://support.monday.com/)
  * [API coverage gaps](https://developer.monday.com/api-reference/docs/coverage-gaps)

Powered by [](https://readme.com?ref_src=hub&project=monday-api-target)

# Importing items in bulk

Learn how to create and update items in bulk via the platform API using ingest_items, backfill_items, and fetch_job_status

> 🚧
> 
> **Only available in API versions[`2026-07`](https://developer.monday.com/api-reference/docs/release-notes#2026-07) and later**

Using the platform API, you can import large quantities of items into a monday.com board through an asynchronous, three-step workflow:

  1. Start an import job ([`ingest_items`](https://developer.monday.com/api-reference/reference/ingest-items-api-reference) or [`backfill_items`](https://developer.monday.com/api-reference/reference/backfill-items-api-reference)) and receive a pre-signed `upload_url` and `job_id`
  2. Upload the CSV file to the `upload_url`
  3. Poll job status with [`fetch_job_status`](https://developer.monday.com/api-reference/reference/ingest-items-api-reference#fetch-job-status)

The API exposes two ways to start an import. **`ingest_items`** is the default for almost every use case. **`backfill_items`** is intended for a one-time, account-admin-only initial load - for example, seeding a board before it goes into day-to-day use.

* * *

# 

Choose how to import

| `ingest_items` (recommended)| `backfill_items`  
---|---|---  
**Use for**|  Integrations, recurring imports, creating or updating items as part of normal board activity| A single large initial setup import before users or agents work in the board day-to-day  
**Maximum rows per job**|  10,000| 20,000  
**Who can call it**|  Any user with board edit access via API (`boards:write`)| Account admin **and** `boards:write`  
**Update or skip existing items**|  Yes, using `on_match`| Not supported; always creates new items  
**Hourly item create/update budget**|  Counts toward the 19,000 items per account per hour budget| Does not consume this budget  
**Impact on other monday.com features**|  None| Automations are not triggered. Item creation is not logged in the Activity Log.  
  
* * *

# 

Supported column types

Both endpoints support the following column types:

  * Date
  * Dropdown
  * Email
  * Link
  * Long Text
  * Number
  * People
  * Phone
  * Status
  * Text
  * Timeline

Rows that include unsupported column types may fail validation. See Column type validation for the per-type CSV format.

* * *

# 

Limitations

Category| `backfill_items`| `ingest_items`  
---|---|---  
Maximum rows per file| 20,000| 10,000  
Maximum file size| 150 MB| 150 MB  
Upload URL expiration| 10 minutes| 10 minutes  
Report URL expiration| 10 minutes| 10 minutes  
Jobs started per account per hour| 100 (shared with `ingest_items`)| 100 (shared with `backfill_items`)  
Item create/update budget per hour| Not consumed| 19,000 items per account  
  
**Notes**

  * File size is enforced after upload by the import service (not by the upload URL itself). Oversized files are rejected with `failure_reason: FILE_TOO_LARGE`.
  * Cancellation of a running job is not supported.

* * *

# 

Getting started

## 

Pre-requisites

  * [API authentication token](https://developer.monday.com/api-reference/docs/authentication)
  * CSV file with valid headers and values (see CSV format)
  * Requests must include the `API-Version: 2026-07` [header](https://developer.monday.com/api-reference/docs/api-versioning#using-the-api-version-header-in-an-http-request)

## 

Step 1: Start the import job

  1. Retrieve the `board_id` and `group_id` where you want to import items by querying [`boards`](https://developer.monday.com/api-reference/reference/boards) and [`groups`](https://developer.monday.com/api-reference/reference/groups).
  2. Call [`ingest_items`](https://developer.monday.com/api-reference/reference/ingest-items-api-reference#ingest-items) unless you specifically need a one-time admin-only initial load via [`backfill_items`](https://developer.monday.com/api-reference/reference/backfill-items-api-reference#backfill-items).
  3. Save the returned `job_id` and `upload_url`. The `upload_url` is only valid for 10 minutes.

**Ingest example (default path)**

GraphQL
    
    
    mutation {
      ingest_items(
        board_id: "1234567890"
        group_id: "topics"
        on_match: { behaviour: UPSERT, match_column_id: "email" }
      ) {
        job_id
        upload_url
      }
    }

**Backfill example (one-time initial load only)**

GraphQL
    
    
    mutation {
      backfill_items(board_id: "1234567890", group_id: "topics") {
        job_id
        upload_url
      }
    }

## 

Step 2: Upload the CSV file

Upload your CSV to the `upload_url` returned in Step 1.

HTTP
    
    
    PUT <upload_url>
    Content-Type: text/csv
    
    <CSV file content>

A successful upload returns HTTP 200 with an `ETag` header.
    
    
    HTTP/1.1 200 OK
    ETag: "abc123def456"

## 

Step 3: Monitor the import status

Poll [`fetch_job_status`](https://developer.monday.com/api-reference/reference/ingest-items-api-reference#fetch-job-status) every ~10 seconds until the job reaches a terminal state (`COMPLETED`, `FAILED`, or `REJECTED`).

GraphQL
    
    
    query {
      fetch_job_status(job_id: "7c9e6679-7425-40de-944b-e07fc1f90ae7") {
        ... on ItemsJobStatus {
          status
          counts {
            submitted
            invalid
            skipped
            created
            updated
            failed
          }
          progress_percentage
          failure_reason
          failure_message
          fully_imported
          report_created
          report_url
        }
      }
    }

When `report_created` is `true`, download `report_url` promptly. The report URL expires after 10 minutes.

* * *

# 

Reference

## 

CSV format

  * UTF-8 encoding is required.
  * Use comma (`,`) as the column separator.
  * Wrap values that contain commas, double quotes, or newlines in double quotes. Escape an embedded double quote by doubling it (`""`).

### 

Headers

  * The first header value must be `name`.
  * The remaining header values must be exact board `column_id` values (case-sensitive).
  * Query [`columns`](https://developer.monday.com/api-reference/reference/columns) to retrieve the correct column IDs for the target board.

### 

Rows

  * The first value in each row is the item name.
  * The remaining values map to the column IDs in the header.
  * Empty values are allowed. Whitespace-only values are treated as empty.
  * In **UPSERT** mode (`ingest_items` only), an empty cell on a matched row is **ignored** \- the existing column value is preserved.
  * In **UPSERT** mode, a cell containing exactly the string `<NULL>` **clears** the column value on the matched item.

### 

Example

csv
    
    
    name,text,status,date,email,numeric,dropdown
    Task 1,Description text,Working on it,2025-12-31,[[email protected]](https://developer.monday.com/cdn-cgi/l/email-protection),100,"Option A, Option B"
    Task 2,Another task,Done,2026-01-15,[[email protected]](https://developer.monday.com/cdn-cgi/l/email-protection),200,Option C
    Task 3,Third task,Stuck,2026-02-28,[[email protected]](https://developer.monday.com/cdn-cgi/l/email-protection),300,
    Task 4,,,,,,

## 

Column type validation

Column type| CSV value format| Validation rules  
---|---|---  
Date| Valid date| ISO format (`YYYY-MM-DD`). Other formats may be normalized.  
Dropdown| Comma-separated labels| Each label must already exist on the column and be active. All labels in a comma-separated list must be valid; otherwise the row fails.  
Email| Valid email or `Name <email>`| Must be a valid email format.  
Link| Valid URL or `[Display Text](URL)`| URL must start with `http://` or `https://`.  
Long Text| Text string| Empty values allowed.  
Number| Numeric string| Integer or decimal.  
People| Comma-separated identifiers, each one of: email (`[[email protected]](https://developer.monday.com/cdn-cgi/l/email-protection)`), `user:<id>` or `user:<name>`, `team:<id>` or `team:<name>`, or a bare name (`Jeremy`) resolved as user or team.| Each identifier must resolve to exactly one active user or team in the account. Fails on no match, multiple matches, or resolution errors. Duplicate identifiers are deduped. Respects the column's `max_people_allowed` setting.  
Phone| Phone number string| Various formats accepted; optional country hints.  
Status| Label text (exact match)| Label must already exist on the column and be active. Case-sensitive.  
Text| Text string| Empty values allowed.  
Timeline| `YYYY-MM-DD/YYYY-MM-DD` for a range, or single `YYYY-MM-DD` (sets `from = to = date`)| Both dates must be valid ISO dates. Other separators (dash with spaces, pipe, JSON) are not accepted.  
  
* * *

# 

Best practices

  1. **Prefer`ingest_items`** for integrations and any import that should behave like normal board activity.
  2. **Use`backfill_items` only** for a planned, one-time initial load.
  3. Poll job status about every 10 seconds - not faster.
  4. Validate the CSV header against the board schema **before** uploading.
  5. Handle GraphQL errors from the API separately from HTTP errors from the file upload step.
  6. Download the report as soon as `report_created` is `true`.
  7. On `RATE_LIMIT_EXCEEDED`, wait using `extensions.retryAfterMs` instead of retrying immediately.
  8. For ingest, spread large volumes across the hour where possible to reduce `ACCOUNT_CAPACITY_EXCEEDED` rejections.

* * *

# 

Troubleshooting

Issue| Symptoms| Resolution  
---|---|---  
Upload URL expired| HTTP 403 on the `PUT` upload (S3 returns "Request has expired")| Start a new job and upload within 10 minutes.  
Invalid CSV format| Status `REJECTED`, `failure_reason: INVALID_UPLOAD`| Verify that the first header is `name`, all column IDs exist on the board, the file is UTF-8, the separator is comma, and embedded quotes are escaped (`""`).  
Items not created| Status `COMPLETED` with high `counts.invalid` or `counts.failed` and low `counts.created`| Download the report from `report_url` and inspect per-row errors. Check column ID typos, status/dropdown label spelling and case, date format, and that referenced users or teams exist.  
Status stuck at `UPLOAD_PENDING`| No progress after uploading the CSV| Confirm the upload returned HTTP 200 with an `ETag` header. If not, start a new job and re-upload.  
Backfill permission denied| Status `REJECTED`, `failure_reason: PERMISSION_DENIED`, or a GraphQL error "Only admin users can perform this operation."| `backfill_items` requires an account admin. Use `ingest_items` instead.  
File too large| Status `REJECTED`, `failure_reason: FILE_TOO_LARGE`| Split the file into chunks at or below 150 MB.  
Hourly capacity exceeded (ingest)| Status `REJECTED`, `failure_reason: ACCOUNT_CAPACITY_EXCEEDED`| The job's valid row count would exceed the remaining 19,000 items-per-hour budget. Spread the load across the hour or wait for the budget to reset.  
Rate limit on starting jobs| GraphQL error `RATE_LIMIT_EXCEEDED` (HTTP 429) on `ingest_items` or `backfill_items`| Honor `extensions.retryAfterMs` before retrying. The 100-call-per-hour limit is shared between `ingest_items` and `backfill_items`.  
  
* * *

# 

Related reference pages

  * [Ingest items API reference](https://developer.monday.com/api-reference/reference/ingest-items-api-reference) (default)
  * [Backfill items API reference](https://developer.monday.com/api-reference/reference/backfill-items-api-reference)
  * [Bulk import other types](https://developer.monday.com/api-reference/reference/bulk-import-other-types)

  


__Updated 16 days ago

* * *

[Validation Rules](https://developer.monday.com/api-reference/docs/validation-rules-guide)[Working with the dependency column](https://developer.monday.com/api-reference/docs/working-with-dependency-column)

Copy Page
