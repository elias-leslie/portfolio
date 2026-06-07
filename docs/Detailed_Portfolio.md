# Elias Leslie — Detailed Portfolio

Last updated: 2026-06-07

## Summary

Elias Leslie builds practical automation systems across AI automation, security automation, cyber security, agentic developer tooling, and full-stack infrastructure. The common thread is operator-grade software: documented setup, secure defaults, tests, runtime smoke checks, secret hygiene, clean install verification, and honest limitations.

## Featured project: Security Hardening Automation (SHA)

SHA is a clean-room security hardening automation platform for Windows and Linux endpoints. It provides a FastAPI control-plane API, a Next.js operator dashboard, deterministic installer-profile artifacts, generated API schemas, and curated public-source starter controls.

Repository: https://github.com/elias-leslie/sha

Problem: Endpoint hardening often becomes a brittle mix of one-off scripts, undocumented baseline assumptions, risky remote access, and unclear rollback paths.

Solution: SHA models hardening as a bounded control plane: enroll endpoints, collect posture, browse curated controls, generate installer profiles, and route disruptive work through approval requests/grants.

Stack: FastAPI, Python 3.13, SQLAlchemy, Pydantic, Next.js 16, React 19, TypeScript, Vitest, pnpm, uv, SQLite for local development.

Built: Backend APIs, dashboard pages for fleet/endpoints/controls/installers/approvals, deterministic Linux/Windows bootstrap artifacts, generated JSON Schemas, Apache-2.0 public release docs, CI, and a clean public control-pack path.

Skills demonstrated: Security automation design, public-source provenance cleanup, secret/history scanning, dependency vulnerability remediation, full-stack testing, browser/runtime smoke checks, and clean Proxmox install verification.

Security and AI relevance: SHA keeps endpoint work bounded to typed hardening workflows, avoids arbitrary shell access, documents approval boundaries, and provides a foundation for supervised operator automation.

Status and limitations: Early public control-plane/dashboard slice. It is not production-ready until authentication, authorization, production migrations/deployment hardening, and a completed privileged endpoint agent are added.

Visual proof: docs/images/sha-control-plane-smoke.png contains an inspected dashboard smoke-test screenshot with no personal, customer, private infrastructure, token, or financial data.

## Selected public projects

Aico: Linux desktop companion for terminal AI agents with floating widgets, isolated tmux sessions, a local FastAPI sidecar, click-to-context capture, optional browser/voice integrations, source installer, CI, and release hardening. Repository: https://github.com/elias-leslie/aico

A-Term: Browser workspace for AI coding agents, shells, files, prompts, and notes. Repository: https://github.com/elias-leslie/a-term

Agent Hub: Self-hosted control plane for multi-provider AI agents, sessions, credentials, prompts, memory, and automation telemetry. Repository: https://github.com/elias-leslie/agent-hub

Portfolio AI: Full-stack investment intelligence workspace with FastAPI, Next.js, PostgreSQL, Redis, and Hatchet workflows. Portfolio materials do not show real balances, holdings, transactions, account IDs, brokerage names tied to real data, or live portfolio values. Repository: https://github.com/elias-leslie/portfolio-ai

Portfolio: Public Markdown/PDF project showcase with safe visual proof and links to released repos. Repository: https://github.com/elias-leslie/portfolio

## Capability areas

AI automation and agentic tooling: local-first agent workflows, prompt/session infrastructure, terminal/browser context capture, multi-provider control planes.

Security automation: endpoint hardening, incident containment concepts, detection workflows, evidence exports, rollout/rollback discipline.

Cyber security engineering: secure defaults, secret scanning, local API boundaries, install-time dependency verification, public release hygiene.

Developer tooling: tmux/session orchestration, desktop/browser integrations, clean installers, CI, test suites, smoke tests.

Full-stack infrastructure: FastAPI, Next.js/Electron, PostgreSQL/Redis-style backends, operator dashboards, Linux service/runtime integration.

## Contact

LinkedIn: https://linkedin.com/in/elias-leslie
GitHub: https://github.com/elias-leslie
