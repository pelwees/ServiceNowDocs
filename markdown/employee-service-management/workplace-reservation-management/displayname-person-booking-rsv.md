---
title: Display name of the person reserving a space
description: Display the name of a person who booked a space on the floor map.
locale: en-US
release: australia
product: Workplace Reservation Management
classification: workplace-reservation-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Configure Workplace Reservation Management portal, Workplace Reservation Management, Workplace Service Delivery, Employee Service Management]
---

# Display name of the person reserving a space

Display the name of a person who booked a space on the floor map.

## Before you begin

On the floor map, when a space is booked, an option to display the name of the person who reserved the space is available.

Verify that the following plugins are installed:

-   Workplace Core
-   Indoor Mapping
-   Workplace Reservation Management

Role required: admin

## Procedure

1.  In the navigation filter search context, enter **sys\_properties.list**.

    The System Properties \[sys\_properties\] table displays a list of properties.

2.  Search for **sn\_wsd\_core.floor\_plan.portal.show\_reservation\_details** and set the Workplace Core property **sn\_wsd\_core.floor\_plan.portal.show\_reservation\_details** to **true**.

3.  Make a reservation or check for an existing reservation in Workplace Reservation Management.

    For more information, see [Create a reservation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/create-reservation-request-1.md).

4.  On the Map view, select the location, building, and a floor where you have made the reservation.

5.  Select the map gear icon \(![Floor map gear settings icon.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../../workplace-safety-mgmt/images/wsd-gear-settings-icon.png)\) to view Display options.

6.  Select **Show name of the person who booked the space**.

7.  Select **Apply**.

    Reserved or booked spaces show the name of person who booked the space.

8.  Select a reserved space to open the Space details page.

    The name of the person who booked or reserved the space is shown.


**Parent Topic:**[Configure Workplace Reservation Management portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/wsd-reservation-setup.md)

**Related topics**  


[Install Workplace Reservation Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/install-wsd-reservation-mgmt.md)

[Add a workplace space for reservation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/add-reservable-items.md)

[Add a workplace room for reservation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/add-workplace-rooms.md)

[Configure a reservable module](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/config-reservable-module.md)

[Assign spaces to an area](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/add-neighbourhood-spaces-to-an-area.md)

[Create a standard service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/add-standard-services.md)

[Create a flexible service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/add-flexible-service.md)

[Create a workplace service to provide an extra service for a reservation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/create-workplace-service-to-provide-extra-service.md)

[Create a reservable view](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/create-a-reservable-view.md)

[Create a user criteria record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/create-user-criteria.md)

[Configure a reservable purpose](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/configure-reservable-purpose.md)

[Create a quick reservation time slot](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/add-reservable-time-slots.md)

[Configure virtual meeting providers](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/configure-virtual-meeting-providers.md)

[Configure Microsoft Teams as virtual meeting provider](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/configure-msteams-as-virtual-meeting-provider.md)

[Connect Workplace Reservation Management with Microsoft Teams](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/connect-rsv-mgmt-with-teams.md)

[Connect Workplace Reservation Management with Zoom](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/connect-rsv-mtm-with-zoom.md)

[Display permanent seat assignments on floor maps](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/display-permanent-seats-on-maps.md)

[Manage check-in and check-out reservations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/check-in-check-out-process.md)

[Configure automatic check-in for reserved spaces](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/configure-rsv-check-in.md)

[Configure reservation multi-day settings in Reservable Module](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/rsv-config-rsv-mod-value.md)

