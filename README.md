# facial-recognition-for-project
## windows
Ha szeretnéd használni a windows FaceRec-et akkot le kell tölteni az opecv-t és be kell rakni a facial-recognition-for-project\local\windows\dependences mappába
és hozzá kell adni a windows rendszer változókhoz
https://www.youtube.com/watch?v=trXs2r6xSnI iit egx videó hozzá
ami iit fontos az 1:50-től 3:000 ig van 
az opencv elérési útja más lesz: 
facial-recognition-for-project/local/windows/dependences/opencv/build/x64/vc16/bin/
elötte persze oda kell tenni a projekt mappának az elérési útját pl:
C:/user/desktop/
https://github.com/opencv/opencv/releases/tag/4.7.0

## linux
Linux használatához telepíteni kell az OpneCV-t amihez itt egy tutorial:
https://www.geeksforgeeks.org/how-to-install-opencv-in-c-on-linux/

utánna futtatni kell a cmak-et
``` bash
cmake .
```

``` bash 
make
```

``` bash
./main
```