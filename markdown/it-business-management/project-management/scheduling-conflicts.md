---
title: Schedule conflicts between project tasks
description: Scheduling conflict helps you to identify project tasks that are not honoring dependencies. A scheduling conflict occurs when one project task prevents other task from starting on the specified date because of dependencies or constraint types.
locale: en-US
release: australia
product: Project Management
classification: project-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Basics of Project Management, Exploring Project Management, Project Management, Project Portfolio Management, Strategic Portfolio Management]
---

# Schedule conflicts between project tasks

Scheduling conflict helps you to identify project tasks that are not honoring dependencies. A scheduling conflict occurs when one project task prevents other task from starting on the specified date because of dependencies or constraint types.

A scheduling conflict occurs when any action such as applying a dependency, changing constraint type, or constraint date causes the task start date to violate the project's constraint date.

When a scheduling conflict occurs, the system warns you about the conflict. You can choose to cancel the action that is causing the conflict or continue with the conflict. If you choose to continue with the conflict, the constraint date is given highest precedence and dates are recalculated. The start date is moved till allowed by the task constraint date, but dependency is not honored.

For example, consider the following scenario:

For a project with project task's **Constraint date** set as 20 January, there are two tasks:

-   T1 with constraint type set to As soon as possible and start date of 20 January.
-   T2 with constraint type set to Start no later than and start date of 20 January.

If you add an FS dependency between tasks T1 and T2, the task T2 should start on 21 January, but due to Start no later than constraint, task T2 cannot start on 21 January. This inability of starting task T2 on the specified date is an example of conflict.

In this example, if you choose to proceed with the conflict, the start date of task T2 is moved to 20 January which is the constraint date.

Scheduling conflict between tasks is shown for tasks with **Start no later than** and **Start on specific date** time constraints.

If you want the task to honor the dependency and adjust the start accordingly, change the constraint type of the task to **Start ASAP**.

When a scheduling conflict is identified, you can identify such tasks in the planning console.

-   The client-side planning console displays a pop-up message with an option to proceed with the conflict or cancel the action. If you proceed with the conflict, the constraint type is applied or date is changed appropriately to the next feasible date.
-   The calendar icon \(![Calendar icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../image/calendar-icon.png)\) on the client side planning console changes to red \(![Conflict icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../image/pc-task-dep-icon.png)\) to indicate the conflict.
-   The calendar icon on the server side planning console changes to red \(![Conflict icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../image/pc-task-dep-icon.png)\) to indicate the conflict.

**Parent Topic:**[Basics of Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ProjectTasks.md)

**Related topics**  


[Parent-child rollup task calculations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ParentChildRollupTaskCalcs.md)

[Project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../task/t_CreateAProjectTask.md)

[Change requests and project tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_ChangeRequestsAndProjectTasks.md)

[Project task checklists](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_project-task-checklists.md)

[Task resources](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/c_TaskResources.md)

[Project and project task states](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/project-and-project-task-states.md)

[Composite Fields](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/pm-composite-fields.md)

[Cost plan breakdown](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/cost-plan-breakdown.md#)

[Actual project costs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/actual-project-costs.md)

[Types of external dependencies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/external-dependency-types.md)

[Project and portfolio funding](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../../project-portfolio-suite-with-financials/concept/c_ProjectAndPortfolioFunding.md)

[Project scheduling in Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/project-scheduling.md)

[Task constraints](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/task-constraints-project-management.md)

