import re
# function for extarct words beginning with 'me'
def extract_me_words(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Find all words starting with 'me' using regex
        pattern = r'\bme\w*'
        me_words = re.findall(pattern, text, re.IGNORECASE)

        # Convert the list to a tuple
        me_words_tuple = tuple(me_words)

        return me_words_tuple

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return ()
  
# testcase
file_path = 'C:\Amri\KULIAH_UMS\Semester4\labASD\modul7\indonesia.txt'
me_words = extract_me_words(file_path)
print(me_words)

#========================================================================
def extract_di_words(file_path):
    try:
        # Buka file dan baca isinya
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Cari semua kata yang diawali dengan 'di' menggunakan regex
        pattern = r'\bdi\w+'
        di_words = re.findall(pattern, text, re.IGNORECASE)

        # Konversi list menjadi tuple
        di_words_tuple = tuple(di_words)

        return di_words_tuple

    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    return ()

file_path = 'C:\Amri\KULIAH_UMS\Semester4\labASD\modul7\indonesia.txt'
di_words = extract_di_words(file_path)
print(di_words)

#==============================================================================
import re

def extract_di_tempat(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Find all occurrences of 'di' followed by a word
        pattern = r'\bdi\s+(\w+)'
        di_words = re.findall(pattern, text)

        return di_words

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return []