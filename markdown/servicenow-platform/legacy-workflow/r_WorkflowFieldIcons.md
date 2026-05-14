---
title: Workflow stage field icons and tooltips
description: A workflow stage field displays icons to indicate the workflow stage.Based on the stage renderer selected for a workflow, workflow stage icons may display tooltips with detailed information about a stage.
locale: en-US
release: australia
product: Legacy Workflow
classification: legacy-workflow
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Create a workflow stage field, Workflow stages, Workflow management, Classic Workflow, ServiceNow AI Platform Additional Capabilities, Extend ServiceNow AI Platform capabilities]
---

# Workflow stage field icons and tooltips

A workflow stage field displays icons to indicate the workflow stage.

Based on the stage renderer selected for the workflow, these icons may display a tooltip with additional information.

|Icon|Workflow stage|
|----|--------------|
|![Current active step icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/WorkflowActive.png)|Current active step|
|![Approval pending icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/WorkflowAwaiting.png)|Approval pending|
|![Approval rejected icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/WorkflowRejected.png)|Approval rejected|
|![Complete icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/WorkflowComplete.png)|Complete|
|![Late or Canceled icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/WorkflowLate.png)|Late \(Change/Request\) or Canceled \(Catalog\)|
|![Skipped icon](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/WorkflowSkipped.png)|Skipped \(Catalog only\)|

**Parent Topic:**[Create a workflow stage field](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../task/t_CreateAWorkflowStageField.md)

## Stage tooltips

Based on the stage renderer selected for a workflow, workflow stage icons may display tooltips with detailed information about a stage.

<table id="table_zkz_1kh_hr"><thead><tr><th>

Renderer

</th><th>

Tooltip behavior

</th></tr></thead><tbody><tr><td>

Legacy

</td><td>

When a user points to a stage, the tooltip displays the name of the stage. In the expanded view, the activity status appears in parentheses next to the stage.

 ![Stage tooltip with no name of approver.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/stage-tooltip-no-approver.png)

</td></tr><tr><td>

Other renderers

</td><td>

When a user points to a stage, the tooltip displays the name of the stage. If the stage is a gated approval, the tooltip also shows the name of the approver. In the expanded view, the activity status appears in parentheses next to the stage.

 ![Stage tooltip that includes approver.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/legacy-workflow/../image/stage-tooltip-includes-approver.png)

</td></tr></tbody>
</table>If you do not want the approver's name included in the tooltip, navigate to **System Properties** &gt; **Service Catalog** and clear the **Show the current pending approver's name in the stage widget mouseover** check box.

![](../image/ApprovalHover2.png "Property for displaying pending approver's name")

