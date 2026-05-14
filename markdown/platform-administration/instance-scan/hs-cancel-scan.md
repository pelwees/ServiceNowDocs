---
title: Cancel a scan
description: Cancel or abort an ongoing scan by either selecting Cancel Scan in the scan execution modal or the Cancel Scan related link in the results record.
locale: en-US
release: australia
product: Instance Scan
classification: instance-scan
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Using Instance Scan, Instance Scan, Maintain and monitor, Administer the ServiceNow AI Platform]
---

# Cancel a scan

Cancel or abort an ongoing scan by either selecting Cancel Scan in the scan execution modal or the Cancel Scan related link in the results record.

## Before you begin

Role required: admin

## Procedure

1.  Navigate to **All** &gt; **Instance Scan** &gt; **Checks**.

    The list of checks shows up.

2.  Select a scan to run it on the selected check.

    ![Screenshot showing the execution modal.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-cancel-scan-module.png)

    The scan execution modal shows up.

3.  Select **Cancel Scan** to cancel the ongoing scan.

    The Cancel Scan modal shows up with the status of the cancelled transaction. You can also select **Go to Results** to see the results record of the selected scan.

    ![Screenshot showing cancelled scan](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-cancel-scan.png)

    **Note:** The **Cancel Scan** button won’t show up if the scan is complete \(successful or failed\).

4.  Select **Cancel Scan** related link to cancel the scan, if you have selected **Go to Results** in the previous step.

    ![Screenshot showing the status and cancel scan related link](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-cancel-scan-related-link.png)

    **Note:** The **Cancel Scan** related link is visible only if the scan is still running. The **Status** field in the Scan Results form say In Progress if the scan is still ongoing.

5.  Close the Cancel Scan modal or select **Go to Results** in the Cancel Scan modal.

    ![Screenshot showing cancelled status](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/../image/hs-status-cancel.png)

    The Scan Result record is updated. The **Status** field now says Cancelled.

6.  Scroll down to the **Scan Findings** related list.

    It generates the findings of the scan till the point it was cancelled.

    **Note:** Since the scan is already cancelled, the Cancel Scan related link doesn’t show up.


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

[Using the Instance Scan dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/instance-scan/hs-implement-dashboard.md)

