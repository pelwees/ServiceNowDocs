---
title: Security Incident Details section
description: This section displays the security incident form fields that are rendered from the security incident classic UI.
locale: en-US
release: australia
product: Security Incident Response
classification: security-incident-response
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Working with Security Incident Records, Use, Security Incident Response Workspace, Security Incident Response, Enterprise security case management applications, Security Operations]
---

# Security Incident Details section

This section displays the security incident form fields that are rendered from the security incident classic UI.

The Classic UI has a view called **SIRW** View created. This view is mapped to the **Details** tab in the workspace. Any customizations that are required need to be implemented in this view.

The form fields are grouped into the following sections and displayed on the Details tab form view. Select any of the section or jump to the respective section within the form:

-   Security Incident
-   Priority
-   Source
-   Parent
-   Assignment
-   Access Controls
-   Affected Items
-   Restriction
-   Resolution

The **Details** tab contains the **Activity** stream section within the details form itself for a quick access to the security analysts to add any comments and post it. Additionally, you can also use the **Email** option, to send email about this security incident to the necessary stakeholders.

![Malicious code activity view: Details tab.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/details-tab.png "Details tab and Activity stream")

**View the SIR Analyst Workspace view:**

1.  Navigate to **All** &gt; **Security Incident** &gt; **Show Open incidents**.
2.  Select any security incident record.
3.  Click on the context menu and select **View** &gt; **sirw**.

    **Note:** You can customize using **sirw** workspace view in the classic UI form.

    ![Classic UI security incident](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/sir-classic-view.png)

4.  The security incident workspace view is rendered as shown below.

    ![Security incident in SIR workspace view](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/classic-view-sirw.png "SIR workspace view")

5.  On the Security Incident record, right click and go to **Configure** &gt; **Form Layout**.

    ![Form layout](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/form-layout.png "Form layout")

6.  Drill down to the **Form view and section** and select **New** from **Section** to create a new section.

    ![Creating a new section](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/form-layout-section-view.png "Form layout - section view")

7.  Provide the new section name and select **OK**.

    For example, Incident form.

8.  The new section is created and added to the **Section**.

    ![Incident form section and Selected fields highlighted](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/add-section-fields.png)

9.  Select your new section and add the required section fields to the slush bucket and select **Save**.

    ![Adding fields to the new section](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/add-section-fields.png "Section fields")

10. The newly added section is displayed along with the existing section layout within the security incident form.

    ![Incident form tab highlighted](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../image/newly-added-section-fields.png)

11. Select **Switch to SIR workspace** to jump to the security incident form and the customized section within the **Details** tab of the workspace.

-   **[Security incident Details tab](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../reference/security-incident-details-form.md)**  
This section describes all the fields of the **Details** tab of a security incident.

**Parent Topic:**[Working with Security Incident Records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/using-analyst-workspace.md)

**Related topics**  


[Security Incident Overview section](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/security-incident-overview.md)

[SIR Workspace Orchestration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/security-incident-response-workspace-orchestration-activities.md)

[Security Incident Response Tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/security-incident-response-tasks.md)

[Security Incident Response Other Records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/security-incident-response-other-records.md#)

[Security Incident Response Post Incident Review](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/security-incident-response-post-incident-review.md)

[Update information in security incident related records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../task/edit-related-records-in-list.md)

[TISC integration within SIR Workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/../../secops-integration-threat-security-center/concept/tisc-sir-workspace.md)

[Reports in Security Incident Response](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/report-templates-sir.md)

[Collaborate using conference call or chat in Security Incident Response](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/collab-sir-call-chat.md)

[Viewing incident details with a relationship graph](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/sir-relationship-graph.md)

[MITRE attack and defend technique graph](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/security-incident-response/mitre-attack-defend-graph-sir.md)

