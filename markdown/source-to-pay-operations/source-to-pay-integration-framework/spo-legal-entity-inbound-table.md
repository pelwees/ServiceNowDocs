---
title: Legal Entity Stage inbound staging table
description: The Legal entity stage inbound \[sn\_fcms\_intg\_legal\_entity\_stage\] staging table temporarily stores important data about legal entities before this data is sent to the primary table.
locale: en-US
release: australia
product: Source-to-Pay Integration Framework
classification: source-to-pay-integration-framework
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 6
breadcrumb: [Inbound staging tables Sourcing Procurement, Inbound staging tables, Source-to-Pay integration framework, Integration with third-party applications, Integrations, Source-to-Pay Operations, Finance and Supply Chain]
---

# Legal Entity Stage inbound staging table

The Legal entity stage inbound \[sn\_fcms\_intg\_legal\_entity\_stage\] staging table temporarily stores important data about legal entities before this data is sent to the primary table.

The following table lists the fields for the Legal Entity Stage inbound \[sn\_fcms\_intg\_legal\_entity\_stage\] staging table.

<table id="table_c23_ss5_hzb"><thead><tr><th>

Field

</th><th>

Data type

</th><th>

Description

</th></tr></thead><tbody><tr><td>

City

</td><td>

String

</td><td>

City where the legal entity is located.

</td></tr><tr><td>

Country

</td><td>

String

</td><td>

Country where the legal entity is located.

</td></tr><tr><td>

ERP company code

</td><td>

String

</td><td>

Company code of the supplier in the ERP system.This is a mandatory field.

</td></tr><tr><td>

ERP source

</td><td>

String

</td><td>

ERP source from which data is imported. For purchase order, receipt, and invoice integrations, the ERP source is determined through the legal entity associated with these records.This is a mandatory field.

</td></tr><tr><td>

Global company

</td><td>

String

</td><td>

Global company that the entity is linked to.

</td></tr><tr><td>

Industry

</td><td>

String

</td><td>

Industry type of the legal entity.

</td></tr><tr><td>

Legal name

</td><td>

String

</td><td>

Legal name of the entity that corresponds to its operating location.

</td></tr><tr><td>

Local currency

</td><td>

String

</td><td>

Local currency that corresponds to the entity's operating location.

</td></tr><tr><td>

Street

</td><td>

String

</td><td>

Street where the legal entity is located.

</td></tr></tbody>
</table>**Parent Topic:**[Inbound staging tables for Sourcing and Procurement Operations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/../concept/spo-inbound-staging-tables.md)

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

[Office Location Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-office-loc-inbound-table.md)

[Order Acknowledgement staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/order-acknowledgement-staging-table.md)

[Order Acknowledgement Error staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/order-acknowledgement-error.md)

[Payment Terms Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-pay-terms-inbound-table.md)

[Price Import staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/price-import-staging-table.md)

[Price Error outbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/price-error-staging-table.md)

[Product Model Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-prod-mod-inbound-table.md)

[Purchase Entity Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-purch-entity-inbound-table.md)

[Purchase Line Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-purch-line-stage-inbound-table.md)

[Purchase Requisition staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/purchase-requisition-staging-table.md)

[Spend Shipment Import inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spend-shipment-import-inbound-table.md)

[Shipment Error staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/shipment-error-staging-table.md)

[Supplier Product Stage inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/spo-supp-prod-inbound-table.md)

[Third Party Sourcing Registration staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/third-party-sourcing-registration-staging-table.md)

[Third Party Unit Mapping staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/third-party-unit-mapping-staging-table.md)

[Third Party Unit staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/third-party-unit-staging-table.md)

[Unit of Measure inbound staging table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/source-to-pay-integration-framework/unit-measure-inbound-staging-table.md)

