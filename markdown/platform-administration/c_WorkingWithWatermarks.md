---
title: Watermarks on notification emails
description: By default, a unique watermark label will be generated at the bottom of each notification email to allow matching incoming email to existing records.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Email and SMS notifications, System notifications, Notifications, Configure core features, Administer the ServiceNow AI Platform]
---

# Watermarks on notification emails

By default, a unique watermark label will be generated at the bottom of each notification email to allow matching incoming email to existing records.

Starting with the Jakarta release, randomized watermarks will be automatically generated for notification emails in base systems. The random character string succeeded by an underscore reduces the possibility of a watermark being guessed or coincidentally matching the watermark of an email from another instance.

**Note:** If you are upgrading from a release before Jakarta, random watermark support is optional and requires the Random Watermark Support plugin to be activated.

## Watermark format

The email watermark always begins with "**Ref:**" to identify the label as a watermark. After this identifier, the default label is 31 characters in length and consists of:

-   A customizable prefix — The default prefix is **MSG**.
-   An auto-numbered identifier — The numeric string identifying the source record, such as incident, problem, or change request.
-   An underscore character followed by a random character string.

![Randomized watermark format](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../image/random-watermark-format.png "Randomized watermark example")

When inbound emails are processed, the system matches random watermarks to the appropriate source records.

## Watermark configuration

Watermarks are always generated, but you can configure them as follows:

-   Create a custom watermark prefix for each instance to prevent accidentally triggering events in the wrong instance.
-   Use custom prefix characters after MSG.
-   Hide all email watermarks globally.
-   Omit watermarks from individual email messages.

If watermarks are omitted from email notifications, inbound email actions might not work properly. Without a watermark, the system processes inbound email messages as described in [Criteria for matching email to inbound actions](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/inbound-action-type-criteria.md).

**Note:** Email clients that use the plain text version of the email still show the watermark.

-   **[Create a custom watermark prefix for email notifications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../task/t_CreatingCustomWatermarkPrefixes.md)**  
By default, email notifications use the watermark prefix **MSG**, but you can create a custom watermark prefix.
-   **[Omit an email notification watermark](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../task/t_OmitWatermarksIndEmailNotif.md)**  
You can omit watermarks on email notifications if you do not want the instance to match the notification to an existing record.
-   **[Hide email watermarks globally](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../task/t_HidingWatermarksGlobally.md)**  
Rather than omitting watermarks, it is possible to hide watermarks for global application using HTML markup.

**Parent Topic:**[Email and SMS notifications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/c_EmailNotifications.md)

**Related topics**  


[Create notification categories](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../task/create-notification-categories.md)

[Create an email notification](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../task/t_CreateANotification.md)

[Email notifications dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/email-notifications-dashboard.md)

[Email diagnostics dashboard](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/email-diagnostics-dashboard.md)

[Email templates](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/c_EmailTemplates.md)

[Email layouts](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/email-layouts.md)

[Email retention](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/email-retention.md)

[Parse an email thread](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/../task/parse-email.md)

[Email digests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/email-digests.md)

[Domain separation and Notifications](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/domain-separation-notifications.md)

[Email FAQs and troubleshooting notification emails](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/troubleshooting-notification-emails.md)

