from mcp.server.fastmcp import FastMCP
from agent_tools.weather import get_alerts, get_forecast
from agent_tools.add import add_numbers

# Create single MCP server with both tool sets
mcp = FastMCP("")

# Create an MCP server
mcp = FastMCP(
    name="multi-tool-server",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8000,  # only used for SSE transport (set this to any port)
)

# Add weather tools
mcp.tool()(get_alerts)
mcp.tool()(get_forecast)

# Add add tool
mcp.tool()(add_numbers)


# Run the server
if __name__ == "__main__":
    transport = "sse"
    #transport = "stdio"
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")
    


#def main():
#
#    # use studio to run the server and test the tools
#    #mcp.run(transport="stdio") 
#
#    # Use SSE (Server-Sent Events) transport which works over HTTP
#    mcp.run(transport="sse")
#
#if __name__ == "__main__":
#    main()

