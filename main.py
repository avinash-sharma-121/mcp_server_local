from mcp.server.fastmcp import FastMCP
from agent_tools.weather import get_alerts, get_forecast
from agent_tools.add import add_numbers

# Create single MCP server with both tool sets
mcp = FastMCP("multi-tool-server")

# Add weather tools
mcp.tool()(get_alerts)
mcp.tool()(get_forecast)

# Add add tool
mcp.tool()(add_numbers)

def main():

    # use studio to run the server and test the tools
    # mcp.run(transport="stdio") 

    # Use SSE (Server-Sent Events) transport which works over HTTP
    mcp.run(transport="sse")

if __name__ == "__main__":
    main()
