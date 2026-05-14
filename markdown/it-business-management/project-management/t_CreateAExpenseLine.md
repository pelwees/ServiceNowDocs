---
title: Create an expense line
description: A project expense line is cost associated with a specific source, such as a user, fixed asset, or a CI. Expense lines are part of project cost plans.
locale: en-US
release: australia
product: Project Management
classification: project-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Starting a project, Using Project Management, Project Management, Project Portfolio Management, Strategic Portfolio Management]
---

# Create an expense line

A project expense line is cost associated with a specific source, such as a user, fixed asset, or a CI. Expense lines are part of project cost plans.

## Before you begin

Role required: it\_project\_manager

Application required: Project Portfolio Management with Financials

## About this task

Only processed expense lines are considered for projects, project tasks, and demands. You can create multiple expense lines for a project or demand.

## Procedure

1.  Open the project form.

2.  In the related lists, select **Cost Plans**.

3.  Right-click on a cost plan.

4.  Select **Create Expense Line**.

5.  On the form, fill in the details.

    For more information, see [Expense line form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../reference/expense-line-form.md).

6.  Select **Submit**.

    **Note:**

    -   Imported processed expense lines are not rolled up to the Total actual cost field in Cost Plans.
    -   If you change the **Amount** of a Pending expense line and change the state to Processed, the latest value is captured in expense line and the same is rolled up to Total actual costs in Cost Plans.

## Result

Once the expense line is processed, the actual amount incurred becomes part of the cost plan.

The actual amount spent is recorded against the project cost plan under the appropriate expense type: **Capex** or **Opex**. Not providing a cost plan reference when creating an expense line, the actual cost is recorded at the project level in the cost plan related list.

If you create an expense line without populating the **Cost Plan** field, a [system-generated cost plans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/../concept/cost-plan-breakdown.md#) is created.

**Parent Topic:**[Starting a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProject.md)

**Related topics**  


[Create a project task from a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateATaskFromAProject.md)

[Create a parent-child relationship on the Project Task form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateParentChildRelationship.md)

[Create a monetary benefit plan for a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/create-project-benefit-plan.md)

[Create a non-monetary benefit plan for a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/create-a-non-monetary-benefit-plan-for-a-project.md)

[Associate monetary and non-monetary benefit plans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/associate-monetary-and-non-monetary-benefit-plans-project.md)

[Create a project cost plan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProjectCostPlan.md)

[Recalculating costs of all resource plans in a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/recalculate-resource-costs-of-a-project.md)

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

[Generate labor costs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/gen-cost-pln-prj-wrkspc.md)

[Create a project status report](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/t_CreateAProjectStatusReport.md)

[Allocate budget to a project](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/allocate-budget-to-project.md)

[Migrate budget of active projects to Next Experience](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/fin-migrate-budget-project-ppm.md)

[Migrate financial baselines of projects to Next Experience](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-business-management/project-management/migrate-fin-baselines-projects.md)

