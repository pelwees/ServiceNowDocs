---
title: Masked
description: The masked variable inserts a field that masks the text entered.
locale: en-US
release: australia
product: Service Catalog
classification: service-catalog
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Types of service catalog variables, Service catalog variables, Service Catalog Reference, Service Catalog, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Masked

The masked variable inserts a field that masks the text entered.

Each character entered is displayed as an asterisk \(\*\). Use this variable to ask users for sensitive or confidential data such as passwords.

By selecting the **Use encryption** check box, you can configure the variable to encrypt its value using various encryption algorithms before storing in the database. These values can only be decrypted by using now\_GR.variables.var\_name.getDecryptedValue\(\) on RITM, Catalog Task, or any task extension record created using a record producer.

**Note:** By default, the **Use encryption** field is set to true to ensure secure storage of information.

On the variable editor, you can also decrypt and encrypt the values of a masked variable using the **Show** and **Hide** buttons. These buttons are not available for a fulfiller \(itil\) without the catalog\_view\_masked role. You can only view the value that you specified while requesting.

<table id="table_lrq_5vv_vdb"><tbody><tr class="sub-head"><td rowspan="2">

Action

</td><td colspan="3">

Roles

</td></tr><tr class="sub-head"><td>

Requester

</td><td>

Fulfiller with the catalog\_view\_masked role

</td><td>

Fulfiller without the catalog\_view\_masked role

</td></tr><tr><td>

View or hide the encrypted value on catalog forms

</td><td>

Yes

</td><td>

Not applicable

</td><td>

Not applicable

</td></tr><tr><td>

Edit the encrypted value on catalog forms

</td><td>

Yes

</td><td>

Not applicable

</td><td>

Not applicable

</td></tr><tr><td>

View or hide the encrypted value on the variable editor

</td><td>

Yes

</td><td>

Yes

</td><td>

No

</td></tr><tr><td>

Edit the encrypted value on the variable editor

</td><td>

Yes**Note:** If the masked variable is read-only on the variable editor, the variable value is not editable

</td><td>

Yes**Note:** If the masked variable is read-only on the variable editor, the variable value is not editable

</td><td>

No

</td></tr></tbody>
</table>![A masked variable](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/service-catalog/../image/VariableMaskedVarTypesG.png "Example: masked variable")

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

