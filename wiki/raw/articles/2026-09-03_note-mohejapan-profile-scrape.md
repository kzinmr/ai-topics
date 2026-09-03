---
title: "Note profile scrape: もへじのお部屋 (mohejapan)"
source_url: https://note.com/mohejapan
scraped: 2026-09-03
scrape_method: r.jina.ai
note: |
  Verification scrape performed during skeleton-enrich-daily run.
  Identity resolution FAILED: see verification section below.
---

# Note profile: もへじのお部屋 (@mohejapan)

## Profile page content (scraped 2026-09-03 via r.jina.ai)

- Display name: **もへじのお部屋** ("Moheji's Room")
- Fixed/pinned article: 「もへじのプロフィール」 (Moheji's Profile), published ~4 years ago (i.e., ~2022)
- Recent visible article series: **楽々古事記** ("Easy Kojiki") — ongoing numbered series on the Japanese mythological classic *Kojiki*; recent entries:
  - 楽々古事記【48】宇陀の兄弟
  - 楽々古事記【47】ヤタガラス（八咫烏）
  - 楽々古事記【46】霊剣あらたか
  - 楽々古事記【45】イツセ 散る
  - 楽々古事記【44】トミビコとの戦い
  - 楽々古事記【43】神武東征

Notably, the visible recent content is mythology commentary, **not** LLM/generative-AI technical content.

## Verification attempt for index claim "Takumi Handa's Japanese LLM publishing hub"

The index.md one-liner (added 2026-08-31 trending-topics, then lost) claims:
"Takumi Handa's Japanese LLM/generative-AI publishing hub: 52k+ X followers, 5,600+ note writers, 1,000+ articles, weekly AI news series 300+ issues."

Checks performed 2026-09-03:

1. `note.com/mohejapan` — profile name is "もへじのお部屋"; no AI-hub branding visible; recent posts are Kojiki mythology series. Cannot confirm AI-hub identity from the profile page alone.
2. `@handaline` on X — **does not exist** (X API v2 `users/by/username/handaline`: Not Found).
3. `@moheji1` on X — exists but the account name is 茂木秀樹 (Hideki Motegi), not Takumi Handa / Moheji-the-AI-writer.
4. DuckDuckGo/Bing searches for もへじ + LLM / ハンダリン / Takumi Handa: no result directly connecting "もへじ" + "半田匠" + an AI publishing hub.
5. No raw article, newsletter, RSS scan (`inbox/rss-scans/trending-topics-2026-08-31.md`), or X bookmark in the repo mentions Mo Hit Main / もへじ / Handa / moheji in an AI context. The trending-topics 2026-08-31 log entry adds `index.md: entities/mo-hit-main` but the underlying report contains no matching mention.

## Conclusion

The claim cannot be verified from primary sources. The most likely provenance is an **LLM hallucination in the trending-topics 2026-08-31 run** (index entry added without a supporting source mention in the report). Page marked `status: needs-identification`, `confidence: low`.
