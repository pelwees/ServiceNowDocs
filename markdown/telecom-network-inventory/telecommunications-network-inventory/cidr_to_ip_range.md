---
title: CIDR to IP range function
description: Classless Inter-Domain Range \(CIDR\) to IP range flow action enables you to create a set of IP addresses using the Classless Inter-Domain Range \(CIDR\) using Telecommunications Network Inventory application based on the input that you receive when you instantiate an inventory.
locale: en-US
release: australia
product: Telecommunications Network Inventory
classification: telecommunications-network-inventory
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Function catalog, Reference, Telecommunications Network Inventory]
---

# CIDR to IP range function

Classless Inter-Domain Range \(CIDR\) to IP range flow action enables you to create a set of IP addresses using the Classless Inter-Domain Range \(CIDR\) using Telecommunications Network Inventory application based on the input that you receive when you instantiate an inventory.

Upon calling this flow action, a CIDR is fetched using the given IP subnetwork. Further, using the CIDR a set of IP addresses are created. These IP addresses are further stored in the allocated IP addresses table.

This function also ensures that there is no other allocated IP address created for this particular IP subnetwork.

## Roles and availability

Users with the admin role can add an action to a flow and define the configuration details of the flow. This function is available as a Flow Designer action in the Telecommunications Network Inventory application so that you can perform inventory-related data operations.

## Input fields

|Field name|Description|Data type|
|----------|-----------|---------|
|Change Task|Provide change task number for this task|Reference|
|IP Subnetwork|Provide name of the subnetwork from where the CIDR must be fetched|String|

## Output

The following table lists the information about the function output.

|Name|Description|Data type|
|----|-----------|---------|
|Allocated IP address|Returns a glide a record|Record|

**Parent Topic:**[Telecommunications Network Inventory function catalog](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/tni-flow-action.md)

**Related topics**  


[Allocate Free Number function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/allocate-free-number-action.md)

[Create CI From Template function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/add-card-action.md)

[Cascade Update function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/cascade-update-action.md)

[Create and Assign Range/Single Number function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/create-assign-range-single-number-function.md)

[Create Logical Interface function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/create-logical-interface-action.md)

[Create Logical Connection function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/create-logical-connection-action.md)

[Create Physical Connection function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/create-physical-connection-action.md)

[Create IP subnetwork function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/create_ip_subnetwork.md)

[Get Interface Summary function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/get-interface-summary-action.md)

[Lookup Next Hub function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/lookup-next-hub-action.md)

[Path Search function](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/telecom-network-inventory/telecommunications-network-inventory/path-compute-action.md)

