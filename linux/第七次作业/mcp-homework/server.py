from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import asyncio
import json

app = Server("my-mcp-server")


@app.list_tools()
async def list_tools():
    return [
        Tool(
            name="say_hello",
            description="向指定的人打招呼",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "人的名字"
                    }
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="calculate",
            description="执行简单的数学计算",
            inputSchema={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，比如 1+2*3"
                    }
                },
                "required": ["expression"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "say_hello":
        person = arguments.get("name", "世界")
        return [TextContent(type="text", text=f"你好，{person}！我是运行在 Docker 里的 MCP 服务！")]

    elif name == "calculate":
        expr = arguments.get("expression", "")
        try:
            result = eval(expr)
            return [TextContent(type="text", text=f"{expr} = {result}")]
        except Exception as e:
            return [TextContent(type="text", text=f"计算错误：{str(e)}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())