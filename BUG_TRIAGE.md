# Bug Triage — Initial Pass

## Rule
No fixes before classification.

---

### 1. Task Status Reverts to "In Progress"
- Type: State Machine / Business Logic
- Surface: Backend
- Severity: High
- Why: Invalid state transitions allowed

---

### 2. Admin Cannot Start or Complete Task
- Type: Authorization / RBAC
- Surface: Backend API
- Severity: Critical
- Why: Role check blocks admin incorrectly

---

### 3. Admin Cannot Change Assignee
- Type: Authorization + Validation
- Surface: Backend API
- Severity: High
- Why: Update path missing permission or constraint

---

### 4. Appraisals Not Visible to Employee
- Type: Data Fetch / Query Filter
- Surface: Backend
- Severity: High
- Why: Workspace/user filter mismatch

---

### 5. Performance Dashboard Not Updating
- Type: Aggregation / Caching
- Surface: Backend + UI
- Severity: Medium
- Why: Derived data not recalculated

---

### 6. Project Live Dashboard Mapping Wrong
- Type: Join Logic / Data Model
- Surface: Backend
- Severity: High
- Why: Incorrect task ↔ employee mapping

---

### 7. Edit Project Returns 404
- Type: Routing
- Surface: Backend or Frontend Router
- Severity: Critical
- Why: Route exists in UI but not backend

---

### 8. Log Time Entry Fails
- Type: Validation / Transaction
- Surface: Backend
- Severity: High
- Why: Required fields or FK missing

---

### 9. Mark As Read Not Working
- Type: UI Event → API mismatch
- Surface: Frontend + Backend
- Severity: Medium
- Why: Click fires but backend not called or ignored

---

### 10. Employee Sees All Tasks Instead of Assigned
- Type: Authorization / Query Filter
- Surface: Backend
- Severity: Critical
- Why: Missing userId filter

---

### 11. Assignee Dropdown Missing Employees
- Type: Data Fetch / UI
- Surface: Backend or Frontend
- Severity: Medium
- Why: Pagination or role filter wrong

---

### 12. Announcements Dropdown Broken
- Type: UI Logic + Role Constraint
- Surface: Frontend
- Severity: Medium
- Why: UI shows admin-only feature to employee

---

### 13. Dashboard UI Size Inconsistent
- Type: UI Layout
- Surface: Frontend
- Severity: Low
- Why: CSS grid misuse
