---
title: Contains queries and domain access
description: Use a "contains" query only in special cases, such as when users or groups need to see data from a domain that they don't have access to, but you don't want to move those users to a domain. Creating domain "contains" and user or group access for a domain should be an exception, only when absolutely needed.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Recommended practices for service providers, Domain separation for service providers, Access Management]
---

# Contains queries and domain access

Use a "contains" query only in special cases, such as when users or groups need to see data from a domain that they don't have access to, but you don't want to move those users to a domain. Creating domain "contains" and user or group access for a domain should be an exception, only when absolutely needed.

"Contains" is a domain-to-domain relationship that is many-to-many, and has no effect on the flow of process. If you create a large number of domain "contains" relationships or provide broad access, you will generate queries with too many OR conditions. OR conditions are slow and impact the performance of your instance. Instead of using too many "contains" relationships, set up your domain hierarchy as follows:

![Sample query](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../image/bp-contains-domain-visibility.png "Sample query")

Before you move users to a domain, make sure that they really should have access to that domain. Weigh the benefits and limitations. The query above is for just one contains relationship. If you have a domain that contains another domain, and that domain is the parent of a number of other domains, you will have many more OR conditions. Be careful when you create a domain map so that you do not impact the performance of your instance.

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

[Domain paths query method](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-query-method.md)

[Slow queries and SQL debugging](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-debug-sql.md)

[Before Query business rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-before-query-business-rules.md)

[Avoiding domain path in scripts](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-no-domain-path-in-scripts.md)

[Domain assignments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-assignment.md)

[Domain separation and the Customer Service Management \(CSM\) plugin](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-ds-and-csm.md)

