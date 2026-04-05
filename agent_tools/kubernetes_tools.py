"""
Kubernetes tools - all in Python using kubectl and Python k8s client
No Node.js dependency needed!
"""

import subprocess
import json
from typing import Optional

# ========================
# Pod Management
# ========================

def list_pods(namespace: str = "default") -> str:
    """List all pods in a Kubernetes namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl get pods -n {namespace} -o json",
            shell=True,
            text=True
        )
        pods_data = json.loads(result)
        pods = []
        for pod in pods_data.get("items", []):
            name = pod["metadata"]["name"]
            status = pod["status"]["phase"]
            pods.append(f"  - {name} ({status})")
        return f"Pods in {namespace}:\n" + "\n".join(pods) if pods else f"No pods found in {namespace}"
    except Exception as e:
        return f"Error listing pods: {str(e)}"

def get_pod_details(pod_name: str, namespace: str = "default") -> str:
    """Get detailed information about a specific pod
    
    Args:
        pod_name: Name of the pod
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl describe pod {pod_name} -n {namespace}",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting pod details: {str(e)}"


def get_pod_logs(pod_name: str, namespace: str = "default", tail: int = 50) -> str:
    """Get logs from a Kubernetes pod
    
    Args:
        pod_name: Name of the pod
        namespace: Kubernetes namespace (default: default)
        tail: Number of lines to tail (default: 50)
    """
    try:
        result = subprocess.check_output(
            f"kubectl logs {pod_name} -n {namespace} --tail={tail}",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting pod logs: {str(e)}"


def delete_pod(pod_name: str, namespace: str = "default") -> str:
    """Delete a Kubernetes pod
    
    Args:
        pod_name: Name of the pod to delete
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl delete pod {pod_name} -n {namespace}",
            shell=True,
            text=True
        )
        return f"Pod deleted: {result}"
    except Exception as e:
        return f"Error deleting pod: {str(e)}"

# ========================
# Deployment Management
# ========================


def list_deployments(namespace: str = "default") -> str:
    """List all deployments in a Kubernetes namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl get deployments -n {namespace} -o json",
            shell=True,
            text=True
        )
        deps_data = json.loads(result)
        deployments = []
        for dep in deps_data.get("items", []):
            name = dep["metadata"]["name"]
            replicas = dep["spec"].get("replicas", 0)
            ready = dep["status"].get("readyReplicas", 0)
            deployments.append(f"  - {name} ({ready}/{replicas} ready)")
        return f"Deployments in {namespace}:\n" + "\n".join(deployments) if deployments else f"No deployments found in {namespace}"
    except Exception as e:
        return f"Error listing deployments: {str(e)}"


def get_deployment_details(deployment_name: str, namespace: str = "default") -> str:
    """Get detailed information about a deployment
    
    Args:
        deployment_name: Name of the deployment
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl describe deployment {deployment_name} -n {namespace}",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting deployment details: {str(e)}"


def scale_deployment(deployment_name: str, replicas: int, namespace: str = "default") -> str:
    """Scale a Kubernetes deployment to desired number of replicas
    
    Args:
        deployment_name: Name of the deployment
        replicas: Desired number of replicas
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl scale deployment {deployment_name} --replicas={replicas} -n {namespace}",
            shell=True,
            text=True
        )
        return f"Deployment scaled: {result}"
    except Exception as e:
        return f"Error scaling deployment: {str(e)}"


def restart_deployment(deployment_name: str, namespace: str = "default") -> str:
    """Restart a Kubernetes deployment
    
    Args:
        deployment_name: Name of the deployment
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl rollout restart deployment/{deployment_name} -n {namespace}",
            shell=True,
            text=True
        )
        return f"Deployment restarted: {result}"
    except Exception as e:
        return f"Error restarting deployment: {str(e)}"

# ========================
# Service Management
# ========================


def list_services(namespace: str = "default") -> str:
    """List all services in a Kubernetes namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl get services -n {namespace} -o json",
            shell=True,
            text=True
        )
        svc_data = json.loads(result)
        services = []
        for svc in svc_data.get("items", []):
            name = svc["metadata"]["name"]
            svc_type = svc["spec"]["type"]
            services.append(f"  - {name} ({svc_type})")
        return f"Services in {namespace}:\n" + "\n".join(services) if services else f"No services found in {namespace}"
    except Exception as e:
        return f"Error listing services: {str(e)}"


def get_service_details(service_name: str, namespace: str = "default") -> str:
    """Get detailed information about a service
    
    Args:
        service_name: Name of the service
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl describe service {service_name} -n {namespace}",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting service details: {str(e)}"

# ========================
# Namespace Management
# ========================


def list_namespaces() -> str:
    """List all Kubernetes namespaces"""
    try:
        result = subprocess.check_output(
            "kubectl get namespaces -o json",
            shell=True,
            text=True
        )
        ns_data = json.loads(result)
        namespaces = []
        for ns in ns_data.get("items", []):
            name = ns["metadata"]["name"]
            status = ns["status"]["phase"]
            namespaces.append(f"  - {name} ({status})")
        return "Namespaces:\n" + "\n".join(namespaces) if namespaces else "No namespaces found"
    except Exception as e:
        return f"Error listing namespaces: {str(e)}"


def create_namespace(namespace_name: str) -> str:
    """Create a new Kubernetes namespace
    
    Args:
        namespace_name: Name of the namespace to create
    """
    try:
        result = subprocess.check_output(
            f"kubectl create namespace {namespace_name}",
            shell=True,
            text=True
        )
        return f"Namespace created: {result}"
    except Exception as e:
        return f"Error creating namespace: {str(e)}"

# ========================
# ConfigMap Management
# ========================


def list_configmaps(namespace: str = "default") -> str:
    """List all ConfigMaps in a Kubernetes namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl get configmaps -n {namespace} -o json",
            shell=True,
            text=True
        )
        cm_data = json.loads(result)
        configmaps = []
        for cm in cm_data.get("items", []):
            name = cm["metadata"]["name"]
            keys = len(cm.get("data", {}))
            configmaps.append(f"  - {name} ({keys} keys)")
        return f"ConfigMaps in {namespace}:\n" + "\n".join(configmaps) if configmaps else f"No ConfigMaps found in {namespace}"
    except Exception as e:
        return f"Error listing ConfigMaps: {str(e)}"

# ========================
# Cluster Information
# ========================


def get_cluster_info() -> str:
    """Get Kubernetes cluster information"""
    try:
        result = subprocess.check_output(
            "kubectl cluster-info",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting cluster info: {str(e)}"


def get_cluster_version() -> str:
    """Get Kubernetes cluster version"""
    try:
        result = subprocess.check_output(
            "kubectl version",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting cluster version: {str(e)}"


def get_nodes() -> str:
    """List all nodes in the Kubernetes cluster"""
    try:
        result = subprocess.check_output(
            "kubectl get nodes -o json",
            shell=True,
            text=True
        )
        nodes_data = json.loads(result)
        nodes = []
        for node in nodes_data.get("items", []):
            name = node["metadata"]["name"]
            status = node["status"]["conditions"][-1]["type"]
            nodes.append(f"  - {name} ({status})")
        return "Cluster Nodes:\n" + "\n".join(nodes) if nodes else "No nodes found"
    except Exception as e:
        return f"Error getting nodes: {str(e)}"


def get_node_details(node_name: str) -> str:
    """Get detailed information about a node
    
    Args:
        node_name: Name of the node
    """
    try:
        result = subprocess.check_output(
            f"kubectl describe node {node_name}",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting node details: {str(e)}"

# ========================
# StatefulSet Management
# ========================


def list_statefulsets(namespace: str = "default") -> str:
    """List all StatefulSets in a Kubernetes namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl get statefulsets -n {namespace} -o json",
            shell=True,
            text=True
        )
        ss_data = json.loads(result)
        statefulsets = []
        for ss in ss_data.get("items", []):
            name = ss["metadata"]["name"]
            replicas = ss["spec"].get("serviceName", "")
            statefulsets.append(f"  - {name}")
        return f"StatefulSets in {namespace}:\n" + "\n".join(statefulsets) if statefulsets else f"No StatefulSets found in {namespace}"
    except Exception as e:
        return f"Error listing StatefulSets: {str(e)}"

# ========================
# Resource Monitoring
# ========================


def get_resource_usage(namespace: str = "default") -> str:
    """Get resource usage (CPU, memory) for pods in a namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
    """
    try:
        result = subprocess.check_output(
            f"kubectl top pods -n {namespace}",
            shell=True,
            text=True
        )
        return result if result else f"No resource metrics available for {namespace}. Metrics server may not be installed."
    except Exception as e:
        return f"Error getting resource usage: {str(e)}. Make sure metrics-server is installed."


def get_node_resource_usage() -> str:
    """Get resource usage for cluster nodes"""
    try:
        result = subprocess.check_output(
            "kubectl top nodes",
            shell=True,
            text=True
        )
        return result if result else "No resource metrics available. Metrics server may not be installed."
    except Exception as e:
        return f"Error getting node resource usage: {str(e)}"

# ========================
# Useful Helper Tools
# ========================


def get_events(namespace: str = "default", limit: int = 20) -> str:
    """Get recent Kubernetes events in a namespace
    
    Args:
        namespace: Kubernetes namespace (default: default)
        limit: Number of events to return (default: 20)
    """
    try:
        result = subprocess.check_output(
            f"kubectl get events -n {namespace} --sort-by='.lastTimestamp' | tail -{limit}",
            shell=True,
            text=True
        )
        return result
    except Exception as e:
        return f"Error getting events: {str(e)}"


def apply_yaml(yaml_file: str) -> str:
    """Apply a Kubernetes YAML configuration file
    
    Args:
        yaml_file: Path to the YAML file
    """
    try:
        result = subprocess.check_output(
            f"kubectl apply -f {yaml_file}",
            shell=True,
            text=True
        )
        return f"YAML applied successfully: {result}"
    except Exception as e:
        return f"Error applying YAML: {str(e)}"
