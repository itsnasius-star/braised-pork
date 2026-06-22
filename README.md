# Cursor Setup Assignment

## Tools Installed

- Cursor IDE
- Claude Code for VS Code extension by Anthropic
- Claude Code CLI
- Codex add-on in Cursor
- macOS Command Line Tools
- Node.js and npm

## Steps Completed

1. Installed and opened Cursor IDE.
2. Opened the Extensions panel in Cursor.
3. Searched for "Claude Code".
4. Installed the official "Claude Code for VS Code" extension by Anthropic.
5. Installed macOS Command Line Tools.
6. Installed Node.js and npm.
7. Installed Claude Code CLI using npm.
8. Ran Claude Code successfully in Terminal.
9. Searched for "Codex" in Cursor Extensions.
10. Installed the Codex add-on in Cursor.
11. Created this README.md file to document the setup process.

## Issues Encountered and Solutions

### 1. Cursor shortcut did not open Extensions

At first, pressing `Cmd + Shift + X` did not open the Extensions panel. I solved this by opening the editor window and accessing the Extensions panel from there.

### 2. Claude command not found

After installing the Claude Code extension, running `claude` in Terminal showed:

`zsh: command not found: claude`

This happened because the Claude Code CLI was not installed yet. I solved this by installing the Claude Code CLI using npm.

### 3. npm command not found

When trying to install Claude Code CLI, npm was not available. I solved this by installing Node.js, which includes npm.

### 4. Permission denied during npm install

When running:

`npm install -g @anthropic-ai/claude-code`

I received a permission error. I solved it by running:

`sudo npm install -g @anthropic-ai/claude-code`

After entering my Mac password, the installation completed successfully.

### 5. Codex was not visible in Cursor Customize

At first, I searched for "Codex" in Cursor's Customize/Marketplace section, but there was no result. I solved this by using the Extensions panel instead, where I found and installed the Codex add-on.

## Result

Claude Code was successfully installed and launched in Terminal. It opened as Claude Code v2.1.175 and displayed the initial setup screen. The Codex add-on was also installed successfully in Cursor.

# B2B SaaS YouTube Content Strategy Research Project

## Topic Chosen

YouTube content strategy for B2B SaaS.

## Why This Topic

I chose this topic because YouTube content is public, transcript-friendly, and suitable for systematic research using free tools. This makes it a practical choice for collecting source material without relying on paid subscriptions or restricted platform scraping.

The topic is relevant to B2B SaaS because many SaaS founders, marketers, and operators use long-form video, interviews, webinars, and educational content to build trust, explain complex products, generate demand, and repurpose content across LinkedIn, newsletters, blogs, and sales materials.

## Research Approach

This project prioritizes signal over volume. I selected practitioners and channels based on their relevance to B2B SaaS growth, demand generation, positioning, content strategy, and founder-led marketing.

Instead of collecting a large number of generic sources, I am collecting a smaller set of high-signal transcripts that could support a practical B2B SaaS content strategy playbook later.

## Current Progress

- Created research folder structure
- Added source selection criteria
- Created placeholder folders for transcripts and supporting materials
- Built a small transcript collection script using `youtube-transcript-api`
- Collected YouTube transcripts from 10 selected experts/channels:
  - Dave Gerhardt / Exit Five
  - Chris Walker / Refine Labs
  - TK Kader
  - April Dunford
  - Peep Laja / Wynter / CXL
  - Jason Lemkin / SaaStr
  - Lenny Rachitsky
  - Nathan Latka
  - Adam Robinson
  - Ross Simmonds

## Final Collection Summary

This research project collected 10 YouTube transcript sources from practitioners and channels relevant to B2B SaaS growth, content strategy, positioning, demand generation, founder-led marketing, and content distribution.

The project uses a focused source selection approach instead of collecting a large number of generic sources. Each expert was selected because their content can support a future practical playbook on YouTube content strategy for B2B SaaS.

## Repository Structure

- `/research/sources.md` — expert list, source links, and annotations
- `/research/youtube-transcripts/` — collected YouTube transcripts organized by expert/video
- `/research/linkedin-posts/` — optional supporting LinkedIn materials
- `/research/other/research-log.md` — research reasoning and selection criteria
- `/scripts/fetch_youtube_transcript.py` — script used to collect public YouTube transcripts

## Research Principle

The goal is not to maximize volume. The goal is to build a clean, well-documented research base that shows source judgment, technical collection ability, and practical relevance to B2B SaaS content strategy.