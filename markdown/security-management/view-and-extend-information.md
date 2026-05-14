---
title: Extend the MITRE-ATT&amp;CK data
description: Extend the MITRE-ATT&amp;CK repository data in the ServiceNow AI Platform by enriching it.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [MITRE-ATT&amp;CK administration, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Extend the MITRE-ATT&amp;CK data

Extend the MITRE-ATT&amp;CK repository data in the ServiceNow AI Platform by enriching it.

## Before you begin

Role required:

-   sn\_ti.admin: delete access
-   sn\_ti.read: read access
-   sn\_ti.write: create, write access

## About this task

You can extend the Malware, Group, Mitigation, and Tool objects to a technique in the MITRE-ATT&amp;CK repository.

You can create a new object and establish a relationship between a technique and the new object in the MITRE ATT&amp;CK Repository module, but you can't define the relationship type in this module. For more information about defining relationship types, see [object to object relationships](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/define-object-object.md). To define a relationship type, navigate to the **Threat Intelligence** &gt; **IoC Repository** &gt; **Object-Object Relationships** module.

If you map the relationship type between an existing technique and an existing object, then you must define the technique as the target object and the object as the source object. To do so, navigate to the **IoC Repository** &gt; **Object-Object Relationships** module.

You can create a group and associate it with an attack pattern, but in the MITRE ATT&amp;CK Repository, you can only establish the relationship between the group and the attack pattern. To define the object-to-object relationship type, you must do so in the IoC Repository.

**Note:** Any customizations that you make to the objects are saved during scheduled updates.

## Procedure

1.  Navigate to **Threat Intelligence** &gt; **MITRE ATT&amp;CK Repository** &gt; **Techniques**.

2.  Click a techniques or sub-technique to view all the associated information with this technique.

    In the following illustration, you can see that the Botnet \(T1584.005\) technique is not associated with any group. If you have additional information about a technique or sub-technique, you can enrich it by adding or modifying the information.![Associate a Botnet with another object.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../image/mitre-botnet.png)

3.  Click a related list to enrich its data to associate it with a new group.

    In the following illustration, a group, Custom1, has been associated with the Botnet sub-technique.

    ![Extend MITRE object information by enriching its data.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../image/mitre-extend-object.gif)


**Parent Topic:**[MITRE-ATT&amp;CK administration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/mitre-att-ck-administration.md)

**Related topics**  


[Get started with MITRE-ATT&amp;CK framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/get-started-with-mitre.md)

[Understand the MITRE to STIX data model](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/understand-the-mitre-to-stix-data-model-mapping.md)

[Domain separation and MITRE-ATT&amp;CK](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/domain-separation-and-mitre-att-ck.md)

[Set up the MITRE-ATT&amp;CK framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/setup-mitre-profile.md)

[Manage matrices](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/view-mitre-collection.md)

[Manage techniques](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/view-techniques.md)

[Manage mitigations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-mitigations.md)

[Manage groups](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-groups-threat-intel.md)

[Manage malware](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-malware.md)

[Manage tools](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-tools.md)

[Manage MITRE relationships](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-mitre-relationships.md)

[Manage CVE and technique mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-cve-and-technique-mapping.md)

[Define the data source and detection tool mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-mitre-att-ck-data-sources.md)

[Define the data source and data component mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-the-data-source-and-data-components.md)

[Define the technique detection coverage](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/define-technique-coverage.md)

[Map your technique detection coverage to a technique](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-technique-coverage.md)

[Define the mitigation coverage](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/define-the-mitigation-coverage.md)

[Map your mitigation coverage to a technique](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-your-mitigation-coverage-to-a-technique.md)

[Create and map detection rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/create-detection-rules.md)

[Auto-extract technique rules for importing MITRE-ATT&amp;CK information](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/auto-extract-technique-rules.md#)

[Review threat group and MITRE-ATT&amp;CK techniques mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/review-threat-group-and-techniques-mapping.md)

[Threat group to technique heatmap definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/threat-group-to-technique-heatmap-definition.md)

[Review the MITRE-ATT&amp;CK system properties](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/configure-mitre-att-ck-properties.md)

