---
title: Data extraction modes
description: Extraction modes determine how the data is extracted in the document task and how the task is processed. The mode changes the behavior of the fields in the Document Intelligence workspace.
locale: en-US
release: australia
product: Document Intelligence
classification: document-intelligence
topic_type: reference
last_updated: "2026-03-12"
reading_time_minutes: 3
breadcrumb: [Reference, Document Intelligence, Enable AI experiences]
---

# Data extraction modes

Extraction modes determine how the data is extracted in the document task and how the task is processed. The mode changes the behavior of the fields in the Document Intelligence workspace.

**Important:** Starting with the Zurich release, Document Intelligence is being prepared for future deprecation. It will be hidden and no longer activated on new instances but will continue to be supported. For details, see the Deprecation Process article \[[KB0867184](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0867184)\] in the Now Support Knowledge Base. Instead, you can extract information from documents using the Now Assist in Document Intelligence application. For more information, see [Now Assist in Document Intelligence](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/../concept/docintel-nowassist-landing.md).

DocIntel uses the following extraction modes.

<table id="table_pmc_dqx_qbc"><thead><tr><th>

Extraction mode

</th><th>

Description

</th></tr></thead><tbody><tr><td>

Recommendation

</td><td>

DocIntel provides recommendations for the fields in the Document Intelligence workspace. Choose the recommendation or manually enter the value. All fields must be reviewed.

 Recommendations are ordered based on how confident the AI is in the prediction. As DocIntel continues processing your documents, recommendations improve over time.

</td></tr><tr><td>

Auto-fill

</td><td>

DocIntel auto-fills the fields in the Document Intelligence workspace. All fields must be reviewed.

 Auto-fill works only if the AI has enough confidence to make the prediction. You can change the confidence threshold by updating the **Auto-fill threshold** field in the use case.

</td></tr><tr><td>

Fully automated

 \(Straight-through processing\)

</td><td>

DocIntel automatically extracts the data for all fields and processes the document task if the confidence scores for all required fields are above the defined confidence threshold. Fields don’t need to be reviewed.

 **Note:** For Fully automated mode to process tasks successfully, the use case must have at least one field designated as required.

 DocIntel becomes more confident over time, as it processes more and more documents. Choose Fully automated mode for frequently processed documents or if you’re confident in the system.

</td></tr></tbody>
</table>**Parent Topic:**[Document Intelligence references](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/docintel-references.md)

**Related topics**  


[Components installed with Document Intelligence](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/installed-with-document-intelligence.md)

[Confidence scores](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/../concept/docintel-confidence-scores.md)

[Data normalization](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/../concept/data-normalization.md)

[Document field statuses](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/docintel-field-statuses.md)

[Document Intelligence forms](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/document-intelligence-forms.md)

[Document Intelligence properties](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/document-intelligence-properties.md)

[Document Intelligence roles](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/document-intelligence-user-roles.md#)

[Document Intelligence terminology](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/../concept/docintel-terminology.md#)

[Document task statuses](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/docintel-task-statuses.md)

[Domain separation and Document Intelligence](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/domain-separation-and-doc-intel.md)

[Languages supported by Document Intelligence](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/../concept/languages-supported-by-document-intelligence.md)

[Limitations in Document Intelligence](https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/intelligent-experiences/document-intelligence/hard-limits-in-doc-intel.md)

