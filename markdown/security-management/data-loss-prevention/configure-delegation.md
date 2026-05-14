---
title: Create user delegate configurations
description: Prevent certain executives in the organization from receiving notifications about the incidents assigned or escalated to them.
locale: en-US
release: australia
product: Data Loss Prevention
classification: data-loss-prevention
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Administer, Data Loss Prevention Incident Response, Security Operations]
---

# Create user delegate configurations

Prevent certain executives in the organization from receiving notifications about the incidents assigned or escalated to them.

## Before you begin

Role required:

-   sn\_dlir.admin - Create, edit, and delete.
-   sn\_dlir.analyst and sn\_dlir.analyst\_read - View \(read-only\).

## About this task

Consider a scenario where the executive is a user who belongs to a leadership or executive group. The executive should not be sent emails about incident assignment or escalation. A delegated user can then take the necessary action on behalf of the executive.

Once a user has assigned a particular person, Henry, as a delegate, another user cannot assign Henry as a delegate again. Similarly, a delegate cannot assign another user as a delegate.

## Procedure

1.  Navigate to **All** &gt; **DLP Administration** &gt; **Delegate Configuration**.

2.  Click **New**.

3.  On the form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |User|Name of the user who needs a delegate for DLP incidents.|
    |Delegate|Name of the user who can respond to the DLP incident on behalf of the original end user.|

4.  Click **Submit**.


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

[Create a Data Loss Prevention Incident Response SLA trigger](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/sla-records.md)

[Create a Data Loss Prevention Incident Response SLA definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/dlp-sla-definitions.md)

[Create assessments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-and-manage-assessments-for-dlp-incidents.md)

[Configure response option for your DLP incidents](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-response-option-mapping.md)

[Create incident response option rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-end-user-action.md)

[Create age chart configurations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-age-chart.md)

[Create repeat offender identification rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/repeat-offender-identification-rules.md)

[Create additional incident data fields](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/create-custom-fields-dlp.md)

[DLP SLA Definition form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../reference/dlp-sla-def-properties.md)

[Configure advanced settings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/configure-advanced-settings-dlp.md)

[Monitor DLP Integration Run process](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../../dlp-microsoft/concept/configure-microsoft-dlp-integration-run-process.md)

[DLP Incident Access Restrictions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/../concept/dlp-incident-access-restrictions.md)

[DLP Incidents Archival](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/data-loss-prevention/dlp-archiving-rule.md)

