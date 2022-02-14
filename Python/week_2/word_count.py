#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise
Google's Python class
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
Use str.split() (no arguments) to split on all whitespace.
Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
"""

import sys

filename=open('D:\\App_Folders\\vscode\\Python\\vumaasha-s-py\\workouts\\Python-Play Ground\\07-11-2020.py', "r+")

def dict_generator(filename):
  strings =filename.read().split()
  word_count={}
  for string in strings:
    string=string.lower()
    if string not in word_count:
      word_count[string]=1
    word_count[string]+=1
  return word_count

def print_words(filename):
  word=dict_generator(filename)
  words=sorted(word.keys())
  for wrd in words:
    print(wrd,word[wrd])


def print_top(filename):
  word=dict_generator(filename)
  list1=list(word.items())
  desc_order=sorted(list1,key = lambda wrd: wrd[1],reverse=True)
  for rev in desc_order:
      print(rev)

def main():
  print('''Choose one of The Options Below:
  1) count ---> unordered 
  2) topcount ---> most used words first
  Type 1 or 2 :
              ''')
  option = input()
  if int(option) == 1:
    print_words(filename)
    sys.exit(1)
  elif int(option) == 2:
    print_top(filename)
    sys.exit(1)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
