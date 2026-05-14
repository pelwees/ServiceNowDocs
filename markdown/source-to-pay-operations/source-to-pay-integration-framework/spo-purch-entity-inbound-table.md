---
title: Purchase Entity Stage inbound staging table
description: The Purchase Entity Stage inbound \[sn\_fcms\_intg\_imp\_purchase\_entity\] staging table temporarily stores important data about purchase entities before this data is sent to the primary table.
locale: en-US
release: australia
product: Source-to-Pay Integration Framework
classification: source-to-pay-integration-framework
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Inbound staging tables Sourcing Procurement, Inbound staging tables, Source-to-Pay integration framework, Integration with third-party applications, Integrations, Source-to-Pay Operations, Finance and Supply Chain]
---

# Purchase Entity Stage inbound staging table

The Purchase Entity Stage inbound \[sn\_fcms\_intg\_imp\_purchase\_entity\] staging table temporarily stores important data about purchase entities before this data is sent to the primary table.

The following table lists the mandatory fields for the Purchase Entity Stage inbound \[sn\_fcms\_intg\_imp\_purchase\_entity\] staging table.

|Field|Data type|Description|
|-----|---------|-----------|
|ERP source|String|ERP source from which data is imported. For purchase order, receipt, and invoice integrations, the ERP source is determined through the legal entity associated with these records.|
|ERP number|String|Unique identifier for the ERP system from which data is imported.|
|Legal entity|String|Detailed information about individual suppliers, including banking details, payment methods, and credit terms.|
|Name|String|Name of the purchase entity.|

**Parent Topic:**[Inbound staging tables for Sourcing and Procurement Operations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/../concept/spo-inbound-staging-tables.md)

**Related topics**  


[CMDB Model Category Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-prod-cate-inbound-table.md)

[CMDB Service Model Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-serv-mod-inbound-table.md)

[CMN Location Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-loc-inbound-table.md)

[Catalog Import staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/catalog-import-staging-table.md)

[Catalog Error staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/catalog-error.md)

[Cost Center Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-cost-center-inbound-table.md)

[Department Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-dept-inbound-table.md)

[ERP Plant Address Mapping Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-erp-plant-address-inbound-table.md)

[FX Currency Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-fx-currency-inbound-table.md)

[FX Rate Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-fx-rate-inbound-table.md)

[Fixed asset details stage inbound table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/fixed-asset-details-stage-inbound-table.md)

[GL Account Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-gl-account-inbound-table.md)

[Import Availability Updates inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-import-avail-inbound-table.md)

[Availability Error staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/availability-error-staging-table.md)

[Cost Allocation inbound staging table \(Deprecated\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-cost-alloc-inbound-table.md)

[Invoice inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-inbound-invoice-table.md)

[Purchase Order inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-inbound-pur-order-table.md)

[Purchase Order Line inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-inbound-pol-table.md)

[Receipt inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-inbound-receipt-table.md)

[Legal Entity Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-legal-entity-inbound-table.md)

[Office Location Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-office-loc-inbound-table.md)

[Order Acknowledgement staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/order-acknowledgement-staging-table.md)

[Order Acknowledgement Error staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/order-acknowledgement-error.md)

[Payment Terms Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-pay-terms-inbound-table.md)

[Price Import staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/price-import-staging-table.md)

[Price Error outbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/price-error-staging-table.md)

[Product Model Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-prod-mod-inbound-table.md)

[Purchase Line Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-purch-line-stage-inbound-table.md)

[Purchase Requisition staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/purchase-requisition-staging-table.md)

[Spend Shipment Import inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spend-shipment-import-inbound-table.md)

[Shipment Error staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/shipment-error-staging-table.md)

[Supplier Product Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-supp-prod-inbound-table.md)

[Third Party Sourcing Registration staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/third-party-sourcing-registration-staging-table.md)

[Third Party Unit Mapping staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/third-party-unit-mapping-staging-table.md)

[Third Party Unit staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/third-party-unit-staging-table.md)

[Unit of Measure inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/unit-measure-inbound-staging-table.md)

