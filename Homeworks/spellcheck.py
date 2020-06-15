import urllib.request
print("Type text; enter a blank line to end.")
text = input()
stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')
correct_list = []

while len(text) > 1:
    # obtaining list of words from site
    for line in stream:
        text_line = line.decode('utf-8')
        no_newline = text_line.strip()
        row = no_newline
        correct_list.append(row)
    capitalize_list = []

    # Finding which words have to be capitalized
    for i in correct_list:
        if i[0] == i.capitalize()[0]:
            capitalize_list.append(i)
    #print(capitalize_list)

    # stripping the text that is inputted
    text = text.strip().strip(".?!,()\"'").split()
    empty = []

    # stripping each word in text inputted
    for word in text:

        word = word.strip(".?!,()\'\"") #.strip('"').strip("'").strip('!').strip('?')
        empty.append(word)

    # finding which words are misspelled
    for words in empty:

        words = words.strip().strip("?,.!/()\'\"")
        #print(words)
        if words[0] == "'" and words[-1] == "'":
            if words.find("'") > 0 and words.find("'") < len(words) and words.strip("'") not in correct_list:
                newwords = words.strip("'")
                #print(newwords)
                print("  MISSPELLED: " + newwords)
                #print("lol1")

            elif words.strip("'") not in correct_list:
                newwords = words.strip("'")
                print("  MISSPELLED: " + newwords)
                #print("lol")
            else:
                ...
        elif words.find("?,!/") > 0 and words.find("?,!/") < len(words):
            newword = words.strip(("?,!/"))
        elif words[0] == "'" or words[-1] == "'":
            if words.find("'") > 0 and words.find("'") < len(words) and words.strip("'") not in correct_list:
                newwords = words.strip("'")
                print("  MISSPELLED: " + newwords)

            elif words.strip("'") not in correct_list:
                newwords = words.strip("'")
                print("  MISSPELLED: " + newwords)
            else:
                ...
            #print("lol2")

        if words[0] == words.capitalize()[0]:
            if words == empty[0]:
                ...
            if words.lower() in correct_list and words not in capitalize_list:
                ...
            elif words not in capitalize_list:
                print("  MISSPELLED: "+words)
                #print("lol3")
        elif words.lower() not in correct_list:
            #newwords = words.strip('\'')
            print("  MISSPELLED: "+words)
            #print("lol4")
    text = input()
    #print(empty)


