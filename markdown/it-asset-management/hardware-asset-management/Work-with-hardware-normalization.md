---
title: Work with hardware normalization
description: Asset Management Hardware Model Normalization enables users to normalize the details, such as manufacturer, product, model, and device type, of your hardware and consumable models. Data from the models is compared against the data in the Hardware Model Normalization Content Service.
locale: en-US
release: australia
product: Hardware Asset Management
classification: hardware-asset-management
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 7
breadcrumb: [Using Hardware Asset Management, Hardware Asset Management, IT Asset Management]
---

# Work with hardware normalization

Asset Management Hardware Model Normalization enables users to normalize the details, such as manufacturer, product, model, and device type, of your hardware and consumable models. Data from the models is compared against the data in the Hardware Model Normalization Content Service.

The Normalization Data Services Client \(com.glide.data\_services\_canonicalization.client\) plugin is also activated when you activate the Hardware Model Normalization plugin.

**Note:** This documentation is for Hardware Model Normalization. For additional information on Asset Management, see the [Asset Management documentation](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/it-service-management/asset-management/c_AssetManagement.md).

## Scheduled jobs

To standardize your hardware and consumable models, the asset data must be normalized. You can manually update the model records with the normalization content, or you can compare your data against the Hardware Asset Management Content Service.

The **HAM- Hardware Normalization** scheduled job runs daily. This job does not add, remove, or merge models, nor does it modify original fields like Model Name, Manufacturer, or Model Number. It only updates the normalization-related fields for existing models, such as Normalized Product, Normalized Manufacturer, Normalized Model, and so on.

Content from the Hardware Model Normalization Content Service is pulled into the ServiceNow AI Platform. Use the Asset Job Log \(asset\_job\_log\) table to review the status of the scheduled job.

The normalization status of models can be reverted by clicking **Revert Normalization** on the model. Any normalization that occurred on the model gets reverted and the rule gets deactivated. When the scheduled job runs, the models are processed with the active rules and the status is updated.

The scheduled job generates hardware and consumable model reports. These reports identify the overall status of your models and provide a breakdown of the normalization status.

The following reports are included.

-   Hardware Product Overall Normalization Status
-   Consumable Product Overall Normalization Status
-   Hardware Model Normalization Status
-   Consumable Model Normalization Status

-   **[Opt-in to the Hardware Asset Management Content Service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/opt-in-hardware-normalization.md)**  
Opt in to the Hardware Asset Management Content Service to improve the normalization process by sharing hardware and consumable model data from your organization with ServiceNow.
-   **[Import and export content data](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/import-export-ham.md)**  
Import and export content data to the ServiceNow Hardware Asset Management content service to improve the normalization process. On-premise users can use the Manage Hardware Library module to import or export data via a zip file.
-   **[Create a hardware or consumable model](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/create-hardware-consumable-model.md)**  
To begin tracking your hardware and consumable assets, create a hardware or consumable model. Then, add lifecycle information to keep track of the lifecycle phase of your model.
-   **[Copy a hardware model from the Content lookup portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/copy-hardware-model.md)**  
Copy a hardware model record from the Content lookup portal to add a new model entry to the Product Model \[cmdb\_model\] table.
-   **[Normalize hardware and consumable models](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/normalize-hardware-consumable-models.md)**  
After you have created your hardware and consumable models, normalize the information of the model.
-   **[Revert normalization of hardware and consumable models](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/revert-norm-ham.md)**  
Revert the normalization of hardware and consumable models in the Hardware Asset Workspace.
-   **[Add a custom product](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/add-custom-hardware-model.md)**  
If you have a product that is not represented in the Asset Management Content Service yet, you can create a custom product.
-   **[Add a custom hardware model](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/add-custom-model.md)**  
If you have a hardware model that isn't represented in the Asset Management Content Service yet, you can create a custom model.

**Parent Topic:**[Using Hardware Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/using-ham-classic.md)

**Related topics**  


[Manage asset bundles from your inventory](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/create-bundled-assets.md)

[Manage your inventory through pallet assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/pallets-for-inventory-management.md)

[Manage loaner assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/manage-loaner-asset.md)

[Donate assets to charity organizations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/donate-asset-to-charity-organizations.md)

[Use Advanced Shipment Notification](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/advanced-shipment-notification.md)

[Manage RMA requests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-rma-req.md)

[Create an inventory stock order request](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/create-inventory-stock-order.md)

[Create a disposal order](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/create-disposal-order.md)

[Use a hardware asset request flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/hardware-request-flow.md)

[Audit hardware asset inventory](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/ham-inventory-audit.md)

[Request a Hardware Asset Refresh](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/hardware-asset-refresh.md#)

[Manage your expiring contracts for leased hardware assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/manage-your-leased-hw-asts-expiring-contract.md)

[Reclaim hardware assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-asset-reclaim.md)

[View RFID information of assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/view-rfid-info.md)

[Manage the lifecycle of hardware models with calculated lifecycle templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-ham-lifecycle-temp.md)

[Receive asset warranty details from Lenovo](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/receive-warranty-details-lenovo.md)

[Manage stockrooms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-your-stockrooms.md)

[Track shipments using the integration framework](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/tracking-shipments-using-integration-framework.md)

[Track asset location using indoor maps](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/track-asset-location-using-indoor-maps.md)

[Assess performance of Hardware Asset Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/suc-goal-act-hw.md)

[Manage refresh of assets using Zero Touch Refresh](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/refresh-hardware-uisng-ztr.md)

[Configure the Total Cost of Ownership of assets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/configure-ham-tco.md)

[Manage Hardware Asset Management subscriptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/managing-ham-subscriptions.md)

[Manage repair of defective assets in your stockroom in the Hardware Asset Workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-repair-of-defective-ham-assets.md)

[Manage picking hardware assets within your stockroom for Hardware Asset Management workflows](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-asset-picking-stockroom-ham-ws.md)

[Manage hardware asset tasks using the Mobile Agent application](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-hardware-asset-tasks-mobile-agent.md)

[Manage asset put away using the Hardware Asset Workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/manage-asset-putaway-stockroom-hardware-asset-workspace.md)

[Audit your hardware assets by using Asset Attestation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/audit-hardware-assets-attestation.md)

[Acknowledge receipt of assets on the Employee Center portal](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/receive-assets-employee-center.md)

[Update associated Decision tables for HAM flows](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/../task/trigger-flow-ham.md)

[Hardware Model Normalization](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-asset-management/hardware-asset-management/hardware-normalization.md#)

