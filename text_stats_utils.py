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
    return len(set(words))


def get_longest_word(words):
    return max(words, key=len)

def get_most_common_word(words):
    word_counts = {}
    # loop over words
    # append the word and the count to the word_counts dict
    
    for word in words:
      if word not in word_counts:
        word_counts[word] = 1
      else:
        word_counts[word] += 1
    
    most_common_word = None
    highest_count = 0
    
    # Part 2
    # loop through the word_counts
    for word, count in word_counts.items():
      if count > highest_count:
        most_common_word = word
        highest_count = count
        
    return {"word": most_common_word, "count": highest_count}