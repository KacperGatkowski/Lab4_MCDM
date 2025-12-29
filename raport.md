# Lab 4 – Wprowadzenie do biblioteki pymcdm

## Cel zadania
Celem laboratorium było zapoznanie się z biblioteką **pymcdm** oraz
zastosowanie metod wielokryterialnego podejmowania decyzji (MCDM),
w szczególności **TOPSIS** i **SPOTIS**, do wyznaczenia rankingu alternatyw.

## Dane decyzyjne
Rozważono cztery alternatywy decyzyjne opisane czterema kryteriami:
- C1 – koszt (minimalizacja)
- C2 – zysk (maksymalizacja)
- C3 – ryzyko (minimalizacja)
- C4 – czas realizacji (minimalizacja)

Zastosowano wektor wag:  
**[0.35, 0.30, 0.20, 0.15]**

## Metody
W analizie wykorzystano:
- **TOPSIS** – metoda oparta o odległość od rozwiązania idealnego
- **SPOTIS** – metoda bazująca na odległości od punktu referencyjnego

Dane zostały znormalizowane metodą min–max.

## Wyniki
Obie metody wygenerowały ranking alternatyw.
Najlepsza alternatywa według:
- **TOPSIS**: A4
- **SPOTIS**: A4

## Wnioski
Uzyskane rankingi są zgodne – obie metody wskazały tę samą alternatywę
jako najlepszą. Oznacza to, że rozwiązanie jest stabilne i odporne
na wybór metody decyzyjnej. Alternatywa A3 charakteryzuje się dobrym
balansem pomiędzy kosztem, zyskiem i ryzykiem.
