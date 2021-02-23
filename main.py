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
        num = re.findall(self.s_w, self.f_r, re.M | re.I)
        return num


def file_create(s_w, num):
    n_f = s_w + ".txt"
    new_file = open(n_f, "a")
    new_file.write("The total occurrence of the word is:")
    new_file.write(str(len(num)) + "\n")
    for i in num:
        new_file.write(i + "\n")

    '''    for i in num:
        count+=1
        new_file.writelines(str(count)+' :')
        new_file.writelines(i[1]+'\n')
    '''


" This the the main function of the project "
if __name__ == '__main__':
    search_word = input("Enter the word to be searched in the file\n")  # Asking user to enter the word to be searched
    find = Wordsearch(search_word)
    count = find.search_for_word()
    file_create(search_word, count)
