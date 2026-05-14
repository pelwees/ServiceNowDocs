---
title: Define an audience for your variant
description: An audience represents a group of users in your organization. You can define who can access this page variant by adding one or more predefined audiences.
locale: en-US
release: australia
product: UI Builder
classification: ui-builder
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Learn UI Builder by example, Learning UI Builder, UI Builder, Builder library, Developing your application, Building applications]
---

# Define an audience for your variant

An audience represents a group of users in your organization. You can define who can access this page variant by adding one or more predefined audiences.

## Before you begin

Role required: ui\_builder\_admin

## About this task

In the previous procedure, you created a page variant that can be viewed by anyone accessing a record from the Task table. For this procedure, you will duplicate the variant and configure it so that it is accessible only to audiences with the Admin role.

## Procedure

1.  Open the main page for your demo experience.

2.  Select the experience you created, expand a page and select **Default**.

    ![Demo experience Editor page.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/../image/audience-experience-view.png "Demo Experience")

3.  Select the **Open menu** icon.

    ![Open menu button.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/../image/open-menu.png "Open menu")

4.  Select **Duplicate variant**.

5.  On the **Tell us about your variant** screen, enter **Admin only** in the **Name** field.

6.  Select **+ Add** next to **Audiences**, and select the **Admin** audience.

    ![Select the Admin audience.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/../image/admin-audience.png "Select the Admin audience")

7.  Select **Create**.

    The variant is duplicated and only users with the Admin role can view this page.


## What to do next

Select the **Next topic** link to learn how to apply conditions to the variant so that the variant is visible only when the defined conditions are met.

**Parent Topic:**[Learn UI Builder by example](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/../concept/learning-uib-by-example.md)

**Related topics**  


[Create a demo experience to explore UI Builder](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/learn-by-example-create-experience.md)

[Create a blank page](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/learn-by-example-create-blank-page.md)

[Create a record page using a template](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/learn-by-example-create-page-with-template.md)

[Define conditions for your variant](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/learn-by-example-define-conditions.md)

[Customize forms within a form component](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/application-development/ui-builder/learn-by-example-edit-form-component.md)

