---
title: Guided Self-Service reference
description: Use the following reference information for the Guided Self-Service functionality.
locale: en-US
release: australia
product: Employee Experience Foundation
classification: employee-experience-foundation
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 4
breadcrumb: [Employee Center reference, Employee Center, Unified Employee Experience, Employee Service Management]
---

# Guided Self-Service reference

Use the following reference information for the Guided Self-Service functionality.

## Guided Self-Service: Things to remember

You can display Guided Self-Service as a widget on the home page or as a quick link or as a widget on topic pages. Remember the following information:

-   Ensure that the **sn\_hr\_sp.esc\_admin** user has the **playbook.write** role to edit the playbook design and **playbook\_experience.admin** to preview the guided experience.
-   Only when the playbook and guided help process are in an active state, the guided help process appears on the Employee Center.
-   Guided Self-Service can’t be created from the playbook page directly, create the process from the GSS form, see [Configure Guided Self-Service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../task/gss-guided-help-config.md).
-   Guided Self-Service flow is a single-stage flow.
-   The Activity Definition \[sys\_pd\_activity\_definition\] table lists the definitions for the activities that you can add to a playbook in **Workflow Studio**.

    To access the activity definitions, navigate to **Process Automation** &gt; **Process Automation Administration** &gt; **Activity Definitions**

-   State management of your choices in an activity is retained for 24 hours only.
-   When a guided process activity is partially completed or aborted mid-way, you can resume and complete the rest of the process within 24 hours.
-   Currently, the option to restart the activity or change the selections isn’t supported after 24 hours. The process restarts afresh.
-   The completed self-service is purged after 30 days with the auto-flush schedule available from sys\_trigger\_list.
-   The `Cancel incomplete guided help playbook` scheduled job for the automatic cancellation of incomplete guidance is only available for admin.
-   Deleting the GSS process from `sn_ex_sp_gd_help_process` doesn’t delete the process from `sys_pd_process_definition`.

**Parent Topic:**[Employee Center reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/emp-center-reference.md)

**Related topics**  


[Activity Configuration form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ec-activity-configuration-form.md)

[Activity Configuration Detail form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/activity-configuration-detail-form.md)

[Approvals experience reference](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/approval-hub-ootb.md)

[Connected Content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/connected-content-form.md)

[Default Employee Profile Header Configuration record](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/default-profile-header.md)

[Employee Center widgets](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../concept/employee-center-widgets-list.md)

[Employee Profile form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/employee-profile-fieldconfig.md)

[Employee Profile Header Configuration form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/profile-header-config-form.md)

[Employee Profile portal configuration form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/profile-portal-config-form.md)

[Employee Profile upgrade scenarios](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/emp-profile-upgrade.md)

[Enhanced Requests Experience forms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/req-concept-ec.md)

[External Link form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/external-link-form.md)

[Featured Content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/featured-content-form.md)

[Footer form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ec-footer-form.md)

[Footer Menus form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ec-footer-menus.md)

[Menu Item form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/menu-item-form.md)

[Overview section form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/profile-overview-section-form.md)

[Portal notification configuration form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/portal-notif-config-form.md)

[Portal notification content form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-content-form.md)

[Trigger conditions form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/notif-trigger-form.md)

[Quick Link form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ec-quick-link-form.md)

[Tab widget mapping form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/tab-widget-mapping-form.md)

[Taxonomy form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/taxonomy-form.md)

[Topic form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/topic-form.md)

[User Criteria form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/ec-user-criteria-form.md)

[User Criteria output](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/user-criteria-output.md)

[Schedule appointment form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/schedule-appointment-form.md)

[Location Consent form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/location-consent-form.md)

[Website configuration form](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/config-website-form.md)

[Use Guided Self-Service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/employee-service-management/employee-experience-foundation/../concept/gss-guided-self-service-homepage.md)

