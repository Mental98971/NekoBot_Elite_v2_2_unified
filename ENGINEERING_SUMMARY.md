# Engineering Summary — NekoBot Elite v2.2 (unified)

Single source tree built from every uploaded revision (Production → consolidated → merged →
Elite v2 → Elite v2.1) plus the personality dataset bundles. Base: Elite v2.1 (newest feature set).
Every regression found against earlier builds was ported back.

## Regressions in Elite v2.1 that this build fixes
| Area | Problem in v2.1 | Fix |
|------|-----------------|-----|
| Personality data | `data/personality/dataset/` (few-shot bank, category index, full corpus) and 45 of 109 presets were missing; v2.1's own test suite would fail | Restored; all 109 presets + dataset present |
| Group chats | `_message_addresses_bot` was a sync helper wrapped in the async `safe_handler` → returned a truthy coroutine → bot answered *every* group message | Replaced with the tested mention/reply detector (entity-based) |
| Force-sub | Defaulted **on** for a placeholder channel → silently blocked all non-admin users | Off by default; enabled only when a channel is configured |
| Paths | Several modules used cwd-relative `data/...` paths | All resolve via absolute `settings.data_dir` |
| `/tts` | Stub message ("not available") | Real TTS via `edge-tts` (added to requirements) |
| `/music` `/yt` `/insta` | No size guard, temp files leaked on error, raw errors shown | 50 MB guard, `finally` cleanup, sanitised user-facing errors |
| Startup | Lost the privacy-mode / force-sub misconfiguration diagnostics | Restored |
| Handler groups | Personality listener had no explicit group | `group=8` (no collisions) |
| Logging | Dead `configure_secret_redaction()` stub | Removed |

## New fixes in this revision
- **/menu**: "🎧 Live Music" opened the *file-download* panel (both buttons resolved to key `music`);
  the live-music panel was unreachable. Explicit key override + regression test.
- **/menu**: added ⏰ Schedule panel (`/remind /reminders /schedule /announce /poll`), `/report`, `/guess`;
  removed an advertised command that does not exist (`/bet`).
- **/couples**: daily pair used builtin `hash()` (randomised per process) → changed on every restart;
  now SHA-256 seeded. Removed a per-call HEAD probe of an unrelated external image; art is opt-in via
  `COUPLE_ART_URL`, otherwise text-only.
- `.env.example` now documents every config alias (added `OMDB_API_KEY`, `COUPLE_ART_URL`, personality limits).

## Kept from v2.1 (superior to earlier builds)
`/cosplay` + `/cp` (captionless, multi-source), AFK duration formatting, Couple of The Day UI,
IMDb→Wikipedia fallback, gender-neutral identity rules, 3-page /menu with 46 panels, dashboard,
docker-compose, CI workflows, personality archives (master v1–v5, waves 1–41, expansions, packs).

## Tests
`tests/` = v2.1 suite + config, fun, music-download, utilities, e2e personality-reply tests from the
merged branch, and a rewritten hardening/menu contract suite.
`python -m unittest tests.test_hardening_contracts` runs with no dependencies.
Everything else needs `pip install -r requirements-dev.txt`.

## Deploy
```bash
cp .env.example .env   # set BOT_TOKEN, OWNER_ID (+ optional API keys)
docker compose up -d   # or: pip install -r requirements.txt && python -m bot
```
BotFather → Group Privacy must be **off** (or the bot a group admin) for ambient group features.
