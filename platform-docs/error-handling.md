<!--
  Source: https://developer.monday.com/api-reference/docs/error-handling
  Fetched: 2026-06-06T22:37:48.379951+00:00
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

Error handling

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

# Error handling

If your API request cannot be completed successfully, you will receive an error message.

# 

Error format

Errors returned by the API have the following characteristics:

  * **HTTP status:** Response will be `200 – OK` for application-level errors. Other statuses will be returned for transport-layer errors, such as `500 - Internal server error`, `429 - Too many requests` or `400 - Bad request`
  * **JSON response:** Body will contain an `errors` array with further details about each error
  * **Partial data:** Requests will return partial data, so the `data` object may also contain some information. For example, if you query three fields, you may receive two fields and one error.
  * **`Retry-After`header:** Errors will include the `Retry-After` header to indicate how long you need to wait before making another request
  * Each API response includes a `request_id` in the extensions object that can be used for troubleshooting.

### 

Sample format

Here's an example of an application-level error:

Error onlyPartial data
    
    
    {
      "data" : [],
      "errors": [
        {
          "message": "User unauthorized to perform action",
          "locations": [
            {
              "line": 2,
              "column": 3
            }
          ],
          "path": [
            "me"
          ],
          "extensions": {
            "code": "UserUnauthorizedException",
            "error_data": {},
            "status_code": 403
          }
        }
      ],
      "account_id": 123456
    }
    
    
    {
      "data": {
        "me": {
          "id": "4012689",
          "photo_thumb": null
        },
        "complexity": {
          "query": 12
        }
      },
      "errors": [
        {
          "message": "Photo unavailable.",
          "locations": [
            {
              "line": 4,
              "column": 5
            }
          ],
          "path": [
            "me",
            "photo_thumb"
           ],
          "extensions": {
            "code": "ASSET_UNAVAILABLE"
          }
        }
      ],
      "account_id": 18888528
    }

# 

Errors by status code

## 

2xx errors

Errors with a 2xx status code indicate that monday.com is not accepting the requested action due to a platform restriction, limitation, or rule. These errors occur for various reasons, including passing invalid values, missing permissions, or reaching character limits.

Here are **some** of the most common errors:

Error code| HTTP status code| Description| Resolution  
---|---|---|---  
`API_TEMPORARILY_BLOCKED`| 200| There is an issue with the API and usage has temporarily been blocked| Check the [status page](https://status.monday.com/) for updates and retry your call once the issue has been resolved.  
`ColumnValueException`| 200| Incorrect column value formatting| 

  * Ensure the [column](https://developer.monday.com/api-reference/reference/column-types-reference) is supported by our API and not calculated in the client.
  * Verify that the column value conforms with each [column's data structure](https://developer.monday.com/api-reference/reference/column-types-reference).
  * Check that the [connect boards column](https://developer.monday.com/api-reference/reference/connect) you're referencing is connected to a board via the monday.com UI.

  
`CorrectedValueException`| 200| The query is of the wrong type| If you try to update a column with simple values (`String` values), ensure the column supports this type of value format.  
`CreateBoardException`| 200| Error in your create board mutation| 

  * If you’re creating a board from a template, ensure the template ID is a valid monday template or a board that has template status. To learn more about making a board a template, check out our resource on board templates [here](https://support.monday.com/hc/en-us/articles/360001362625-Does-monday-com-offer-templates-).
  * If you’re duplicating a board, ensure the board ID exists.

  
`InvalidArgumentException`| 200| The argument being passed in the query is invalid, you've hit a pagination limit, you're querying a subitem board ID, or a board ID is not found| 

  * Check your argument for typos.
  * Verify that the argument exists for the object you are querying.
  * Make your result window smaller.

  
`InvalidBoardIdException`| 200| The board ID being passed in the query is invalid| Verify that the board ID exists and that you have access to it.  
`InvalidColumnIdException`| 200| The column ID being passed in the query is invalid| Verify that the column ID exists and that you have access to it.  
`InvalidUserIdException`| 200| The user ID being passed in the query is invalid| Verify that the user ID exists and that the user is assigned to your board.  
`InvalidVersionException`| 200| The requested API version is invalid| Ensure that your request follows the proper [format](https://developer.monday.com/api-reference/docs/api-versioning#selecting-a-version).  
`ItemNameTooLongException`| 200| The item name has exceeded the allotted number of characters| Ensure the item name is 1-255 characters in length.  
`ItemsLimitationException`| 200| You have exceeded the limit of 10,000 items per board| Reduce the number of items on the board.  
`missingRequiredPermissions`| 200| The operation has exceeded the OAuth permission scopes granted for the app| Review your app's [permission scopes](https://developer.monday.com/apps/docs/oauth#permission-scopes) to ensure the correct ones are requested.  
`Parse error on...`| 200| Incorrect query string formatting| 

  * Verify that all strings are valid in your query.
  * Close all parentheses, brackets, and curly brackets.

  
`ResourceNotFoundException`| 200| The ID being passed in your query is invalid| Verify that the ID of the item, group, or board you’re querying exists.  
  
## 

4xx client errors

Errors with a 4xx status code indicate that something went wrong on the client's (your) side. These errors occur for various reasons, including a lack of access to the requested information, excessive use of the API, or providing incorrect input.

Here are **some** of the most common errors:

Error| HTTP status code| Description| Resolution  
---|---|---|---  
`Bad request`| 400| The structure of your query string was passed incorrectly| 

  * Pass your query string with the `query` key.
  * Send your request as a POST request with a JSON body.
  * Avoid unterminated strings in your query.

  
`JsonParseException`| 400| Issues interpreting the provided JSON| Verify all JSON is valid using a JSON validator (e.g., [JSON lint](https://jsonlint.com/) )  
`Unauthorized`| 401| You don't have permission to access the data| 

  * Input a valid API key.
  * Pass the key in the `Authorization` header.

  
`Your ip is restricted`| 401| An account admin has restricted access to the system from specific IP addresses| Confirm that your IP address is not restricted by your account admin.  
`UserUnauthorizedException`| 403| The user doesn't have the required permission to perform the action in question| Verify that the user has permission to access or edit the given resource.  
`USER_ACCESS_DENIED`| 403| The user is unauthorized to use the API| Verify that the user is active, not view-only, and has a confirmed email address.  
`ResourceNotFoundException`| 404| The ID being passed in the query is invalid| Verify that the ID of the user you are querying exists and is assigned to your board.  
`DeleteLastGroupException`| 409| The last group on a board is being deleted or archived| Verify that you have at least one group on the board.  
`IDEMPOTENCY_CONFLICT`| 409| A request with this idempotency key is currently being processed| Retry after the duration specified in the `Retry-After` response header. See [Idempotency](https://developer.monday.com/api-reference/docs/idempotency) for details.  
`RecordInvalidException`| 422| Indicates one of the following:

  * A board has exceeded 400 individual subscribers or 100 team subscribers
  * A user or team has subscribed to more than 10,000 boards

| 

  * Learn how to [optimize board subscribers](tps://support.monday.com/hc/en-us/articles/14667682024594https://support.monday.com/hc/en-us/articles/14667682024594).
  * Unsubscribe from, delete, or archive irrelevant boards.

  
`Resource is currently locked, please try again later`| 423| The board is temporarily locked because another process is performing a concurrent update (e.g., column update, automation). During this time, write operations are blocked to ensure data consistency.| 

  * Retry the request after a short delay.
  * Avoid concurrent updates to the same board from multiple sources.

  
`maxConcurrencyExceeded`| 429| You exceeded the maximum number of queries allowed at once| 

  * Reduce the number of queries sent at once.
  * Use a retry mechanism in your code.

  
`Rate Limit Exceeded`| 429| You made more than 5,000 requests in one minute| Reduce the number of requests sent in one minute.  
`COMPLEXITY_BUDGET_EXHAUSTED`| 429| You have reached the complexity limit| 

  * Utilize the `limits` and `page` arguments.
  * Only request the information you need.
  * Read more about [rate limits](https://developer.monday.com/api-reference/docs/rate-limits).

  
`IP_RATE_LIMIT_EXCEEDED`| 429| You have reached the [IP limit](https://developer.monday.com/api-reference/docs/rate-limits#ip-limit)| 

  * Wait for the specified period in the error response before retrying your call.
  * Learn about [optimizing your API usage](https://developer.monday.com/api-reference/docs/optimizing-api-usage#optimize-your-calls).

  
  
## 

5xx server errors

Errors with a 5xx status code indicate that something went wrong on the server's (monday's) side.

Here are **some** of the most common errors:

Error| HTTP status code| Description| Resolution  
---|---|---|---  
`Internal Server Error`| 500| Indicates that something went wrong. Common causes are:

  * Invalid arguments, such as board or item IDs that don't exist
  * Malformatted JSON column values

| 

  * Retry your request after a short period.
  * Double-check your request's format.
  * Ensure your API token has the right permissions.

  
  
> 📘
> 
> ### 
> 
> Join our developer community!
> 
> We've created a [community](https://developer-community.monday.com/) specifically for our devs where you can search through previous topics to find solutions, ask new questions, hear about new features and updates, and learn tips and tricks from other devs. Come join in on the fun! 😎

 __Updated 14 days ago

* * *

[Idempotency](https://developer.monday.com/api-reference/docs/idempotency)[Release notes](https://developer.monday.com/api-reference/docs/release-notes)

Copy Page
