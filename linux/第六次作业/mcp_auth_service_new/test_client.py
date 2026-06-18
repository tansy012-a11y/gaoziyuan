import subprocess
import json
import time

proc = subprocess.Popen(
    ["python", "mcp_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

def send(req):
    proc.stdin.write(json.dumps(req) + "\n")
    proc.stdin.flush()
    return json.loads(proc.stdout.readline())

# 1 初始化
print(send({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize"
}))

# 2 tools list
print(send({
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list"
}))

# 3 获取 token
resp = send({
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {"name": "get_token", "arguments": {}}
})

print(resp)

token = resp["result"]["content"][0]["text"].split("Token: ")[1]

# 4 错误 token
print(send({
    "jsonrpc": "2.0",
    "id": 4,
    "method": "tools/call",
    "params": {
        "name": "get_server_time",
        "arguments": {"token": "wrong"}
    }
}))

# 5 正确 token
print(send({
    "jsonrpc": "2.0",
    "id": 5,
    "method": "tools/call",
    "params": {
        "name": "get_server_time",
        "arguments": {"token": token}
    }
}))

proc.terminate()
time.sleep(0.5)
proc.kill()