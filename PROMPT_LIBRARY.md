# Prompt Library

This file contains reusable prompts for working on this training project (Git, Jenkins CI/CD, Docker, FastAPI+HTMX). Prompts are written to:

- Assume commands are executed manually in a Linux VM
- Prefer production-grade practices and explicit risk callouts
- Produce actionable steps (not blind automation)

---

## Git

### When to use
- You need to understand repository state, history shape, or why a merge/rebase went wrong.

### Prompt
```
You are a senior DevOps engineer.

Goal: Help me diagnose and fix a Git issue safely.

Repo context:
- Branching model: <describe briefly>
- Remote: <origin URL or name>
- I can run commands manually in Linux.

Problem:
<describe symptom, e.g. "merge conflict in X", "detached HEAD", "rebase went bad">

Outputs I can provide:
- git status
- git log --oneline --decorate -n 20
- git reflog -n 30
- git diff

Requirements:
- Provide a minimal set of commands, in order, with explanation of why each is safe.
- Call out data-loss risks (reset --hard, force-push, reflog expiry).
- If multiple strategies exist, compare them.
```

### Expected output
- A step-by-step diagnostic flow.
- A recommended fix path and a rollback path.
- A short explanation of what likely happened internally (HEAD, index, working tree, commit graph).

---

### When to use
- You need to inspect Git internals (objects, refs, packfiles) to understand "what Git really stores".

### Prompt
```
Teach me Git internals for this scenario.

Scenario:
<e.g. "I committed a file, then amended, then rebased">

I want:
- Which objects are created/updated (blob/tree/commit/tag)
- Which refs move (HEAD, branch refs)
- What the index represents at each step

Give:
- Concrete commands I can run: git cat-file -p, git show, git ls-tree, git rev-parse, git show-ref
- What I should expect to see (example snippets are OK)
- Common mistakes and how to recover using reflog
```

### Expected output
- A precise mapping from user actions to Git data structures.
- A short list of commands and what their output means.

---

## Jenkins CI/CD

### When to use
- You’re designing or reviewing a `Jenkinsfile` pipeline for Docker builds + tests + deploy.

### Prompt
```
Act as a senior CI/CD engineer.

Project constraints:
- App: FastAPI backend + HTMX frontend
- Packaging: Docker
- Deployment: single-tenant, privacy-first
- I run Jenkins agents on <docker|vm|k8s>. Provide steps accordingly.

Task:
<e.g. "design a pipeline", "review my Jenkinsfile", "make builds reproducible">

Requirements:
- Prefer declarative pipeline unless there is a strong reason not to.
- Include stages for: lint/test, build image, security scan (as feasible), push to registry, deploy.
- Use deterministic tagging (git SHA) and avoid mutable latest for deployments.
- Explain credentials handling (Jenkins credentials store), secret masking, and least privilege.
- Call out what should be parameterized (env, image tag, registry).

If you need details, ask targeted questions.
```

### Expected output
- A pipeline outline (stages + rationale).
- A list of required Jenkins credentials and permissions.
- Risks/gaps (e.g., no artifact retention, non-reproducible builds, lack of rollback).

---

### When to use
- A Jenkins build fails and you need fast root-cause analysis.

### Prompt
```
Help me debug a Jenkins failure.

Provide a diagnosis plan:
- What to check first, and why (pipeline logs, agent environment, workspace state)
- How to reproduce locally in Linux (same Docker image / same commands)

Artifacts I can paste:
- failing stage log excerpt
- Jenkinsfile snippet (relevant stages)
- docker build output

Constraints:
- Do not assume plugin availability.
- Prefer fixes that reduce flakiness and improve determinism.
```

### Expected output
- A short hypothesis list ranked by likelihood.
- Minimal reproduction steps.
- Concrete changes to Jenkinsfile / Dockerfile / tests, with rationale.

---

## Docker

### When to use
- You need a production-grade `Dockerfile` and `docker-compose.yml` for a FastAPI app.

### Prompt
```
Act as a production-focused container engineer.

App:
- FastAPI backend
- HTMX server-rendered frontend (templates/static)

Target:
- Single-tenant deployment
- Privacy-first: minimize data egress, secure defaults

Task:
<e.g. "review Dockerfile", "optimize image", "create compose with db">

Requirements:
- Use non-root user where possible.
- Use multi-stage builds if it reduces size and keeps build tools out of runtime.
- Pin base images and major dependencies where feasible.
- Healthcheck guidance and graceful shutdown.
- Explain volume strategy (what must persist vs what must not).
- Provide docker commands I can run manually to validate.
```

### Expected output
- A recommended container structure with rationale.
- A checklist to validate: image size, CVE posture, runtime user, ports, env vars.

---

### When to use
- You suspect networking/env/volume issues in compose deployments.

### Prompt
```
Help me debug a Docker Compose deployment.

Symptoms:
<e.g. "502", "container restarting", "can’t reach db", "migrations fail">

I can provide:
- docker compose ps
- docker compose logs <service>
- docker inspect <container>
- compose YAML snippet

Constraints:
- Provide commands I can run manually on Linux.
- Explain what each command proves/disproves.
```

### Expected output
- A focused investigation path (network, DNS, ports, env, volumes, resource limits).
- Specific fixes and what to change in compose.

---

## FastAPI + HTMX

### When to use
- You’re deciding how to structure the app (routers, templates, services, DB access) with server-rendered HTMX.

### Prompt
```
Act as a senior backend engineer.

Goal:
Design/review FastAPI architecture for an HTMX-driven server-rendered app.

Constraints:
- HTMX (progressive enhancement)
- Single-tenant
- Privacy-first
- Docker deployment

I want:
- Suggested module layout (routers, templates, services, db, config)
- Request/response flow with HTMX partials
- Error handling strategy (user-safe messages vs internal logs)
- Security defaults (CSRF considerations with HTMX, auth/session approach, headers)

If DB is relevant, ask which DB and migration tooling.
```

### Expected output
- A concrete, maintainable layout and why it reduces coupling.
- Key middleware/dependencies and what risks they mitigate.

---

### When to use
- You need to debug FastAPI behavior in production-like conditions (timeouts, startup failures, background tasks).

### Prompt
```
Help me debug a FastAPI issue.

Symptoms:
<e.g. "startup crash", "500 on /route", "template not found", "slow response">

Runtime:
- uvicorn/gunicorn: <which>
- Docker: <yes/no>

I can provide:
- stack trace
- relevant route + dependency code
- Dockerfile/compose snippets

Requirements:
- Provide a minimal reproduction path.
- Suggest logging/observability improvements (structured logs, request IDs) without adding heavy tooling unless justified.
- Explain likely root causes and how to confirm.
```

### Expected output
- Ranked hypotheses + verification steps.
- Targeted code/config changes.

---

## Debugging (General)

### When to use
- You want a disciplined debugging approach across Git/Jenkins/Docker/app.

### Prompt
```
Be my debugging copilot.

System:
- FastAPI app in Docker
- Built/deployed via Jenkins

Problem:
<describe>

Constraints:
- I will run commands manually on Linux.
- Suggest the smallest set of steps that maximizes information gain.
- Separate "observe" steps from "change" steps.
- Include rollback guidance for any destructive action.

Ask for missing info if required.
```

### Expected output
- A short, ordered plan:
  1) Observations to collect (commands/logs)
  2) Hypotheses
  3) Small experiments
  4) Fix + prevention

---

## Notes on privacy-first / single-tenant assumptions

### When to use
- You’re validating whether a proposed change violates privacy-first constraints.

### Prompt
```
Review this design change for privacy-first, single-tenant constraints.

Change:
<describe>

Answer:
- What data leaves the box (telemetry, Sentry, metrics, third-party APIs)
- What logs may contain PII and how to scrub/minimize
- Secrets handling (env vars, files, Jenkins credentials)
- Default network exposure (ports, admin endpoints)
- Residual risk and mitigations
```

### Expected output
- A concise risk assessment with concrete mitigations.







## What TinyAnalytics taught me as an engineer

1. Architecture comes before code; without it, scaling is guesswork.
2. Docker is not magic—it is disciplined packaging of runtime, dependencies, and ports.
3. Running services in the background (detached containers) is normal in real systems.
4. CI/CD exists to reduce human error, not to show tool knowledge.
5. Rate limiting protects infrastructure, not just endpoints.
6. Background jobs exist to keep databases healthy over time.
7. Public links must be read-only, revocable, and unguessable.
8. Security is about defaults: deny first, then allow.
9. Hotfixes must be small, fast, and well-documented.
10. AI accelerates scaffolding, but human judgment ensures correctness.
11. Reading and tracing code is more important than writing new code.






