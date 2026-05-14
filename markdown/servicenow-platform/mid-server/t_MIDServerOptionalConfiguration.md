---
title: Set the MID Server JVM memory size
description: The MID Server starts with a default JVM memory allocation, but you can modify this setting in the configuration file.
locale: en-US
release: australia
product: MID Server
classification: mid-server
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [MID Server reference, MID Server, Manage instance data sources, Extend ServiceNow AI Platform capabilities]
---

# Set the MID Server JVM memory size

The MID Server starts with a default JVM memory allocation, but you can modify this setting in the configuration file.

## Before you begin

Role required: admin

<table id="table_l5y_xrf_khb"><tbody><tr><td>

![Links to each of the MID Server sections](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../image/MIDRefIconBar.png)

</td></tr></tbody>
</table>## About this task

In the base ServiceNow system, the MID Server JVM memory is set to 1024 MB, which is configured in the `\agent\conf\wrapper-override.conf` file in the MID Server installation directory. This setting might not be appropriate for the way your organization uses the MID Server. If you want the MID Server to work harder, allocate more resources to it. If the MID Server is located in a small branch office and runs in an environment where memory allocation is shared between a print server, mail server, or web proxy server, the allocation might have to be reduced.

**Note:** For a complete list of minimum MID Server requirements, see [MID Server system requirements](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/r_MIDServerSystemRequirements.md).

## Procedure

1.  Open the `\ServiceNow\<MID Server name>\agent\conf\wrapper-override.conf` file in a text editor.

    For more information about this file, see [Installing Multiple MID Servers on a Single System](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/t_InstallMultplMIDSvrOnASingleSys.md#).

2.  Locate the following lines in the file:

    ```
    # OPTIONAL: Maximum Java Heap Size (in MB)
    wrapper.java.maxmemory=1024
    ```

3.  Edit the memory allocation.

4.  Remove the comment tag \(\#\) from the memory allocation parameter.

5.  Save the file.

6.  Restart the MID Server service.


**Parent Topic:**[MID Server reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-server-reference-information.md)

**Related topics**  


[MID Server system requirements](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/r_MIDServerSystemRequirements.md)

[MID Server upgrades](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/c_UpgradeAndTestMIDServer.md)

[Resolving MID Server issues](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/r_MIDServerTroubleshooting.md)

[MID Server dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/c_MIDServerDashboard.md)

[MID Server properties](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/r_MIDServerProperties.md#)

[MID Server parameters](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/mid-server-parameters.md#)

[MID Server Configuration Parameter settings and priority](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/mid-config-param-priority.md)

[MID Server File Cleaner](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid_file_cleaner.md)

[MID Server protected records and reserved characters](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/mid-server-reserved-characters.md)

[MID Server privileged commands](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/c_PrivilegedCommandsForMIDServer.md#)

[MIDSystem methods](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/r_MIDSystemMethods.md)

[Manually start, stop, and restart a MID Server](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/t_InstallMIDServerAsWinService.md)

[MID Server heartbeat](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/r_MIDServerHeartbeat.md)

[Pause the MID Server](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/t_PauseTheMIDServer.md#)

