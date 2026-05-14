---
title: Zing filters search results with access controls
description: Zing filters search results to only display records the user can access.
locale: en-US
release: australia
product: Search Administration
classification: search-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 1
breadcrumb: [Zing text indexing and search engine, Search administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Zing filters search results with access controls

Zing filters search results to only display records the user can access.

For example, suppose you index the System Property \[sys\_properties\] table. When the ITIL user searches for a term in the System Property table, Zing returns no search results because the ITIL user doesn't meet the ACL rule requirements.

![Empty search results page for ITIL user search in System Property table.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../image/ITILUserSearch.png "ITIL User Search")

When a system administrator searches for the same property, Zing returns search results from the System Property table because the administrator meets the ACL rule requirements.

![Search results for system administrator search in System Property table.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../image/SystemAdministratorSearch.png "System Administrator Search")

**Parent Topic:**[Zing text indexing and search engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_ZingTextSearch.md)

**Related topics**  


[Features of Zing text indexing and search engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../reference/features-zing.md)

[Available search options](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_IntroductionToSearching.md)

[Global search finds records from multiple tables](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_GlobalTextSearch.md)

[Zing generates search results in four phases](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_SearchProcess.md)

[Zing computes document scores using three components](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_DocumentScoring.md)

[Zing indexes words](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/zing-indexes-words.md)

[Zing can include attachments in search results](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_SearchingForAttachments.md)

[Zing removes stop words from queries](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/stop-words-removed-from-queries.md)

[Zing matches derived words with stemming](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/stemming-matches-derived-words.md)

[Zing can expand search results with synonyms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/search-synonyms-expand-results.md)

[Zing displays search suggestions as users enter search terms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/search-suggestions-zing.md)

[Installed with Zing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../reference/installed-with-zing.md)

