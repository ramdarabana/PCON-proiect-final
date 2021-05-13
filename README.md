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



## Elemente obligatorii

1. Acest readme completat. Titlu, descriere, mod de utilizare, istoric, link-uri utile.

   Poți include și imagini și chiar [gif-uri animate](https://www.screentogif.com/), sau link-uri către materiale audio/video.
   
   Vezi [aici](https://charlesmartin.com.au/blog/2020/08/09/student-project-repository) mai multe sugestii.

2. [Declarația de originalitate](statement-of-originality.yml) completată. Tot ce nu este inclus acolo va fi considerat 100% contribuție proprie.

    *(formatul este adaptat de [aici](https://gitlab.cecs.anu.edu.au/comp1720/2018/comp1720-2018-major-project/-/blob/master/statement-of-originality.yml). Da, este un pic ironic să refolosim un doc [de altundeva](https://cs.anu.edu.au/courses/comp1720/resources/faq/#how-do-i-fill-out-my-statement-of-originality), dar menționăm sursa deci nu este plagiat!)*

3. Proiectul în sine. Tot codul trebuie să fie prezent, proiectul trebuie să poată rula conform instrucțiunilor din readme. Dacă e nevoie de asset-uri mari (sunete, video etc), [folosește Git LFS](https://git-lfs.github.com/) sau include link de download în instrucțiunile de instalare.

