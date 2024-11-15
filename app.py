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
