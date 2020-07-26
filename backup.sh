#!/bin/bash

backup () 
{
sudo systemctl stop findface-security
sudo -u postgres pg_dump ffsecurity > ffsecurity_postgres_backup.sql

tar -cvf bkp.tar /var/lib/ffsecurity/uploads/

TNT=$(ls /etc/tarantool/instances.enabled/ | wc -l)
for i in $(seq 1 $TNT); do sudo systemctl stop tarantool@shard-00$i.service ; done

tar rvf bkp.tar /opt/ntech/var/lib/tarantool/
tar rvf bkp.tar ffsecurity_postgres_backup.sql
gzip -9 bkp.tar
exit 0
}


restore () 
{
TNT=$(ls /etc/tarantool/instances.enabled/ | wc -l)
for i in $(seq 1 $TNT); do sudo systemctl stop tarantool@shard-00$i.service ; done

sudo tar -zxvf bkp.tar.gz -C / opt/
sudo tar -zxvf bkp.tar.gz -C / var/
sudo tar -zxvf bkp.tar.gz -C . ffsecurity_postgres_backup.sql
sudo systemctl stop findface-security

sudo -u postgres psql -c "drop database ffsecurity;"
sudo -u postgres psql -c "CREATE DATABASE ffsecurity WITH OWNER ntech ENCODING 'UTF-8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE template0;"
sudo -u postgres psql -d ffsecurity -f ffsecurity_postgres_backup.sql

for i in $(seq 1 $TNT); do sudo systemctl start tarantool@shard-00$i.service ; done
sudo systemctl start findface-security
exit 0
}


while [ -n "$1" ]
do
case "$1" in
-backup) backup;;
-restore) restore;;
*) echo "Unknown param. Use -backup or -restore";;
esac
shift
done
