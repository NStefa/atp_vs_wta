# Dashboard porównujący rozgrywki ATP i WTA

## Opis projektu

Projekt został zrealizowany w ramach zaliczenia przedmiotu **Modelowanie i wizualizacja danych z wykorzystaniem BI**.  
Moim celem było przygotowanie interaktywnego dashboardu porównującego tenisowe rozgrywki **męskie (ATP)** i **żeńskie (WTA)** w oparciu o dane z lat 1968–2018. Analiza obejmuje m.in. liczbę meczów, kalendarz turniejowy, typy nawierzchni, styl gry i profil zawodników.

Dashboard opiera się na przetworzonych danych źródłowych i został zaprojektowany w oparciu o zasady czytelności, interaktywności i interpretowalności.

## Struktura projektu

- `dashboard_ATP_vs_WTA.pbix` – główny plik z raportem Power BI
- `verify.py` – skrypt w języku Python użyty do **eliminacji konfliktów związanych z różnicami nazewnictwa niektórych turniejów**. 
- `atp_singles.csv`, `wta_singles.csv` – pliki CSV po **wstępnym czyszczeniu i transformacji danych** z wykorzystaniem kodu z pliky `verify.py`

## Zakres analizy

Dashboard obejmuje:

- porównanie liczby meczów, średniego czasu trwania i liczby turniejów
- analizę typów nawierzchni (clay, grass, hard, carpet)
- średni wiek zwycięzców w poszczególnych turniejach
- profil zawodników (wzrost, ręczność, styl serwowania)
- wskaźniki dotyczące stylu gry: liczba asów, błędów serwisowych, ranking zwycięzców

## Narzędzia

- **Power BI**
- **Python (`pandas`, `numpy`)** 
- **Power Query (M)** 
- **DAX** 
- **CSV**

