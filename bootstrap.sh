#!/bin/sh
echo "Installing Python requirements...";
pip install -r requirements.txt;
echo "Setting up database...";
psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='detectweb'" | grep -q 1 || createuser -d detectweb;
createdb -U detectweb -O detectweb detectweb_db;
createdb -U detectweb -O detectweb test_detectweb_db;

echo "Migrating database...";
python detectweb/manage.py migrate;
