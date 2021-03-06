#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#In a grid of 6 by 6 squares you want to place a skyscraper in each square with only some clues:
#
#The height of the skyscrapers is between 1 and 6
#No two skyscrapers in a row or column may have the same number of floors
#A clue is the number of skyscrapers that you can see in a row or column from the outside
#Higher skyscrapers block the view of lower skyscrapers located behind them

def colour_change(colour1, colour2):
#    function to determine the output from a pair of colours
    if colour1 == colour2:
        return colour1
    colour = [e for e in ['R','G','B'] if e not in (colour1, colour2)]
    return str(colour[0])
        

def triangle(row):
#   iterates through the initial string and outputs the final colour
    current_row = row
    for i in range(0,len(row) - 1):
        next_row = []
        for j in range(len(current_row) - 1):
          next_row.append(colour_change(current_row[j],current_row[j+1]))          
        current_row = next_row
    return str(current_row[0])
