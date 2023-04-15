# facial-recognition-for-project
## windows
### Csak anacondaval tudtam telepíteni de ott működött. Anaconda letöltése után az anaconda powershell promton belül kell telepíteni a modulokat és futtatni a programot.
``` powershell
conda install -c conda-forge face-recognition
conda install -c conda-forge opencv
git clon https://github.com/andris1177/facial-recognition-for-project.git
cd facial-recognition-for-project/local
python face_rec.py
```

<br>

## linux
### Itt nem volt a telepítéssel semmi baj. Futtatás előtt a web/adminSite/takePicture mappában létre kell hozni egy images mappát, ide fogja az elkészült képeket menteni.
``` bash
git clone https://github.com/andris1177/facial-recognition-for-project.git
cd /facial-recognition-for-project/local
pip install -r requirements.txt
python3 face_rec.py
```
<br>

## Web szerver
### Bármilyen webszerver jó én apache-t használtzam xampon belül, mert van beépített mysql adatbázisa.

<br>

## adatbázis létrehozása
``` sql
CREATE DATABASE users;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password VARCHAR(255) NOT NULL
);
```