---
title: Types of external dependencies
description: The Project management application supports two types of external dependencies - hard and soft.
locale: en-US
release: australia
product: Project Management
classification: project-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Basics of Project Management, Exploring Project Management, Project Management, Project Portfolio Management, Strategic Portfolio Management]
---

# Types of external dependencies

The Project management application supports two types of external dependencies - hard and soft.

The type of external dependency can be set during [adding a dependency](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../task/create-external-dependency-planning-console.md) between two projects tasks on the planning console.

## Hard dependencies

In a hard dependency, any changes made in the predecessor project are automatically propagated to the successor project. A [notification](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../reference/r_PlanningConsoleTasks.md#table_ukw_ftd_2s) for the changes made is triggered in the successor project. The following image shows the process flow for a hard dependency type:

![Process flow for a hard dependency type](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../image/ExternalHardDependency.png "External hard dependency")

## Soft dependencies

In a soft dependency, any changes made in the predecessor project trigger a notification in the successor project. As the project manager of the successor project, you can choose to accept or reject the changes in the notification. If you accept the notification changes, the changes in the predecessor project are synced to the successor project and the project is recalculated. If you reject the notification changes, the changes are not propagated to the successor project. The following image shows the process flow for a soft dependency type:

![Process flow for a soft dependency type](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../image/ExternalSoftDependency.png "External soft dependency")

**Parent Topic:**[Basics of Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ProjectTasks.md)

**Related topics**  


[Parent-child rollup task calculations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ParentChildRollupTaskCalcs.md)

[Project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../task/t_CreateAProjectTask.md)

[Schedule conflicts between project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/scheduling-conflicts.md)

[Change requests and project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ChangeRequestsAndProjectTasks.md)

[Project task checklists](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_project-task-checklists.md)

[Task resources](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_TaskResources.md)

[Project and project task states](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/project-and-project-task-states.md)

[Composite Fields](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/pm-composite-fields.md)

[Cost plan breakdown](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/cost-plan-breakdown.md#)

[Actual project costs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/actual-project-costs.md)

[Project and portfolio funding](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../../project-portfolio-suite-with-financials/concept/c_ProjectAndPortfolioFunding.md)

[Project scheduling in Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/project-scheduling.md)

[Task constraints](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/task-constraints-project-management.md)

