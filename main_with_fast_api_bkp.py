from mcp.server.fastmcp import FastMCP
from agent_tools.weather import get_alerts, get_forecast
from agent_tools.add import add_numbers
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

# Create single MCP server with both tool sets
mcp = FastMCP("multi-tool-server")

# Add weather tools
mcp.tool()(get_alerts)
mcp.tool()(get_forecast)

# Add add tool
mcp.tool()(add_numbers)

# Create FastAPI app for UI
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Nothing to do on startup/shutdown
    yield

app = FastAPI(lifespan=lifespan)

# Mount the MCP SSE server to the FastAPI app
mcp.fastapi_app = app

# Serve the UI at root
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MCP Tools Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background: white;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                margin-bottom: 10px;
            }
            .subtitle {
                color: #666;
                margin-bottom: 30px;
            }
            .tools-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            .tool-card {
                background: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 6px;
                padding: 20px;
                transition: transform 0.2s;
            }
            .tool-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }
            .tool-name {
                font-size: 18px;
                font-weight: bold;
                color: #0066cc;
                margin-bottom: 10px;
            }
            .tool-desc {
                color: #666;
                font-size: 14px;
                line-height: 1.5;
                margin-bottom: 15px;
            }
            .tool-params {
                background: white;
                padding: 10px;
                border-radius: 4px;
                font-size: 13px;
                color: #555;
            }
            .param {
                margin: 5px 0;
            }
            .status {
                background: #e8f5e9;
                color: #2e7d32;
                padding: 15px;
                border-radius: 6px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 MCP Tools Server</h1>
            <p class="subtitle">Multi-tool MCP server with weather and arithmetic tools</p>
            
            <div class="status">
                ✅ Server is running and ready to use
            </div>
            
            <h2>Available Tools</h2>
            <div class="tools-grid">
                <div class="tool-card">
                    <div class="tool-name">🌦️ get_alerts</div>
                    <div class="tool-desc">Get weather alerts for a US state</div>
                    <div class="tool-params">
                        <div class="param"><strong>Parameters:</strong></div>
                        <div class="param">• state: Two-letter US state code (e.g., CA, NY)</div>
                    </div>
                </div>
                
                <div class="tool-card">
                    <div class="tool-name">📊 get_forecast</div>
                    <div class="tool-desc">Get weather forecast for a location</div>
                    <div class="tool-params">
                        <div class="param"><strong>Parameters:</strong></div>
                        <div class="param">• latitude: Latitude of location</div>
                        <div class="param">• longitude: Longitude of location</div>
                    </div>
                </div>
                
                <div class="tool-card">
                    <div class="tool-name">➕ add_numbers</div>
                    <div class="tool-desc">Add two numbers together</div>
                    <div class="tool-params">
                        <div class="param"><strong>Parameters:</strong></div>
                        <div class="param">• a: First number</div>
                        <div class="param">• b: Second number</div>
                    </div>
                </div>
            </div>
            
            <h2 style="margin-top: 40px;">Connection Info</h2>
            <div class="tool-params">
                <div class="param"><strong>MCP Server Name:</strong> multi-tool-server</div>
                <div class="param"><strong>Transport:</strong> SSE (Server-Sent Events)</div>
                <div class="param"><strong>Base URL:</strong> http://localhost:8000</div>
                <div class="param"><strong>Status:</strong> Running ✅</div>
            </div>
        </div>
    </body>
    </html>
    """

def main():
    # Run with uvicorn
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
