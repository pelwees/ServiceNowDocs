---
title: Set up integrations for Health Log Analytics from the Integrations Launchpad
description: Set up integrations from the Event Management Integrations Launchpad in Service Operations Workspace for ITOM.
locale: en-US
release: australia
product: Health Log Analytics
classification: health-log-analytics
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 5
keywords: [ServiceNow, Health Log Analytics, HLA, data input setup, integration, Integrations Launchpad]
breadcrumb: [Set up HLA on your instance, Configuring, Health Log Analytics, ITOM AIOps, IT Operations Management]
---

# Set up integrations for Health Log Analytics from the Integrations Launchpad

Set up integrations from the Event Management Integrations Launchpad in Service Operations Workspace for ITOM.

## Integrations Launchpad

The Integrations Launchpad tool provides a unified interface for convenient integration with connectors that feed raw log messages from external sources into your ServiceNow instance for processing and analysis. For more information, see [Integrations Launchpad in Service Operations Workspace for ITOM](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../../service-operations-workspace-itom/concept/integrations-launchpad.md).

## Integrations for Health Log Analytics

The Integrations Launchpad enables the following integrations for Health Log Analytics:

-   **Pull integrations**

    These integrations pull log data from external data sources and stream the data to your instance, typically via a MID Server. Select an integration in the table to open a page with the setup procedure.

<table id="table_qzq_kf1_mcc"><thead><tr><th>

Integration

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[Amazon CloudWatch](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/hla-data-input-cloudwatch.md)

</td><td>

Streams log data from Amazon CloudWatch to your instance.

</td></tr><tr><td>

[Amazon S3](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-aws-s3.md)

</td><td>

Streams log data from Amazon S3 \(Simple Storage Service\) buckets to your instance.

</td></tr><tr><td>

[Apache Kafka](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-kafka.md)

</td><td>

Streams log data from Apache Kafka to your instance.

</td></tr><tr><td>

[Elasticsearch](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-elasticsearch.md)

</td><td>

Streams log data from Elasticsearch indices to your instance.

</td></tr><tr><td>

[Microsoft Azure Event Hubs](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-event-hubs.md)

</td><td>

Streams events from Microsoft Azure Event Hubs to your instance.

</td></tr><tr><td>

[Microsoft Azure Event Hubs \(MID-less\)](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-eventhubs-midless.md)

</td><td>

Streams events from Microsoft Azure Event Hubs to your instance without a MID Server.

</td></tr><tr><td>

[Microsoft Azure Log Analytics](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-azure-la.md)

</td><td>

Streams log data from Microsoft Azure Log Analytics to your instance. The connector points the Health Log Analytics AI engine to a data source in your Microsoft Azure Log Analytics account.

</td></tr><tr><td>

[MID Server](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-mid.md)

</td><td>

Collects log messages from the MID Server and streams them to your instance.

</td></tr><tr><td>

[ServiceNow System Logs Retriever](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-glide-syslog.md)

</td><td>

Sends log data from the ServiceNow System Log table to the Health Log Analytics AI engine.This integration doesn't run on a MID Server.

**Note:** Only a single ServiceNow System Logs Retriever data input can exist in the system, and only users with the admin role can create and configure it.

</td></tr><tr><td>

[Splunk Poller](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-splunk-polling.md)

</td><td>

Pulls log data from Splunk to your ServiceNow instance periodically by query.

</td></tr></tbody>
</table>-   **Push integrations**

    These integrations connect to external data sources that push log data to your instance, typically via a MID Server. Select an integration in the table to open a page with the setup procedure.

<table id="table_ezf_rh1_mcc"><thead><tr><th>

Integration

</th><th>

Description

</th></tr></thead><tbody><tr><td>

[Amazon Data Firehose](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-firehose.md)

</td><td>

Streams log messages from Amazon Data Firehose directly to the collector service in ITOM Gateway, where it’s queued for Health Log Analytics processing.This integration doesn't run on a MID Server.

</td></tr><tr><td>

[Cribl](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-cribl.md)

</td><td>

Enables Health Log Analytics to process Cribl log messages streaming into the ServiceNow instance.

</td></tr><tr><td>

[Edge Delta REST](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-edgedelta-rest.md)

</td><td>

Enables Health Log Analytics to process logs it receives from Edge Delta in a distinct format. These logs stream into the ServiceNow instance via REST.

</td></tr><tr><td>

[Edge Delta TCP](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-edgedelta-tcp.md)

</td><td>

Enables Health Log Analytics to process logs it receives from Edge Delta in a distinct format. These logs stream into the ServiceNow instance over the TCP transport protocol.

</td></tr><tr><td>

[GCP PubSub](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-gcp-pubsub.md)

</td><td>

Receives log messages that were published to a Google Cloud Pub/Sub topic and streams them to your instance.

</td></tr><tr><td>

[REST API](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-rest-api.md)

</td><td>

Streams log data to your instance in JSON format.

</td></tr><tr><td>

[Splunk TCP](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-splunktcp.md)

</td><td>

Streams log messages to your ServiceNow instance over the TCP transport protocol using a Splunk heavy forwarder.

</td></tr><tr><td>

[Splunk UDP](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-splunkudp.md)

</td><td>

Streams log messages to your ServiceNow instance over the UDP transport protocol using a Splunk heavy forwarder.

</td></tr><tr><td>

[TCP](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-tcp.md)

</td><td>

Sends raw log messages to your instance directly over a TCP/SSL socket.

</td></tr><tr><td>

[UDP](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-udp.md)

</td><td>

Sends raw log messages to your instance directly over a UDP socket.

</td></tr><tr><td>

[Vector Agent](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/../task/il-connector-hla-vector.md)

</td><td>

Enables Health Log Analytics to process log messages that are streaming into the ServiceNow instance via a Vector Agent.

</td></tr></tbody>
</table>
**Parent Topic:**[Set up Health Log Analytics on your ServiceNow instance](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/it-operations-management/health-log-analytics/hla-implement.md)

