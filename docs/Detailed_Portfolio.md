# Elias Leslie — Detailed Portfolio

Last updated: 2026-06-07

## Summary

Elias Leslie builds practical automation systems across AI automation, security automation, cyber security, agentic developer tooling, and full-stack infrastructure. The common thread is operator-grade software: documented setup, secure defaults, tests, runtime smoke checks, and honest limitations.

## Featured project: Aico

Aico is a Linux desktop companion for terminal AI agents. It provides floating widgets, isolated tmux sessions, a local FastAPI sidecar, click-to-context capture, and optional browser/voice integrations.

Repository: https://github.com/elias-leslie/aico

Problem: Terminal AI agents are useful but fragmented across shells, browser context, desktop selection, and project state. Public release also required installable docs and proof that private/internal material was not exposed.

Solution: Aico wraps agent terminals in a desktop companion with a local-only sidecar API, source installer, optional integrations, and hardened public docs/config.

Stack: Electron, TypeScript, Vite, FastAPI, Python 3.13, tmux, uv, Node.js, browser extension APIs.

Built: Floating desktop widgets, tmux-backed terminal sessions, FastAPI health/selection/widget APIs, optional speech-to-text websocket client, Chrome/Chromium extension, clean source installer, CI, Apache-2.0 release docs.

Skills demonstrated: Desktop integration, secure local service design, TypeScript/Python testing, Linux packaging realities, secret/history scanning, clean-room install verification.

Security/AI relevance: Aico keeps sensitive workflow state local by default, uses loopback APIs, degrades when optional integrations are absent, and makes terminal agents faster to operate without granting unnecessary access.

Status and limitations: Public source release for single-user Linux desktops. Wayland/global shortcut support can be limited by desktop environment. Agent CLIs, browser extension, and voice backend are optional and user-provided.

## Selected public projects

A-Term: Browser workspace for AI coding agents, shells, files, and notes. Repository: https://github.com/elias-leslie/a-term

Security Hardening Automation: Security hardening automation platform for Windows and Linux endpoints with a FastAPI control plane and Next.js operator dashboard. Repository: https://github.com/elias-leslie/sha

Agent Hub: Self-hosted control plane for multi-provider AI agents, sessions, credentials, prompts, and automation telemetry. Repository: https://github.com/elias-leslie/agent-hub

Portfolio AI: Full-stack investment intelligence workspace with FastAPI, Next.js, PostgreSQL, Redis, and Hatchet workflows. Portfolio materials do not show real balances, holdings, transactions, account IDs, or brokerage data. Repository: https://github.com/elias-leslie/portfolio-ai

## Capability areas

AI automation and agentic tooling: local-first agent workflows, prompt/session infrastructure, terminal/browser context capture, multi-provider control planes.

Security automation: endpoint hardening, incident containment concepts, detection workflows, evidence exports, rollout/rollback discipline.

Cyber security engineering: secure defaults, secret scanning, local API boundaries, install-time dependency verification, public release hygiene.

Developer tooling: tmux/session orchestration, desktop/browser integrations, clean installers, CI, test suites, smoke tests.

Full-stack infrastructure: FastAPI, Next.js/Electron, PostgreSQL/Redis-style backends, operator dashboards, Linux service/runtime integration.

## Contact

LinkedIn: https://linkedin.com/in/elias-leslie
GitHub: https://github.com/elias-leslie
