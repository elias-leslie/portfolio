# Elias Leslie — AI, Security Automation, and Infrastructure Tooling

I build practical automation systems at the intersection of **AI automation, security automation, cyber security, agentic developer tooling, and full-stack infrastructure**. My work emphasizes local-first control planes, secure defaults, reproducible release paths, and operator-focused interfaces that turn complex workflows into auditable tools.

I use agentic AI heavily, but I keep the engineering bar concrete: documented setup, real tests, runtime smoke checks, secret hygiene, and honest limitations.

## Featured public release: Aico

**Aico** is a Linux desktop companion for terminal AI agents: floating widgets, isolated tmux sessions, a local FastAPI sidecar, click-to-context capture, and optional browser/voice integrations.

[Repository](https://github.com/elias-leslie/aico) · [Install docs](https://github.com/elias-leslie/aico/blob/main/docs/INSTALL.md) · [Security policy](https://github.com/elias-leslie/aico/blob/main/SECURITY.md)

![Aico public release smoke test visual](./images/aico-release-smoke.svg)

**Case study**

- **Problem:** Terminal AI agents are useful but fragmented across shells, browser context, desktop selection, and project state. A public release also needed clean install docs and proof that no private/internal material was exposed.
- **Solution:** Aico wraps agent terminals in a desktop companion with a local-only sidecar API, source installer, optional integrations, and hardened public docs/config.
- **Stack:** Electron, TypeScript, Vite, FastAPI, Python 3.13, tmux, uv, Node.js, browser extension APIs.
- **What was built:** Floating desktop widgets, tmux-backed terminal sessions, FastAPI health/selection/widget APIs, optional speech-to-text websocket client, Chrome/Chromium extension, clean source installer, CI, Apache-2.0 release docs.
- **Skills demonstrated:** Desktop integration, secure local service design, TypeScript/Python testing, Linux packaging realities, secret/history scanning, clean-room install verification.
- **Security/automation/AI relevance:** Keeps sensitive workflow state local by default, uses loopback APIs, degrades when optional integrations are absent, and makes terminal agents faster to operate without handing them unnecessary access.
- **Current status and limitations:** Public source release for single-user Linux desktops. Wayland/global shortcut support can be limited by desktop environment. Agent CLIs, browser extension, and voice backend are optional and user-provided.

## Public project showcase

### Aico — desktop companion for terminal AI agents

- **Repo:** <https://github.com/elias-leslie/aico>
- **Built:** Electron desktop app, Python sidecar, tmux session orchestration, browser extension, source install path, CI, release hardening.
- **Why it matters:** Demonstrates agentic tooling that is useful without relying on private infrastructure or cloud-only assumptions.

### A-Term — browser workspace for AI coding agents

- **Repo:** <https://github.com/elias-leslie/a-term>
- **Problem:** Agentic coding often needs shells, files, notes, and workspace state in one browser-accessible environment.
- **Solution:** A browser workspace for AI coding agents, shells, files, and notes.
- **Stack/skills:** Python, web UI, terminal/session management, workspace orchestration, developer-experience tooling.
- **Status:** Public project; capabilities depend on the local environment and installed agent CLIs.

### Security Hardening Automation (SHA)

- **Repo:** <https://github.com/elias-leslie/sha>
- **Problem:** Endpoint hardening needs repeatable checks, staged rollout, operator visibility, and rollback paths.
- **Solution:** Security hardening automation platform for Windows and Linux endpoints with a FastAPI control plane and Next.js operator dashboard.
- **Stack/skills:** FastAPI, Next.js, endpoint security automation, policy/check orchestration, dashboard UX, evidence-oriented workflows.
- **Security relevance:** Turns hardening into auditable automation instead of one-off scripts.
- **Status:** Public project; production use requires environment-specific validation.

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
- **Security/data note:** Portfolio materials use only public repo claims and do not show real balances, holdings, transactions, account IDs, or brokerage data.
- **Status:** Public project; users must configure their own data sources and secrets.

## Capability areas

- **AI automation and agentic tooling:** local-first agent workflows, prompt/session infrastructure, terminal/browser context capture, multi-provider control planes.
- **Security automation:** endpoint hardening, incident containment concepts, detection workflows, evidence exports, rollout/rollback discipline.
- **Cyber security engineering:** secure defaults, secret scanning, local API boundaries, install-time dependency verification, public release hygiene.
- **Developer tooling:** tmux/session orchestration, desktop/browser integrations, clean installers, CI, test suites, smoke tests.
- **Full-stack infrastructure:** FastAPI, Next.js/Electron, PostgreSQL/Redis-style backends, operator dashboards, Linux service/runtime integration.

## Downloads

- [Detailed portfolio PDF](./Detailed_Portfolio.pdf)
- [Security automation summary PDF](./Elias_Leslie_Portfolio_Summary_Security_Automation.pdf)
- [Detailed PDF Markdown source](./Detailed_Portfolio.md)
- [Summary PDF Markdown source](./Elias_Leslie_Portfolio_Summary_Security_Automation.md)

## Contact

- LinkedIn: <https://linkedin.com/in/elias-leslie>
- GitHub: <https://github.com/elias-leslie>

_Last updated: 2026-06-07_
