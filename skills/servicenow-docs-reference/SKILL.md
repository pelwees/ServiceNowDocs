# ServiceNow Docs Reference — Multi-Version Knowledge Base

**Doel:** Raadplegen van versiegestuurd ServiceNow documentatie via GitHub repo

**Bron:** https://github.com/pelwees/ServiceNowDocs (fork van officiële ServiceNow docs)

---

## Branches (ServiceNow versies)

| Branch | Status | Default |
|---|---|---|
| `australia` | Nieuwste / current | ✓ |
| `xanadu` | Vorige versie | — |
| `yokohama` | Ouder | — |
| `zurich` | Oudste | — |

**Default branch:** `australia` — tenzij je een andere versie specificeert.

---

## Structuur

Elke branch volgt dezelfde opbouw:
/
├── README.md (root inhoudsopgave, links naar sub-folders)
├── integration-hub/
│   ├── index.md (overzicht + links naar sub-topics)
│   ├── fundamentals.md
│   ├── flows.md
│   └── ...
├── scripting/
│   ├── index.md
│   ├── script-includes.md
│   ├── business-rules.md
│   └── ...
├── api-reference/ (⚠️ zeer groot, ~100K+ lines)
│   ├── index.md
│   ├── rest-api.md
│   ├── glide-api.md
│   └── ... (veel sub-docs)
└── ...

---

## Raadplegen

**Workflow:**

1. **Root README** voor inhoudsopgave:
https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/README.md

2. **Sub-folder index** voor topic-overzicht:
https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/integration-hub/index.md

3. **Specifiek document:**
https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/integration-hub/flows.md

**Versie-wisselen:** Vervang `australia` in URL door `xanadu` / `yokohama` / `zurich`.

---

## API Reference — Speciale handeling

**Waarschuwing:** API Reference is zeer groot (~100K+ regels). Niet altijd compleet laden.

**Strategie:**
- Default: raadpleeg sub-topics (REST API, GlideAPI, etc.)
- Bij code-schrijven: **ik stel proactief voor** om API Reference op te halen als nodig
  - "Wil je dat ik de exacte methode-signatuur uit API Reference haal voor [onderdeel]?"
  - "Dit zou beter met API Reference kunnen — zal ik [specifieke pagina] ophalen?"
- Jij zegt: "Ja, haal [onderdeel] op" → ik fetch die specifieke doc/sectie

**Wanneer nuttig:**
- Exacte GlideAPI method signatures
- REST API endpoint specs
- Parameter types / return formats
- Error codes

---

## Gebruik in projecten

Wanneer gelinkt in Claude project:

1. **Bij vragen over ServiceNow concepts:** ik raadpleeg relevante docs
2. **Bij code-schrijven:** ik stel proactief voor om API Reference te laden
3. **Versie-specifiek:** je zegt "Gebruik Xanadu", ik switch branch
4. **Bij twijfel:** ik vraag eerst — "Wil je Australia of andere versie?"

---

## Notes

- Alle docs zijn Markdown, web_fetch-friendly
- Geen auth nodig (public repo)
- Wijzigingen push je naar GitHub, automatisch beschikbaar
- API Reference is voortdurend groeien/wijzigen → altijd versie-aware
