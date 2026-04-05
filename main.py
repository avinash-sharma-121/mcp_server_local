from mcp.server.fastmcp import FastMCP
from weather import get_alerts, get_forecast
from add import add_numbers

from weather import mcp
from add import mcp_add


def main():
    #mcp.run(transport="stdio")
    mcp_add.run(transport="stdio")


if __name__ == "__main__":
    main()
