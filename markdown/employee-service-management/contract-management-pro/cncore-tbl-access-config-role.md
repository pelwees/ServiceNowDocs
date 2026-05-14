---
title: Assign a role for configuring template mappings
description: Enable a contract user to configure information placed in the contract document by assigning a contract configurator role.
locale: en-US
release: australia
product: Contract Management Pro
classification: contract-management-pro
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 2
keywords: [Template mapping role, Contract document]
breadcrumb: [Configure CM Pro for your workspace, Configure, Contract Management Pro, Legal and Contract Operations, Employee Service Management]
---

# Assign a role for configuring template mappings

Enable a contract user to configure information placed in the contract document by assigning a contract configurator role.

## Before you begin

Role required: admin

## About this task

Template mappings automatically insert default information in the contract document. To configure template mappings, the contract user requires a contracts configurator \(sn\_cm\_core.contract\_config\) role.

## Procedure

1.  Navigate to **All** &gt; **User Administration** &gt; **Users**.

2.  Search for and select the user.

3.  In the Roles related list, select **Edit**.

4.  Move the sn\_cm\_core.contract\_config role from the Available list to the Selected list.

    ![Add sn_cm_core.contract_config to the user](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/../image/cmpro-bu-add-config-role.png "Add sn_cm_core.contract_config role to user")

5.  Select **Save**.

6.  Save the user record by selecting **Update**.


## Result

The user who with the sn\_cm\_core.contract\_config role can update template mappings to pre-fill information that's placed in the contract document. For more information, [Update contract template mappings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-template-mapping.md).

**Parent Topic:**[Add and configure contract request functionality into your workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/../concept/cncore-uptake-steps.md)

**Related topics**  


[Configure non-task tables for contract templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cmpro-config-non-tsk-tbl-cn-tmplt.md)

[Add a workspace action button for initiating a contract request](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-config-initiate-cont.md)

[Add Contract requests tab to the contract request record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-add-relatedlist-conreq.md)

[Add amendment tabs to contract repository record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-BU-amend-relatedlist.md)

[Add Contract documents tab to the contract repository record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-add-con-doc-relatedl.md)

[Copy fields from parent request to contract request](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-copy-fld-frm-parent.md)

[Group contract documents by contract type in a contract request](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-config-srp-grouping.md)

[Add access to obligation management from contract repository records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cmpro-add-access-to-ob-mgmt.md)

[Configure the contract request form header for your workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-configure-header.md)

[Enable contract request fields in condition builders](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-add-cmr-condtion-build.md)

[Configuring the Playbook tab on contract repository records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cmpro-config-playbook-tab.md)

