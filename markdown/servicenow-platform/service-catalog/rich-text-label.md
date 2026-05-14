---
title: Rich Text Label
description: This variable displays a formatted label on a catalog item form.
locale: en-US
release: australia
product: Service Catalog
classification: service-catalog
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Types of service catalog variables, Service catalog variables, Service Catalog Reference, Service Catalog, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Rich Text Label

This variable displays a formatted label on a catalog item form.

In the TinyMCE rich text editor, you can format the label and add images or links. This variable supports the HTML tags.

**Note:**

-   You can make this variable visible using catalog client scripts and catalog UI policies.
-   You cannot cascade this variable in an order guide.
-   You cannot set this variable as mandatory.
-   In the Automated Test Framework, this variable is only supported in the Variable State Validation step to check the visibility.
-   This variable is not supported in the following:
    -   Variable summarizer
    -   Multi-row variable set
    -   Condition builders and reports
-   You cannot specify the following for this variable:
    -   Help text and instructions
    -   Tool tip
    -   Permissions
    -   Variable width
    -   Example text
-   The g\_form.setValue\(\), g\_form.setReadOnly\(\), and g\_form.setMandatory\(\) APIs are not supported in catalog client scripts. Only the g\_form.setVisible\(\) API is supported.

![The Rich Text Label variable](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/../image/RichTextVariable.png "Rich Text Label variable")

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

[Requested for](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/requested-for.md)

[Select box](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/select-box.md)

[Single-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/single-line-text.md)

[UI page](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/ui-page.md)

[URL](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/url.md)

[Wide single-line text](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/wide-single-line-text.md)

[Yes/No](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/yes-no.md)

[Variable support in various channels](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/variables-availability.md)

