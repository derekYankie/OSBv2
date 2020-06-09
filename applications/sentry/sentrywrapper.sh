#!/bin/bash

set -e

echo "**** S:INI ****"
export SENTRY_SECRET_KEY=$(./entrypoint.sh config generate-secret-key)

chown -R postgres /var/lib/postgresql/9.6/

if [ ! -d "/var/lib/postgresql/9.6/main/base" ]; then
    echo "create new cluster"
    su postgres -c "/usr/lib/postgresql/9.6/bin/initdb -D /var/lib/postgresql/9.6/main"
    /etc/init.d/postgresql start &&\
        su postgres -c "psql --command \"CREATE USER sentry WITH SUPERUSER PASSWORD 'secret';\"" &&\
        su postgres -c "createdb -O $SENTRY_DB_USER $SENTRY_DB_NAME"

    # Adjust PostgreSQL configuration so that remote connections to the
    # database are possible.
    echo "host all  all    127.0.0.1/0  trust" >> /etc/postgresql/9.6/main/pg_hba.conf
    # And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
    echo "listen_addresses='127.0.0.1'" >> /etc/postgresql/9.6/main/postgresql.conf
fi

service postgresql start
service exim4 start
service redis-server start

sleep 10

./entrypoint.sh upgrade --noinput   
./entrypoint.sh createuser --email sentry@opensourcebrain.org --password sentry --superuser --no-input 
echo "**** E:INI ****"

echo "**** S:CEL ****"
nohup ./entrypoint.sh run cron 2>&1 > /var/log/sentrycron.log &
nohup ./entrypoint.sh run worker 2>&1 > /var/log/sentryworker.log &
echo "**** E:CEL ****"

echo "**** S:RUN ****"
./entrypoint.sh $*
echo "**** E:RUN ****"
