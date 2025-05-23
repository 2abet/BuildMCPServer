# Import depdendencies
from mcp.server.fastmcp import FastMCP
import json
import requests
from typing import List
import logging

# Server created
mcp = FastMCP("churnandburn")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="mcp_serve.log", 
)


# Create the tool
@mcp.tool()
def PredictChurn(data: List[dict]) -> str:
    """This tool predicts whether an employee will churn or not, pass through the input as a list of samples.
    Args:
        data: employee attributes which are used for inference. Example payload

        [{
        'YearsAtCompany':10,
        'EmployeeSatisfaction':0.99,
        'Position':'Non-Manager',
        'Salary:5.0
        }]

    Returns:
        str: 1=churn or 0 = no churn"""

    payload = data[0]
    response = requests.post(
        "http://127.0.0.1:8000",
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        data=json.dumps(payload),
    )

    return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")
