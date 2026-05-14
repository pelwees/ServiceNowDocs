---
title: Location migration
description: Learn how to migrate location data from the ServiceNow Locations table to the Workplace Location table to use them in Workplace Service Delivery applications.
locale: en-US
release: australia
product: Workplace Core
classification: workplace-core
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
breadcrumb: [Manage workplace safety activities, Workplace Core, Workplace Service Delivery, Employee Service Management]
---

# Location migration

Learn how to migrate location data from the ServiceNow Locations table to the Workplace Location table to use them in Workplace Service Delivery applications.

You can create a hierarchy to be used while migrating location data from the ServiceNow Location table \[cmn\_location\] to the Workplace Location \[sn\_wsd\_core\_workplace\_location\] table.

You can perform the following actions while creating a location migration record:

-   Configure location migration records by setting a parent location and a child location based on which the locations created in the Locations table \[cmn\_location\] are migrated to the Workplace Location \[sn\_wsd\_core\_workplace\_location\] table.
-   Specify conditions to filter the locations from the Locations table \[cmn\_location\] based on their Location types.

You can set a location hierarchy configuration as optional depending on the Floor infrastructure. For example, for the **Floor** &gt; **Area** &gt; **Room/Space** hierarchy, you can set the location migration configuration record of **Area** &gt; **Room** as an optional hierarchy because some floors might not have areas or only have spaces or rooms.

When you set a configuration as optional, then the records that don’t match that configuration are matched with the next hierarchy. For example, if there are locations that don’t match the **Area** &gt; **Room** hierarchy, then they’re matched with the next hierarchy, which is **Floor** &gt; **Room**. If there are Rooms that aren’t assigned to any Areas, then they’re matched with Floors because the Area is optional.

After migrating the locations, if you create a location in the Workplace Core application, the location is automatically added in the ServiceNow® Location \[cmn\_location\] table. You can configure the type of the location by setting Dictionary Overrides.

-   **[Configure location migration hierarchy](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/add-location-migration-hierarchy.md)**  
Create a hierarchy for how the location data from the ServiceNow® Location table \[cmn\_location\] must be migrated to the Workplace Location \[sn\_wsd\_core\_workplace\_location\] table of Workplace Service Delivery.
-   **[Set the location type in Location table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/set-loc-type-in-loc-table.md)**  
Set the location type of a location by creating a dictionary override of the table.

**Parent Topic:**[Manage workplace safety activities](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/manage-wsd-activites.md)

**Related topics**  


[Import your workspaces data from an Excel spreadsheet](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/import-excel-spreadsheet-workspace-data-wsd.md)

[Add a space type configuration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/add-space-type-configuration-wsd.md)

[Configure a workplace card](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/configure-workplace-card.md)

[Block a workplace location](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/block-workplace-location.md)

[Configure Workplace entity and entity types](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/workplace-entity.md)

[Managing Neighborhoods](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../../workplace-space-management/concept/neighborhoods.md)

[Enable favorites option for Workplace Service Portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/confgure-favourites-option-for-ws-portal-wsd.md)

[Create a workplace performer criteria](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/create-workplace-performer-criteria.md)

[Mapping employees to their designated workspaces](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/mapping-employees-to-existing-work-locations-wsd.md)

[Assign the workplace user role to employees](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/assign-workplace-user-role-to-employees-of-a-location-wsd.md)

[Configuring shifts for your workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/configuring-shifts-for-your-workplace-wsd.md)

[Managing workplace shifts that you own](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/managing-shifts-you-own-wsd.md)

[Managing workplace reservations for employees](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/managing-workplace-reservations-wsd.md)

[Setting and tracking arrivals at the workplace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/scheduling-employees-arrival-to-the-workplace-wsd.md)

[Approve employee workplace reservation requests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../task/approve-workplace-reservation-requests-wsd.md)

[Managing workplace tasks](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/managing-workplace-maintenance-tasks.md)

[Workplace knowledge management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/workplace-knowledge-mgmt-wsd.md)

[QR code management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/qr-code-mgmt.md)

[View workplace service usage analytics with Usage Insights](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-core/../reference/appsee-intergration-wsd.md)

