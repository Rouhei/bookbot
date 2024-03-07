def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report = format_report("books/frankenstein.txt", get_word_count(file_contents), get_char_count(file_contents))
        print(report)

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

def format_report(filename, wordcount, char_count):
    report = f"--- Begin report on {filename} --- \n{wordcount} words found in the document \n"
    char_list = sort_characters(char_count)
    for i in char_list:
        report += f"The letter '{i["char"]}' was found {i["count"]} times \n"
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
    
    
    

main() 