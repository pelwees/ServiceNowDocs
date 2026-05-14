---
title: Rules based engine
description: The rule based engine maps the invoice line with purchase order line using fields such as unit price, delivered unit price, exact description, exact amount and amount round off.
locale: en-US
release: australia
product: Accounts Payable Operations
classification: accounts-payable-operations
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Using Accounts Payable Invoice Processing, Use, Accounts Payable Operations, Finance and Supply Chain]
---

# Rules based engine

The rule based engine maps the invoice line with purchase order line using fields such as unit price, delivered unit price, exact description, exact amount and amount round off.

The digitized invoice in accepted state moves to suspected duplicate state where the AP specialist verifies if the invoice is duplicate or not. When the invoice is confirmed to be not duplicate, the state of the invoice changes to received. The rules-based engine maps the fields in invoice such as unit price, derived unit price, exact description, exact amount and amount round off with the purchase order lines. If the invoice fields doesn't match with any of the fields in the purchase order lines, then the invoice state changes to matching error.

![Rules based engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/../image/rules-based-engine.png)

**Parent Topic:**[Using Accounts Payable Invoice Processing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/use-ap-invoice-processing.md)

**Related topics**  


[Invoice ingestion using Application programming interface \(API\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/invoice-ingestion-using-api.md)

[Work with invoices](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/work-with-invoices.md)

[Invoice processing cases](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/working-with-ingestion-cases.md)

[Invoice exceptions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/work-with-invoice-exceptions.md)

[Tolerance Rules and Variances for invoices](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/tolerance-rules-and-variance.md)

[Invoice approvals](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/invoice-approvals.md)

[View invoice documents in the Source-to-Pay Workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/source-to-pay-operations/accounts-payable-operations/../task/view-invoice-attachment.md)

