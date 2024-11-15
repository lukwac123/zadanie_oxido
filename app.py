import openai
import os


# Funkcja służąca do wczytywania treści artykułu z pliku.
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Funkcja służąca do zapisania wynikowego kodu w pliku HTML.
def save_html(content, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Funkcja służąca do wysyłania żądania do API OpenAI
def process_article_with_openai(api_key, article_content, prompt):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym asystentem generującym kod HTML."},
            {"role": "user", "content": f"{prompt}\n\n{article_content}"}
        ]
    )
    return response['choices'][0]['message']['content']


# Definicja funkcji głównej programu
def main():
    # Ustawienia
    # Klucz API OpenAI
    api_key = "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"
    # Nazwa pliku z artykułem na wejściu
    input_file = "artykul.txt"
    # Nazwa pliku wynikowego
    output_file = "artykul.html"
    # Treść promptu dla AI
    prompt = ("Przekształć poniższy artykuł na kod HTML. "
              "Użyj odpowiednich tagów HTML, dodaj obrazy w kluczowych miejscach za pomocą tagu "
              "<img src='image_placeholder.jpg'> z odpowiednimi atrybutami alt oraz podpisami pod obrazkami. "
              "Pomiń CSS i JavaScript, uwzględnij jedynie zawartość w obrębie <body>.")

    # Wczytywanie treści artykułu
    article_content = read_article(input_file)

    # Przetwarzanie artykułu za pomocą OpenAI
    try:
        html_content = process_article_with_openai(api_key, article_content, prompt)
        # Zapisywanie wynikowego HTML
        save_html(html_content, output_file)
        print(f"Plik HTML zapisano w: {output_file}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()