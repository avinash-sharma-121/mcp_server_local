# mcp_server_local
working with multiple local agent with the power of mcp_server


#installation steps

curl -LsSf https://astral.sh/uv/install.sh | sh

# python project intilize 
uv init mcp_server_local

# Create virtual environment and activate it
cd mcp_server_local
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch weather.py

# how to start mcp server in terminal
uv run mcp dev main.py 


