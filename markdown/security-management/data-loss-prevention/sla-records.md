---
title: Create a Data Loss Prevention Incident Response SLA trigger
description: Create a Data Loss Prevention Incident Response SLA trigger condition that enables a prompt and efficient response to an incident when triggered.
locale: en-US
release: australia
product: Data Loss Prevention
classification: data-loss-prevention
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Administer, Data Loss Prevention Incident Response, Security Operations]
---

# Create a Data Loss Prevention Incident Response SLA trigger

Create a Data Loss Prevention Incident Response SLA trigger condition that enables a prompt and efficient response to an incident when triggered.

## Before you begin

Role required:

-   sn\_dlir.admin - Create, update, and delete DLP SLA triggers
-   sn\_dlir.analyst.read - Read Trigger table.

## Procedure

1.  Navigate to **All** &gt; **DLP Administration** &gt; **SLA Triggers**.

2.  Select **New** to create the SLA trigger.

    |Field|Description|
    |-----|-----------|
    |Name|Name of the trigger|
    |Order|Order in which the trigger is considered.|
    |Active|Option to evaluate the SLA trigger.|
    |Trigger when a DLP incident is updated|Option to evaluate the trigger condition on each update of the DLP incident.|

3.  Configure a condition by selecting the rule record and defining conditions in the **Trigger Condition** field.

    For example, the trigger condition to set SLAs on DLP incidents from an email scan source would be **\[Scan Source\]\[is\]\[Email SMTP\]**.

4.  Select **Submit**.


## Result

Once a task SLA record for a Data Loss Prevention Incident Response incident is created, the SLA records tab becomes visible for that particular incident in the workspace. This tab enables you to use an SLA system for your organization's task.

**Parent Topic:**[DLP Incident Response Administration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../concept/data-loss-prevention-administration.md)

**Related topics**  


[DLP default configuration settings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-data-loss-prevention.md)

[Create end user lookup rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-enduser-lookup-rules.md)

[Create assignment rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-assignment-rules.md)

[Create incident consolidation rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-incident-consolidation-rules-to-consolidate-your-dlp-incidents.md)

[Create response due date rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/setup-response-due-date-rules.md)

[Create Approval Rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-approval-rules.md)

[Create user instructions templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-and-manage-user-instructions-template-for-dlp-incidents.md)

[Create email templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-and-manage-email-templates.md)

[Create a Data Loss Prevention Incident Response SLA definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/dlp-sla-definitions.md)

[Create assessments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-and-manage-assessments-for-dlp-incidents.md)

[Configure response option for your DLP incidents](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-response-option-mapping.md)

[Create incident response option rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-end-user-action.md)

[Create age chart configurations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-age-chart.md)

[Create user delegate configurations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-delegation.md)

[Create repeat offender identification rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/repeat-offender-identification-rules.md)

[Create additional incident data fields](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-custom-fields-dlp.md)

[DLP SLA Definition form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../reference/dlp-sla-def-properties.md)

[Configure advanced settings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-advanced-settings-dlp.md)

[Monitor DLP Integration Run process](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../../dlp-microsoft/concept/configure-microsoft-dlp-integration-run-process.md)

[DLP Incident Access Restrictions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../concept/dlp-incident-access-restrictions.md)

[DLP Incidents Archival](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/dlp-archiving-rule.md)

