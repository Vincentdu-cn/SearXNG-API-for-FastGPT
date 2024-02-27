FROM python:3.11-alpine

WORKDIR /app

ENV SEARXNG_API="http://192.168.199.110:22222/search"

ADD ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install fastapi pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install uvicorn pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install requests pip -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . /app

EXPOSE 10000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
