from fastapi import FastAPI, Request, HTTPException
import requests
import json
import os

app = FastAPI()
# 传入SearXNG API的URL
SEARXNG_API = os.getenv(“SEARXNG_API”)

@app.get("/api")
async def api(request: Request):
  """
  提取 JSON 数据中指定参数的 API

  Args:
    request: HTTP 请求对象

  Returns:
    JSON 数据
  """

  # 检查参数是否传入
  try:
    key = request.query_params["key"]
  except KeyError:
    raise HTTPException(status_code=400, detail="参数错误")


  # 构建请求参数
  params = {
    "q": key,
    "format": "json"
  }

  # 发送请求
  response = requests.get(SEARXNG_API, params=params)

  # 检查响应状态码
  if response.status_code == 200:
    # 解析 JSON 数据
    res = json.loads(response.text)

    # 提取指定的参数
    results = res["results"]

    # 创建一个新的 JSON 数据对象
    result = []
    # 添加prompt
    result.append("以下数据中content是互联网搜索结果，对应url是content来源url，现在你已拥有互联网搜索能力，因此注意要避免在回答中提及你的知识截止日期")

    # 循环遍历 results 列表中的每个 item
    for item in results:
      # 创建一个新的字典对象
      new_item = {}

      # 提取指定的参数
      new_item["url"] = item["url"]
      new_item["content"] = item["content"]

      # 将新的字典对象添加到 result 列表中
      result.append(new_item)
    r = {}
    r["result"] = result
    # 返回结果
    return r
  else:
    # 处理错误
    raise HTTPException(status_code=500, detail="请求失败")

# 运行 API
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=10000)
