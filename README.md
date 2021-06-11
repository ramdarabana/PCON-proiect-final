# Step Sequencer
Acest step sequencer se bazeaza pe computer vision pentru a urmari pozitia unor obiecte albe si negre (tokens) in interiorul unei matrici. OpenCV va procesa un flux video live de la o camera web, convertind iamginea in alb si negru pentru a izola pe rand piesele albe si negre. Se va folosi algoritmul de detectare a blob-ului din OpenCV pentru a se putea identifica centrul fiecarei piese asezata in matrice. Piesele albe, respectiv negre, vor fi mapate in doua matrici distincte ce vor fi trimise mai departe catre Max MSP prin OSC.

## Instalare

### Dependente
- OpenCV
- Numpy
- Max MSP
- OSC (

### IP Webcam
Am optat pentru a folosi telefonul pe post de camera web, prin intermediul acestei aplicatii de pe Play Store.

### step_sequencer.py
Acest cod analizeaza fluxul video, aplica algoritmul de detectie a blobului pentru a identifica piesele de culoare alba si neagra si mapeaza locatiile pieselor in interiorul unei matrici 8x8.

### step_sequencer.maxpat
Acest patch primeste doua tipuri de mesaje OSC, cu locatiile pieselor albe si negre, se vor updata continuu cu sunetele generate de fiecare pozitie ocupata in matrice (piesele albe genereaza cate o melodie pentru primele patru coloane si un drone pentru urmatoarele patru coloane, iar piesele negre genereaza cate un sunet de percutie diferit pentru fiecare coloana, cu posibilitatea de a genera ).


## Utilizare
Este necesara o camera web (telefon) centrata deasupra matricei de piese. Se va rula scriptul python stream_script.py care va cere incadrarea matricei intre patru margini apoi pornirea streamului. Apoi se va rula patch-ul.

## Istoric

(13.05) Documentarea privind alegerea unui algoritm de detectie cat mai eficient (blob_detection.py), realizarea conexiunii cu o camera web (android_cam.py).

(3.06) ...

(X.06) ...

## (Link-uri)
