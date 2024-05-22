import re

def extract_me_words(file_path):
  try:
    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
      text = file.read()

    # Find all words that start with 'me' using regex
    pattern = r'\bme\w*' # \b = word boundary, \w = word character, * = zero or more
    me_words = re.findall(pattern, text, re.IGNORECASE)
    
    # Convert the list to a tuple
    me_words_tuple = tuple(me_words)
    return me_words_tuple
  
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")
  return ()

#===================================
