"""
Description: This program takes a user input as a keyword and search the occurrence of the word in the file and the
                count total occurrences and store these details in a new file
Author: RAJAT MEHTA
PS No: 99003741
Contact: rajat.mehta@ltts.com
Date of Creation: 23/02/2021
"""
import re


class Wordsearch:
    def __init__(self, s_w):
        self.file_info = open("Input.txt", 'r')
        self.f_r = self.file_info.read()
        self.s_w = s_w

    def search_for_word(self):
        count = 0
        n_f = self.s_w + ".txt"
        new_file = open(n_f, "w")
        m = re.split(r'\W+', self.f_r)
        print(m)
        for num in range(len(m)):
            if re.fullmatch(self.s_w, m[num], re.M | re.I):
                var = m[num - 1] + " " + m[num] + " " + m[num + 1] + '\n'
                new_file.write(str(var))
                count += 1
        new_file.write("Total occurrence of word " + self.s_w + " is: " + str(count))
        new_file.close()


def search_word():
    keyword = input("Enter the word to be searched in the file\n")  # Asking user to enter word to be searched
    return keyword


" This the the main function of the project "
if __name__ == '__main__':
    key = search_word()
    find = Wordsearch(key)
    find.search_for_word()
    find.file_info.close()
