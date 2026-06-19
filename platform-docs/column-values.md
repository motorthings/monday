<!--
  Source: https://developer.monday.com/api-reference/docs/change-column-values
  Fetched: 2026-06-06T22:37:47.219892+00:00
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

Changing column values

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

# Changing column values

Every monday.com board has one or more columns, each of which holds a particular piece of information. Each column has a certain type, and different column types expect a different set of parameters to update their values.

You will most likely need to change item column values in two scenarios: when updating the value of an item using the `change_column_value()` mutation, or when setting the initial values of an item using the `create_item()` mutation.

## 

JSON vs. Strings Formatting

To update a column value, you should send either a JSON-formatted string or simple string in your mutation.

While all of the columns supported by our API will accept `JSON` formatting, not all of these columns will accept `String` formatting as well.

When sending data to a particular column, use a JSON-formatted string (if you’re using Javascript, you can use `JSON.stringify()` to convert a JSON object into a string).

## 

Changing a Single Column Value

To change a single column value, utilize either the `change_simple_column_value()` or the `change_column_value()` methods.

Depending on which column type's value you're attempting to change, it will necessitate a different method to use. Some columns will only accept `JSON` values, while others will accept both `Strings` and `JSON` values.

## 

Changing Multiple Column Values

In addition to changing a simple column's values, you are also able to change multiple columns' values using the `change_multiple_column_values()` mutation. This mutation allows you to update multiple column values of a specific Item (row).

Each column is of a certain type, and different column types expect a different set of parameters to update their values.

The `column_values` argument requires a JSON string (key-value pairs). The JSON string should have column IDs as keys, and the values you want to set as the values. For the values, you can use either a `String` value, or mix `String` and `JSON` values.

Here is an example of a `column_values` argument with a Text and a Status column using `String`:  
{"text0": "New text", "status2": "Done"}.

Here is the same example of a `column_values` argument with a Text and a Status column using a combined `String` and `JSON` value:  
{"text5": "New text", "status3": {"label": "Done"}}.

In the second example, you can see that the Status column is sent a `JSON` value of {"label": "Done"}, instead of the `String` value "Done" sent in the first example.

> 📘
> 
> ### 
> 
> NOTE
> 
> Status columns also accept a `JSON` value with `"index"` (the label's numeric ID) instead of `"label"`. For example: {"status3": {"index": 1}}. Using the index is more reliable since label text can be changed by board admins. See the [status column reference](https://developer.monday.com/api-reference/docs/status) for details.

## 

Setting Column Values upon Item Creation

Much like setting column values with the `change_column_value()`, the `change_simple_column_value()`, and the `change_multiple_column_values()`, setting column values upon item creation involves sending `JSON` values.

## 

Removing Column Values

To remove a column value (i.e. delete an existing column value), send either an empty string for Text and Number columns, or send an empty object for columns that accept JSON values.

**Raw JSON (use this in your column values variables):** `JSON.stringify({});`

**JSON string (use this in the GraphiQL editor):** `"{}"`

GraphQL
    
    
    mutation {
      change_simple_column_value(item_id: 123456789, board_id: 11223344, column_id: "text", value: "") {
        id
      }
    }

GraphQL
    
    
    mutation {
      change_column_value(item_id: 123456789, board_id: 11223344, column_id: "email", value: "{}") {
        id
      }
    }

> 📘
> 
> ### 
> 
> NOTE
> 
> Removing the column value of a **File column** requires explicitly setting the `clear_all` flag as this action cannot be undone.
> 
> **Raw JSON (use this in your column values variables):**  
>  `JSON.stringify({ "clear_all": true });`
> 
> **JSON string (use this in the GraphiQL editor):** `"{\"clear_all\":true}"`

## 

Do you have questions?

Join our [developer community](https://community.monday.com/c/developers/8)! You can share your questions and learn from fellow users and monday.com product experts.

Don’t forget to search before opening a new topic!

__Updated 3 months ago

* * *

[Working with multi-level boards](https://developer.monday.com/api-reference/docs/working-with-multi-level-boards)[Searching across your account](https://developer.monday.com/api-reference/docs/searching-across-your-account)

Copy Page
