from mcp.server.fastmcp import FastMCP
from weather import get_alerts, get_forecast
from add import add_numbers

# Create single MCP server with both tool sets
mcp = FastMCP("multi-tool-server")

# Add weather tools
mcp.tool()(get_alerts)
mcp.tool()(get_forecast)

# Add add tool
mcp.tool()(add_numbers)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
