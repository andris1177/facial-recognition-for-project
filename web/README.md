# Használata

windows:
Első lépés hogy meg kell nyitni a powershelt rendszergazdaként.
A futtatáshoz elösször engedélyezni kell hoyg lehessen futtatni scripteket "Set-ExecutionPolicy RemoteSigned"
utánna ./setup.ps1

A server futtatása
cd /website
py manage.py runserver

linux:
chmod +x setup.sh
./setup.sh

cd /website
py manage.py runserver