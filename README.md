# Matched-Pairs ranking script

This program implements a system for a single user to rank items using a matched-pairs approach. 

The program takes in a list of options as strings (either from an input text file or entered manually), shuffles the list, and presents the user a pair of options. The user selects which option they prefer. That item gets 1 point. The program continues for every possible pairing of the options, then it presents the full list of options ranked by score, with the first item having the most points and the last item having the least points. (Scores are also shown.)

## Running the program

This program is implemented in Python. To run it, you will need the Python interpreter installed. 

To run this program, simply open a termminal, navigate to the directory containing the matched-pairs.py script, and run the following:

> python3 matched-pairs.py

This script does not take any command line arguments.

## Example Output:

> Enter name of input text file. (Blank line to enter candidates manually.)
> example_input_file.txt
> Answer each prompt with either "1" or "2".
> Enter which of the two you prefer:
>     1: Option B
>     2: Option C
> 1
> Enter which of the two you prefer: 
>     1: Option B
>     2: Option A
> 2
> Enter which of the two you prefer: 
>     1: Option B
>     2: Option E
> 1
> Enter which of the two you prefer: 
>     1: Option B
>     2: Option D
> 1
> Enter which of the two you prefer: 
>     1: Option C
>     2: Option A
> 2
> Enter which of the two you prefer: 
>     1: Option C
>     2: Option E
> 1
> Enter which of the two you prefer: 
>     1: Option C
>     2: Option D
> 1
> Enter which of the two you prefer: 
>     1: Option A
>     2: Option E
> 1
> Enter which of the two you prefer: 
>     1: Option A
>     2: Option D
> 1
> Enter which of the two you prefer: 
>     1: Option E
>     2: Option D
> 2
> RANKED RESULTS (Option: Score)
> Option A: 4
> Option B: 3
> Option C: 2
> Option D: 1
> Option E: 0
