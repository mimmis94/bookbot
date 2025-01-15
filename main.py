#main fuction to read the file contents 
def main():
    with open("/Users/mariustissen/workspace/github.com/mimmis94/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents

#function to count the number of words in a file 

def word_split(file_contents):
    split = file_contents.split()
    words = 0 
    for word in split:
        words += 1
    return words

# function to count the occurrences of each character 

def count_characters(file_contents):
    char_lower = file_contents.lower() # convert zu lowercase
    char_count = {}
    for char in char_lower:
        if char.isalpha():              #only count alphabetic characters 
            char_count[char] = char_count.get(char , 0) +1 #increment count 
    return char_count


#function to sort characters alphabetically: 
def sort_characters(char_count):
  sort_letters = (sorted(char_count.items(), key=lambda x: x[1], reverse = True)) #sort by values 
  return sort_letters

# main programm execution

if __name__ == "__main__":

    #step 1: read file contents
    file_contents = main()

    #step 2: count and display the count of words: 
    total_words = word_split(file_contents)

    #step 3: count and display character occurances: 
    char_count = count_characters(file_contents)

    #step 4: sort and display chcharacter occurence alphabetically 
    sorted_characters = sort_characters(char_count)
    
    #generate and print the report: 
    print(f"---Begin report of {("/books/frankenstein.txt")} ---")
    print(f"{total_words} words found in the document\n")

    for char, count in sorted_characters:
        print(f"'{char}' character was found {count} times")
    print("--- End report ---")


