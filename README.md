# Step Sequencer
Acest step sequencer se bazeaza pe computer vision pentru a urmari pozitia unor obiecte albe si negre (tokens) in interiorul unei matrici patratice de dimensiune variabila (aici este de 8x8). OpenCV va procesa un flux video live de la o camera web, convertind iamginea in alb si negru pentru a izola pe rand piesele albe si negre. Se va folosi algoritmul de detectare a blob-ului din OpenCV pentru a se putea identifica centrul fiecarei piese asezata in matrice. Piesele albe, respectiv negre, vor fi mapate in doua matrici distincte ce vor fi trimise mai departe catre Max MSP prin OSC. Patch-ul de Max va genera 3 tipuri de sunete, melodie si drone pentru piese albe si percutie pentru piese negre, in functie de asezarea acestor piese.

## Instalare

### Dependente
- OpenCV
- Numpy
- Max MSP
- OSC (pythonosc)

### IP Webcam
Am optat pentru a folosi telefonul pe post de camera web, prin intermediul acestei aplicatii de pe Play Store.

### step_sequencer.py
Acest cod analizeaza fluxul video, aplica algoritmul de detectie a blobului pentru a identifica piesele de culoare alba si neagra si mapeaza locatiile pieselor in interiorul unei matrici 8x8.

### step_sequencer.maxpat
Acest patch primeste doua tipuri de mesaje OSC, cu locatiile pieselor albe si negre, care vor updata continuu sunetele generate de fiecare pozitie ocupata in matrice (piesele albe genereaza cate o melodie pentru primele patru coloane si un drone pentru urmatoarele patru coloane, iar piesele negre genereaza cate un sunet de percutie diferit pentru fiecare coloana, cu posibilitatea de a genera acelasi sunet de percutie de mai multe ori daca minim doua piese se afla pe acelasi rand).


## Utilizare
Este necesara o camera web (telefon conectat la Wi-Fi) centrata deasupra matricei de piese si mentinuta fix. Se va rula scriptul python step_sequencer.py unde se va deschide o fereastra 'Output' cu un cadru static al matricei. Se va apasa pe rand fiecare colt al matricei in ordinea urmatoare: stanga sus, stanga jos, dreapta jos, dreapta sus, apoi se apasa orice tasta. Se va deschide o noua fereastra 'Final' unde se va putea urmari plasarea pieselor albe si negre in matrice. Se va rula scriptul Max step_sequencer.maxpat.

! Trebuie avut in vedere ca in scriptul python, link-ul catre stream-ul video sa fie cel din aplicatie, ip-ul de client sa fie cel al retelei locale iar portul sa fie identic cu cel din patch-ul Max.

## Istoric

(13.05) Documentarea privind alegerea unui algoritm de detectie cat mai eficient (blob_detection.py), realizarea conexiunii cu o camera web (android_cam.py).

(3.06) ...

(11.06) 

## (Link-uri)
