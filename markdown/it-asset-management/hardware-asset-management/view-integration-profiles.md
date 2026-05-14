---
title: View the carrier integration profile details
description: View the details of the carrier API used to connect your ServiceNow instance to the third-party shipping carrier application.
locale: en-US
release: australia
product: Hardware Asset Management
classification: hardware-asset-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Track shipments using the integration framework, Using Hardware Asset Management, Hardware Asset Management, IT Asset Management]
---

# View the carrier integration profile details

View the details of the carrier API used to connect your ServiceNow instance to the third-party shipping carrier application.

## Before you begin

Role required: admin, domain\_admin, asset, inventory\_admin, or sn\_hamp.ham\_system\_admin

## Procedure

1.  Navigate to **All** &gt; **Hardware Asset Workspace** &gt; **Asset operations**.

2.  From the **Shipment** list, select **Carrier integration profiles**.

    The third-party carrier application automatically inserts records into the Carrier integration profiles list. You can also create a carrier integration profile.

3.  Select the carrier integration profile of your carrier.

<table id="table_ejc_bcz_lxb"><thead><tr><th>

Field

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Name

</td><td>

Name of the integration profile.

</td></tr><tr><td>

Connection details

</td><td>

Reference to the Connection and Credentials Aliases table that stores the credentials of the customer.**Note:** Your credentials must be updated in the Connection and Credentials Aliases table so that you’re authenticated to connect to the carrier API.

</td></tr><tr><td>

API

</td><td>

Name of the script that has the integration business logic.

</td></tr><tr><td>

Job

</td><td>

Name of the scheduled job that invokes the carrier API to fetch the shipments details. This job is created by a job that runs daily, The ITAM: Process integration profiles and stale shipment job.

</td></tr><tr><td>

Active

</td><td>

Option that indicates the status of the integration profile.**Note:** Only users with the admin or domain\_admin role can deactivate the integration profile but they can’t delete the integration profile. When an integration profile is deactivated, the associated job that invokes the carrier API is deactivated automatically.

</td></tr></tbody>
</table>
**Parent Topic:**[Track shipments using the integration framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/tracking-shipments-using-integration-framework.md)

**Related topics**  


[Creating an integration script include for third-party carrier applications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/creating-integration-script-include-ham.md)

[Connect your ServiceNow instance with a shipping carrier application](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/associate-shipping-carrier-int-profile.md)

[Remove a shipping carrier from an integration profile](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/remove-shipping-carrier.md)

[Create a carrier integration profile](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/create-carrier-integration-profile.md)

[Test the integration with the carrier API](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/test-carrier-api-integration.md)

[Create a shipping carrier record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/create-shipping-carrier.md)

[View hardware asset shipment details](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/view-hardware-asset-shipments.md)

[Stale shipments](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/stale-shipments.md)

[Track a hardware asset shipment](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/track-hardware-asset-shipments.md)

