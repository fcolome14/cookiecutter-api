# Use the base image from the devcontainer
FROM python:3.11-bullseye

ARG DEBIAN_FRONTEND=noninteractive

ENV container docker
ENV WORKDIR /app

USER root

# Set a working directory
WORKDIR ${WORKDIR}

# Install OS dependencies
RUN apt-get update\
    && apt-get install\
        build-essential\
        curl\
        git-all\
        htop\
        nano\
        wget\
        zsh\
        ca-certificates\
        -y --no-install-recommends\
    && apt-get upgrade -y\
    && apt-get full-upgrade -y\
    && apt-get autoremove -y\
    && apt-get autoclean -y\
    && apt-get clean\
    && rm -rf /var/lib/apt/lists/*

# Install Poetry + Update pip
RUN pip install --upgrade --no-cache-dir wheel pip poetry==1.8.0

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev --no-root

WORKDIR ${WORKDIR}

COPY . ${WORKDIR}

RUN poetry install --no-dev

# When running the container it will: make run
CMD ["make", "run"]
