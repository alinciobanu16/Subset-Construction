Ciobanu Alin-Matei 335CB

Ideea implementarii:
- construiesc lista L in care adaug perechi de forma (stare, lista_cu_stari):
pentru fiecare stare compusa asociez o stare
- initial adaug perechea (0, eps(0)), starea initiala din dfa va fi eps(0) mapat
prin starea 0
- parcurg lista L si o actualizez la fiecare pas
- cat timp mai am elemente in L:
- selectez lista l din L mapata prin starea curenta
- pe fiecare caracter din alfabet vad unde pot ajunge din fiecare stare continuta in l
- construiesc o lista noua l2 care contine starile si inchiderile lor epsilon
care sunt accesibile din starea din l pe caracter
- daca nu exista deja in L, adaug l2 in L atribuindu-i o  noua stare
- construiesc tranzitia in dfa
- trec la urmatoarea stare din L si repet algoritmul

Functii ajutatoare:
- epsilonClosure(delta, state): intoarce un set cu inchiderea epsilon a starii
- onestep(delta, state, c): intoarce un set cu toate starile accesibile din state
pe caracterul c (inclusiv inchiderile epsilon)
- isInList(l, L): verifica daca lista l se gaseste in L
- findStateInL(l, L): intoarce starea asociata listei l in L
- findListInL(state, L): intoarce lista asociata lui state in L
