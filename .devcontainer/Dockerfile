FROM python:3.11

WORKDIR /workspace/sqeleton

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev

COPY . .
