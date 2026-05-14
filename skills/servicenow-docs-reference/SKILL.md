# ServiceNow Docs Reference — Multi-Version Knowledge Base

**Doel:** Raadplegen van versiegestuurd ServiceNow documentatie via GitHub repo

**Bron:** https://github.com/pelwees/ServiceNowDocs (fork van officiële ServiceNow docs)

---

## Branches (ServiceNow versies)

| Branch | Status | Default |
|---|---|---|
| `australia` | Nieuwste / current | ✓ |
| `xanadu` | Ouder | — |
| `yokohama` | Oudste  | — |
| `zurich` | Vorige versie  | — |

**Default branch:** `australia` — tenzij je een andere versie specificeert.

---

## Structuur

Elke branch volgt dezelfde opbouw:
```
/
├── README.md                  (inhoudsopgave met absolute raw-URLs naar alle publicaties)
├── markdown/
│   ├── integration-hub/
│   │   ├── index.md
│   │   └── ...
│   ├── api-reference/         (⚠️ zeer groot, ~100K+ lines)
│   │   ├── index.md
│   │   └── ...
│   └── <publicatie-folder>/
│       ├── index.md
│       └── ...
```

---

## Raadplegen

**Workflow:**

1. **Root README** ophalen voor inhoudsopgave (bevat absolute raw-URLs):
   ```
   https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/README.md
   ```

2. **URL voor gewenste publicatie** staat letterlijk in de README — direct ophalen:
   ```
   https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/index.md
   ```

3. **Specifiek sub-document** via link in de index:
   ```
   https://raw.githubusercontent.com/pelwees/ServiceNowDocs/australia/markdown/integrate-applications/integrationhub.md
   ```

**Versie-wisselen:** Vervang `australia` in URL door `xanadu` / `yokohama` / `zurich`.

> **Belangrijk:** Construeer URLs nooit zelf op basis van aannames. Haal altijd eerst de README op en gebruik de URLs die daar letterlijk in staan. Geconstrueerde URLs worden geblokkeerd door het fetch-mechanisme.

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
- README bevat absolute raw-URLs — geen URL-constructie nodig
- Wijzigingen push je naar GitHub, automatisch beschikbaar
- API Reference groeit voortdurend → altijd versie-aware
