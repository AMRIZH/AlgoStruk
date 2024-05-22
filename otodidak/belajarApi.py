import requests

def translate(text, source_lang, target_lang):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    if response.status_code == 200:
        translation = response.json()["data"]["translations"][0]["translatedText"]
        return translation
    else:
        return "Error: " + str(response.status_code)

# Example usage
text = "Hello, how are you?"
source_lang = "en"
target_lang = "fr"

translated_text = translate(text, source_lang, target_lang)
print(f"Original text: {text}")
print(f"Translated text: {translated_text}")