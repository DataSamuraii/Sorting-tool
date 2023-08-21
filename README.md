This is the *Sorting Tool (Python)* project I made myself.

<p>In the modern world, data has become so abundant that processing it is no easy business. How can anyone make sense of all those words and numbers? In this project, you will write a program that processes textual and numeric data and sorts it. Your program will be able to determine the largest or most frequent pieces of data and perform the necessary calculations on them. Data is waiting to be sorted!</p>

---
## Sorting Tool

A command-line tool for sorting data of various types and with different sorting criteria. 

### Features
- **Data Types**: Supports sorting lines (`line`), words (`word`), and numbers (`long`).
- **Sorting Types**: Allows natural sorting (`natural`) or sorting by count (`byCount`).
- **Input/Output Files**: Can read data from a specified input file and write sorted results to an output file.

### Usage
```bash
python sorting_tool.py [-h] [-dataType {long,line,word}] [-sortingType {byCount,natural}] [-inputFile INPUTFILE] [-outputFile OUTPUTFILE]
```

### Options

#### `-dataType {long,line,word}`
- Specifies the type of data to be sorted.
- Acceptable values: `long`, `line`, `word`.
- Default: `word`.

#### `-sortingType {byCount,natural}`
- Specifies the sorting method.
- Acceptable values: `byCount`, `natural`.
- Default: Natural sorting.

#### `-inputFile INPUTFILE`
- Path to an input file containing the data to be sorted.
- If not provided, the tool will read from the standard input.

#### `-outputFile OUTPUTFILE`
- Path to a file where sorted results will be written.
- If not provided, the tool will print to the standard output.

### Sorting Types Explained

#### Natural Sorting
- Sorts data in their natural order (alphanumerically).
- For numbers, sorts them in ascending order.
- For text, sorts them alphabetically.

#### Sorting by Count
- Groups data by their occurrences and sorts the groups by count.
- Inside groups with the same count, items are sorted naturally.
- For numbers, groups are sorted by count, then by value.
- For text, groups are sorted by count, then alphabetically.

### Examples
Sort numbers naturally:
```bash
python sorting_tool.py -dataType long -sortingType natural -inputFile numbers.txt
```

Sort words by count:
```bash
python sorting_tool.py -dataType word -sortingType byCount -inputFile words.txt -outputFile sorted_words.txt
```

### Errors and Warnings
- The tool provides clear error messages for common mistakes, such as missing required parameters or invalid input data.

### Support and Contributions
Feel free to open an issue or submit a pull request if you find a bug or have suggestions for improvements.

---
Here's the link to the project: https://hyperskill.org/projects/307

Check out my profile: https://hyperskill.org/profile/103100057
