---
title: Maintenance plan fields for Enterprise Asset Management
description: A detailed description of all maintenance plan fields in the Enterprise Asset Management application.
locale: en-US
release: australia
product: Enterprise Asset Management
classification: enterprise-asset-management
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Enterprise Asset Management reference, Enterprise Asset Management, IT Asset Management]
---

# Maintenance plan fields for Enterprise Asset Management

A detailed description of all maintenance plan fields in the Enterprise Asset Management application.

## Maintenance Plan

|Field|Description|
|-----|-----------|
|Active|Option that indicates if the maintenance plan is active.|
|Name|Name of the maintenance plan.|
|Short description|Brief description of the maintenance plan.|

## Target Assets

<table id="table_r2v_f5w_cwb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Table

</td><td>

Target Enterprise Asset Management table that lists the enterprise assets that you want to apply the maintenance plan to. The default table is **Enterprise asset**.

</td></tr><tr><td>

Filter conditions

</td><td>

Filter conditions that enable you to apply the maintenance plan to only specific subsets of enterprise assets.

 You can add multiple filter conditions to a single maintenance plan using the following options:

-   **or**: Enables you to specify any of the conditions that an enterprise asset can meet to have the maintenance plan applied to it.
-   **and**: Enables you to specify all the conditions that an enterprise asset must meet to have the maintenance plan applied to it.
-   **+ New condition set**: Enables you to specify additional sets of conditions that an enterprise asset can meet to have the maintenance plan applied to it.

</td></tr><tr><td>

Apply to new matching records

</td><td>

Option to apply the maintenance plan to any subsequent enterprise assets that are added to the target Enterprise Asset Management table and meet the specified filter conditions.

</td></tr><tr><td>

Task creation policy

</td><td>

Policy that specifies what action you want to take when the maintenance plan is applied to an enterprise asset that is already under maintenance.

 Select one of the following options:

-   **Leave alone**: Prevents the creation of tasks for the new maintenance plan and the deletion of tasks that are associated with the existing maintenance plan.
-   **Cancel existing**: Deletes all tasks that are associated with the existing maintenance plan.
-   **Add to existing**: Adds both new tasks and existing active tasks to the new maintenance plan.

</td></tr></tbody>
</table>**Parent Topic:**[Enterprise Asset Management reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/../concept/reference-enterprise-asset-management.md)

**Related topics**  


[Domain separation and Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/../concept/domain-separation-eam.md)

[Enterprise Asset Management roles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/eam-roles.md)

[OT Asset Workspace roles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/ot-workspace-roles.md)

[Asset fields for enterprise assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/asset-fields-eam.md)

[Asset audit fields for enterprise assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/asset-audit-record-fields-eam.md)

[Audit results](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/audit-results-eam.md)

[Enterprise model categories and corresponding classes](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/enterprise-model-categories.md)

[Mandatory fields in the bulk import spreadsheets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/mandatory-bulk-fields.md)

[Normalization status for enterprise models](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/norm-status-eam.md)

[Model fields for Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/eam-model-fields.md)

[Contract fields for Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/contract-fields-eam.md)

[Maintenance schedule fields for Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/maintenance-schedule-fields-eam.md)

[Work plan fields for Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/wp-fields-eam.md)

[Work plan schedule fields for Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/work-plan-schedule-fields-eam.md)

[Expense line fields for Enterprise Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/expense-line-fields-eam.md)

[Fields inherited from a parent asset group to a sub group](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/subgroups-parent-fields-eam.md)

[Enterprise asset disposal order stages](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/eamasset-disposalorder-stages.md)

[Terminology for linear assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/terms-eam.md)

[Scheduled jobs and tables installed with normalization of firmware models](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/firmware-tables-jobs-ot.md)

[Asset put away task fields](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/enterprise-asset-management/put-away-task-form-eam.md)

