FROM python:3.11-alpine

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install fastapi pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install uvicorn pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install requests pip -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . /app

EXPOSE 10000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
