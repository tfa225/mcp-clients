// Simple MCP server for testing
const { Server } = require('@modelcontextprotocol/sdk/server');
const { StdioServerTransport } = require('@modelcontextprotocol/sdk/server/stdio');

async function main() {
  // Create a new MCP server
  const server = new Server({
    name: 'test-mcp-server',
    version: '1.0.0',
  });

  // Define a simple calculator tool
  server.defineTool({
    name: 'calculator',
    description: 'A simple calculator that can add, subtract, multiply, and divide numbers',
    inputSchema: {
      type: 'object',
      properties: {
        operation: {
          type: 'string',
          enum: ['add', 'subtract', 'multiply', 'divide'],
          description: 'The operation to perform',
        },
        a: {
          type: 'number',
          description: 'The first number',
        },
        b: {
          type: 'number',
          description: 'The second number',
        },
      },
      required: ['operation', 'a', 'b'],
    },
    handler: async (input) => {
      const { operation, a, b } = input;
      let result;
      
      switch (operation) {
        case 'add':
          result = a + b;
          break;
        case 'subtract':
          result = a - b;
          break;
        case 'multiply':
          result = a * b;
          break;
        case 'divide':
          if (b === 0) {
            return {
              content: 'Error: Division by zero',
            };
          }
          result = a / b;
          break;
        default:
          return {
            content: `Unknown operation: ${operation}`,
          };
      }
      
      return {
        content: `Result of ${operation}(${a}, ${b}) = ${result}`,
      };
    },
  });

  // Connect to the transport
  const transport = new StdioServerTransport();
  await server.listen(transport);
}

main().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});