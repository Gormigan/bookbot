def word_counter(text):
    words = text.split()
    count = 0
    for i in words:
        count += 1
    return count

def char_counter(text):
    char_dict = {}
    char_list = list(text.lower())
    for i in char_list:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    return char_dict

def sort_chars(char_dict):
    dict_list = []
    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        dict_list.append(char_info)
    
    def sort_on(dict_item):
        return dict_item["count"]
    
    dict_list.sort(reverse=True, key=sort_on)

    return dict_list
    