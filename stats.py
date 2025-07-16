
def get_num_words(content):
    words = content.split()
    return len(words)

def get_num_char(content):
    num_char = {}
    for char in content.lower():
        if char in num_char:
            num_char[char] += 1
        else:
            num_char[char] = 1
    return num_char

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    dict_list = []
    for key in dict:
        if key.isalpha():
            dict_list.append({"char":key, "num": dict[key]})
    dict_list.sort(reverse=True, key=sort_on)    
    return dict_list
