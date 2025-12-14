# TinyAnalytics – Architecture

## Purpose
Privacy-first, single-tenant analytics service for page views without cookies.

## Constraints
- No user accounts
- No third-party telemetry
- Single VM deployment
- Dockerized
- Jenkins-based CI

## Tech Stack
- Backend: FastAPI
- Frontend: HTMX + templates
- DB: SQLite (initial)
- CI: Jenkins (VM agent)
- Runtime: Docker

## Non-goals
- Multi-tenancy
- SaaS billing
- External auth providers

## Data Model (Conceptual)
- PageView
  - url
  - timestamp
  - hashed_ip (for abuse control, not identity)

- Page
  - url
  - total_views

- ShareLink
  - id (UUID)
  - created_at

## Request Flow
1. A visitor opens a webpage.
2. A lightweight tracking request is sent to the backend.
3. The backend records an anonymous page view.
4. The dashboard queries stored data to display analytics.
5. Optional: a public share link allows read-only viewing.

## Failure Modes
- Backend unavailable → tracking requests dropped
- Database full or locked → page views not recorded
- Invalid tracking payload → request rejected (400)

## Security & Privacy Considerations
- No cookies or local storage
- IP addresses hashed immediately
- No authentication or user identification
- No third-party scripts or analytics

## Deployment Assumptions
- Single Linux VM
- Docker used for runtime isolation
- Jenkins triggers builds and deployments
- No horizontal scaling initially
