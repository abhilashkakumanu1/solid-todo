FROM python:3.10
RUN mkdir /usr/code
WORKDIR /usr/code
# Install poetry:
RUN pip install poetry
# Copy in the config files:
COPY pyproject.toml poetry.lock ./
# No need for virtual env inside docker
RUN poetry config virtualenvs.create false
# Install dependencies (including dev dependencies):
RUN poetry install
# Copy in everything else
COPY . .
# Entrypoint
CMD ["python", "src/server.py"]
