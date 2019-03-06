import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(file_given_way=str(input("Путь к файлу: ")), file_new=str(input("Сохранить в: ")), given_lang=str(input("Язык файла:")), trans_lang='ru'):
    with open(file_given_way) as text_file:
        text = text_file.read()
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(given_lang, trans_lang),
    }
    response = requests.post(URL, params=params)
    json_ = response.json()
    new_text = json_.get("text")
    with open(file_new, 'w') as new_file:
        new_file.write(new_text[0])
        print("Сохранено в", new_file)
print(translate_it())