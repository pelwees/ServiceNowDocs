---
title: Security Operations Integration- Get Network Statistics capability
description: The Get Network Statistics capability retrieves a list of active network connections from a host or endpoint. It can be used for incident enrichment during investigations. This capability is triggered automatically when a configuration item is added to a security incident.
locale: en-US
release: australia
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Integration capabilities, Security Operations Integration Reference, Security Operations common functionality, Security Operations]
---

# Security Operations Integration- Get Network Statistics capability

The Get Network Statistics capability retrieves a list of active network connections from a host or endpoint. It can be used for incident enrichment during investigations. This capability is triggered automatically when a configuration item is added to a security incident.

The **Get Network Statistics** capability has a flow, [Security Operations Integrations - Get Network Statistics flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../../security-operations-integrations/task/secops-integration-get-network-stats-workflow.md) that accepts one or more CIs and tasks. The flow iterates over each implementation and each CI and re-invokes the implementation flow.

**Note:** If no implementations are available, capability actions are not displayed in product menus.

-   **[Security Operations Integrations - Get Network Statistics flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../../security-operations-integrations/task/secops-integration-get-network-stats-workflow.md)**  
The Security Operations Integrations - Get Network Statistics flow retrieves a list of active network connections from a host or endpoint.
-   **[Security Incident Response- Get Network Statistics flow](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../../security-incident-response-orchestration/task/obtain-network-statistics-workflow.md)**  
The **Security Incident Response** &gt; **Get Network Statistics** flow retrieves the network statistics for an affected Windows-based resource when added to a security incident in the **Analysis** state.

**Parent Topic:**[Integration capabilities](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/integration-capabilities.md)

**Related topics**  


[Security Operations Integration- Block Request capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/block-request-capability.md)

[Security Operations Integration- Email Search and Delete capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/email-search-capability.md)

[Security Operations Integration- Enrich CI capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/enrich-ci-capability.md)

[Security Operations Integration- Enrich Observable capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/enrich-observable-capability.md)

[Security Operations Integration- Get Running Processes capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/get-running-processes-capability.md)

[Security Operations Integration- Isolate Host capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/isolate-host-capability.md)

[Security Operations Integration- Publish to Watchlist capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/pubish-to-watchlist-capability.md)

[Security Operations Integration- Sightings Search capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/sightings-search-capability.md)

[Security Operations Integration - Threat Lookup capability](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/sec-ops-threat-lookups-capability.md)

[Change the order of flow execution](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/security-management/../task/change-wf-execution-order.md)

