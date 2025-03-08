from bs4 import BeautifulSoup
import requests
# from googletrans import Translator
from translate import Translator

translator = Translator(to_lang="ru")

#
# translator = Translator()

def get_english_words():
    url = "https://randomword.com/"

    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()


        return{
            "english_word": english_words,
            "word_definition": word_definition
        }

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def word_game():
    print("Добро пожаловать в игру")

    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")
        translated = translator.translate(word_definition)

        print(f"Значение слова - {translated}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        play_again = input("Хотите сыграть еще раз? y/n ")
        if play_again != "y":
            print("Спасибо за игру!")
            break


word_game()