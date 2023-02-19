# facial-recognition-for-project
## windows
Ha szeretnéd használni a windows FaceRec-et akkot le kell tölteni az opecv-t és be kell rakni a facial-recognition-for-project\local\windows\dependences mappába
és hozzá kell adni a windows rendszer változókhoz
https://www.youtube.com/watch?v=trXs2r6xSnI iit egy videó hozzá
ami it fontos az 1:50-től 3:00-ig van 
az opencv elérési útja más lesz: 
facial-recognition-for-project/local/windows/dependences/opencv/build/x64/vc16/bin/
elötte persze oda kell tenni a projekt mappának az elérési útját pl:
C:/user/desktop/
https://github.com/opencv/opencv/releases/tag/4.7.0

## linux
Linux használatához telepíteni kell az OpneCV-t amihez itt egy tutorial:
https://www.geeksforgeeks.org/how-to-install-opencv-in-c-on-linux/


``` bash
git clone https://github.com/andris1177/facial-recognition-for-project.git
cd  facial-recognition-for-project/local/linux
mkdir build
cd build
cmake ../
make
```

futtatás
``` bas
./main
```
asd
test2