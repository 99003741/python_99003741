"""
Description: This program takes a user input as a keyword and search the
                occurrence of the word in the file and the
        count total occurrences and store these details in a new file
Author: RAJAT MEHTA
PS No: 99003741
Contact: rajat.mehta@ltts.com
Date of Creation: 23/02/2021
"""
import re

"----------------------------- SUPER CLASS --------------------------------"
"""
Basic or First class(Super class)
This initializes the word to be searched and
also opens the file to be searched in once a object is created
"""


class Wordsearch:
    def __init__(self, s_w):
        self.file_info = open("Input.txt", 'r')
        self.f_r = self.file_info.read()
        self.s_w = s_w


"--------------------- END OF SUPER CLASS --------------------------------"

"------------------------ SUB CLASS --------------------------------------"
"""
This is second class which has inherited attributes of first class(sub class)
This class finds the user given word in the file and
creates a new file and print the result in that file
"""


class Words(Wordsearch):
    def search_for_word(self):
        count = 0
        n_f = self.s_w + ".txt"
        new_file = open(n_f, "w")
        m = re.split(r'\W+', self.f_r)
        for num in range(len(m)):
            if re.fullmatch(self.s_w, m[num], re.M | re.I):
                var = m[num - 1] + " " + m[num] + " " + m[num + 1] + '\n'
                new_file.write(str(var))
                count += 1
        if count != 0:
            new_file.write("Total occurrence of word " + self.s_w + " is: " + str(count))
        elif count == 0:
            new_file.write("The word " + self.s_w + " is not found in the file :(")
        new_file.close()


"--------------------- END OF SUB CLASS ----------------------------------"

"-------------------- USER INPUT FUNCTION --------------------------------"
"""
This function ask the user to input the words to be searched in the file
"""


def search_word():
    # Asking user to enter word to be searched
    keyword = input("Enter the word to be searched in the file\n")
    return keyword


"--------------------- END OF USER INPUT FUNCTION ------------------------"

"-------------------------- MAIN PROGRAM ---------------------------------"
" This the the main function of the project "
if __name__ == '__main__':
    text = int(input("Number of words you want to search: "))
    for i in range(text):
        key = search_word()
        find = Words(key)
        find.search_for_word()
        find.file_info.close()
"-------------------------- END OF PROGRAM ---------------------------------"
