# Generator HTML za pomocą OpenAI

Ta aplikacja w Pythonie przetwarza plik tekstowy zawierający artykuł, wysyła go do API OpenAI w celu przekształcenia, a następnie zapisuje wynik w pliku HTML. Wygenerowany HTML zawiera poprawnie zorganizowaną treść, miejsca na obrazy oraz opisy w atrybutach alt.

## Funkcje

- Łączy się z API OpenAI za pomocą biblioteki `openai`.
- Odczytuje treść artykułu z pliku tekstowego (`artykul.txt`).
- Przekształca treść na ustrukturyzowany kod HTML, który zawiera:
  - Tagi do nagłówków, akapitów i innych elementów.
  - Tagi `<img>` z `src="image_placeholder.jpg"` i odpowiednimi atrybutami `alt`.
  - Podpisy pod obrazami.
- Zapisuje wygenerowaną treść w pliku `artykul.html`.

## Wymagania

- Python 3.8+
- Biblioteka OpenAI (`openai`)

## Instalacja i użycie

1. **Zainstaluj wymagane biblioteki**:
   ```bash
   pip install openai

2. **Skonfiguruj środowisko**:
Zastąp TWOJ_KLUCZ_API w skrypcie swoim kluczem API OpenAI.
Upewnij się, że plik artykul.txt znajduje się w katalogu głównym i zawiera artykuł do przetworzenia.

4. **Uruchom aplikację**:
```
bash
python app.py
```

4. **Sprawdź wynik**:
Wygenerowany HTML znajdziesz w pliku artykul.html w katalogu głównym.
