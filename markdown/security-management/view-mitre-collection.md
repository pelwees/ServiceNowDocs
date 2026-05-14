---
title: Manage matrices
description: Manage the matrices that have been imported from the MITRE TAXII collections. Matrices are a collection of tactics and techniques. You can view the matrices to review if your collections are available in the MITRE-ATT&amp;CK repository.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [MITRE-ATT&amp;CK administration, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Manage matrices

Manage the matrices that have been imported from the MITRE TAXII collections. Matrices are a collection of tactics and techniques. You can view the matrices to review if your collections are available in the MITRE-ATT&amp;CK repository.

## Before you begin

**Note:** Review and verify that only the matrix you intend to use in your organization is set to active and disable the other matrices. For example, if you intend to use the Enterprise ATT&amp;CK matrix, then the Enterprise ATT&amp;CK matrix is activated at the [TAXII collection](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/setup-mitre-profile.md) level and in the Matrices level. Disable the other Mobile ATT&amp;CK and ICS ATT&amp;CK matrices at the TAXII collection and at the Matrices level.

Role required:

-   sn\_ti.admin: delete access
-   sn\_ti.read: read access
-   sn\_ti.write: create, write access

## Procedure

1.  Navigate to **All** &gt; **Threat Intelligence** &gt; **MITRE ATT&amp;CK Repository** &gt; **Matrices**.

    All matrices are disabled by default.

2.  To activate a matrix, point to **Active**, double-click, and select **true**.

3.  To view all the associated information, click a matrix.

4.  To view all the tactics that are associated with this collection, click the **MITRE Tactics** tab.

5.  To view additional details and the techniques that are associated with a selected tactic, click a tactic.

6.  Under the **MITRE ATT&amp;CK Techniques** tab, select a technique.

7.  Under the related lists, view the associations that are available for the technique that you selected.

    In the following illustration, you can see the navigational path from the Enterprise ATT&amp;CK matrix, to the Initial Access \(TA0001\) tactic, and then to the Phishing \(T1566\) technique. On the Attack Pattern - Phishing technique page, you can view the related list - Tactic, Sub Technique, Group, Mitigation, External References, Malware, and Tools.

    ![Threat Intelligence: MITRE ATT&CK matrix.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../image/enterprise-matrice-view.gif)


## What to do next

You can [extend the information](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/view-and-extend-information.md) in some of these related list objects based on the technique that you selected. For example, you can add new information for Group, Mitigation, External References, Malware, and Tools.

**Parent Topic:**[MITRE-ATT&amp;CK administration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/mitre-att-ck-administration.md)

**Related topics**  


[Get started with MITRE-ATT&amp;CK framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/get-started-with-mitre.md)

[Understand the MITRE to STIX data model](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/understand-the-mitre-to-stix-data-model-mapping.md)

[Domain separation and MITRE-ATT&amp;CK](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/domain-separation-and-mitre-att-ck.md)

[Set up the MITRE-ATT&amp;CK framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/setup-mitre-profile.md)

[Manage techniques](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/view-techniques.md)

[Manage mitigations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-mitigations.md)

[Manage groups](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-groups-threat-intel.md)

[Manage malware](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-malware.md)

[Manage tools](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-tools.md)

[Manage MITRE relationships](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-mitre-relationships.md)

[Manage CVE and technique mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-cve-and-technique-mapping.md)

[Extend the MITRE-ATT&amp;CK data](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/view-and-extend-information.md)

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

