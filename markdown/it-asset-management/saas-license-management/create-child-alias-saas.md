---
title: Create a child alias to set up multiple integration profiles
description: Create a child alias to set up multiple integration profiles with unique connections and manage different configurations for each integration profile.
locale: en-US
release: australia
product: SaaS License Management
classification: saas-license-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [SaaS License Management, Software Asset Management, IT Asset Management]
---

# Create a child alias to set up multiple integration profiles

Create a child alias to set up multiple integration profiles with unique connections and manage different configurations for each integration profile.

## Before you begin

Role required: sam\_integrator

## Procedure

1.  Create an integration profile.

    For more information about creating an integration profile, see [Integrate with SaaS applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/create-integration-profile.md).

2.  Open the connection &amp; credential record set on the integration profile.

    If the **Parent Alias** field on an alias is empty, then the alias is a parent. If the field is filled, then the alias is a child of the alias specified in the **Parent Alias** field.

    -   If the record is a parent alias, select the **Child Aliases** tab.
    -   If the record is a child alias, select the **Parent Alias** record and then select the **Child Aliases** tab.
3.  Select **New**.

    **Tip:** If the **New** button isn't visible, change the scope to the respective application of the alias from the application scope.

4.  Reload the Connection &amp; Credential Aliases page.

5.  On the new child alias form that opens up, provide a name of your choice for the alias.

6.  Select **Submit**.

7.  Open the child alias record that you created, select **Create New Connection &amp; Credential**.

8.  Configure the connection and credential in the same way that you have done for the parent integration.

9.  After the connection is configured, return to the integration profile and then select the newly created child alias on the **Connection &amp; Credential** field.

10. Select **Save** and publish the integration profile.


**Parent Topic:**[SaaS License Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/sam-subscription-management.md)

**Related topics**  


[Request SaaS License Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/request-saas-license-management.md)

[SaaS License Management setup for large companies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/saas-setup-large-companies.md)

[SaaS Overview dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/saas-overview-dashboard.md)

[Integrate with SaaS applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/create-integration-profile.md)

[Integrate with SSO providers](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/saas-sso-integration.md)

[Playbook for SaaS integrations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/playbook-saas-integrations.md)

[Viewing your SaaS and SSO subscriptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/usage-summary-saas.md)

[Review a software reclamation rule](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/add-reclamation-rule-sub.md)

[Reclaiming user subscriptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/reclaiming-user-subscriptions-saas.md)

[Create a child alias to set up multiple Cisco Webex integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/create-child-alias-webex.md)

[Create a child alias to set up multiple Confluence Cloud integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/create-child-alias-confluence.md)

[Create a child alias to set up multiple Jira integration profiles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/create-child-alias-jira.md)

[Associate a user with subscription records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/map-user-data.md)

[Disconnect SSO apps](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../task/disconnect-azure-ad-apps.md)

[Delete an integration profile](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/delete-saas-integration.md)

[Subscription identifiers for SaaS and SSO applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/subscription-identifiers.md#)

[Subscription exclusions for SaaS and SSO applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/saas-license-management/../concept/subscription-exclusions.md#)

