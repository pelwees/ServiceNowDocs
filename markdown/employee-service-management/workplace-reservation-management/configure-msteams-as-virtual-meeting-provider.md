---
title: Configure Microsoft Teams as virtual meeting provider
description: Set Microsoft Teams as your virtual meeting provider.
locale: en-US
release: australia
product: Workplace Reservation Management
classification: workplace-reservation-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Configure Workplace Reservation Management portal, Workplace Reservation Management, Workplace Service Delivery, Employee Service Management]
---

# Configure Microsoft Teams as virtual meeting provider

Set Microsoft Teams as your virtual meeting provider.

## Before you begin

-   Ensure the following:
    -   Update the Workplace Reservation Management application only after installing the Microsoft Teams spoke. Otherwise, you must repair the Workplace Reservation Management application.
    -   Microsoft Teams works only with a Microsoft account \(Exchange Online, Exchange OnPrem\). If you have both Google and a Microsoft Teams account, the virtual meeting provider cannot be added. If you want to create a Microsoft Teams account, you must create a Microsoft account. The Microsoft Teams account is mapped to the Microsoft account and not to the Google account.
    -   For Microsoft Teams, to create a meeting link on behalf of other users, refer to [Microsoft documentation](https://learn.microsoft.com/en-us/graph/cloud-communication-online-meeting-application-access-policy/).

The Workplace Reservation Management application provides the **Template** virtual meeting provider by default. After you setup a connection between Workplace Reservation Management and Microsoft Teams, the system, by default, provides the **Microsoft Teams** virtual meeting provider configured with the following flows:

|Field|Flow|
|-----|----|
|Create meeting|`Create Microsoft Teams Meeting`|
|Get meeting details|`Get MS Teams Thread ID`|
|Get recording|`Get Microsoft Teams Recording`|

For more information on how to create a flow, refer to [Create a flow](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/build-workflows/workflow-studio/create-flow.md).

**Important:** The virtual meeting providers are deactivated by default. Change the **Active** status of the desired virtual meeting provider to **true** to start using.

Role required: sn\_wsd\_rsv.admin

## Procedure

1.  Connect Workplace Reservation Management and Microsoft Teams.

    To create a connections, refer to [Connect Workplace Reservation Management with Microsoft Teams](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/connect-rsv-mgmt-with-teams.md).

    After the connection is configured, the application by default provides with the **Microsoft Teams** virtual meeting provider.

2.  Navigate to **All** &gt; **Workplace Reservation Management** &gt; **Administration** &gt; **Virtual Meeting Providers**.

3.  Select **Microsoft Teams**.

4.  On the form, to activate, select the **Active** check box.


## Result

Microsoft Teams is set as the virtual meeting provider.

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

[Connect Workplace Reservation Management with Microsoft Teams](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/connect-rsv-mgmt-with-teams.md)

[Connect Workplace Reservation Management with Zoom](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/connect-rsv-mtm-with-zoom.md)

[Display permanent seat assignments on floor maps](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/display-permanent-seats-on-maps.md)

[Display name of the person reserving a space](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/displayname-person-booking-rsv.md)

[Manage check-in and check-out reservations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/check-in-check-out-process.md)

[Configure automatic check-in for reserved spaces](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/configure-rsv-check-in.md)

[Configure reservation multi-day settings in Reservable Module](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-reservation-management/../concept/rsv-config-rsv-mod-value.md)

