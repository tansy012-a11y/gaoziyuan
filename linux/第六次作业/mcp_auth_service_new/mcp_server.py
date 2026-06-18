#!/usr/bin/env python3
import sys
import json
import secrets
import time

FIXED_TOKEN = "my_secret_token_2026"

TOKEN = FIXED_TOKEN if FIXED_TOKEN else secrets.token_hex(16)

def send_response(response):
    print(json.dumps(response), flush=True)

def handle_initialize(req_id):
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "protocolVersion": "0.1.0",
            "capabilities": {"tools": {}},
            "serverInfo": {
                "name": "auth-mcp-server",
                "version": "1.0.0"
            }
        }
    }

def handle_tools_list(req_id):
    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "result": {
            "tools": [
                {
                    "name": "get_token",
                    "description": "获取 token",
                    "inputSchema": {"type": "object", "properties": {}}
                },
                {
                    "name": "get_server_time",
                    "description": "获取服务器时间",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "token": {"type": "string"}
                        },
                        "required": ["token"]
                    }
                }
            ]
        }
    }

def handle_tools_call(req_id, params):
    name = params.get("name")
    args = params.get("arguments", {})

    if name == "get_token":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{
                    "type": "text",
                    "text": f"Token: {TOKEN}"
                }]
            }
        }

    if name == "get_server_time":
        token = args.get("token")

        if token != TOKEN:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32001, "message": "token 无效"}
            }

        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{
                    "type": "text",
                    "text": f"服务器时间：{time.strftime('%Y-%m-%d %H:%M:%S')}"
                }]
            }
        }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": "未知工具"}
    }

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break

        try:
            req = json.loads(line)
        except:
            continue

        req_id = req.get("id")
        method = req.get("method")

        if method == "initialize":
            resp = handle_initialize(req_id)
        elif method == "tools/list":
            resp = handle_tools_list(req_id)
        elif method == "tools/call":
            resp = handle_tools_call(req_id, req.get("params", {}))
        else:
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": "方法未实现"}
            }

        send_response(resp)

if __name__ == "__main__":
    main()