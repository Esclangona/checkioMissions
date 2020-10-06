def popular_words(text: str, words: list) -> dict:
    text = " ".join(text.splitlines()).lower().split(" ")
    count_dict = {}
    
    for word in words:
        count_dict[word] = text.count(word)
        
    return count_dict
        
