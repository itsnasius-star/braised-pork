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
