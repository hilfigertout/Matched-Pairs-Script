#MIT License
#
#Copyright (c) 2022 Ian Roberts
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

import random
#This program implements a pairwise comparison method for ranking.

def get_candidates():
    cand_list = []
    print("Enter the name of the first candidate: ")
    cand_name = input()
    while (cand_name != ""):
        cand_list.append(cand_name)
        print("Enter the name of the next candidate. (blank line to stop): ")
        cand_name = input()
    return cand_list

def read_candidates_from_file(filename):
    cand_list = []
    with open(filename) as in_file:
        cand_list = in_file.readlines()
    cand_list = [ line.strip() for line in cand_list ]
    return cand_list

def get_score_order(cand_dict):
    winner_list = []
    for i in range(len(cand_dict)):
        winning_name = ""
        max = -1
        for x in cand_dict:
            if cand_dict[x] > max:
                winning_name = x
                max = cand_dict[x]
        winner_list.append(winning_name)
        cand_dict.pop(winning_name)
    return winner_list

def main():
    print("Enter name of input text file. (Blank line to enter candidates manually.)")
    filename = input()
    cand_list = []
    if (filename == ""):
        cand_list = get_candidates()
    else:
        cand_list = read_candidates_from_file(filename)
    random.shuffle(cand_list)
    score_list = [0]*len(cand_list)
    print("Answer each prompt with either \"1\" or \"2\".")
    for i in range(len(cand_list)):
        for j in range(i + 1, len(cand_list)):
            print("Enter which of the two you prefer: ")
            print("    1: " + cand_list[i])
            print("    2: " + cand_list[j])
            choice = input()
            try: 
                if (int(choice) == 1):
                    score_list[i] = score_list[i] + 1
                elif (int(choice) == 2):
                    score_list[j] = score_list[j] + 1
                else:
                    print("That's not a valid answer.")
                    j = j - 1
            except:
                print("That's not a valid answer")
                j = j - 1

    cand_dict = {}
    for i in range(len(cand_list)):
        cand_dict[cand_list[i]] =  score_list[i]
    cand_dict_clone = cand_dict.copy()
    winner_list = get_score_order(cand_dict_clone)
    print("RANKED RESULTS (Option: Score)")
    for x in winner_list:
        print(x + ": " + str(cand_dict[x]))

if __name__ == "__main__":
    main()
