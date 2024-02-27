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

## FastGPT接入HTTP请求模块
> 入参：key
>
> 出参：result

![D8%CF86_7CI}LLYUZVETF}M](https://github.com/Vincentdu-cn/SearXNG-API-for-FastGPT/assets/65072410/904ea894-0eb1-4872-8e9a-0190079d8c7f)
