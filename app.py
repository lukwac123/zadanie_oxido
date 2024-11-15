import openai
import os


# Funkcja służąca do wczytywania treści artykułu z pliku.
def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
