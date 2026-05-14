---
title: Zing matches derived words with stemming
description: Convert any multiple-character search keyword to its stem form to find derived versions of the word.
locale: en-US
release: australia
product: Search Administration
classification: search-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Zing text indexing and search engine, Search administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Zing matches derived words with stemming

Convert any multiple-character search keyword to its stem form to find derived versions of the word.

Stemming removes a variety of common word inflections, such as plurals and past tense forms. Zing treats all words with a common stem as synonyms of the original search term. Stemming doesn't apply to searches involving single-character words such as Chinese and Japanese pictograms.

Zing uses the [Porter Stemming Algorithm](https://tartarus.org/martin/PorterStemmer/), which is most effective for English text, but supports stemming in these languages.

-   English
-   French
-   German

The stemming language determines how the system generates indexes of record data. The system only supports one stemming language at a time regardless of how many languages the instance supports. When you change the stemming language, the system creates any new index entries based on the new language stemming rules, but doesn't regenerate any existing index records. You must manually regenerate indexes for tables you want to use the new stemming language.

**Parent Topic:**[Zing text indexing and search engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_ZingTextSearch.md)

**Related topics**  


[Features of Zing text indexing and search engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../reference/features-zing.md)

[Available search options](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_IntroductionToSearching.md)

[Global search finds records from multiple tables](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_GlobalTextSearch.md)

[Zing generates search results in four phases](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_SearchProcess.md)

[Zing filters search results with access controls](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/zing-filters-search-results.md)

[Zing computes document scores using three components](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_DocumentScoring.md)

[Zing indexes words](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/zing-indexes-words.md)

[Zing can include attachments in search results](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_SearchingForAttachments.md)

[Zing removes stop words from queries](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/stop-words-removed-from-queries.md)

[Zing can expand search results with synonyms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/search-synonyms-expand-results.md)

[Zing displays search suggestions as users enter search terms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/search-suggestions-zing.md)

[Installed with Zing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../reference/installed-with-zing.md)

