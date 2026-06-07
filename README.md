# Elias Leslie — AI, Security Automation, and Infrastructure Tooling

I build practical automation systems at the intersection of **AI automation, security automation, cyber security, agentic developer tooling, and full-stack infrastructure**. My work emphasizes local-first control planes, secure defaults, reproducible release paths, and operator-focused interfaces that turn complex workflows into auditable tools.

I use agentic AI heavily, but I keep the engineering bar concrete: documented setup, real tests, runtime smoke checks, secret hygiene, clean install verification, and honest limitations.

![Portfolio project showcase overview](./docs/images/portfolio-showcase-overview.svg)

## Featured public release: Security Hardening Automation (SHA)

**SHA** is a clean-room security hardening automation platform for Windows and Linux endpoints. It combines a FastAPI control-plane API, a Next.js operator dashboard, deterministic installer-profile artifacts, generated API schemas, and curated public-source starter controls.

[Repository](https://github.com/elias-leslie/sha) · [README](https://github.com/elias-leslie/sha/blob/main/README.md) · [Security policy](https://github.com/elias-leslie/sha/blob/main/SECURITY.md)

![SHA security control plane dashboard smoke test](./docs/images/sha-control-plane-smoke.png)

**Case study**

- **Problem:** Endpoint hardening often becomes a brittle mix of one-off scripts, undocumented baseline assumptions, risky remote access, and unclear rollback paths.
- **Solution:** SHA models hardening as a bounded control plane: enroll endpoints, collect posture, browse curated controls, generate installer profiles, and route disruptive work through approval requests/grants.
- **Stack:** FastAPI, Python 3.13, SQLAlchemy, Pydantic, Next.js 16, React 19, TypeScript, Vitest, pnpm, uv, SQLite for local development.
- **What was built:** Backend APIs, dashboard pages for fleet/endpoints/controls/installers/approvals, deterministic Linux/Windows bootstrap artifacts, generated JSON Schemas, Apache-2.0 public release docs, CI, and a clean public control-pack path.
- **Skills demonstrated:** Security automation design, public-source provenance cleanup, secret/history scanning, dependency vulnerability remediation, full-stack testing, browser/runtime smoke checks, and clean Proxmox install verification.
- **Security/automation/AI relevance:** Keeps endpoint work bounded to typed hardening workflows, avoids arbitrary shell access, documents approval boundaries, and provides a foundation for supervised operator automation.
- **Current status and limitations:** Early public control-plane/dashboard slice. It is not production-ready until authentication, authorization, production migrations/deployment hardening, and a completed privileged endpoint agent are added.

## Public project showcase

### Aico — desktop companion for terminal AI agents

- **Repo:** <https://github.com/elias-leslie/aico>
- **Problem:** Terminal AI agents are useful but fragmented across shells, browser context, desktop selection, and project state.
- **Solution:** Linux desktop companion with floating widgets, isolated tmux sessions, a local FastAPI sidecar, click-to-context capture, and optional browser/voice integrations.
- **Stack/skills:** Electron, TypeScript, Vite, FastAPI, Python 3.13, tmux, uv, Node.js, browser extension APIs, source installer, CI, release hardening.
- **Security/AI relevance:** Keeps sensitive workflow state local by default, uses loopback APIs, and degrades when optional integrations are absent.
- **Status:** Public source release for single-user Linux desktops; Wayland/global shortcut support varies by desktop environment.

![Aico public release smoke test visual](./docs/images/aico-release-smoke.svg)

### A-Term — browser workspace for AI coding agents

- **Repo:** <https://github.com/elias-leslie/a-term>
- **Problem:** Agentic coding often needs shells, files, notes, prompts, and workspace state in one browser-accessible environment.
- **Solution:** Browser workspace for AI coding agents, shells, files, and notes.
- **Stack/skills:** Python, web UI, terminal/session management, workspace orchestration, developer-experience tooling.
- **Status:** Public project; capabilities depend on the local environment and installed agent CLIs.

### Agent Hub — self-hosted control plane for AI agents

- **Repo:** <https://github.com/elias-leslie/agent-hub>
- **Problem:** Multi-provider AI agent workflows need routing, sessions, prompts, credentials, memory, and telemetry in one governed place.
- **Solution:** Self-hosted control plane for multi-provider AI agents, sessions, credentials, prompts, and automation telemetry.
- **Stack/skills:** Full-stack infrastructure, API design, credential boundaries, prompt/memory systems, automation telemetry.
- **AI relevance:** Provides a safer foundation for agentic workloads than ad hoc local model calls.
- **Status:** Public project; deployment requires careful secret management.

### Portfolio AI — investment intelligence workspace

- **Repo:** <https://github.com/elias-leslie/portfolio-ai>
- **Problem:** Financial research workflows need repeatable ingestion, analysis, and reporting without exposing private holdings.
- **Solution:** Full-stack investment intelligence workspace with FastAPI, Next.js, PostgreSQL, Redis, and Hatchet workflows.
- **Stack/skills:** FastAPI, Next.js, PostgreSQL, Redis, workflow orchestration, data pipelines, UI reporting.
- **Security/data note:** Portfolio materials use only public repo claims and do not show real balances, holdings, transactions, account IDs, brokerage names tied to real data, or live portfolio values.
- **Status:** Public project; users must configure their own data sources and secrets.

### Portfolio repo — public proof hub

- **Repo:** <https://github.com/elias-leslie/portfolio>
- **Problem:** Public work needs a credible, hiring-focused hub that is polished without exposing proprietary/customer/private claims.
- **Solution:** Markdown-first GitHub portfolio with project case studies, safe visual proof, PDF sources/exports, and links to public repos.
- **Stack/skills:** GitHub README/Pages-style Markdown, maintainable PDF source, release screenshots/demo visuals, public-claim hygiene.
- **Status:** Public portfolio repository; updated incrementally as projects are released.

## Capability areas

- **AI automation and agentic tooling:** local-first agent workflows, prompt/session infrastructure, terminal/browser context capture, multi-provider control planes.
- **Security automation:** endpoint hardening, incident containment concepts, detection workflows, evidence exports, rollout/rollback discipline.
- **Cyber security engineering:** secure defaults, secret scanning, local API boundaries, install-time dependency verification, public release hygiene.
- **Developer tooling:** tmux/session orchestration, desktop/browser integrations, clean installers, CI, test suites, smoke tests.
- **Full-stack infrastructure:** FastAPI, Next.js/Electron, PostgreSQL/Redis-style backends, operator dashboards, Linux service/runtime integration.

## Downloads

- [Detailed portfolio PDF](./docs/Detailed_Portfolio.pdf)
- [Security automation summary PDF](./docs/Elias_Leslie_Portfolio_Summary_Security_Automation.pdf)
- [Detailed PDF Markdown source](./docs/Detailed_Portfolio.md)
- [Summary PDF Markdown source](./docs/Elias_Leslie_Portfolio_Summary_Security_Automation.md)

## Contact

- LinkedIn: <https://linkedin.com/in/elias-leslie>
- GitHub: <https://github.com/elias-leslie>

_Last updated: 2026-06-07_
