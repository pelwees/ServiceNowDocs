---
title: Outbound cost allocation staging table
description: The outbound cost allocation \[sn\_spend\_intg\_outbound\_invoice\_cost\_allocation\] staging table stores important data about cost allocation information so that an ERP integrator can export this data to a third-party ERP system.
locale: en-US
release: australia
product: Accounts Payable Operations
classification: accounts-payable-operations
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Reference, Accounts Payable Operations, Finance and Supply Chain]
---

# Outbound cost allocation staging table

The outbound cost allocation \[sn\_spend\_intg\_outbound\_invoice\_cost\_allocation\] staging table stores important data about cost allocation information so that an ERP integrator can export this data to a third-party ERP system.

## Outbound cost allocation staging table

The following table lists fields for the outbound cost allocation \[sn\_spend\_intg\_outbound\_invoice\_cost\_allocation\] staging table.

|Field|Data type|Description|
|-----|---------|-----------|
|Number|String|An auto-generated number that uniquely identifies the invoice.|
|Allocation type|Choice|The cost allocation type that you would like to assign cost to.|
|Cost center|Reference|Cost center for which the invoice is generated.|
|Ledger account|Reference|A reference field for the account used to generate the  invoice.​|
|Allocate by|String|Determines whether the cost allocation is based on amount or percentage.|
|Allocation amount|String|Amount that is allocated.|
|Invoice line|Reference|Line items on the invoice.|
|Integration status|Choice|Status of the integration process.|

**Parent Topic:**[Accounts Payable Operations reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/acc-pay-reference.md)

**Related topics**  


[Accounts Payable Operations properties](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/acc-pay-properties.md)

[Create New Invoice Line form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/create-invoice-line-form.md)

[Create invoice cost allocation form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/create-invoice-cost-allocation-form.md)

[Distribution set form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/distribution-set-form.md)

[Create New Invoice case form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/create-new-ap-case-form.md)

[Create New Invoice task form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/create-apm-task-form.md)

[Invoice processing case form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/invoice-processing-case-form.md)

[Tax lines](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/create-tax-lines-apo.md)

[Invoice exception form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/exception-form-fields.md)

[Request Help form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/ur-request-help-form.md)

[Master data table for Accounts Payable Operations](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/master-data-table-apo.md)

[Invoice exception definition form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/invoice-exception-definition-form.md)

[Approval Rule form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/new-approval-rule-form.md)

[Approval Plan form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/approval-plan-form.md)

[Accounts Payable Operations glossary](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/../concept/apo-glossary.md#)

