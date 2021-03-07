FROM python:3.9.2-alpine3.13 as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

SHELL ["/bin/ash", "-eo", "pipefail", "-c"]

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.4

RUN apk add --no-cache alpine-sdk=1.0-r0 libffi-dev=3.3-r2 rust=1.47.0-r2 cargo=1.47.0-r2 libressl-dev=3.1.5-r0 musl-dev=1.2.2-r0

RUN pip install "poetry==$POETRY_VERSION"

RUN python -m venv /venv

# This is needed because pkuseg has an undeclared install time dependency for numpy. 
RUN /venv/bin/pip install numpy==1.20.1

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry run pytest
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM base as final

# Make sure gunicorn is on the path
ENV PATH="/venv/bin:${PATH}"

COPY --from=builder /venv /venv
COPY language_service /app/

EXPOSE 8000
CMD ["gunicorn", "LanguageService:app", "--config=gunicorn.conf.py"]
