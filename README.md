# Makenix

Makenix is a developer-focused AI coding assistant (Cursor-like) that combines an editor UX with code intelligence, retrieval, and tool execution. This document outlines the product blueprint and build plan.

## Vision
Build a fast, reliable AI coding assistant that:
- Understands the full repository context.
- Suggests high-quality inline edits and refactors.
- Chats about code, errors, and design.
- Executes safe, auditable actions (search, edit, test, format).

## Product Scope (MVP)
Start with a narrow set of features to ship quickly:
1. **Chat with your repo** (RAG over codebase).
2. **Inline code suggestions** (single-file context).
3. **Quick apply** patching UI with undo.

## Architecture Overview
### 1) Editor / Frontend
- VS Code extension or Electron app (Monaco).
- Chat panel + inline ghost text.
- Streaming responses and “apply” diff UI.

### 2) Backend Orchestration
- API layer for authentication, rate limiting, usage metering.
- Prompt assembly with context retrieval.
- Tool executor for safe actions.

### 3) Retrieval (RAG)
- Index repository content into embeddings.
- Retrieve top-K relevant files and chunks.
- Send snippets + file paths as context.

### 4) Code Intelligence
- Tree-sitter or LSP for symbols, references.
- Incremental indexing as files change.
- Language-aware chunking for RAG.

## Model Strategy
Choose a model approach based on cost and control:
- **API-first** (fastest to ship): OpenAI / Anthropic / Mistral.
- **Self-host** (control + privacy): Llama / Qwen / Mixtral.
- **Hybrid**: local autocomplete + API for complex tasks.

## Core Workflow
1. User asks question or requests change.
2. Retrieve relevant files/snippets.
3. Generate response with citations or patches.
4. Apply patch to working tree (with review).
5. Optionally run tests/formatters.

## Suggested Tech Stack
- **Frontend**: VS Code extension, React.
- **Backend**: FastAPI / Node / Go.
- **Vector DB**: Qdrant / FAISS.
- **Observability**: OpenTelemetry + metrics.
- **Billing/Auth**: Stripe + Clerk/Auth0.

## Milestones
1. **Week 1–2**: Repo indexing + RAG chat endpoint.
2. **Week 3–4**: VS Code extension UI + streaming chat.
3. **Week 5–6**: Inline suggestions + patch apply.
4. **Week 7–8**: Tool execution (search/test/format).

## Quality & Safety
- Show diffs before applying edits.
- Keep an audit log of actions and tool calls.
- Respect secrets: never index `.env` or credentials.
- Add rate limits and prompt injection defenses.

## Next Steps
- Decide MVP target (chat, inline, or refactor).
- Pick model strategy (API-first recommended).
- Implement repository indexing and retrieval.
- Build a minimal editor UI for chat and apply.

---
If you want, specify the exact MVP feature and preferred stack, and this plan can be converted into a detailed implementation checklist.

## Quickstart (Demo App)
This repo now includes a minimal Flask-based demo for Makenix.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/main.py
```

Then open `http://localhost:8000` in your browser.
