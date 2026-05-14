---
title: Define the technique detection coverage
description: Define the technique detection coverage that your organization must measure and detect specific adversary techniques.
locale: en-US
release: australia
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [MITRE-ATT&amp;CK administration, MITRE-ATT&amp;CK framework overview, Threat Intelligence, Enterprise security case management applications, Security Operations]
---

# Define the technique detection coverage

Define the technique detection coverage that your organization must measure and detect specific adversary techniques.

## Before you begin

-   Role required: sn\_ti.admin, sn\_si.admin: write access
-   Role required: sn\_ti.read: read access

## About this task

The technique coverage definitions are used in the overall technique detection mapping. You can use the base system technique coverage. The [base system technique coverage](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/scoring-definition.md) consists of coverage types None, Poor, Fair, Good, Very Good, and Excellent. The base system technique coverage is also associated with pre-defined colors. You can customize the coverage type entries and colors, or create your own entries. For example, you can modify the base system coverage types to Not Applicable, Partial Coverage, and Complete Coverage. Alternatively, you can also create numerical measures for the coverage types such as 0-25 percent, 25–50 percent, and 50–100 percent. The type of modifications done to the base system coverage are not limited to the examples shared.

The customizations that you make to the coverage type and color are used in the [overall technique detection mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-technique-coverage.md) and also in the [heat map](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/mitre-att-ck-heatmap-and-navigator.md#).

**Note:** If you modify the base system coverage definition, the Coverage Type icons do not display with the techniques in the heat map. The heat map works as expected when you modify the same fields as the base system's-defined technique detection coverage and coverage colors. However, if you delete existing fields from the overall technique detection coverage, the heat map does not display the coverage type icons.

![Coverage type symbols are not displayed if you modify the coverage definition.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../image/mitre-heatmap-coverage-type.png)

## Procedure

1.  Navigate to **All** &gt; **Threat Intelligence** &gt; **MITRE ATT&amp;CK Administration** &gt; **Detection Coverage Definition**.

2.  Review the overall technique detection entries and customize the entries for your environment.

<table id="table_nb5_ldk_wnb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Overall Technique Detection Coverage

</td><td>

Name of the overall technique detection coverage. The [base system technique coverage](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/scoring-definition.md) consists of None, Poor, Fair, Good, Very Good, or Excellent.

</td></tr><tr><td>

Coverage Color

</td><td>

Color that is assigned to the detection coverage score. The color that you define is used for the technique detection coverage in the heat map.You can customize the colors using HEX codes and RGB\(A\) values.

</td></tr><tr><td>

Description

</td><td>

Overall technique detection coverage. See the base system definition in the [Scoring Definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/scoring-definition.md).

</td></tr></tbody>
</table>    The following illustration shows the Detection Coverage Definition list.

    ![Define the technique coverage.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../image/mitre-detection-coverage.png)

3.  To add an entry, click **New**, complete the entries, and click **Submit**.


-   **[MITRE-ATT&amp;CK Scoring definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../reference/scoring-definition.md)**  
Define your organization's MITRE-ATT&amp;CK scoring system so that you can measure how effectively your organization can detect specific adversary techniques.

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

[Extend the MITRE-ATT&amp;CK data](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/view-and-extend-information.md)

[Define the data source and detection tool mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/manage-mitre-att-ck-data-sources.md)

[Define the data source and data component mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-the-data-source-and-data-components.md)

[Map your technique detection coverage to a technique](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-technique-coverage.md)

[Define the mitigation coverage](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/define-the-mitigation-coverage.md)

[Map your mitigation coverage to a technique](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/map-your-mitigation-coverage-to-a-technique.md)

[Create and map detection rules](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/create-detection-rules.md)

[Auto-extract technique rules for importing MITRE-ATT&amp;CK information](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../concept/auto-extract-technique-rules.md#)

[Review threat group and MITRE-ATT&amp;CK techniques mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/review-threat-group-and-techniques-mapping.md)

[Threat group to technique heatmap definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/threat-group-to-technique-heatmap-definition.md)

[Review the MITRE-ATT&amp;CK system properties](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/configure-mitre-att-ck-properties.md)

