from better_profanity import profanity

def is_bad_word(text):
    profanity.load_censor_words()
    return profanity.contains_profanity(text)
