# Skill selection for TMC

Reviewed 17 September 2026. Best fit means useful for TMC's current non-video work, inspectable instructions, permissive licensing and portability. This is a comparison of selected candidates, not a universal ranking or measured quality benchmark.

| Source | Decision | Contribution | TMC adjustment |
|---|---|---|---|
| Anthropic knowledge-work-plugins: content-creation | Selected | Blog, email, social and website output structures | Remove unsupported example claims, generic frequency/length promises and mandatory proof blocks |
| Anthropic knowledge-work-plugins: email-sequence | Selected | Sequence strategy, timing, conditions, exits and complete email drafts | Five-email checklist scope; no assumed sender integration, benchmark guarantees or automatic sending |
| Corey Haines marketingskills: social | Selected | Platform adaptation and carousel narrative choices | TMC audience/volume/voice prevail; video and engagement outreach deferred |
| Corey Haines marketingskills: copy-editing | Selected | Focused editing passes and plain-language review | No invented specificity, false risk reversals, required expert personas or endless revision loops |
| Anthropic general skills repository | Reviewed as an alternative | General document/design capabilities | Host-dependent production tools; not a replacement for TMC editorial rules |
| Existing TMC skills | Retained as primary | Positioning, evidence boundaries, audience and format specificity | Connect shared context, reconcile legacy carousel assumptions, package consistently |

The social skill's current folder is `skills/social`, not the older `social-content` path still present in search results. Installation used pinned commits rather than an unreviewed moving main branch.

## Sources

- [Corey Haines marketing skills](https://github.com/coreyhaines31/marketingskills), MIT, commit `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`.
- [Anthropic marketing skills](https://github.com/anthropics/knowledge-work-plugins/tree/main/marketing), Apache-2.0, commit `bdf7160f2b33598fb0cb3860027e033cbaec7ce6`.
- [Anthropic general skills](https://github.com/anthropics/skills).
- [OpenAI skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins).
- [OpenAI projects](https://learn.chatgpt.com/docs/projects).
- [Claude skill installation](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
- [Claude custom skill packaging](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

## Review and deployment boundary

Four upstream folders were downloaded with the skill-installer helper into vendor/. Upstream source snapshots remain unmodified. We do not activate their generic triggers or execute their example commands. The runtime pack contains selected TMC adaptations with licenses and provenance; it does not enable social outreach, video or external connectors.

Upstream sources contain dated platform heuristics, example statistics and assumptions about external services. These must not become TMC facts. The adapted runtime deliberately omits generic posting quotas, fabricated personal hooks, guarantees and unsupported analytics benchmarks. Downloaded references are reference material, not permission to run commands.

The source lock contains versions and SHA-256 hashes. This establishes provenance and detects local changes; it does not certify the upstream repository or replace behavioural testing.
