from fastmcp import FastMCP

# 运行  fastmcp run mcp1.py:mcp --transport http --port 8000


mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)