#!/usr/bin/env python3
import json
import sys
from mcp.server import Server
from mcp.server.stdio import StdioServerTransport

def main():
    # Create a new MCP server
    server = Server(name="mcp-document-server", version="1.0.0")
    
    # Define a get_docs tool
    @server.tool(
        name="get_docs",
        description="Get documentation on a specified topic",
        input_schema={
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic to get documentation for",
                },
            },
            "required": ["topic"],
        }
    )
    async def get_docs(input_data):
        topic = input_data["topic"]
        
        # Simple documentation examples
        docs = {
            "mcp": "Model Context Protocol (MCP) is a protocol for LLMs to communicate with tools.",
            "tools": "MCP tools are functions that can be called by LLMs through the MCP client.",
            "client": "The MCP client connects to an MCP server and provides tools to LLMs.",
            "server": "The MCP server hosts tools that can be used by LLMs through the MCP client.",
        }
        
        if topic.lower() in docs:
            return {"content": docs[topic.lower()]}
        else:
            return {"content": f"Documentation for '{topic}' not found. Available topics: {', '.join(docs.keys())}"}
    
    # Define a debug_search tool
    @server.tool(
        name="debug_search",
        description="Search for debugging information",
        input_schema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query",
                },
            },
            "required": ["query"],
        }
    )
    async def debug_search(input_data):
        query = input_data["query"]
        
        # Simple debug search responses
        debug_info = {
            "error": "Debugging errors: Check logs, verify API keys, check network connections, inspect stack traces.",
            "connection": "Connection issues: Verify server is running, check network settings, confirm ports are open.",
            "setup": "Setup problems: Ensure all dependencies are installed, check configuration files, verify environment variables.",
        }
        
        for key, info in debug_info.items():
            if key in query.lower():
                return {"content": info}
        
        return {"content": f"No specific debug info found for '{query}'. Try searching for: {', '.join(debug_info.keys())}"}
    
    # Start the server with stdio transport
    transport = StdioServerTransport()
    server.listen(transport)

if __name__ == "__main__":
    main()
