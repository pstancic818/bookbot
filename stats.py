def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def sort_character_count(count_dict):
    new_dict = []
    for k,v in count_dict.items():
        new_dict.append({"char": k, "count": v})
    new_dict.sort(reverse=True, key=lambda x: x['count'])
    return new_dict

def get_character_count(text):
    count_dict = {}
    for char in text:
        if (char.lower() not in count_dict):
            count_dict[char.lower()] = 1
        else:
            count_dict[char.lower()] += 1
    return count_dict
