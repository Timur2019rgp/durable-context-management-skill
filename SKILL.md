---
name: durable-context-management
description: Route durable context to one verified owner.
version: 0.1.0
author: Timur2019rgp (Timur), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [memory, context, routing, provenance]
    related_skills: []
---

# Durable Context Management

Classify information before durable storage, select one authoritative owner,
and verify the write. This skill governs semantic storage decisions; it does
not configure or troubleshoot memory providers.

## When to Use

Use when the user asks to save, remember, retain, capture, or preserve
information for future sessions, or when auditing profile memory, persistent
memory, project context, or procedural skills.

Do not use for ordinary edits to a file whose ownership is already explicit,
or when the user says the conversation is discussion-only and requests no
writes.

## Procedure

1. **Apply the write gate.**
   Stop on discussion-only mode, secrets, unresolved sensitivity, or missing
   permission for canonical, architectural, destructive, or meaning-changing
   changes. Completion: durable writes are permitted or explicitly blocked.

2. **Run initial admission exactly once.**
   Return `ADMIT`, `REJECT_INITIAL`, `ASK_INITIAL`, or `BLOCK_INITIAL`.
   Completion: the value of preserving the material is decided without
   selecting a target.

3. **Build an unwritten candidate.**
   Preserve wording, source, type, scope, sensitivity, epistemic status,
   attempted targets, and rejected targets. Never convert possibility to plan,
   reaction to trait, hypothesis to fact, discussion to decision, or idea to
   commitment. Completion: no durable write occurred and source meaning is
   intact.

4. **Start with the broad canonical store.**
   Treat the admitted material as a candidate for the user's canonical project
   or knowledge store. This is a routing assumption, not a physical write.

5. **Check promotion.**
   Ask:

   > Can this information serve its purpose better on a narrower or more
   > automatically active layer?

   `NO` finalizes the broad target after validation. `YES` or `POSSIBLY`
   validates the next semantically suitable target. `UNKNOWN` requires minimal
   context retrieval or a question only when the ambiguity changes meaning.
   Potential usefulness starts validation; it never authorizes a write.

6. **Validate one target.**
   Candidate targets include session-only context, canonical project store,
   procedural skill, user profile, persistent memory, associative memory,
   archive, or protected secret storage. Return exactly one of:
   `ACCEPT_TARGET`, `REJECT_TARGET`, `AMBIGUOUS_TARGET`, or
   `EXCEPTION_TARGET`.

   A target validates only its own category. It cannot revoke `ADMIT`.
   Completion: one target accepts or the candidate returns for reclassification.

7. **Reclassify after `REJECT_TARGET`.**
   Exclude the rejected category unless the meaning changes. Do not rerun
   initial admission. If every plausible owner fails after `ADMIT`, write
   nothing and report the contradiction instead of silently dropping material.

8. **Choose the least additive operation.**
   Use this order:

   `SKIP_DUPLICATE → ROUTE_ELSEWHERE → REPLACE → CONDENSE → ADD`

   Keep one authoritative owner and only necessary projections. Completion:
   the operation respects the target's size and activation budget.

9. **Write once, verify, and report.**
   Use the owning tool, read back or verify its receipt, and report what was
   stored, where, why, and what was intentionally not promoted. Completion:
   one authoritative write is verified.

## Target Boundaries

- **Session-only:** temporary details needed only for the current task.
- **Canonical project store:** detailed and changing project context, decisions,
  facts, history, and provenance.
- **Skill:** verified reusable procedures, triggers, pitfalls, and checks; not
  live state, biography, canon, or one-time logs.
- **User profile:** stable cross-topic user facts and interaction preferences;
  not project state or procedures.
- **Persistent memory:** compact critical routes and boundaries whose absence
  repeatedly causes costly errors; not detailed notes or ordinary preferences.
- **Associative memory:** recall evidence and synthesis; not canonical truth.
- **Archive:** replaced versions and historical snapshots with explicit status.
- **Protected store:** secrets only when a specialized secure mechanism exists.

## Decision Contract

For complex cases, keep one contract per semantic unit:

```yaml
admission: ADMIT
wording: source-preserving text
type: preference | fact | procedure | decision | hypothesis | status | route
scope: session | project | domain | global
source: user | file | live-system | session-history | agent-inference
sensitivity: public | personal | sensitive | secret
status: direct-quote | verified | user-hypothesis | assistant-hypothesis | decision | unknown
attempted_targets: []
rejected_targets: []
result: ACCEPT_TARGET | REJECT_TARGET | AMBIGUOUS_TARGET | EXCEPTION_TARGET
target: session | canonical_project_store | skill | user_profile | persistent_memory | associative_memory | archive | protected_store
operation: SKIP_DUPLICATE | ROUTE_ELSEWHERE | REPLACE | CONDENSE | ADD | NONE
```

Do not expose the full contract in ordinary conversation unless debugging,
evaluating, or resolving a storage conflict.

## Pitfalls

- Treating “remember this” as “append to persistent memory”.
- Re-running admission after a target rejects its category.
- Duplicating one fact across profile, memory, notes, and skills.
- Treating provider availability as proof that retain/recall works.
- Using associative recall as current canonical truth.
- Creating a new memory subsystem because naming or retrieval is inconvenient.
- Converting a hypothesis, possibility, or discussion into a fact or decision.

## Verification

Before finalizing, confirm:

- the write gate ran before storage;
- admission ran once;
- the candidate stayed unwritten during routing;
- source wording and epistemic status were preserved;
- exactly one authoritative owner was selected;
- rejected targets were not silently retried;
- the least additive operation was used;
- the final write was verified and receipted.
