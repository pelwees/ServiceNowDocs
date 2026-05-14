---
title: Update cost plan related to a resource plan
description: If a resource plan is associated to a project, project task, or demand and has a related cost plan, then a requester or a resource manager can update the related cost plan after updating the resource plan.
locale: en-US
release: australia
product: Resource Management
classification: resource-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Resource plans, Resource Management classic, Project Portfolio Management, Strategic Portfolio Management]
---

# Update cost plan related to a resource plan

If a resource plan is associated to a project, project task, or demand and has a related cost plan, then a requester or a resource manager can update the related cost plan after updating the resource plan.

## Before you begin

Role required: resource\_user or resource\_manager or it\_project\_manager or it\_demand\_manager

## About this task

If a resource plan does not have a related cost plan, the **Update Cost Plan** related link is not displayed for the resource plan.

## Procedure

1.  Save the updates to the resource plan.

2.  Click the **Update Cost Plan** related link.

    The cost plan associated to a resource plan is automatically updated as soon as the **Planned cost** in the resource plan is updated. The planned cost on resource plan gets updated when there is a change in:

    -   Planned hours
    -   User
    -   State
    -   Start and end dates

## Result

The cost plan associated to the resource plan is updated as follows:

-   If the resource plan is in Planning or Requested state, planned hours is updated in the cost plan.
-   If the resource plan is in Confirmed/Allocated state and the Confirmed/Allocated hours are less than planned hours, then the higher of the planned cost and Confirmed/Allocated cost is updated in the cost plan.
-   If the resource plan is in Confirmed/Allocated state and the Confirmed/Allocated hours are equal to or more than planned hours, then the Confirmed/Allocated cost is updated in the cost plan.

Cost from resource plan will be interfaced to the unit\_cost field on the Cost Plan \[cost\_plan\] table.

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

[Complete a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_CloseAResourcePlan.md)

[Cancel a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_CancelAResourcePlan.md)

[Delete a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_DeleteAResourcePlan.md)

[Extend a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/extend-resource-plan.md)

[Request extension of an allocated resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/request-extension-allocated-resource-plan.md)

[Allocate resources for the extended period](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/allocate-resources-for-extended-period.md)

[Reduce the duration of a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/reduce-resource-plan.md)

[Time zones in resource plans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/../concept/c_TimeZonesInResourcePlans.md)

[Associate a time card with a resource plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/resource-management/t_AssocATimeCardWithAResourcePlan.md)

