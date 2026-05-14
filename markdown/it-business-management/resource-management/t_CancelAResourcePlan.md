---
title: Cancel a resource plan
description: If a resource plan is no longer needed, you can cancel it which also cancels its past and future allocations.
locale: en-US
release: australia
product: Resource Management
classification: resource-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Resource plans, Resource Management classic, Project Portfolio Management, Strategic Portfolio Management]
---

# Cancel a resource plan

If a resource plan is no longer needed, you can cancel it which also cancels its past and future allocations.

## Before you begin

The resource plan to be canceled must be in the Planning, Requested, Confirmed, or Allocated state.

Role required: resource\_user, resource\_manager

## About this task

Project and demand managers can also [cancel resource plans from a project, project task, planning console, or demand](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/cancel-resource-plan-from-project-or-demand.md).

## Procedure

1.  Navigate to **All** &gt; **Resource** &gt; **Resource Plans** &gt; **All**.

2.  Open the resource plan record that you want to cancel.

3.  On the form header, select **Cancel**.


## Result

-   The resource plan moves into the Cancelled state.
-   All past and future allocations for the resource plan are also canceled. If there are any actual hours logged against an allocation, that allocation isn’t deleted. But the allocated hours become zero and the actual hours are retained.

## What to do next

If you want to make changes and use the plan again, edit a canceled plan. To move the resource plan back to Planning state, select **Re-plan**.

**Note:** The state of a resource plan can be changed back from Cancelled to Planning, only if it has no past allocations.

-   **[Cancel a resource plan from a project, planning console, or demand record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/cancel-resource-plan-from-project-or-demand.md)**  
If a project or a project task is marked Closed, the project manager can cancel the associated future resource plans. Similarly, the demand manager can cancel the future resource plans for a Closed or Deferred demand.

**Parent Topic:**[Resource plans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/../concept/c_ResourcePlans.md)

**Related topics**  


[Create a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_CreateResourcePlanProjectTask.md)

[Use Resource Finder to analyze resource availability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/create-resource-plan-with-finder.md)

[Create an operational resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/create-operational-plan.md)

[Request resources](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_RequestResourcePlanApproval.md)

[Confirm a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/confirm-resource-plan.md)

[Confirm and allocate a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/confirm-allocate-resource-plan.md)

[Request a change to a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_RequestAChangeToAResourcePlan.md)

[Recalculate costs of a resource plan of a project or demand](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/recalculate-resource-costs.md)

[Update cost plan related to a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_UpdateRelatedCostPlan.md)

[Complete a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_CloseAResourcePlan.md)

[Delete a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_DeleteAResourcePlan.md)

[Extend a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/extend-resource-plan.md)

[Request extension of an allocated resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/request-extension-allocated-resource-plan.md)

[Allocate resources for the extended period](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/allocate-resources-for-extended-period.md)

[Reduce the duration of a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/reduce-resource-plan.md)

[Time zones in resource plans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/../concept/c_TimeZonesInResourcePlans.md)

[Associate a time card with a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_AssocATimeCardWithAResourcePlan.md)

