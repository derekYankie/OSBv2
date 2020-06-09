ARG SENTRY_VERSION=latest
FROM sentry:$SENTRY_VERSION

RUN apt update
RUN apt -y install telnet vim wget procps

RUN apt -y install exim4
ADD exim.conf /etc/exim4/update-exim4.conf.conf
RUN update-exim4.conf
RUN service exim4 restart

RUN mkdir -p /usr/share/man/man1
RUN mkdir -p /usr/share/man/man7

RUN apt -y install postgresql-9.6 postgresql-client-9.6 postgresql-contrib-9.6
RUN apt -y install redis-server

ADD sentrywrapper.sh ./sentrywrapper.sh
RUN chmod +x ./sentrywrapper.sh

ENV SENTRY_REDIS_HOST=localhost
ENV SENTRY_REDIS_PORT=6379
ENV SENTRY_POSTGRES_HOST=localhost
ENV SENTRY_POSTGRES_PORT=5432
ENV SENTRY_DB_NAME=sentry
ENV SENTRY_DB_USER=sentry
ENV SENTRY_DB_PASSWORD=secret
ENV SENTRY_EMAIL_HOST=127.0.0.1
ENV SENTRY_SERVER_EMAIL=sentry@opensourcebrain.org

ENTRYPOINT ["./sentrywrapper.sh", "run", "web"]
