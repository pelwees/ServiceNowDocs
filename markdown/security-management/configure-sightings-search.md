---
title: Configure MISP sighting searches
description: Configure the ServiceNow AI Platform to do sighting searches for observables in the MISP instance. With this information, you can determine how often threats occur.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [MISP administration, MISP integration for Security Operations, Threat Intelligence integrations, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Configure MISP sighting searches

Configure the ServiceNow AI Platform to do sighting searches for observables in the MISP instance. With this information, you can determine how often threats occur.

## Before you begin

-   [Review the MISP user role and permissions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/misp-user-roles-and-permissions.md) that are required for using the MISP bi-directional features.
-   Role required: sn\_si.admin, sn\_ti.admin

## About this task

The [Security Operations Integration - Sightings Search workflow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../../security-operations-integrations/task/secops-integration-sightings-search-workflow.md) executes the sighting searches. This workflow accepts a list of observables, finds any implementing capabilities, creates the queries that are based on the sighting search configurations, and executes the searches that are based on the configured workflow.

The MISP integration for Security Operations provides a base system sighting search profile that enables you to configure automatic sighting searches. With this profile, you can access the related observable sighting information of an organization and also see the external sightings from other organizations.

## Procedure

1.  Navigate to **All** &gt; **MISP Integration** &gt; **Sighting Search Configuration**.

2.  Click **New**.

3.  On the form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Name|Name for the capability profile.|
    |Is saved search|Search configuration that is saved when you select this option. The saved search configuration queries are example queries. You can substitute them with the parameters for your environment and create additional saved search configurations as required.|
    |Sightings search source|Source for the sightings search. Select the MISP log store as the source.|
    |Active|Option that enables the saved search configuration. Only active search configurations can perform a sightings search.|
    |Observable type|Observable type such as the IP address, hash value, URL, and domain name.|
    |Maximum observable per search|Maximum number of observables that you can view from a search query.|
    |Search|Default search string that is `$(observable)`. However, you define your own search query by specifying the MISP log store supported parameters.|

4.  Click **Submit**.


## Result

You created a MISP sightings search configuration profile.

**Parent Topic:**[MISP administration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/misp-administration.md)

**Related topics**  


[Getting started with MISP integration for Security Operations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/get-started-with-misp-integration-for-security-operations.md)

[Install and configure the MISP integration for Security Operations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/install-and-configure-misp.md)

[Review the MISP integration settings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/review-the-misp-integration-settings.md)

[Configure how an automatic event is created](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/configure-automatic-event-creation-profile.md#)

[MISP event data](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/misp-event-data.md)

[Associated MISP events](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/associated-misp-events.md)

[MISP user information](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/misp-user-information.md)

[Domain separation and MISP](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/domain-separation-and-misp.md)

[Troubleshooting MISP integration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/troubleshooting-misp-integration.md)

