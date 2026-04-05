"""Linux server management tools for MCP server."""
import subprocess
from typing import Any


async def get_system_info() -> str:
    """Get detailed system information including OS, kernel, and uptime.
    
    Returns:
        System information details
    """
    try:
        result = subprocess.run(
            ["uname", "-a"],
            capture_output=True,
            text=True,
            timeout=5
        )
        uptime = subprocess.run(
            ["uptime"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"System Information:\n{result.stdout}\nUptime:\n{uptime.stdout}"
        else:
            return f"Error getting system info: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def get_disk_usage(path: str = "/") -> str:
    """Get disk usage for a specified path.
    
    Args:
        path: File system path to check (default: /)
    
    Returns:
        Disk usage details
    """
    try:
        result = subprocess.run(
            ["df", "-h", path],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Disk Usage for {path}:\n{result.stdout}"
        else:
            return f"Error getting disk usage: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def get_memory_usage() -> str:
    """Get memory and swap usage statistics.
    
    Returns:
        Memory usage details
    """
    try:
        result = subprocess.run(
            ["free", "-h"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Memory Usage:\n{result.stdout}"
        else:
            return f"Error getting memory usage: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def get_cpu_usage() -> str:
    """Get CPU usage and load averages.
    
    Returns:
        CPU usage details
    """
    try:
        # Get CPU info
        cpu_result = subprocess.run(
            ["nproc"],
            capture_output=True,
            text=True,
            timeout=5
        )
        # Get load average
        load_result = subprocess.run(
            ["cat", "/proc/loadavg"],
            capture_output=True,
            text=True,
            timeout=5
        )
        result = f"CPU Cores: {cpu_result.stdout.strip()}\nLoad Average:\n{load_result.stdout}"
        return result
    except Exception as e:
        return f"Error: {str(e)}"


async def get_top_processes(count: int = 5) -> str:
    """Get top CPU consuming processes.
    
    Args:
        count: Number of top processes to return (default: 5)
    
    Returns:
        Top processes by CPU usage
    """
    try:
        result = subprocess.run(
            ["ps", "aux", "--sort=-%cpu"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            lines = result.stdout.split("\n")
            header = lines[0]
            top_processes = "\n".join(lines[:count+1])
            return f"Top {count} Processes by CPU Usage:\n{top_processes}"
        else:
            return f"Error getting processes: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def check_service_status(service: str) -> str:
    """Check the status of a systemd service.
    
    Args:
        service: Service name (e.g., nginx, mysql, docker)
    
    Returns:
        Service status
    """
    try:
        result = subprocess.run(
            ["systemctl", "status", service],
            capture_output=True,
            text=True,
            timeout=5
        )
        return f"Service '{service}' Status:\n{result.stdout}\n{result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def get_network_info() -> str:
    """Get network interface information.
    
    Returns:
        Network configuration details
    """
    try:
        result = subprocess.run(
            ["ip", "addr"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Network Information:\n{result.stdout}"
        else:
            return f"Error getting network info: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def check_open_ports() -> str:
    """Check open ports and listening services.
    
    Returns:
        Open ports and services
    """
    try:
        result = subprocess.run(
            ["ss", "-tlnp"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Open Ports and Listening Services:\n{result.stdout}"
        else:
            return f"Error getting open ports: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def get_installed_packages_count() -> str:
    """Get count of installed packages (works with apt, yum, etc).
    
    Returns:
        Count of installed packages
    """
    try:
        # Try apt first (Debian/Ubuntu)
        result = subprocess.run(
            ["dpkg", "-l"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            count = len([l for l in result.stdout.split("\n") if l.startswith("ii")])
            return f"Installed Packages: {count}"
        else:
            # Try rpm (RedHat/CentOS)
            result = subprocess.run(
                ["rpm", "-qa"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                count = len(result.stdout.split("\n")) - 1
                return f"Installed Packages: {count}"
            else:
                return "Could not determine installed packages"
    except Exception as e:
        return f"Error: {str(e)}"


async def check_disk_inode_usage(path: str = "/") -> str:
    """Check inode usage for a file system.
    
    Args:
        path: File system path to check (default: /)
    
    Returns:
        Inode usage details
    """
    try:
        result = subprocess.run(
            ["df", "-i", path],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Inode Usage for {path}:\n{result.stdout}"
        else:
            return f"Error getting inode usage: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def get_systemd_failed_units() -> str:
    """Get list of failed systemd units.
    
    Returns:
        Failed systemd units
    """
    try:
        result = subprocess.run(
            ["systemctl", "list-units", "--failed"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Failed Systemd Units:\n{result.stdout}"
        else:
            return f"Error getting failed units: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


async def check_file_permissions(path: str) -> str:
    """Check permissions for a file or directory.
    
    Args:
        path: File or directory path
    
    Returns:
        File permissions and details
    """
    try:
        result = subprocess.run(
            ["ls", "-ld", path],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return f"Permissions for {path}:\n{result.stdout}"
        else:
            return f"Error: Path not found or error: {result.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"
