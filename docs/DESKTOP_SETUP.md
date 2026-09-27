# TMC desktop setup

Release 0.1: a shared instruction pack for non-video TMC content. Both apps receive identical knowledge and operating rules. Native integrations and rendered outputs depend on each session's actual tools. This release has not been installed or tested inside either target account.

## Shared project-file route (both apps)

1. Create a TMC Content Engine project in the chosen app.
2. Paste project-files/PROJECT_INSTRUCTIONS.md into its project instructions.
3. Add TMC_CONTEXT.md, TMC_FORMATS.md and TMC_WORKFLOW.md from project-files as project knowledge/sources. Retain the notices/licenses with the distributed package.
4. Add the two logo PNGs when creating visual content, and upload source media, approved claims and job files needed for that task. Uploads or actual folder connections are required; a pasted local path is not sufficient.
5. Start a fresh conversation inside the project using a pilot prompt below.

Use one app at a time for an individual asset version. Move the latest job record and content files when switching apps. Copies do not synchronise automatically. Replace old knowledge files after rebuilding, rather than uploading several conflicting versions.

## Claude native skill route

Where custom skills are available: Customize > Skills > + Create skill > Upload a skill. Upload tmc-content-workflow.zip and enable it. The ZIP has one root folder with SKILL.md, three bundled references, logos, a job template and licenses. Do not upload the entire dist folder as a skill. The reference pack is self-contained; the older TMC skills do not also need to be installed for this release.

Enable the file creation/code execution capabilities needed for the requested outputs, if available under the account's settings. Workspace controls may limit skills. If native skill upload is unavailable, use the shared project-file route.

## ChatGPT route

Use project instructions and uploaded knowledge as the baseline. Current OpenAI documentation also describes native skills and explicit @ mentions. If the account exposes a skill creation/import workflow, supply the tmc-content-workflow folder through that supported workflow. Do not assume the Claude ZIP upload UI exists in ChatGPT.

An ordinary ChatGPT project uses uploaded/connected sources. A local project or work environment may offer folder access; verify it before asking the assistant to write to disk. No Codex-only configuration is required for the project-file baseline.

## First prompt

"Use the TMC content workflow. Tell me whether you can read the TMC context, formats and workflow files. Then draft a TMC company LinkedIn post for principals about three questions to discuss before choosing a school-trip destination. Use general planning advice, no TMC performance claims and no CTA. Include a short QA result and a portable job record."

Then run system/SMOKE_TESTS.md (included in TMC_WORKFLOW.md) in both apps. Record outputs rather than assuming identical behaviour from identical instructions. The next visual pilot needs approved photos or an agreed text-led design and a verified rendering capability.

## What is ready and what comes next

Ready: shared brand context, format routing, adapted external methods, review/version rules, job template, native skill archive and project-file pack.

Next: import into both accounts and run the same text pilot; approve visual templates and test actual PNG/PDF/editable-source exports; connect approved factual sources and media permissions; build the checklist funnel when its website/email setup is known.

No publishing, scheduled tasks, messaging, account connections or subscriptions are configured by this pack.

## Maintainer rebuild

Edit system/ and the existing skills/ or brand-brief.md as appropriate. Run `python scripts/build_desktop_pack.py`. It uses only the standard library and writes a fresh dist/tmc-0.1.0-* release without replacing prior releases. Pin and review upstream updates before changing vendor sources. Do not edit generated knowledge files in only one app.

## Verified product documentation (17 September 2026)

- [OpenAI projects and source access](https://learn.chatgpt.com/docs/projects)
- [OpenAI skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Claude custom skill installation](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Claude skill folder and ZIP structure](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
