---
title: WMI connector methods
description: The Windows Management Instrumentation \(WMI\) connector methods act as interfaces with the WMI to send various requests and get responses in the RPA Desktop Design Studio.
locale: en-US
release: australia
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [ITSM connector, Automation components, RPA Desktop Design Studio, Workflow Data Fabric]
---

# WMI connector methods

The Windows Management Instrumentation \(WMI\) connector methods act as interfaces with the WMI to send various requests and get responses in the RPA Desktop Design Studio.

## Connect

Establishes a connection with the WMI. You must execute this method first before executing any other method.

-   **Input**

    [Hostname](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-input-hostname)

    [Username](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-input-username)

    [Password](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-connect-input-password)


## GetDiskDetails

Returns the disk details such as the name, manufacturer, model, and media type of a local or remote computer.

-   **Output**

    [Hashtable](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-wmi-getdiskdetails-output-hashtable)


## GetEnvironmentValue

Returns the environment variable values in the local or remote computers.

-   **Input**

    [Var](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-wmi-GetEnvironmentValue-input-var)

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-wmi-GetEnvironmentValue-output-returns)


## GetProcessesByCpuUsage

Returns the CPU usage by all processes in the remote or local computer.

-   **Output**

    [Return \(Sorted Dictionary\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#GetProcessesByCpuUsage-input-return)


## GetProcessesByMemUsage

Gets the memory usage by all processes in the remote or local computer.

-   **Output**

    [Return \(Sorted Dictionary\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#GetProcessesByMemUsage-output-return)


## PageFaultsPerSecond

Gets the total page exceptions per second. It returns the page exceptions as objects.

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#PageFaultsPerSecond-output-return)


## PageFilePercentUsage

Gets the usage of page files by the local or remote computers as percentages. It returns the page percentages as objects.

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#PageFilePercentUsage-output-return)


## PercentMemoryUsage

Returns the percentage of the total memory that is used in the local or remote computers. It returns the percentages as objects.

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#PercentMemoryUsage-output-return)


## PercentProcessorUsage

Gets the percentage of the total processes that are used in the local or remote computers. It returns the percentages as objects.

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#PercentProcessorUsage-output-return)


## Query

Queries a local or remote computer by specifying the class and filter.

-   **Input**

    [Class](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-wmi-class-input-class)

    [Filter](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-wmi-query-input-filter)

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#parameter-wmi-query-output-return)


## TotalPhysicalMemory

Provides the total available physical memory. It returns the output as an object.

## AvailableMBytes

Provides the total available megabytes.

-   **Output**

    [Return](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/connector-wmi-method-parameters.md#AvailableMBytes-output-return)


**Parent Topic:**[ITSM connector](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/../concept/itsm.md)

