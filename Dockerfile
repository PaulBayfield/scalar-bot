FROM python:3.12.10-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . ./ScalarBot

WORKDIR /ScalarBot

RUN uv sync --frozen

CMD ["uv", "run", "__main__.py"]
