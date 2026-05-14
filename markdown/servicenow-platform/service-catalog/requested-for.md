---
title: Requested for
description: Before submitting a catalog item request, this variable helps you specify who this request can be submitted for.
locale: en-US
release: australia
product: Service Catalog
classification: service-catalog
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Types of service catalog variables, Service catalog variables, Service Catalog Reference, Service Catalog, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Requested for

Before submitting a catalog item request, this variable helps you specify who this request can be submitted for.

## Requested For

You should specify this information while answering catalog item questions.

**Important:**

-   You can only specify users from the User \[sys\_user\] table.
-   If you don’t specify the default value for this variable, the current logged-in user requesting the item is considered as the default Requested For variable value.
-   You can submit the request for a user based on access to a catalog item. The **Access Type** field of the catalog item can be used to specify if a request can be submitted for a user who does not have access to the catalog item.
-   For this variable, item variable assignment is not supported in the rule base of an order guide. If the order guide contains the Requested For variable, the value would be cascaded to the equivalent variable of items in the rule base as read-only.

Using the **Enable also request for** field of the Requested For variable, you can request a catalog item for different users under one request.

For information about delegated request experience, see [Delegated request experience](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/../concept/delegated-request-exp.md).

**Important:**

-   You can add this variable to a catalog item or variable set. However, when submitting the request, a catalog item can have only one Requested For variable.
-   You can add only one Requested For variable for a variable set.
-   This variable is not supported in a multi-row variable set.
-   After the request is submitted, this variable value is visible in the variable editor and variable summarizer.

![Screenshot for the Requested For variable](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/../image/ReqForVariable.png "Requested For variable")

**Parent Topic:**[Types of service catalog variables](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/r_VariableTypes.md)

**Related topics**  


[Attachment](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/attachment.md)

[Break](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/break.md)

[Check box](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/check-box.md)

[Container start, container split, and container end](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/contain-start-split-end.md)

[Date, Date and time, and Duration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/date.md)

[Email](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/email.md)

[HTML](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/html.md)

[IP Address](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/ip-address.md)

[Label](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/label.md)

[List collector](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/list-collector.md)

[Lookup multiple choice](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/lookup-multiple-choice.md)

[Lookup select box](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/lookup-select-box.md)

[Custom and Custom with label](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/custom.md)

[Masked](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/masked.md)

[Multi-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/multi-line.md)

[Multiple choice](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/multiple-choice.md)

[Numeric scale](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/numeric-scale.md)

[Reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/reference.md)

[Rich Text Label](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/rich-text-label.md)

[Select box](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/select-box.md)

[Single-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/single-line-text.md)

[UI page](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/ui-page.md)

[URL](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/url.md)

[Wide single-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/wide-single-line-text.md)

[Yes/No](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/yes-no.md)

[Variable support in various channels](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/variables-availability.md)

