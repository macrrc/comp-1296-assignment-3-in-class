"""
Assignment 3 – Text Stats
"""

def clean_and_tokenize(input_text):
    # clean and tokenize text
    lowercase_text = input_text.lower()
    # replace punctuation with spaces
    punctuation_marks = ",.;:!?\"()-"
    cleaned_characters = []
    # loop through the lowered text
    # check if the char is in punctuation marks
    
    for char in lowercase_text:
      if char in punctuation_marks:
        cleaned_characters.append(" ")
      else:
        cleaned_characters.append(char)
    
    
    cleaned_text = "".join(cleaned_characters)
    return cleaned_text.split()
  
def get_unique_word_count(words):
    ...

def get_longest_word(words):
    ...

def get_most_common_word(words):
    ...

def get_letter_frequencies(text):
    ...
    
def main(input_text):

    words = clean_and_tokenize(input_text)
    
    print(words)
    # Placeholder structure – we’ll fill these in.
    output_lines = [
      f"INPUT_TEXT: {input_text}",
      f"UNIQUE_WORDS: {None}",
      f"LONGEST_WORD: {None}",
      f"MOST_COMMON_WORD: {None}",
      f"MOST_COMMON_WORD_COUNT: {None}",
      "LETTER_FREQUENCIES:", # a..z lines will go here
    ]
    
    # print("\n".join(output_lines))

if __name__ == "__main__":
    input_text = "Cats and dogs are fun, but cats are definitely funnier than dogs."
    main(input_text)