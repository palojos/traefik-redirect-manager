FROM python:3.10-bullseye

ARG POETRY_VERSION=1.2.0

ENV POETRY_HOME=/opt/poetry \
    POETRY_VERSION=${POETRY_VERSION}

# Install poetry
RUN mkdir -p /opt/poetry \
    && curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to path
ENV PATH=${PATH}:${POETRY_HOME}/bin

# Smoke test poetry
RUN poetry --version

# User args
ARG DEV_USER=developer
ARG DEV_GROUP=developer
ARG DEV_UID=1000
ARG DEV_GID=1000

# Create development environment
RUN groupadd --gid ${DEV_GID} ${DEV_GROUP} \
    && useradd --uid ${DEV_UID} --gid ${DEV_GID} -m -s /bin/bash -d /dev_home ${DEV_USER} \
    && mkdir -p /workspace \
    && mkdir -p /dev_home \
    && chown -R ${DEV_UID}:${DEV_GID} /workspace \
    && chown -R ${DEV_UID}:${DEV_GID} /dev_home

WORKDIR /workspace

USER ${DEV_USER}

CMD ["sleep", "infinity"]