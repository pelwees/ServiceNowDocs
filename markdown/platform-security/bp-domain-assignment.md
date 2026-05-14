---
title: Domain assignments
description: How you assign a domain impacts the value of the sys\_domain field. The assignments contain designs and business properties that affect how the application functions in each domain.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Recommended practices for service providers, Domain separation for service providers, Access Management]
---

# Domain assignments

How you assign a domain impacts the value of the sys\_domain field. The assignments contain designs and business properties that affect how the application functions in each domain.

## Value of the sys\_domain field

The value of the **sys\_domain** field contains the domain that is assigned to the record by any of the following:

-   Company to which the user belongs
-   Business rule that is used when creating the record
-   Module that is used when creating the record
-   Form template that is used when creating the record
-   Domain of the parent record
-   Domain that is assigned to the User record
-   Domain of the user who creates it

Make sure that your domain assignment strategies and designs are well documented and tested so that you are creating records as those strategies and designs are inserted into the correct domain. That way you can see that the properties of each domain should you need to duplicate or modify them.

**Parent Topic:**[Domain separation recommended practices for service providers](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-sep-recommended.md)

**Related topics**  


[Domain separation explained](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-what-is-domain-separation.md)

[Domain separation hierarchies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-sep-hierarchies.md)

[Context and domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-sep-context.md)

[Segregating and securing data with domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-segregate-secure.md)

[Alternatives to domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-separation-alternatives.md)

[Evaluating the need for domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-evaluation-dom-sep.md)

[Benefits of domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-advantages-dom-sep.md)

[How a database query works with domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-db-query-with-ds.md)

[Domain separation levels of support](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-levels.md)

[Service provider reference architecture](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-sp-reference-arch-ds.md)

[Domain separation terms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-terms-conditions.md)

[Domain-separate a custom table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-ds-custom-table.md)

[Customizing domain properties and themes](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-prop-themes.md)

[Managing domain separation for specific uses](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-emails-catalog-users.md)

[Configuring domain separation with the domain picker](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-picker-config-process.md)

[Domain separation performance considerations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-performance-considerations.md)

[Setting up domain hierarchies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-hierarchy.md)

[Checking domain logs for errors and warnings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-logs.md)

[Importance of the Default domain](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-default-domain.md)

[Contains queries and domain access](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-contains-domain-visibility.md)

[Domain paths query method](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-query-method.md)

[Slow queries and SQL debugging](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-debug-sql.md)

[Before Query business rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-before-query-business-rules.md)

[Avoiding domain path in scripts](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-no-domain-path-in-scripts.md)

[Domain separation and the Customer Service Management \(CSM\) plugin](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-ds-and-csm.md)

