"""
Assignment 3 – Text Stats
"""

def main(input_text):
    # Placeholder structure – we’ll fill these in.
    output_lines = [
      f"input_text: {input_text}",
      f"UNIQUE_WORDS: {None}",
      f"LONGEST_WORD: {None}",
      f"MOST_COMMON_WORD: {None}",
      f"MOST_COMMON_WORD_COUNT: {None}",
      "LETTER_FREQUENCIES:", # a..z lines will go here
    ]
    
    print("\n".join(output_lines))

if __name__ == "__main__":
    input_text = "Cats and dogs are fun, but cats are definitely funnier than dogs."
    main(input_text)