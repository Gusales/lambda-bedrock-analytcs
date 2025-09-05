from typing import Dict, Optional, Any

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    return { "message": "Hello From Lambda Bedrock Analytcs" }