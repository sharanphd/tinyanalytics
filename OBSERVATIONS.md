17th and 18th Dec 2025
What broke today





What I fixed





What confused me






What I now understand better


# Engineering Observations

## 1. How I debug a failing feature
- Check UI behavior (state, buttons, disabled states)
- Check API request payload (what is sent)
- Check backend validation / permissions
- Check DB transaction (commit / rollback)
- Check logs, not assumptions

## 2. What breaks systems most often
- State transitions without guards
- Role-based permissions inconsistencies
- UI showing success when backend failed
- DB writes assumed to be idempotent but are not

## 3. Docker / Runtime lessons
- Containers must be stateless by default
- DB initialization must be idempotent
- Startup failures = production outages
- Logs are part of the product

## 4. How I will approach any new codebase
1. Find entry point
2. Trace one request end-to-end
3. Identify data writes
4. Identify failure surfaces
5. Only then suggest fixes

## 5. What I will NOT do
- Redesign before understanding
- Add features before stability
- Assume intent without reading code
