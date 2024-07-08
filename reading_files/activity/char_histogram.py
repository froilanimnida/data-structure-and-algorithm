"""
A text file contains some text (nothing unusual) but we need to know how often (or how rare)
each letter appears in the text. Such an analysis may be useful in cryptography, so we want
to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc


Part 2:
Sorted character frequency histogram
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter
should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the
suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:
"""


from os import strerror


def char_histogram(filename):
    """to know how often (or how rare)
        each letter appears in the text"""
    char_dictionary = {}
    try:
        text_file = open(file=f"{filename}.txt", mode='r', encoding='utf-8')
    except IOError as e:
        print(f"IOError: {strerror(e.errno)}")
    else:
        with text_file:
            lines = text_file.read()
            for char in lines:
                x = char.lower()
                if char in ['', ' ', '\n']:
                    continue

                if x not in char_dictionary:
                    char_dictionary.update({x: 1})
                else:
                    occurrence = (char_dictionary[x]) + 1
                    char_dictionary.update({x: occurrence})

    return char_dictionary


file_name = input("Enter txt filename: ")

result = dict(sorted(char_histogram(filename=file_name)
                     .items(), key=lambda item: item[1], reverse=True)).items()

for letter, count in result:
    print(f"{letter} -> {count}")

try:
    hist_file = open(f"{file_name}.hist.txt", mode="+wt", encoding='utf-8')
except IOError as errr:
    print(f"IOError: {strerror(errr.errno)}")
else:
    with hist_file:
        for letter, count in result:
            hist_file.write(f"{letter} -> {count}\n")


# Reading the file
try:
    hist_file = open(f"{file_name}.hist.txt", mode='r', encoding='utf-8')
except IOError as err:
    print(f"IOError: {strerror(err.errno)}")
else:
    with hist_file:
        line = hist_file.read()
        for char in line:
            print(char, end='')
