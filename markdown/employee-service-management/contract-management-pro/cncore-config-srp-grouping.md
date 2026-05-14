---
title: Group contract documents by contract type in a contract request
description: As an administrator, group the contract documents by contract type in a contract request.
locale: en-US
release: australia
product: Contract Management Pro
classification: contract-management-pro
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
keywords: [BU configuration, Group contract documents, Uptake steps CM Pro]
breadcrumb: [Configure CM Pro for your workspace, Configure, Contract Management Pro, Legal and Contract Operations, Employee Service Management]
---

# Group contract documents by contract type in a contract request

As an administrator, group the contract documents by contract type in a contract request.

## Before you begin

Role required: admin

## About this task

**Note:** In Legal Counsel Center and Contract Workspace, the contract documents are grouped based on the contract type, by default.

Customize the Standard Record Page \(SRP\) to display contract documents grouped by contract type in the Contract document tab through UI Builder, a web user interface builder. For more information, see [UI Builder](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/application-development/ui-builder/ui-builder-overview.md).

![Grouping of contract documents](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/../image/cmpro-bu-ctypr-grouping-result.png "Contract document grouping")

## Procedure

1.  Navigate to **Now Experience Framework** &gt; **UI Builder**.

2.  Search and select your workspace.

3.  Navigate to **Record** &gt; **SRP record**.

4.  In the Page content list, under **Body** &gt; **Resizable panes** &gt; **left** &gt; **Main Tab** &gt; **Related List**, select **list related**.

    ![Select related list configuration for your workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/../image/cmpro-bu-ctype-group-related-list.png "UI builder related list configuration")

5.  In the **Configure** pane, select **Group by** field.

    ![Select group from the Configure pane](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/../image/cmpro-bu-ctype-group-script.png "Configure pane")

6.  Enter the following code in the **Group by** field:

    ```
    function evaluateProperty({api, helpers}) {
      var isContractRequestForm = api.item.value.parentTable =="sn_cm_core_contract_request";
      var isContractRevisionTab = api.item.value.table == "sn_cm_core_document_revision";
      if( isContractRequestForm && isContractRevisionTab){
        return 'document';
      }
    return '';
    }
    ```

    **Note:** If the field is not editable, select the scope applicable to your workspace in the **Select an application** drop-down list at the top of the page.

7.  Select **Apply**.


## Result

The contract documents will be grouped by contract type in the Contract document tab while viewing a contract request.

**Parent Topic:**[Add and configure contract request functionality into your workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/../concept/cncore-uptake-steps.md)

**Related topics**  


[Configure non-task tables for contract templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cmpro-config-non-tsk-tbl-cn-tmplt.md)

[Add a workspace action button for initiating a contract request](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-config-initiate-cont.md)

[Add Contract requests tab to the contract request record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-add-relatedlist-conreq.md)

[Add amendment tabs to contract repository record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-BU-amend-relatedlist.md)

[Add Contract documents tab to the contract repository record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-add-con-doc-relatedl.md)

[Copy fields from parent request to contract request](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-copy-fld-frm-parent.md)

[Add access to obligation management from contract repository records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cmpro-add-access-to-ob-mgmt.md)

[Configure the contract request form header for your workspace](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-configure-header.md)

[Assign a role for configuring template mappings](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-tbl-access-config-role.md)

[Enable contract request fields in condition builders](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cncore-add-cmr-condtion-build.md)

[Configuring the Playbook tab on contract repository records](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/contract-management-pro/cmpro-config-playbook-tab.md)

