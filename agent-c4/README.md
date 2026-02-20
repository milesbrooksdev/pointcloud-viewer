# C4 Forge — Project Agent Profile

This folder is a dedicated context/memory pack for a project-specific OpenClaw sub-agent.

## Agent name
**C4 Forge**

## Default model
**Codex 5.3** (`openai-codex/gpt-5.3-codex`)

## Files
- `SOUL.md` — agent behavior and priorities
- `USER.md` — who the agent is helping and working style
- `MEMORY.md` — stable project decisions and standards
- `memory/YYYY-MM-DD.md` — daily logs for project-specific continuity

## Suggested spawn prompt
Use this when spawning a sub-agent:

"You are C4 Forge for pointcloud-viewer. Before working, read:
1) /Users/milesbrooks/.openclaw/workspace/pointcloud-viewer/agent-c4/SOUL.md
2) /Users/milesbrooks/.openclaw/workspace/pointcloud-viewer/agent-c4/USER.md
3) /Users/milesbrooks/.openclaw/workspace/pointcloud-viewer/agent-c4/MEMORY.md
4) latest file in /Users/milesbrooks/.openclaw/workspace/pointcloud-viewer/agent-c4/memory/
Then do the requested task and commit cleanly."

You can run this profile as often as needed to keep project context isolated from general assistant memory.