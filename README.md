# Program generujący HTML przy użyciu OpenAI

Program napisany w języku Python, który przetwarza plik tekstowy zawierający artykuł, wysyła go do API OpenAI w celu przekształcenia, a następnie zapisuje go w formie pliku HTML
(zawiera poprawnie zorganizowaną treść, miejsca na obrazy oraz opisy w atrybutach alt).

## Funkcje programu:

1. Łączy się z API OpenAI za pomocą biblioteki **openai**
2. Odczytuje treść artykułu z pliku tekstowego _artykul.txt_
3. Przekształca treść na ustrukturyzowany kod HTML, który zawiera:
   + tagi nagłówków, akapitów i innych elementów
   + tagi _<img>_ z _src="image_placeholder.jpg"_ i odpowiednimi artybutami _alt_
   + podpisy pod obrazami
4. Zapisuje wygenerowaną treść w pliku _artykul.html_

## Wymagania:
+ Python 3.8+
+ biblioteka OpenAI ('openai')

## Instalacja i użycie

Po utworzeniu projektu i środowiska wirtualnego należy zainstalować dodatkowo bibliotekę OpenAI:
```
pip install openai
```
## Skonfigurowaanie środowiska
Dla zmiennej `api_key` należy wprowadzić klucz API OpenAI.

Należy upewnić się że plik wejściowy z artykułem w formacie tekstowym `artykul.txt` znajduje się w katalogu głównym projektu.

## Uruchomienie programu
Program uruchamiany jest poprzez wpisanie w terminalu polecenia
```
python app.py
```
Poprawne działanie programu zakończy się komunikatem **_Plik HTML zapisano w: artykul.html_** oraz pojawieniem się pliku w folderze głównym projektu.
