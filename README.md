# Generating inverted indexes in Python
A program for generating inverted indexes from text files.

This program constructs an inverted index from the words contained within a series of text files; the index is generated in memory and them saved to disk immediately. The index is constructed in a way where all files associated with a word are contained within a single text file; in other words, each word has its own text file - each text file contains a JSON string object, which contains a list of objects, which each contain which file contained the word and how many times the word occurred.

## Word file structure
The word “hello” found in files: file_1.txt and file_2.txt
```html
{"hello": [{"file_name": "file_1.txt", "occurrences": 6}, {"file_name": "file_2.txt", "occurrences": 2}]}
```

The advantage of splitting words into separate files is that it will be much faster to read and load each file into memory when running searches - compared to storing the entire index inside one text file.

For this repo I have uploaded 5 sample text files: hamlet.txt, othello.txt, macbeth.txt, julius-caesar.txt, and romeo-and-juliet.txt - each file contains all text from each play (thanks to http://shakespeare.mit.edu).
Using a 2016 MacBook air with a 1.6GHz CPU and 4GB of RAM I was able to index all of these text files in around ~20 seconds - this produced 23,636 word files.

## Example word file: thou.txt
```html
{"thou": [{"file_name": "hamlet.txt", "occurrences": 85}, {"file_name": "julius-caesar.txt", "occurrences": 101}, {"file_name": "macbeth.txt", "occurrences": 65}, {"file_name": "othello.txt", "occurrences": 115}, {"file_name": "romeo-and-juliet.txt", "occurrences": 233}]}
```

Fun fact: Romeo and Juliet contains the word "thou" 233 times.
