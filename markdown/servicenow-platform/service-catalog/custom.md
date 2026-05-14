---
title: Custom and Custom with label
description: The custom variable inserts a UI macro into the catalog item. Custom with label variable inserts a UI macro with a label.
locale: en-US
release: australia
product: Service Catalog
classification: service-catalog
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Types of service catalog variables, Service catalog variables, Service Catalog Reference, Service Catalog, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Custom and Custom with label

The custom variable inserts a UI macro into the catalog item. Custom with label variable inserts a UI macro with a label.

## Custom

This variable inserts a UI macro into the catalog item.

UI macros in the service catalog do not support the following glide\_list functions: clickthrough, slushbucket editing, and email field.

-   Use [phase one](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/api-reference/scripts/c_ExtensionsToJellySyntax.md) Jelly only for any UI macros added as variables. Phase two Jelly within the macro is not processed and appears on the page as standard content.
-   This variable is not yet supported on Classic Mobile devices.
-   This variable is supported in Service Portal through widgets. Create a widget with the same functionality as that of a macro and link the widget with the variable.

![A Custom variable](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/../image/Macro.png "Example: Custom variable")

## Custom with label

This variable inserts a UI macro with a label.

-   This variable is not yet supported on Classic Mobile devices.
-   This variable is supported in Service Portal through widgets. Create a widget with the same functionality as that of a macro with label, and link it with the variable.

![A Custom with label variable](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/../image/MacroWithLabel.png "Example: Custom with label variable")

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

[Masked](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/masked.md)

[Multi-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/multi-line.md)

[Multiple choice](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/multiple-choice.md)

[Numeric scale](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/numeric-scale.md)

[Reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/reference.md)

[Requested for](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/requested-for.md)

[Rich Text Label](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/rich-text-label.md)

[Select box](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/select-box.md)

[Single-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/single-line-text.md)

[UI page](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/ui-page.md)

[URL](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/url.md)

[Wide single-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/wide-single-line-text.md)

[Yes/No](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/yes-no.md)

[Variable support in various channels](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/variables-availability.md)

