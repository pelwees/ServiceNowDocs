---
title: SaaS License Management setup for large companies
description: Set up SaaS License Management for large companies to confirm that you can view all SaaS usage data in your ServiceNow instance.
locale: en-US
release: australia
product: SaaS License Management
classification: saas-license-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [SaaS License Management, Software Asset Management, IT Asset Management]
---

# SaaS License Management setup for large companies

Set up SaaS License Management for large companies to confirm that you can view all SaaS usage data in your ServiceNow instance.

Some large companies must update the **com.snc.pa.dc.max\_row\_count\_indicator\_source** system property before creating integration profiles. If either of the following conditions is true for your company, an admin must update this property.

-   If there are more than 50,000 user subscriptions for the [SaaS applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/create-integration-profile.md), excluding the subscriptions for [Adobe Cloud](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/adobe-cloud-integration.md) and [Microsoft 365](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/integrate-with-microsoft.md).
-   If there are more than 50,000 user subscriptions for Adobe Cloud and Microsoft 365 combined.

Update the **com.snc.pa.dc.max\_row\_count\_indicator\_source** system property to be the greater value between your subscriptions for the two groups. For example, if you have 60,000 user subscriptions for [SaaS applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/create-integration-profile.md) combined and 25,000 user subscriptions for [Adobe Cloud](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/adobe-cloud-integration.md) and [Microsoft 365](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/integrate-with-microsoft.md) combined, update the property to be `60,000`.

**Note:** For more information about how to use the **com.snc.pa.dc.max\_row\_count\_indicator\_source** property, see [Data collector properties](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/now-intelligence/performance-analytics/pa-properties.md).

**Parent Topic:**[SaaS License Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/sam-subscription-management.md)

**Related topics**  


[Request SaaS License Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/request-saas-license-management.md)

[SaaS Overview dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/saas-overview-dashboard.md)

[Integrate with SaaS applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/create-integration-profile.md)

[Integrate with SSO providers](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/saas-sso-integration.md)

[Playbook for SaaS integrations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/playbook-saas-integrations.md)

[Viewing your SaaS and SSO subscriptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/usage-summary-saas.md)

[Review a software reclamation rule](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/add-reclamation-rule-sub.md)

[Reclaiming user subscriptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/reclaiming-user-subscriptions-saas.md)

[Create a child alias to set up multiple integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../reuse/create-child-alias-saas.md)

[Create a child alias to set up multiple Cisco Webex integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/create-child-alias-webex.md)

[Create a child alias to set up multiple Confluence Cloud integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/create-child-alias-confluence.md)

[Create a child alias to set up multiple Jira integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/create-child-alias-jira.md)

[Associate a user with subscription records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/map-user-data.md)

[Disconnect SSO apps](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/disconnect-azure-ad-apps.md)

[Delete an integration profile](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/delete-saas-integration.md)

[Subscription identifiers for SaaS and SSO applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/subscription-identifiers.md#)

[Subscription exclusions for SaaS and SSO applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/subscription-exclusions.md#)

