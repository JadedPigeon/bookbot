def word_count(text):
    return len(text.split())

def character_count(text):
    characters = {}
    for c in text.lower():
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters

def sort_on(dict):
    return dict["count"]

def dictionary_sort(dict_to_sort):
    new_dict = []
    for key in dict_to_sort:
        new_dict.append({"character": key, "count": dict_to_sort[key]}) 

    new_dict.sort(reverse=True, key=sort_on)
    return new_dict