# Step Sequencer
Acest step sequencer se bazeaza pe computer vision pentru a urmari pozitia unor obiecte albe si negre (tokens) in interiorul unei matrici. OpenCV va procesa un flux video live de la o camera web, convertind iamginea in alb si negru pentru a izola pe rand piesele albe si negre. Se va folosi algoritmul de detectare a blob-ului din OpenCV pentru a se putea identifica centrul fiecarei piese asezata in matrice. Piesele albe, respectiv negre, vor fi mapate in doua matrici distincte ce vor fi trimise mai departe catre Max MSP prin OSC.

## Instalare

### Dependente
- OpenCV
- Numpy
- Max MSP
- OSC

### IP Webcam
Am optat pentru a folosi telefonul pe post de camera web, prin intermediul acestei aplicatii de pe Play Store.

### WIP
### stream_script.py
Acest cod va analiza flux video, va mapa locatiile pieselor in doua matrici.

### step_sequencer.maxpat
Acest patch va primi mesage OSC care se va updata continuu cu sunetul generat de fiecare pozitie ocupata in matrice.


## Utilizare
Este necesara o camera web (telefon) centrata deasupra matricei de piese. Se va rula scriptul python stream_script.py care va cere incadrarea matricei intre patru margini apoi pornirea streamului. Apoi se va rula patch-ul.

## Istoric

(13.05) Formularea unui plan cat mai concret, documentarea privind alegerea unui algoritm de detectie cat mai eficient (blob_detection.py), realizarea conexiunii cu o camera web (android_cam.py).

(3.06) ...

(X.06) ...

## (Link-uri)
https://learnopencv.com/blob-detection-using-opencv-python-c/
