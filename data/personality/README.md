# Personality Data — Complete Integration

All personality datasets from every supplied archive are present.

## Runtime loaders use
- `skins/` — active character skins (109)
- `presets/`
- `nanora_dataset.jsonl` — full Nanora conversation corpus
- `packs/personality_pack/` and `packs/all_personality_pack/` — generator + banks + personality JSONs

## Character style waves (drop-in)
- `character_styles/character_styles_wave{1..41}.zip` — full set from master_v5 (animals + historical included)

## Expansions
- `expansions/` — missing_personalities expansions from v5

## Source archives (nothing dropped)
All original archives are preserved under `archives/`:
- master_personality_datasets.zip (v1)
- master_personality_datasets_v2.zip
- master_personality_datasets_v3.zip
- master_personality_datasets_v4.zip
- master_personality_datasets_v5.zip
- all_personality_datasets.zip
- personality_pack_full.zip

Operators may extract additional waves or packs as needed; loaders already resolve against `settings.data_dir / "personality"`.
