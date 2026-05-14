---
title: Project and project task states
description: In the base system, the states in project and project task inherit the states in Task table.
locale: en-US
release: australia
product: Project Management
classification: project-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Basics of Project Management, Exploring Project Management, Project Management, Project Portfolio Management, Strategic Portfolio Management]
---

# Project and project task states

In the base system, the states in project and project task inherit the states in Task table.

The states are grouped into different categories as shown below:

|State|Label|Category|
|-----|-----|--------|
|-5|Pending|Pending|
|1|Open|Open|
|2|Work in Progress|Work in Progress|
|3|Closed Complete|Closed|
|4|Closed Incomplete|Closed|
|7|Closed Skipped|Closed|

The category information for the states is declared in [dictionary override](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/table-administration-and-data-management/c_DictionaryOverrides.md) of State column in Planned task \(`planned_task`\) table in **Attributes** field. Planned task is the parent table for project and project task tables.

The start and end dates are displayed based on the project or task status:

-   Pending/Open: Planned start date is displayed.
-   Open/Work in Progress: Actual start date is displayed.
-   Closed: Actual end date is displayed.

**Parent Topic:**[Basics of Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ProjectTasks.md)

**Related topics**  


[Parent-child rollup task calculations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ParentChildRollupTaskCalcs.md)

[Project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../task/t_CreateAProjectTask.md)

[Schedule conflicts between project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/scheduling-conflicts.md)

[Change requests and project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ChangeRequestsAndProjectTasks.md)

[Project task checklists](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_project-task-checklists.md)

[Task resources](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_TaskResources.md)

[Composite Fields](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/pm-composite-fields.md)

[Cost plan breakdown](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/cost-plan-breakdown.md#)

[Actual project costs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/actual-project-costs.md)

[Types of external dependencies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/external-dependency-types.md)

[Project and portfolio funding](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../../project-portfolio-suite-with-financials/concept/c_ProjectAndPortfolioFunding.md)

[Project scheduling in Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/project-scheduling.md)

[Task constraints](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/task-constraints-project-management.md)

[View default project and project task state categories](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../task/view-default-project-task-states.md)

[Customize a state for project or project task](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../task/customize-project-task-states.md)

