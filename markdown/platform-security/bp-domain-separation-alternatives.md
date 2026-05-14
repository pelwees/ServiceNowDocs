---
title: Alternatives to domain separation
description: You can use a separate instance as an alternative to domain separation for your customers. A separate instance allows you the flexibility to meet the requirements for data separation within the groups and departments in an organization with little to no impact on others.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Recommended practices for service providers, Domain separation for service providers, Access Management]
---

# Alternatives to domain separation

You can use a separate instance as an alternative to domain separation for your customers. A separate instance allows you the flexibility to meet the requirements for data separation within the groups and departments in an organization with little to no impact on others.

## Separate instances

|Separate instance|Single instance - without domain|
|-----------------|--------------------------------|
|**Pros**|**Pros**|
|Built to suit each customer/organization|May address simple scenarios|
|Minimize impact of customization on others|Cost|
|Release schedule coordination|**Cons**|
|Clean separation|Extensive modifications to baseline code|
|Choose DATACENTER region|Modified base system code skipped during upgrades|
|**Cons**|Must address all secondary and supporting tables as well|
|Cost|Extensive testing required|
|Alignment of instances|No ServiceNow product team to evolve your custom code|
|Testing effort for upgrades| |
|Duplication of effort| |
|Integrations required| |

You can time upgrades and releases separately for each instance. However, if you choose to use separate instances, you need to do a lot of coordination with other people who are administering instances. By configuring an instance with contextual security, form views, reference qualifiers, filters, and robust conditions, you don't have to use domain separation in your company.

With a separate instance, you may address data and process separation but your instance owners must maintain and keep up with the extensive customizations that is required for separate instances.

**Parent Topic:**[Domain separation recommended practices for service providers](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-sep-recommended.md)

**Related topics**  


[Domain separation explained](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-what-is-domain-separation.md)

[Domain separation hierarchies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-sep-hierarchies.md)

[Context and domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-sep-context.md)

[Segregating and securing data with domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-segregate-secure.md)

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

[Domain assignments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-domain-assignment.md)

[Domain separation and the Customer Service Management \(CSM\) plugin](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-ds-and-csm.md)

[Context and domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../concept/bp-domain-sep-context.md)

[Service provider reference architecture](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-sp-reference-arch-ds.md)

