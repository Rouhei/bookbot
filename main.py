def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(format_report("frankenstein.txt", get_word_count(file_contents), get_char_count(file_contents), get_common_words(file_contents)))
        
        

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(input_text):
    text = input_text.lower()
    lc = {}
    for char in text:
        if char in lc:
            lc[char] += 1
        else:
            lc[char] = 1
    return lc

def format_report(filename, wordcount, char_count, common_word_list):
    report = f"--- Begin report on {filename} --- \n{wordcount} words found in the document \n\n"
    char_list = sort_characters(char_count)
    for i in char_list:
        report += f"The letter '{i["char"]}' was found {i["count"]} times \n" 
    report += "\nThe ten most common words within the text are:\n"
    for i in common_word_list:
        report += f"The word '{i["word"]}' - {i["count"]} occurences \n"
    return report

def sort_characters(char_count):
    char_list = []
    for c in char_count:
        if c.isalpha():
            c_dict ={}
            c_dict["char"] = c
            c_dict["count"] = char_count[c]
            char_list.append(c_dict)
    char_list.sort(reverse=True, key=dic_sort)
    return char_list

def dic_sort(dict):
    return dict["count"]

def get_common_words(input_text):
    text = input_text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    words = text.split()
    dull_words = ["the",  "a", "on", "in", "and", "i", "of", "to", "my", "was", "that", "had", "but", "with", "he", "which", "his", "me", "as", "their", "been", "would"
        "not", "by", "you", "for", "it", "her", "she", "from", "this", "have", "be", "at", "when", "is", "were", "your", "an", "they", "so", "could", "one", "will", "if",
        "all", "not", "would", "or", "we", "are", "no", "who", "should", "more", "these", "me", "him", "some", "yet", "now", "before", "our", "upon", "into", "its", 
        "what", "only", "did", "am", "every",  "shall", "first", "do", "own", "towards", "even",  "those",  "than", "might", "myself", "may", "saw", "can", "most", "such",
        "then", "whom", "how", "them", "being", "where", "said", "any", "again"]
    word_dict ={}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        elif word not in dull_words:
            word_dict[word] = 1
    common_words = sort_words(word_dict)
    return common_words    
    
def sort_words(word_dict):
    word_list = []
    for w in word_dict:
        w_dict ={}
        w_dict["word"] = w
        w_dict["count"] = word_dict[w]
        word_list.append(w_dict)
    word_list.sort(reverse=True, key=dic_sort)
    return word_list[:10:]
    
    

main() 