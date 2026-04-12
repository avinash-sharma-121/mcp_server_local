from mcp.server.fastmcp import FastMCP
from agent_tools.weather import get_alerts, get_forecast
from agent_tools.add import add_numbers
from agent_tools.about_me import about_developer
from agent_tools.server_managment import (
    get_system_info,
    get_disk_usage,
    get_memory_usage,
    get_cpu_usage,
    get_top_processes,
    check_service_status,
    get_network_info,
    check_open_ports,
    get_installed_packages_count,
    check_disk_inode_usage,
    get_systemd_failed_units,
    check_file_permissions,
)
from agent_tools.kubernetes_tools import (
    list_pods,
    get_pod_details,
    get_pod_logs,
    delete_pod,
    list_deployments,
    get_deployment_details,
    scale_deployment,
    restart_deployment,
    list_services,
    get_service_details,
    list_namespaces,
    create_namespace,
    list_configmaps,
    get_cluster_info,
)

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

# Add server management tools
mcp.tool()(get_system_info)
mcp.tool()(get_disk_usage)
mcp.tool()(get_memory_usage)
mcp.tool()(get_cpu_usage)
mcp.tool()(get_top_processes)
mcp.tool()(check_service_status)
mcp.tool()(get_network_info)
mcp.tool()(check_open_ports)
mcp.tool()(get_installed_packages_count)
mcp.tool()(check_disk_inode_usage)
mcp.tool()(get_systemd_failed_units)
mcp.tool()(check_file_permissions)

# Add Kubernetes tools
mcp.tool()(list_pods)
mcp.tool()(get_pod_details)
mcp.tool()(get_pod_logs)
mcp.tool()(delete_pod)
mcp.tool()(list_deployments)
mcp.tool()(get_deployment_details)
mcp.tool()(scale_deployment)
mcp.tool()(restart_deployment)
mcp.tool()(list_services)
mcp.tool()(get_service_details)
mcp.tool()(list_namespaces)
mcp.tool()(create_namespace)
mcp.tool()(list_configmaps)
mcp.tool()(get_cluster_info)

# Add about me tool
mcp.tool()(about_developer)

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

