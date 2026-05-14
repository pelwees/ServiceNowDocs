---
title: Zing can include attachments in search results
description: Search content from attachments on indexed tables. Display attachments for search results from the Knowledge \[kb\_knowledge\] table.
locale: en-US
release: australia
product: Search Administration
classification: search-administration
topic_type: concept
last_updated: "2026-03-12"
reading_time_minutes: 2
breadcrumb: [Zing text indexing and search engine, Search administration, Configure core features, Administer the ServiceNow AI Platform]
---

# Zing can include attachments in search results

Search content from attachments on indexed tables. Display attachments for search results from the Knowledge \[kb\_knowledge\] table.

![Sample Knowledge search including attachments.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../../../product/knowledge-management/image/Km_search_filter_H.png "Sample Knowledge search showing attachments with matching content")

By default, search only matches content from attachments on Knowledge \[kb\_knowledge\] records. Administrators can [enable search for attachments on other tables](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../../form-administration/task/t_DisablingAttachmentsOnATable.md), but doing so causes the system to re-index the selected table, its parent table, and any children of the parent table.

**Warning:** For large tables, such as the Task table, re-indexing can take several hours and slows down the system until complete. Re-indexing is best performed during non-peak times.

The search results page only displays attachments for search results from the Knowledge \[kb\_knowledge\] table, even if other tables have attachment search enabled.

![Global search results page displaying attachments for Knowledge search results but not for search results from other tables.](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../image/global-search-result-attachments.png "Global search displays attachments for Knowledge search results but not for search results from other tables")

Zing supports indexing and searching these attachment file types.

-   .doc
-   .docx
-   .dot
-   .dotx
-   .htm
-   .html
-   .ini
-   .pdf
-   .pot
-   .potx
-   .ppt
-   .pptx
-   .reg
-   .txt
-   .xls
-   .xlsx
-   .xlt
-   .xltx

-   **[Index attachments on a table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../../form-administration/task/t_DisablingAttachmentsOnATable.md)**  
You can enable attachment indexing for a table so text searches can return matches from the record and its file attachments.

**Parent Topic:**[Zing text indexing and search engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_ZingTextSearch.md)

**Related topics**  


[Features of Zing text indexing and search engine](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../reference/features-zing.md)

[Available search options](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_IntroductionToSearching.md)

[Global search finds records from multiple tables](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_GlobalTextSearch.md)

[Zing generates search results in four phases](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_SearchProcess.md)

[Zing filters search results with access controls](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/zing-filters-search-results.md)

[Zing computes document scores using three components](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/c_DocumentScoring.md)

[Zing indexes words](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/zing-indexes-words.md)

[Zing removes stop words from queries](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/stop-words-removed-from-queries.md)

[Zing matches derived words with stemming](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/stemming-matches-derived-words.md)

[Zing can expand search results with synonyms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/search-synonyms-expand-results.md)

[Zing displays search suggestions as users enter search terms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/search-suggestions-zing.md)

[Installed with Zing](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../reference/installed-with-zing.md)

[Index attachments on a table](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/platform-administration/search-administration/../../form-administration/task/t_DisablingAttachmentsOnATable.md)

