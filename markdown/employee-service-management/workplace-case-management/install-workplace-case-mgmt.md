---
title: Install Workplace Case Management
description: Install the Workplace Case Management application from ServiceNow Store applications. Visit the ServiceNow Store to view all the available apps, and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the ServiceNow Store version history release notes.
locale: en-US
release: australia
product: Workplace Case Management
classification: workplace-case-management
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Configure, Workplace Case Management, Workplace Service Delivery, Employee Service Management]
---

# Install Workplace Case Management

Install the Workplace Case Management application from ServiceNow Store applications. Visit the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home) to view all the available apps, and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the [ServiceNow Store version history release notes](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/sn-store-release-notes.html).

## Before you begin

Complete the following setup checklist.

|Setup tasks|Description|
|-----------|-----------|
|Verify that Workplace Service Delivery - Core \(sn\_wsd\_core\) plugin of minimum version 2.0 is activated.|Navigate to **Subscription Management** &gt; **Subscriptions** in your instance. The list displays the subscriptions that your organization has purchased.|
|Verify that Workplace Case Management \(sn\_wsd\_case\) plugin is activated.|Navigate to **Subscription Management** &gt; **Subscriptions** in your instance. The list displays the subscriptions that your organization has purchased.|

Activate the Workplace Service Delivery - Core plugin of minimum version 2.0 \(sn\_wsd\_core\) in your ServiceNow instance before you install Workplace Case Management.

Use the following details when required:

-   Name of the application: Workplace Case Management
-   ID of the application: sn\_wsd\_case

Role required: admin

## About this task

## Procedure

1.  Navigate to **System Applications** &gt; **All Available Applications** &gt; **All**.

2.  Find the application using the filter criteria and search bar.

    You can search for the application by its name or ID. If you cannot find an application, you may have to request it from ServiceNow store.

    Visit the [ServiceNow Store](https://store.servicenow.com/sn_appstore_store.do#!/store/home) website to view all the available apps and for information about submitting requests to the store. For cumulative release notes information for all released apps, see the [ServiceNow Store version history release notes](https://docs.servicenow.com/bundle/store-release-notes/page/release-notes/store/sn-store-release-notes.html).

3.  Click **Install**.

4.  In the Application installation dialog box, review the application dependencies.

    Dependent plugins and applications are listed if they will be installed, are currently installed, or need to be installed. If there are any plugins or applications that need to be installed, you must install them before you can install Workplace Case Management.

5.  If demo data is available and you want to install it, click **Load demo data**.

    Demo data comprises sample records that describe application features for common use cases. Load demo data when you first install the application on a development or test instance.

    **Important:** If you don't load the demo data during installation, it's unavailable to load later.

6.  Click **Install**.


**Parent Topic:**[Configuring Workplace Case Management](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/../concept/workplace-case-mgmt-setup.md)

**Related topics**  


[Create a Workplace case template](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/wsd-case-template.md)

[Create a Workplace task template](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/wsd-task-template.md)

[Smart Assessment for Workplace Case and Task](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/smart-assessment-for-workplace-case-and-task.md)

[Automating seat assignment for new hires](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/../concept/auto-assign-new-hires.md)

[Configure Approval options](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/config-approval-optns.md)

[Configure a Record producer](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/wsd-create-record-producer.md)

[Configuring a record producer for request edit](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/../concept/config-case-edit-rp.md)

[Configuring a record producer for reservation](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/../concept/config-reservation-rp.md)

[Create an SLA Definition](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/create-sla-defn-case-mgmt.md)

[Create a Workplace service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/create-workplace-service.md)

[Add a workplace service item to a workplace service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/add-workplace-service-items.md)

[Create a workplace template configuration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/create-workplace-template-confguration.md)

[Create a workplace field mapping](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/create-workplace-field-mapping.md)

[Configure an escalation rule](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/configure-escalation-rule.md)

[Add Fulfillment instructions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/add-fulfillment-instructions.md)

[Group similar workplace cases under a parent case](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/workplace-case-management/group-similar-workplace-cases.md)

