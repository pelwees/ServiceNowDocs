---
title: Avoiding domain path in scripts
description: Domain paths can cause the values of your script to change or even break, so don't use them in scripts.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Recommended practices for service providers, Domain separation for service providers, Access Management]
---

# Avoiding domain path in scripts

Domain paths can cause the values of your script to change or even break, so don't use them in scripts.

Your script should not depend on the domain path because if you ever change the domain hierarchy, the domain path recalculates and its value changes. When this happens, your scripts are useless or can throw errors or break. The best strategy is not to write your scripts based on domain paths.

Use the **sys\_domain** field in your scripts rather than depending on the domain path. If you ever change the domain hierarchy, the domain path recalculates and its value changes, which can cause your scripts to be useless, throw errors, or break. Look for base system business rules, which use the **sys\_domain** field, to get some ideas before creating your own scripts.

The ServiceNow platform does not capture the sys\_domain\_path values in an update set in order to avoid issues with differences in the domain hierarchy for each instance. Therefore, you should validate the domain hierarchy after you import an update set to ensure that the domain path values for your records are correct.

To learn more about domain path, see [Request domain separation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../task/t_ActivateDomainSeparation.md) and [Domain Separation Center](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/domain-separation-center.md).

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

[Domain assignments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/../reference/bp-domain-assignment.md)

[Domain separation and the Customer Service Management \(CSM\) plugin](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-security/bp-ds-and-csm.md)

