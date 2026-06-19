<!--
  Source: https://developer.monday.com/api-reference/docs/querying-board-items
  Fetched: 2026-06-06T22:37:48.274165+00:00
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

Querying board items

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

# Querying board items

Learn how to query items on a monday.com board using the platform API

As your monday.com boards grow, it's increasingly important to know how to leverage the API to query all items on a board. Our API uses cursor-based pagination to retrieve up to 500 items in a single query, allowing you to paginate through large boards in just a few steps seamlessly.

This guide walks through each step and includes sample queries to help you structure your own. Following these steps, you can efficiently retrieve all items on a board using the API. Let's get started!

  1. Start by running a GraphQL [`items_page`](https://developer.monday.com/api-reference/reference/items-page) query to retrieve the first 500 items from the board (don't forget to include your board ID as an argument!)

GraphQL
    
    
    query {
      boards (ids: 1234567890){
        items_page {
          cursor
          items {
            id 
            name 
          }
        }
      }
    }

  2. This query returns a cursor value and the first 500 items on your board. Using that cursor value as an argument, run a [`next_items_page`](https://developer.monday.com/api-reference/reference/items-page#cursor-based-pagination-using-next_items_page) query to fetch the next relevant set of items. Please keep in mind that each cursor is valid for 60 minutes after the _initial_ request!

GraphQL
    
    
    query {
      next_items_page (cursor: "MSw5NzI4MDA5MDAsaV9YcmxJb0p1VEdYc1VWeGlxeF9kLDg4MiwzNXw0MTQ1NzU1MTE5") {
        cursor
        items {
          id
          name
        }
      }
    }

  3. This query returns another cursor value and the following 500 items on the board. Repeat the same query using the consecutive cursor values until you have paginated through the entire data set!

__Updated 8 months ago

* * *

[Making your first request](https://developer.monday.com/api-reference/docs/getting-started)[Working with multi-level boards](https://developer.monday.com/api-reference/docs/working-with-multi-level-boards)

Copy Page
