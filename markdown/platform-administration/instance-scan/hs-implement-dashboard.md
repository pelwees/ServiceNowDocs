---
title: Using the Instance Scan dashboard
description: Compare and analyze the results of the scans in your instance by representing it on the premium Performance Analytics \(PA\) dashboard.
locale: en-US
release: australia
product: Instance Scan
classification: instance-scan
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Using Instance Scan, Instance Scan, Maintain and monitor, Administer the ServiceNow AI Platform]
---

# Using the Instance Scan dashboard

Compare and analyze the results of the scans in your instance by representing it on the premium Performance Analytics \(PA\) dashboard.

## Before you begin

You've created some checks to execute the full scan. See [Create a check](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-create-health-check.md) and [Execute a full scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-execute-full-scan.md) for more information.

Role required: admin.

## Procedure

1.  Navigate to **All** &gt; **Instance Scan** &gt; **Dashboard**.

2.  Select an option from the **Instance Scan Category** or **Instance Scan Priority** list.

    **Note:** The dashboard is applicable only for full scans. The **Instance Scan Category** appears only if you have data or a finding in the result set that are applicable to the categories.

3.  Select the scan result from the Scan Results list that generates an unexpected number of check findings.

    A related list of findings related to only that scan is expanded.

    ![Image showing the scan that generated unexpected results and its related list of findings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-implement-dashboard.png)

4.  Select the scan column directly from the dashboard to display the related list of checks.

    ![Image showing how to select a particular scan result column](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-click.png)

    The related list of checks appears. The list also indicates the source that the finding has been retrieved from. ![Image showing checks for the selected health scan and the source of the problem](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-dashboard-related-list.png)


## Result

A dashboard showing the results of scans is created.

**Parent Topic:**[Using Instance Scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../concept/hs-using-scans.md)

**Related topics**  


[Create a check](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-create-health-check.md)

[Create a check suite](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hc-create-check-suite.md)

[Executing a scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../reference/hs-execute-scans.md)

[Schedule a full scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-schedule-full-scan.md)

[Schedule a suite scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hc-schedule-suite-scan.md)

[Monitoring a scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-progress-status-full-scan.md)

[Parallel scans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../concept/hs-parallel-scan.md)

[Reviewing of scans](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../reference/hs-review-scans.md)

[Queue your scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-queue-scan.md)

[Cancel a scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-cancel-scan.md)

