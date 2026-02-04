from __future__ import annotations

from dataclasses import dataclass

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@dataclass(frozen=True)
class RoadmapPhase:
    title: str
    detail: str


FEATURES = [
    "Chat with your repository context",
    "Inline code suggestions and refactors",
    "Safe tool execution with reviewable diffs",
]

ROADMAP = [
    RoadmapPhase("Week 1-2", "Repository indexing + RAG chat endpoint"),
    RoadmapPhase("Week 3-4", "Editor UI with streaming responses"),
    RoadmapPhase("Week 5-6", "Inline suggestions + patch apply"),
    RoadmapPhase("Week 7-8", "Tool execution (search/test/format)"),
]


@app.get("/")
def index() -> str:
    return render_template("index.html", features=FEATURES, roadmap=ROADMAP)


@app.get("/api/health")
def health() -> tuple[dict[str, str], int]:
    return {"status": "ok"}, 200


@app.post("/api/plan")
def plan() -> tuple[dict[str, list[dict[str, str]]], int]:
    payload = request.get_json(silent=True) or {}
    goal = str(payload.get("goal", "")).strip()
    if not goal:
        return {"steps": []}, 200

    steps = [
        {
            "title": "Clarify the MVP",
            "detail": f"Define the smallest slice of '{goal}' you can ship in 2 weeks.",
        },
        {
            "title": "Pick a model strategy",
            "detail": "Start API-first for speed, then plan for a hybrid or self-hosted path.",
        },
        {
            "title": "Ship the UI",
            "detail": "Build a minimal chat + apply flow in the editor and iterate with users.",
        },
    ]
    return {"steps": steps}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
