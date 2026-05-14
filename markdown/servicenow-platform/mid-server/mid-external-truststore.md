---
title: Specify an external TrustStore for the MID Server
description: The MID Server JVM can utilize a TrustStore external to the MID installation directory so any certificates added to the TrustStore are not overwritten during an upgrade. It is important that this TrustStore file reside outside of the MID installation directory, and the Truststore location can be specified by adding additional parameters to the MID Server's wrapper-override.conf file.
locale: en-US
release: australia
product: MID Server
classification: mid-server
topic_type: task
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Securing and encrypting MID Server data, MID Server, Manage instance data sources, Extend ServiceNow AI Platform capabilities]
---

# Specify an external TrustStore for the MID Server

The MID Server JVM can utilize a TrustStore external to the MID installation directory so any certificates added to the TrustStore are not overwritten during an upgrade. It is important that this TrustStore file reside outside of the MID installation directory, and the Truststore location can be specified by adding additional parameters to the MID Server's `wrapper-override.conf` file.

## Before you begin

Role required: admin

## Procedure

1.  In the MID Server host, navigate to the `wrapper-override.conf` file.

2.  Specify an external TrustStore by appending a custom parameter to the end of your MID’s `wrapper-override.conf` file.

    For example, on a Windows MID with an external TrustStore found at `C:\external_truststore\cacerts`, the end of the file would appear similar to:

    ```
    # Add additional custom parameters below
    
    wrapper.java.additional.3=-Djavax.net.ssl.trustStore=C:\external_truststore\cacerts
    
    wrapper.java.additional.4=-Djavax.net.ssl.trustStorePassword=<truststore’s password>
    ```

    **Note:** If you have specified other additional parameters in this file then the numerical identifier, in this case 3 and 4, may differ.


**Parent Topic:**[Securing and encrypting MID Server data](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-server-security-encryption.md)

**Related topics**  


[MID Server certificate check policies](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-security-checks.md)

[Encrypt or decrypt MID Server configuration file values](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/mid-server-manual-encryption.md)

[MID Server configuration file security](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/mid-server-encrypter-api.md)

[MID Server authentication credentials and SOAP requests](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-authentication-soap-requests.md#)

[MID Server unified key store](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-unified-keystore.md#)

[Enable MID Server mutual authentication](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/install-mid-mutual-auth.md)

[MID Server Azure Key Vault integration](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/mid-azure-key-vault-integration.md#)

[MID Server command audit log](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-audit-log.md)

[Rekey a MID Server](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/t_RekeyAMIDServer.md)

[Add SSL certificates for the MID Server](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/add-ssl-certificates.md#)

[MID Server SSH cryptographic algorithms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../reference/mid-ssh-algorithms.md)

[Attach a script file to a file synchronized MID Server](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/mid-server-script-attach.md#)

[MID Server FIPS Enforced Mode](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-fips-enforced.md#)

[MID Server Governance](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/servicenow-platform/mid-server/../concept/mid-timeout.md)

