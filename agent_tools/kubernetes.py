"""Kubernetes management tools for MCP server."""
from typing import Any


async def get_pods(namespace: str = "default") -> str:
    """Get list of pods in a Kubernetes namespace.
    
    Args:
        namespace: Kubernetes namespace (default: default)
    
    Returns:
        List of pods in the namespace
    """
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace, "-o", "json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return f"Pods in namespace '{namespace}':\n{result.stdout}"
        else:
            return f"Error getting pods: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}. Make sure kubectl is installed and configured."


async def get_services(namespace: str = "default") -> str:
    """Get list of services in a Kubernetes namespace.
    
    Args:
        namespace: Kubernetes namespace (default: default)
    
    Returns:
        List of services in the namespace
    """
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "get", "services", "-n", namespace, "-o", "json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return f"Services in namespace '{namespace}':\n{result.stdout}"
        else:
            return f"Error getting services: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}. Make sure kubectl is installed and configured."


async def get_deployments(namespace: str = "default") -> str:
    """Get list of deployments in a Kubernetes namespace.
    
    Args:
        namespace: Kubernetes namespace (default: default)
    
    Returns:
        List of deployments in the namespace
    """
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "get", "deployments", "-n", namespace, "-o", "json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return f"Deployments in namespace '{namespace}':\n{result.stdout}"
        else:
            return f"Error getting deployments: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}. Make sure kubectl is installed and configured."


async def get_cluster_info() -> str:
    """Get current Kubernetes cluster information.
    
    Returns:
        Current cluster context and info
    """
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "cluster-info"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return f"Cluster Information:\n{result.stdout}"
        else:
            return f"Error getting cluster info: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}. Make sure kubectl is installed and configured."


async def get_namespaces() -> str:
    """Get list of all namespaces in the cluster.
    
    Returns:
        List of namespaces
    """
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "get", "namespaces", "-o", "json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return f"Available Namespaces:\n{result.stdout}"
        else:
            return f"Error getting namespaces: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}. Make sure kubectl is installed and configured."
