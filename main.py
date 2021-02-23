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


def search_for_word(key_word, file_info):
    num = re.findall(key_word, file_info, re.M | re.I)
    print(len(num))


" This the the main function of the project "
if __name__ == '__main__':
    file = open("Input.txt", 'r')
    file_read = file.read()
    search_word = input("Enter the word to be searched in the file\n")  # Asking user to enter the word to be searched
    search_for_word(search_word, file_read)
