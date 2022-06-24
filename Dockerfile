FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Poetry
COPY pyproject.toml* /srv/
RUN \
    pip install --upgrade pip && \
    pip install poetry
WORKDIR /srv
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev
# End Poetry

# Set work directory
WORKDIR /app

# Copy project
COPY src/ .

