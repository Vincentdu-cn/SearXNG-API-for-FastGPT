# SearXNG-API-for-FastGPT
SearXNG搜索结果优化，只提取url和content内容，通过Fastgpt中HTTP请求模块作为提示词prompt给AI。

## docker build

```bash
git clone https://github.com/Vincentdu-cn/SearXNG-API-for-FastGPT.git
docker build -t search-api .
```

## docker run

```bash
docker run -d -p 10000:10000 --env SEARXNG_API="https://searxng.site/" --name=api search-api
```
