def get_word_count(text):
    word_count = len(text.split())
    print(f"{word_count} words found in the document")

def get_char_count(text):
    char_dict = {}
    for word in text.lower():
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    
    for key, value in char_dict.items():
        print(f"'{key}': {value}")