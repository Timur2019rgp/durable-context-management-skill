# Durable Context Management Skill

A reusable Hermes Agent skill for routing information before durable storage.

## What it does

The skill helps an agent:

- decide whether information should be preserved;
- keep the original meaning and epistemic status;
- choose one authoritative storage owner;
- distinguish a rejected target from rejected information;
- avoid unnecessary duplication across notes, profiles, memory, and skills;
- verify the final write.

Its core discipline is:

```text
admit once → preserve meaning → validate one owner →
reclassify without loss → write minimally → verify
```

## What it does not do

This skill does not configure or troubleshoot memory providers. Provider setup,
migrations, daemon diagnostics, and retain/recall smoke tests belong to a
separate provider-specific workflow.

It is also independent of any particular notes application, vault layout,
project structure, or user's personal memory files.

## Layout

```text
SKILL.md
references/
  provider-boundary.md
  routing-examples.md
  target-contract.md
tests/
  test_durable_context_management_skill.py
```

## Status

This is a publication candidate for an optional Hermes skill. Before merging,
check the target repository's existing memory-related skills and run the
repository's official skill tests and docs generator.

## License

MIT
