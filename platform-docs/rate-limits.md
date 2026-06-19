<!--
  Source: https://developer.monday.com/api-reference/docs/rate-limits
  Fetched: 2026-06-06T22:37:46.784563+00:00
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

Rate limits

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

# Rate limits

Learn more about the monday.com platform API rate limits, calculating complexity, and timeout policies

We strive to provide a top-tier API experience that is reliable and consistent for all users. To maintain a high-quality service and ensure optimal performance, users are subject to the following limits to help manage the API's consumption and throughput:

  * Complexity limit
  * Daily call limit
  * Minute limit
  * Concurrency limit
  * IP limit
  * Resource protection limits

Remembering these limits when using the API is crucial to prevent workflow disruptions and delays.

> 🚧
> 
> ### 
> 
> All limits and exceptions are subject to change. Additional guidelines may be introduced in the future.

# 

Limits

## 

Complexity limit

Complexity defines the load that each call puts on the API. This limit restricts the heaviness of each query to help prevent excessive load and maintain optimal performance. The limit will not affect most users—the quota is set sufficiently high to impact only users making requests that would compromise the stability of the API.

You will receive a `ComplexityException` error if you hit the limit.

The limit varies based on how you're making the call:

Usage| Limit  
---|---  
Individual query| 5,000,000 (5M) complexity points  
Using app tokens to access the API| Read and writes are limited to 5M complexity points per minute* each  
Using API playground to access the API| Reads and writes are limited to 5M complexity points per minute* each or 1M for trial/free accounts  
Using personal API tokens to access the API| Reads and writes have a combined budget of 10M points per minute* or 1M for trial, NGO, and free accounts  
  
_*Per-minute budgets follow a sliding window and reset 60 seconds after the first API call was made_

### 

Calculating complexity

Calculating the complexity of each query in advance can prevent you from hitting the limit. The simplest way to do so is by adding the [complexity](https://developer.monday.com/api-reference/docs/complexity#queries) field to your queries to return the remaining complexity before and after the query, the complexity of the query itself, and when the limit resets.

GraphQL
    
    
    mutation {
      complexity {
        query
        before
        after
      }
      create_item(board_id:1234567890, item_name:"test item") {
        id
      }
    }

### 

Reducing complexity

You can avoid hitting the complexity limit by:

  * Requesting only the data you need
  * Reducing nested queries
  * Utilizing the `page` and `limit` arguments

## 

Daily call limit

The daily call limit helps prevent disruptions caused by excessive load from individual accounts, maintains the API service as a free feature across all plans, and controls operational costs to continue delivering value to all our users.

All API calls made through personal tokens, private applications, and public applications (excluding marketplace apps and those developed by monday.com) count towards this limit.

You will receive a `DAILY_LIMIT_EXCEEDED` error if you hit the limit.

The limit varies based on your [monday.com plan](https://monday.com/pricing):

Tier| Daily call limit (resets at midnight UTC)  
---|---  
Free/Standard/Basic| 1,000  
Pro| 10,000 (soft limit)*  
Enterprise| 25,000 (soft limit)*  
  
_*Indicates the recommended usage. Please request an increase through the[API analytics dashboard](https://developer.monday.com/api-reference/docs/api-analytics) if your account consistently exceeds this limit._

### 

Exceptions

A single API request typically deducts one call from your daily limit. However, there are exceptions for specific calls:

API call| Contribution to the daily limit| Resolution  
---|---|---  
Requests that hit a rate limit ([complexity](https://developer.monday.com/api-reference/docs/errors#complexityexception), [minute rate limit](https://developer.monday.com/api-reference/docs/errors#rate-limit-exceeded), [concurrency](https://developer.monday.com/api-reference/docs/errors#concurrency-limit-exceeded), etc.)| 0.1 calls| Every rate limit error returns a `retry_in_seconds` field. Only retry your call after waiting for the indicated time to avoid wasteful retries.  
Querying `complexity` to check a query's complexity cost| 0.1 calls| On their own, [`complexity`](https://developer.monday.com/api-reference/reference/complexity) queries count as **less than one call**. We recommend including this query in other API requests to save this usage.  
High complexity queries| 1+ calls| Each API call incurs a complexity cost, and some of these calls contribute extra to the daily call limit. To reduce your daily API call usage, you can [reduce your call's complexity](https://developer.monday.com/api-reference/docs/rate-limits#calculating-complexity).  
  
## 

Minute limit

The minute limit restricts the number of requests in a given period. It is defined per minute, but you may not need to wait for the full minute before retrying your request. You can use the `Retry-After` header to determine when you can retry the request.

You will receive a `Minute limit rate exceeded` error if you hit the limit.

The limit varies based on your [monday.com plan](https://monday.com/pricing):

Tier| Queries per minute  
---|---  
Enterprise| 5,000  
Pro| 2,500  
Other| 1,000  
  
### 

Endpoint-specific minute limits

Each endpoint is subject to the limits mentioned above, but some have additional limits to keep in mind:

Endpoint| Limit  
---|---  
[Create a board mutation](https://developer.monday.com/api-reference/docs/boards#create-a-board)| 40 mutations per minute  
[Duplicate a board mutation](https://developer.monday.com/api-reference/docs/boards#duplicate-a-board)| 40 mutations per minute  
[Duplicate a group mutation](https://developer.monday.com/api-reference/docs/groups#duplicate-group)| 40 mutations per minute  
[Connect project to portfolio mutation](https://mondaydotdev.readme.io/api-reference/reference/portfolio#connect-project-to-portfolio)| 15 mutations per minute  
[Items query](https://developer.monday.com/api-reference/docs/items#queries)| 100 items  
[App subscriptions query](https://developer.monday.com/api-reference/reference/app-subscriptions)| 120 times per minute  
[`display_value`](https://developer.monday.com/api-reference/reference/formula#fields)field on`FormulaValue`implementation| 
* 10,000 formula values per minute (each cell counts as one)
* Up to five formula columns in each request  
  
## 

Concurrency limit

The concurrency limit restricts the number of requests being handled at any moment. You will receive a [`Concurrency limit exceeded`](https://developer.monday.com/api-reference/docs/errors#concurrency-limit-exceeded) error if you hit the limit.

The limit varies based on your [monday.com plan](https://monday.com/pricing) and the type of request:

Tier| Maximum concurrent requests  
---|---  
Enterprise| 250  
Pro| 100  
Other| 40  
  
## 

IP limit

The IP limit helps control the API traffic coming from a given IP address within a short period. You will receive an [`IP_RATE_LIMIT_EXCEEDED`](https://developer.monday.com/api-reference/docs/error-handling#4xx-client-errors) error if you hit the limit.

Source| Limit  
---|---  
Individual IP address| 5,000 requests per 10 seconds  
  
## 

Resource protection limit

In rare cases, an internal monday resource might reject the request. In such a case the same retry logic applies.

# 

Guidelines

  * All requests count towards the stated limits, **even those that fail or return an error.** You can prevent unnecessary API usage by waiting for the time indicated in the `retry_in_seconds` field before retrying the call.
  * The [API SDK](https://developer.monday.com/api-reference/docs/api-sdk) respects the rate-limited responses and waits the appropriate amount of time before automatically retrying the request, up to a configurable maximum number of retries.
  * Unless otherwise noted, limits are measured per account, per app. Usage through a personal token counts toward the same limit.

__Updated about 1 month ago

* * *

[Versioning](https://developer.monday.com/api-reference/docs/api-versioning)[Idempotency](https://developer.monday.com/api-reference/docs/idempotency)

Copy Page
