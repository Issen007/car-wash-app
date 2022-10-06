# Pulling Python Docker Base Image
FROM python:3-alpine

# Set our Working Directory
WORKDIR /src

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUMBUFFERED 1

# Installing PostgreSQL Client
RUN apk add --update --no-cache postgresql-client

# Install Individual dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc \
  libc-dev \
  linux-headers \
  postgresql-dev \
  libffi-dev \
  bash \
  curl

# Install all dependencies
RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy Project to our source directory
COPY ./src/ /src/

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "webserver.wsgi"]