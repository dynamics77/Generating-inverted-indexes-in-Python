# Inverted indexes in Python
A program for generating inverted indexes from text files.

This program constructs an inverted index from the words contained within a series of text files; the index is generated in memory and them saved to disk imminently. The index is constructed in a way where all files associated with a word are contained within a single text file; in other words, each word has its own text file - each text file contains a JSON string object, which contains a list of objects, which each contain which file contained the word and how many times the word occurred.

## Example: hello.txt
The word “hello” found in files: file_1.txt and file_2.txt
```html
{“hello”: [{“file_name”: “file_1.txt”, “occurrences”: 6}, {“file_name”: “file_2.txt”, “occurrences”: 2}]}
```

The advantage of splitting words into separate files is that it will be much faster to read and load each file into memory when running searches - compared to storing the entire index inside one text file.
