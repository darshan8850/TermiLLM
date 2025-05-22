from mcp.server.fastmcp import FastMCP

linux_mcp = FastMCP("Linux")
import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command, shell=True, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr.strip()}")
        return None

@linux_mcp.tool()
def execute_linux_command(command: str) -> str:
    """
    Executes linux command
    """
    ## VERY DANGEROUS!!!!!!
    # run the command and return the command's output
    return run_command(command)

windows_mcp = FastMCP("Windows")

@windows_mcp.tool()
def execute_windows_command(command: str) -> str:
    """
    Executes windows command
    """
    ## VERY DANGEROUS!!!!!!
    # run the command and return the command's output
    return run_command(command)

mac_mcp = FastMCP("Mac")

@mac_mcp.tool()
def execute_mac_command(command: str) -> str:
    """
    Executes mac command
    """
    ## VERY DANGEROUS!!!!!!
    # run the command and return the command's output
    return run_command(command)


linux_mcp.run(host="0.0.0.0", port=5001,transport="sse")
windows_mcp.run(host="0.0.0.0", port=5002,transport="sse")
mac_mcp.run(host="0.0.0.0", port=5003,transport="sse")