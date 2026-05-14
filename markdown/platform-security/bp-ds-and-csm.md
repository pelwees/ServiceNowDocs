---
title: Domain separation and the Customer Service Management \(CSM\) plugin
description: For the best outcome, be aware of how the properties in the CSM plugin work. When the plugin is enabled, you can see the status of your records in your domains.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Recommended practices for service providers, Domain separation for service providers, Access Management]
---

# Domain separation and the Customer Service Management \(CSM\) plugin

For the best outcome, be aware of how the properties in the CSM plugin work. When the plugin is enabled, you can see the status of your records in your domains.

Instance owners should contact Customer Service and Support to enable the **csm\_auto\_account\_domain\_generation** property.

**Note:** This base system property is located in the system properties table and is available after CSM plugins are enabled.

-   **What the property does**

    Whenever a new account in the Customer Service application is created, a domain is created and placed under the TOP domain. If the parent field on the account form is populated, and a new record is inserted, it creates that account as a subdomain of the parent.

-   **What happens if this property is not true and the domain is enabled**

    New account records in a domain-separated environment are automatically placed in the default domain.


In the header bar, you can see the status of the records with the plugin enabled.

**Parent Topic:**[Domain separation recommended practices for service providers](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-sep-recommended.md)

**Related topics**  


[Domain separation explained](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-what-is-domain-separation.md)

[Domain separation hierarchies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-sep-hierarchies.md)

[Context and domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-sep-context.md)

[Segregating and securing data with domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-segregate-secure.md)

[Alternatives to domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-separation-alternatives.md)

[Evaluating the need for domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-evaluation-dom-sep.md)

[Benefits of domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-advantages-dom-sep.md)

[How a database query works with domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-db-query-with-ds.md)

[Domain separation levels of support](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-levels.md)

[Service provider reference architecture](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-sp-reference-arch-ds.md)

[Domain separation terms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-terms-conditions.md)

[Domain-separate a custom table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-ds-custom-table.md)

[Customizing domain properties and themes](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-prop-themes.md)

[Managing domain separation for specific uses](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-emails-catalog-users.md)

[Configuring domain separation with the domain picker](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-picker-config-process.md)

[Domain separation performance considerations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-performance-considerations.md)

[Setting up domain hierarchies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-hierarchy.md)

[Checking domain logs for errors and warnings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-logs.md)

[Importance of the Default domain](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-default-domain.md)

[Contains queries and domain access](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-contains-domain-visibility.md)

[Domain paths query method](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-query-method.md)

[Slow queries and SQL debugging](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-debug-sql.md)

[Before Query business rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-before-query-business-rules.md)

[Avoiding domain path in scripts](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-no-domain-path-in-scripts.md)

[Domain assignments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-assignment.md)

