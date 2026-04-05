from typing import Any
import httpx
import mcp
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp_add = FastMCP("sum")

@mcp_add.tool()
async def add_numbers(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number
        b: Second number
    """
    return a + b

