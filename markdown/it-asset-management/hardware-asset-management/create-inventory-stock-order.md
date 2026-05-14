---
title: Create an inventory stock order request
description: Create an inventory stock order request so that you can order new hardware in bulk for your stockrooms. After your request is approved, the Hardware Stock Order flow takes you through the process of requesting, sourcing, and receiving your order.
locale: en-US
release: australia
product: Hardware Asset Management
classification: hardware-asset-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Using Hardware Asset Management, Hardware Asset Management, IT Asset Management]
---

# Create an inventory stock order request

Create an inventory stock order request so that you can order new hardware in bulk for your stockrooms. After your request is approved, the Hardware Stock Order flow takes you through the process of requesting, sourcing, and receiving your order.

## Before you begin

Role required: Inventory user

## About this task

A stock order is a catalog request to replenish the stock in a stockroom.

You can manually create a hardware inventory stock order request. However, an inventory stock order request is automatically created from a stock rule trigger when the stock rule threshold breaches.

After your stock order request is approved, the Hardware Stock Order flow is triggered. The Workflow Studio application is used to create the Hardware Stock Order flow to take you through the entire process of requesting, sourcing, and receiving your order.

![Hardware stock order flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../image/hardware-stock-order-flow.png "Hardware Stock Order Flow")

Role required: inventory\_admin

## Procedure

1.  Navigate to **All** &gt; **Inventory** &gt; **Submit Stock Order**.

2.  On the form, fill in the fields.

    |Field|Description|
    |-----|-----------|
    |Model|New hardware that you want to order.|
    |Quantity|Amount of the new hardware that you want to order.|
    |Stockroom|Stockroom where you want to stock the new hardware.|
    |Comments|Details that are specific to your order request.|

3.  Click **Order Now**.

    The Order Status form displays all the order details. An existing service catalog request workflow takes care of all the required approvals for the request. You can now source your request.

4.  Click the request number to open the request.

    The price of the request item is the price of the model. The price of the request is calculated as quantity of the request Item multiplied by the price of the request Item. The price of the request item that's shown in the Requested Items related list is the price of the model calculated by the quantity.

    Price of the Request Item is the Price of the Model and Price of the Request is calculated as Quantity of Request Item \* Price of the Request Item.

    A catalog task is created after the request is approved.

5.  Click **Catalog Tasks** and open the catalog task.

6.  Click **Source Request**.

    The Source Request form layout lists the model name, the quantity of items to be sourced, and the total quantity of the hardware in stock.

7.  Click **Add Transfer Order** or **Add Purchase Order** to source the request via a transfer order or a purchase order.

    The quantity mentioned in **Total in Stock** does not include the stock that's available in the destination stockroom.

    If the requested item is not available in any stockroom, then **Add Transfer Order** is disabled. If there are no available vendors for the requested item, then **Add Purchase Order** is disabled.

    To enable **Add Purchase Order**, do one of the following:

    -   add a designated vendor by navigating to vendor items.
    -   add a catalog item for the requested model with vendor details.

**Parent Topic:**[Using Hardware Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/using-ham-classic.md)

**Related topics**  


[Work with hardware normalization](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/Work-with-hardware-normalization.md)

[Manage asset bundles from your inventory](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/create-bundled-assets.md)

[Manage your inventory through pallet assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/pallets-for-inventory-management.md)

[Manage loaner assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-loaner-asset.md)

[Donate assets to charity organizations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/donate-asset-to-charity-organizations.md)

[Use Advanced Shipment Notification](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/advanced-shipment-notification.md)

[Manage RMA requests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-rma-req.md)

[Create a disposal order](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/create-disposal-order.md)

[Use a hardware asset request flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/hardware-request-flow.md)

[Audit hardware asset inventory](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/ham-inventory-audit.md)

[Request a Hardware Asset Refresh](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/hardware-asset-refresh.md#)

[Manage your expiring contracts for leased hardware assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-your-leased-hw-asts-expiring-contract.md)

[Reclaim hardware assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-asset-reclaim.md)

[View RFID information of assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/view-rfid-info.md)

[Manage the lifecycle of hardware models with calculated lifecycle templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-ham-lifecycle-temp.md)

[Receive asset warranty details from Lenovo](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/receive-warranty-details-lenovo.md)

[Manage stockrooms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-your-stockrooms.md)

[Track shipments using the integration framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/tracking-shipments-using-integration-framework.md)

[Track asset location using indoor maps](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/track-asset-location-using-indoor-maps.md)

[Assess performance of Hardware Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/suc-goal-act-hw.md)

[Manage refresh of assets using Zero Touch Refresh](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/refresh-hardware-uisng-ztr.md)

[Configure the Total Cost of Ownership of assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/configure-ham-tco.md)

[Manage Hardware Asset Management subscriptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/managing-ham-subscriptions.md)

[Manage repair of defective assets in your stockroom in the Hardware Asset Workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-repair-of-defective-ham-assets.md)

[Manage picking hardware assets within your stockroom for Hardware Asset Management workflows](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-asset-picking-stockroom-ham-ws.md)

[Manage hardware asset tasks using the Mobile Agent application](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-hardware-asset-tasks-mobile-agent.md)

[Manage asset put away using the Hardware Asset Workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/manage-asset-putaway-stockroom-hardware-asset-workspace.md)

[Audit your hardware assets by using Asset Attestation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../concept/audit-hardware-assets-attestation.md)

[Acknowledge receipt of assets on the Employee Center portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/receive-assets-employee-center.md)

[Update associated Decision tables for HAM flows](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/trigger-flow-ham.md)

