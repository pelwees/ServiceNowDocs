---
title: Install Vault plugins
description: Learn how to review and install the necessary plugins for ServiceNow Vault.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Configuring ServiceNow Vault, ServiceNow Vault]
---

# Install Vault plugins

Learn how to review and install the necessary plugins for ServiceNow Vault.

## Before you begin

Role required: Elevate to sn\_vault\_console.vault\_console\_admin role.

ServiceNow Vault is best used with other ServiceNow security products. Make the most of your tools and metrics by installing and configuring the plugins listed in step 3.

## Procedure

1.  Navigate to **All** &gt; **Vault** &gt; **Vault Console**.

2.  Review the status of your tools.

    |Status|Description|
    |------|-----------|
    |![Limited access](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../images/vault-tool-status-1.png)|Tool has a limited access license. Reported metrics may be affected or unavailable.|
    |![Included with platform](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../images/vault-tool-status-2.png)|Tool is included by default with the platform|
    |![Needs license](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../images/vault-tool-status-3.png)|Tool has no license. Reported metrics may be affected or unavailable.|
    |![Premium license](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../images/vault-tool-status-4.png)|Tool has full access.|

3.  If a status is either limited or needs a license, review its respective installation page.

<table id="table_bf1_qhb_1gc"><thead><tr><th>

Tool

</th><th>

Installation page

</th></tr></thead><tbody><tr><td>

[Data Discovery](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../security/concept/data-discovery-landing.md)

</td><td>

[Activating Data Discovery](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../security/task/activate-data-discovery.md)

</td></tr><tr><td>

[Data Classification](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../security/concept/data-classification.md)

</td><td>

Included with the platform.

</td></tr><tr><td>

[Data anonymization](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../data-privacy-store/concept/dps-data-anonymization.md)

</td><td>

[Activate data privacy](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../data-privacy-store/task/dps-activate-data-privacy.md)**Note:** Data anonymization is installed as part of [Data privacy](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../data-privacy-store/concept/dps-data-privacy.md).

</td></tr><tr><td>

[Cloud Encryption with Key Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../encryption-dare/concept/dare-overview.md)

</td><td>

[Requesting Cloud Encryption for instances with Now Support Service Catalog \[KB1117369\]](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1117369) article in the Now Support Knowledge Base

</td></tr><tr><td>

[Field Encryption](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../encryption/concept/field-encryption.md)

</td><td>

[Activate Field Encryption](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../now-platform-encryption/task/activate-platform-encryption.md)

</td></tr><tr><td>

-   [Zero Trust Access \(ZTA\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../../integrate/authentication/concept/session-access.md)
-   [Continuous Authentication \(CA\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../../integrate/authentication/concept/ca-homepage.md)


</td><td>

-   [Activating Zero Trust Access](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../../integrate/authentication/task/activate-session-access.md)
-   [Activating Continuous Authentication](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../../../integrate/authentication/task/activate-continuous-authentication.md)


</td></tr></tbody>
</table>
