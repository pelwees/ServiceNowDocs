---
title: Tracking message usage in Hermes
description: Message usage through the Hermes Messaging Service is tracked for monitoring and management purposes through the Kafka topic name.
locale: en-US
release: australia
product: Multi-Instance Framework - Hermes
classification: multi-instance-framework-hermes
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Administer, Hermes Messaging Service, Manage service capabilities, Extend ServiceNow AI Platform capabilities]
---

# Tracking message usage in Hermes

Message usage through the Hermes Messaging Service is tracked for monitoring and management purposes through the Kafka topic name.

You access the Hermes Messaging Service exclusively through integrations with other applications, such as Stream Connect and Log Export Service.

You can access Kafka topics in your namespace using the following naming convention:

```
snc.<instance_name>.<namespace>.sn_<app_id>.<topic_name>
```

where:

-   `snc.<instance_name>` is your namespace prefix
-   `<namespace>` is the namespace of the domain your Kafka topic belongs to \(optional\)
-   `sn_<app_id>` is your application ID
-   `<topic_name>` is your unique topic name

**Note:** The full topic name is case-sensitive and limited to 200 characters.

Kafka message usage and licensing impact vary by application. License usage is tracked at the application level.

**Parent Topic:**[Administering Hermes Messaging Service](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/hermes-messaging-service-administration.md)

**Related topics**  


[Check the status of and connection to the Hermes Kafka cluster](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/../task/run-hermes-messaging-service-diagnostics.md)

[Monitoring data usage in Hermes](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/monitoring-data-usage-hermes.md)

[Cloning with Hermes Messaging Service enabled](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/cloning-with-hermes-messaging-service.md)

[View Hermes Messaging Service log messages](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/multi-instance-framework-hermes/../task/view-hermes-log-messages.md)

