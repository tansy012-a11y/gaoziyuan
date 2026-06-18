FROM docker.m.daocloud.io/library/python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY server.py .

CMD ["python", "server.py"]