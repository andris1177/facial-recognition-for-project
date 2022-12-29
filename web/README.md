# Projekt célca

Ez egy arcfelismerő program és hozzátartozó admin weboldal python-al és opencv-vel

## használata

### windows

Első lépés hogy meg kell nyitni a powershelt rendszergazdaként.
A futtatáshoz elösször engedélyezni kell hogy lehessen futtatni scripteket
```powrshel
Set-ExecutionPolicy RemoteSigned
```

A script futtatása
```powershel
./setup.ps1
```

A server futtatása
```powershel
cd /website
py manage.py runserver
```

### linux
A script futtathatóvá tétele
```bash
chmod +x setup.sh
```

A script futtatása
```bas
./setup.sh
```

A szerver futtatása
```BASH
cd /website
py manage.py runserver
```