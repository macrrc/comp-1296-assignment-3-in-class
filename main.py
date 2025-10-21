"""
Assignment 3 – Text Stats
"""
from text_stats_utils import (
  clean_and_tokenize,
  get_unique_word_count,
  get_longest_word,
  get_most_common_word
)


def get_letter_frequencies(text):
    ...
    
def main(input_text):

    words = clean_and_tokenize(input_text)
    unique_word_count = get_unique_word_count(words)
    longest_word = get_longest_word(words)
    most_common_word = get_most_common_word(words)

    # Placeholder structure – we’ll fill these in.
    output_lines = [
      f"INPUT_TEXT: {input_text}",
      f"UNIQUE_WORDS: {unique_word_count}",
      f"LONGEST_WORD: {longest_word}",
      f"MOST_COMMON_WORD: {most_common_word["word"]}",
      f"MOST_COMMON_WORD_COUNT: {most_common_word["count"]}",
      "LETTER_FREQUENCIES:", # a..z lines will go here
    ]
    
    print("\n".join(output_lines))

if __name__ == "__main__":
    input_text = "Cats and dogs are fun, but cats are definitely funnier than dogs."
    main(input_text)