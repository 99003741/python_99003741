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
    def __init__(self):
        self.file_info = open("Input.txt", 'r')
        self.file_read = self.file_info.read()


def search_for_word(s_w, f_r):
    num = re.findall(s_w, f_r, re.M | re.I)
    return (num)


def file_create(s_w, num):
    n_f = s_w + ".txt"
    new_file = open(n_f, "a")
    new_file.write("The total occurrence of the word is:")
    new_file.write(str(len(num)))


" This the the main function of the project "
if __name__ == '__main__':
    file = open("Input.txt", 'r')
    file_read = file.read()
    search_word = input("Enter the word to be searched in the file\n")  # Asking user to enter the word to be searched
    count = search_for_word(search_word, file_read)
    file_create(search_word, count)
