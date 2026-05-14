---
title: Import your workspaces data from an Excel spreadsheet
description: Import your workspaces data from an Excel spreadsheet into the Workplace Core application.
locale: en-US
release: australia
product: Workplace Core
classification: workplace-core
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Manage workplace safety activities, Workplace Core, Workplace Service Delivery, Employee Service Management]
---

# Import your workspaces data from an Excel spreadsheet

Import your workspaces data from an Excel spreadsheet into the Workplace Core application.

## Before you begin

Role required: sn\_wsd\_core.admin

## About this task

Complete [Configuring spreadsheets to import workplace data](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/importing-workspace-data-wsd.md#).

## Procedure

1.  Navigate to **All** &gt; **System Import Sets** &gt; **Load Data**.

2.  Select **Existing table**.

3.  In the **Import set table** field, select **Space Staging \[sn\_wsd\_core\_space\_staging\]**.

4.  In the **Source of the import** field, select **File**.

5.  Select **Choose File** and select the source Excel spreadsheet.

6.  Specify the worksheet number in the **Sheet number** field and header row number in the **Header row** field.

7.  Select **Submit**.

    The imported data is now available in the new Import Set table.

8.  Select **Run Transform**.

    **Important:** Ensure that the Import set field shows sn\_wsd\_core\_space\_staging and the selected map is Space Transform map - sn\_wsd\_core\_space.

9.  Select **Transform**.

10. Verify that the data records were imported into the Spaces table by navigating to **Workplace Safety Management** &gt; **Space Administration** &gt; **Spaces**


## What to do next

[Define shifts for your workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/create-shifts-wsd.md)

**Parent Topic:**[Manage workplace safety activities](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/manage-wsd-activites.md)

**Related topics**  


[Add a space type configuration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/add-space-type-configuration-wsd.md)

[Configure a workplace card](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/configure-workplace-card.md)

[Block a workplace location](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/block-workplace-location.md)

[Configure Workplace entity and entity types](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/workplace-entity.md)

[Managing Neighborhoods](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../../workplace-space-management/concept/neighborhoods.md)

[Enable favorites option for Workplace Service Portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/confgure-favourites-option-for-ws-portal-wsd.md)

[Create a workplace performer criteria](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/create-workplace-performer-criteria.md)

[Mapping employees to their designated workspaces](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/mapping-employees-to-existing-work-locations-wsd.md)

[Assign the workplace user role to employees](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/assign-workplace-user-role-to-employees-of-a-location-wsd.md)

[Configuring shifts for your workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/configuring-shifts-for-your-workplace-wsd.md)

[Managing workplace shifts that you own](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/managing-shifts-you-own-wsd.md)

[Managing workplace reservations for employees](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/managing-workplace-reservations-wsd.md)

[Setting and tracking arrivals at the workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/scheduling-employees-arrival-to-the-workplace-wsd.md)

[Approve employee workplace reservation requests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/approve-workplace-reservation-requests-wsd.md)

[Managing workplace tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/managing-workplace-maintenance-tasks.md)

[Workplace knowledge management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/workplace-knowledge-mgmt-wsd.md)

[QR code management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/qr-code-mgmt.md)

[Location migration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../concept/location-migration.md)

[View workplace service usage analytics with Usage Insights](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../reference/appsee-intergration-wsd.md)

[Run an import](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/system-import-sets/t_RunImport.md)

[Create a transform map](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/integrate-applications/system-import-sets/t_CreateATransformMap.md)

