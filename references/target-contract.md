# Target Contract

A target validator returns one result and validates only its own category.

```yaml
result: ACCEPT_TARGET | REJECT_TARGET | AMBIGUOUS_TARGET | EXCEPTION_TARGET
target: session | canonical_project_store | skill | user_profile | persistent_memory | associative_memory | archive | protected_store
reason_code: stable_machine_readable_code
reason: human-readable explanation
operation: SKIP_DUPLICATE | ROUTE_ELSEWHERE | REPLACE | CONDENSE | ADD | NONE
```

`REJECT_TARGET` means “not my category”. It preserves the earlier `ADMIT` and
returns the candidate for reclassification.
