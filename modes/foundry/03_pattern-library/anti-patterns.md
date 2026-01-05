# Anti-Patterns (Foundry)

- Agent sprawl: too many specialized agents before eval scenarios exist
- Missing ownership: files without a clear owner agent
- No eval loop: rubrics exist but no scenarios or scorecards
- Template bloat: templates so heavy nobody uses them
- Dimension overload: too many dimensions early; unclear deltas
- Unlogged assumptions: outputs pretend certainty without stating data gaps
- Mirror-hostile: dependencies on files outside `modes/foundry/` (prevents clean mirroring)
