"""
opencode-chat-export — MCP server to export OpenCode chat history to Markdown.

Install:
    pip install opencode-chat-export

Add to ~/.config/opencode/opencode.jsonc:
    "chat-export": {
      "type": "local",
      "command": ["opencode-chat-export"],
      "enabled": false
    }

CLI usage:
    opencode-chat-export list
    opencode-chat-export export <session_id>
    opencode-chat-export export-all
"""

from .server import main

__all__ = ["main"]
