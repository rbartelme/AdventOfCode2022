#!/usr/bin/env python3

# break up input into list by elf based on empty lines, these will be stored as strings not integers
with open('day1_input.txt') as fp:
    raw_elvs = [p.strip() for p in fp.read().split('\n\n')]

# convert each string in the list to a list of integers stored in a list of lists
lst_elvish_int = [[int(val)for val in elf.split()] for elf in raw_elvs]
# calculate total calories per elf
lst_elf_calories_carried = [sum(food) for food in lst_elvish_int]
#Part 1: find the elf carrying the most
print("The largest amount of calories carried by an elf is: ", max(lst_elf_calories_carried))
# sort the list from largest to smallest
lst_elf_calories_carried.sort(reverse=True)
# calculate the sum of the calories carried by the top three elves
print("Total calories carried by the top 3 elves is: ", sum(lst_elf_calories_carried[0:3]))
