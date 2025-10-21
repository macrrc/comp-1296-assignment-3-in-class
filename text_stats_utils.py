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