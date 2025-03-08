def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_char_count(text):
    char_dict = {}
    for word in text.lower():
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict
    
    for key, value in char_dict.items():
        print(f"'{key}': {value}")

def sort_dict(dict):
    dict_list = []
    for key, value in dict.items():
        pair = {"char": key, "count": value}
        dict_list.append(pair)
    new_list = sorted(dict_list, key=lambda d: d["count"], reverse=True)
    return new_list
    