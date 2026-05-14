---
title: Generate labor costs
description: Generate labor costs based on the planning attributes configured for financials in the planning attributes page for the resource assignments in a project.
locale: en-US
release: australia
product: Project Management
classification: project-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Starting a project, Using Project Management, Project Management, Project Portfolio Management, Strategic Portfolio Management]
---

# Generate labor costs

Generate labor costs based on the planning attributes configured for financials in the planning attributes page for the resource assignments in a project.

## Before you begin

-   Review the planning attributes enabled for financials. For more information, see [Using the Planning attributes](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../concept/planning-attributes.md).
-   Role required: it\_project\_manager

## Procedure

1.  Navigate to **All** &gt; **Project** &gt; **Projects** &gt; **All** and select the required project.

    Make sure that the resource assignments are finalized to generate cost plans. If there are no resource assignments for the project, migrate the resource plans to resource assignments. For more information, see [Migrate resource plans and cost plans for projects and demands](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../../resource-management/task/migrate-rsrc-plan-rsrc-asgnmnt.md).

2.  Generate labor costs using one of the following options.

<table id="choicetable_v4j_f5z_d1c"><thead><tr><th align="left" id="d55850e103">

Choice

</th><th align="left" id="d55850e106">

Description

</th></tr></thead><tbody><tr><td id="d55850e112">

**Using link from Financials Summary view**

</td><td>

1.  Select **Project Workbench** related link.
2.  Select **Financials** tab and select **Cost Plans**.
3.  Select **Generate Labor Costs**.


</td></tr><tr><td id="d55850e145">

**Using related links**

</td><td>

Select the **Generate Labor Costs** related link.

</td></tr><tr><td id="d55850e157">

**Activate a scheduled job**

</td><td>

1.  Navigate to **All** &gt; **System Definition** &gt; **Scheduled Jobs**.
2.  Filter the Name field to locate the **Generate labor costs for demands and projects** scheduled job and open it.
3.  Select **Active** and on the Scheduled Script Execution form, fill the fields.

For a description of the field names, see [Scheduled Script Execution Form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../reference/scheduled-script-execution-form.md).

4.  Select **Update**.


</td></tr></tbody>
</table>3.  Refresh the browser page to view attribute-based labor costs in the Cost Plans related list.


## Result

Attribute-based labor costs are created for the unique combination of attributes that are reflected as the name of the cost plans.

-   **[Activate a scheduled job to generate labor costs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/gen-labor-costs-scheduled-job-ppm.md#)**  
Activate and trigger a scheduled job to generate attribute-based labor costs for all the projects and demands at a required cadence.

**Parent Topic:**[Starting a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProject.md)

**Related topics**  


[Create a project task from a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateATaskFromAProject.md)

[Create a parent-child relationship on the Project Task form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateParentChildRelationship.md)

[Create a monetary benefit plan for a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/create-project-benefit-plan.md)

[Create a non-monetary benefit plan for a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/create-a-non-monetary-benefit-plan-for-a-project.md)

[Associate monetary and non-monetary benefit plans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/associate-monetary-and-non-monetary-benefit-plans-project.md)

[Create a project cost plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProjectCostPlan.md)

[Recalculating costs of all resource plans in a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/recalculate-resource-costs-of-a-project.md)

[Create an expense line](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAExpenseLine.md)

[Create and manage waterfall projects](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../../project-portfolio-suite/concept/c_CreateAndManageWaterfallProjects.md)

[Schedule a project from a start date](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/schedule-a-project-pm.md)

[Apply or change a task constraint](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/change-task-constraint-project-management.md)

[Update a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_UpdateAProjectInProgress.md)

[Copy a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CopyAProject.md)

[Assign a project schedule](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_UseAProjectSchedule.md)

[Create baseline of a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProjectBaseline.md)

[Create a milestone](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateMilestones.md)

[Activate project task email notifications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_ActivateProjTaskEmailNot.md)

[Change the planned start date of a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/change-planned-start-date-of-project.md)

[Create a cost type definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAResourceTypeDefinition.md)

[Costing add-on in Project Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../concept/c_ProjectManagementCostingAddOn.md)

[Create a project status report](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProjectStatusReport.md)

[Allocate budget to a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/allocate-budget-to-project.md)

[Migrate budget of active projects to Next Experience](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/fin-migrate-budget-project-ppm.md)

[Migrate financial baselines of projects to Next Experience](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/migrate-fin-baselines-projects.md)

[Activate a scheduled job to generate labor costs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/gen-labor-costs-scheduled-job-ppm.md#)

[Scheduled Script Execution Form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../reference/scheduled-script-execution-form.md)

