FROM python:3.8
LABEL author='Surya Bandopadhyay'

WORKDIR /app

# Copy our codebase into the container
COPY . .

# Ops Parameters
ENV WORKERS=2
ENV PORT=80
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.1.4

# Setup cron
ADD crontab /etc/cron.d/updatedb-cron
RUN chmod 0644 /etc/cron.d/updatedb-cron
RUN touch /var/log/cron.log
RUN apt-get update
RUN apt-get -y install cron

# Environment
RUN chmod +x ./docker-entrypoint.sh
RUN apt-get update
RUN apt-get install -y bash vim postgresql-client
RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION" && \
    poetry install

EXPOSE ${PORT}

CMD ./docker-entrypoint.sh
