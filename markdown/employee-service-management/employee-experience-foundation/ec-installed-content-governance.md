---
title: Components installed with Content Governance
description: Several types of components install with the activation of the Content Governance \[sn\_cg\] plugin, including tables, user roles, and scheduled jobs.
locale: en-US
release: australia
product: Employee Experience Foundation
classification: employee-experience-foundation
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Employee Center Pro reference, Employee Center Pro, Unified Employee Experience, Employee Service Management]
---

# Components installed with Content Governance

Several types of components install with the activation of the Content Governance \[sn\_cg\] plugin, including tables, user roles, and scheduled jobs.

**Note:** The Application Files table lists the components that are installed with this application. For instructions on how to access this table, see [Find components installed with an application](https://raw.githubusercontent.com/ServiceNow/ServiceNowDocs/australia/markdown/platform-administration/find-components.md).

Demo data is available for this feature.

**Note:** The Content Governance \[sn\_cg\] plugin activates the sn\_cda.min\_admin\_count system property \[sys\_properties.list\]. This property prevents you from deleting your only Governance admin user by requiring a minimum number \(default is two\) of active users with this role.

## Roles installed

|Role title \[name\]|Description|Contains roles|
|-------------------|-----------|--------------|
|Content request user \[sn\_cg.content\_request\_user\]|Gives read and write access to content request records. This role is automatically assigned to the Content Publishing Content admin \(sn\_cd.content\_admin\) and Content manager \(sn\_cd.content\_manager\) roles.|None|
|Content items request user \[sn\_cg.content\_request\_item\_user\]|Gives read and write access to content items records. This role is automatically assigned to the Content Publishing Content admin \(sn\_cd.content\_admin\) and Content manager \(sn\_cd.content\_manager\) roles.|None|

## Tables installed

|Table|Description|
|-----|-----------|
|Content Request Item \[sn\_cg\_content\_request\_item\]|Content created from the Content Governance interface|
|Content Request \[sn\_cg\_content\_request\]|Request for content created by an employee or manager|

**Parent Topic:**[Employee Center Pro reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/emp-center-pro-reference.md)

**Related topics**  


[Block content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/block-content-form.md)

[Campaign overview and Campaign analytics dashboards](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../concept/ecpro-content-automation-content-pack.md)

[Components installed with Employee Center Pro](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/components-installed-with-employee-center-pro-1.md)

[Components installed with Content engagement](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/installed-content-engagement.md)

[Components installed with Content Experiences](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/installed-with-content-auto.md)

[Components installed with Content Publishing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/installed-with-content-delivery.md)

[Components installed with Content Analytics](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ecpro-installed-content-analytics-1.md)

[Content Analytics dashboards](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../concept/content-analytics-dashboards.md)

[Content engagement dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../concept/ec-pro-content-engagement-dashboard.md)

[Content Library Overview dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../concept/content-library-overview-dashboard.md)

[Employee Center Pro widgets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/employee-center-pro-widgets-list.md)

[Feedback configuration form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ex-feedback-new-record.md)

[Feedback definition form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/fdbck-dfnition-record.md)

[Link content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/link-content-form.md)

[Notification content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notification-content-form.md)

[Properties installed with Content Experiences](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/properties-installed-with-content-auto.md)

[Properties installed with Content Governance](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/properties-installed-content-governance.md)

[Properties installed with Content Publishing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/properties-with-content-delivery.md)

[Standard banner and icon sizes](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ec-portal-images-size.md)

[To-do content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/to-do-content-form.md)

