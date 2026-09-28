# Feature matrix — Neko

Status reflects this codebase as shipped, not a generic bot template.
See `docs/FEATURE_INVENTORY.md` for the full round-by-round history.

| Area | Commands / entry | Flag / deps | Status |
|------|------------------|-------------|--------|
| Start / help / menu | `/start` `/help` `/menu` `/settings` | — | Works — menu buttons map to real command groups |
| AI assistant | `/ai` `/imagine` `/summarize` `/code` `/see` `/transcribe` `/persona` `/aiclear` | provider API key(s) | Works; soft in-character decline if no provider configured |
| AI diagnostics | `/aihealth` | owner only | Works — shows configured providers, no secrets |
| Personality | `/chat`, @mention/reply, `/personality on|off`, `/joke` | `enable_personality` | Works — 109 skins, 109 trait presets |
| Persona admin | `/plist` `/pshow` `/preload` `/padd` `/pdel` `/pmerge` `/pset` `/pdata` `/pmeta` `/pjson` `/padmin` | owner only (superowner) | Works |
| Reactions | `/reactions on|off`, `/hug` `/pat` `/slap` + 22 more | `enable_reactions` | Works — target-mention captions |
| Anime | `/anime` `/manga` `/character` `/seasonal` | — | Works — AniList primary, MyAnimeList/Jikan fallback, 15-min cache |
| Music (file) | `/music` `/tts` | — | `/music` works; `/tts` is text-only (no audio TTS dependency bundled) |
| Live voice-chat music | `/play` `/skip` `/pause` `/resume` `/stop` `/queue` `/nowplaying` `/volume` `/shuffle` `/repeat` `/effects` `/loop` `/seek` `/seekback` `/playlist` `/lyrics` `/channelplay` `/videomode` `/toptracks` `/resetqueue` | `enable_live_music` + Telegram API id/hash + ffmpeg | Works when configured |
| Music diagnostics | `/musichealth` | owner only | Works |
| Fonts | `/f1`–`/f18` `/flip` `/fontfx` `/random` `/mix` `/reverse` `/fonts` | `enable_fonts` | Works |
| Collector | `/grab` `/collection` `/characters` `/listcharacters` `/fav` `/trade` `/gift` `/smelt` `/cstats` `/cprivacy` `/crandom` `/giveaway` `/owners` `/chelp` | `enable_collector` | Works — weighted rarity spawns, stable `file_id` storage |
| Economy | `/daily` `/balance` `/shop` `/level` `/leaderboard` `/pay` | `enable_economy` | Works — atomic balance updates, race-condition tested |
| Games | `/trivia` `/tictactoe` `/poll` | `enable_games` | Works |
| Moderation | `/ban` `/mute` `/kick` `/warn` `/purge` `/tmute` `/tban` | — | Works |
| Security | `/antispam` `/antiflood` `/captcha` `/locks` `/nightmode` | — | Works — admin-status cached (45s TTL) |
| Chat management | `/notes` `/filters` `/welcome` `/rules` `/setwelcome` `/setrules` | — | Works |
| Name history | `/names` | — | Works — throttled ambient tracking |
| Federations | `/newfed` `/joinfed` `/leavefed` `/fedban` `/unfedban` `/fedinfo` `/fpromote` `/fedadmins` | `enable_federation` | Works |
| Admin ops | `/disable` `/enable` `/disabled` `/zombies` `/rmzombies` `/unbanall` | — | Works |
| Owner / sudo ops | `/globalstats` `/activevc` `/blacklistchat` `/authorize` `/maintenance` `/privatemode` `/cleanmode` `/autoend` `/speedtest` `/gban` `/block` | owner/sudo | Works |
| Scheduling / automod | various | flags | Works |
| Force-subscribe | middleware, no command | `FORCE_SUB_ENABLED` (off by default) | Works — off unless an operator opts in with their own channel |
| Dashboard | separate service | — | Read-only heartbeat |

**Not implemented** (do not advertise): Cricket, Cosplay, Pokedex, OCR, Upscale, Telegraph, Imposter, Logo designer, Sports live, AntiBanAll, real audio TTS.

**Deliberately deferred** (see `learnings-and-workflow` notes): `connection.py` (manage a group from DM), `approve.py` (lock/antiflood exemptions), full `datetime.utcnow()` → timezone-aware migration, wider `bot/utils/validation.py` rollout.
