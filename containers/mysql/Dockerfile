FROM mysql:8.0

COPY /conf.d/my.cnf /etc/mysql/conf.d/my.cnf

COPY init.sql /docker-entrypoint-initdb.d
