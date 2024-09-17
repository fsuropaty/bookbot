def read_book(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents


def word_count(text):
    split_text = text.split()

    return len(split_text)


def char_count(text):
    char_count_dict = {}
    lowercase = text.lower()

    for char in lowercase:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else :
            char_count_dict[char] = 1

    return char_count_dict


def sorter(dict):
    sorted_list = []

    for i in dict:
        if i.isalpha():
            char_dict = {"char": i, "count": dict[i]}
            sorted_list.append(char_dict)

    sorted_list.sort(key=lambda x:x["count"], reverse=True)

    return sorted_list


def print_report(books,word_count,sorted_list):
    print(f"--- Begin report of {books} ---")
    print(f"{word_count} words found in the document\n")

    for i in range(0,len(sorted_list)):
        char = sorted_list[i]["char"]
        count = sorted_list[i]["count"]
        formatted = f"The '{char}' character was found {count} times"
        print(formatted)

    print("--- End report ---")

        
def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    w_count = word_count(text)
    c_count = char_count(text)
    sort = sorter(c_count)
    report = print_report(book_path,w_count,sort)

    return report

main()




