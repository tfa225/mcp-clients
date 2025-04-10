# MCP Clients

Tutorial on creating MCP Clients with JavaScript.

## Setup

1. Install dependencies:
```
npm install
```

2. Create a `.env` file with your API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

3. Build the TypeScript project:
```
npm run build
```

4. Install Python requirements for the server:
```
pip install modelcontextprotocol
```

5. Run the client with the Python MCP server:
```
node build/index.js ./documentation/main.py
```

## Usage

Once the client is running, you can interact with it by typing queries. The Python server provides two tools:

- `get_docs`: Get documentation on a specified topic
- `debug_search`: Search for debugging information

Type 'quit' to exit the client.

## Based on

This project is based on Alejandro Ao's tutorial: [YouTube Tutorial](https://www.youtube.com/watch?v=5tl6D-h2_Qc)
