# d1.py
# Advent of Code - Day 1 - wyattboyer
import re

def extract_data(filename: str) -> list[list[int]]:
    raw = ""
    data = []
    # read input as one string
    with open(filename, 'r') as f:
        raw = f.read()
    # replace every newline with a comma
    condense = re.sub(r"\n",',',raw)
    # replace every occurrence of two commas in a row with a newline
    expand = re.sub(r",{2}",'\n', condense)
    # split the array into a list of csv strings
    lines = expand.split()
    for l in lines:
        # split csv strings into lists of integers
        data.append(list(map(int, l.split(','))))
    return data

# calculate and return an list of sums from a 2d list
def getSums(data: list[list[int]]) -> list[int]:
    return [sum(d)for d in data]

# gets the top n calorie counts then sum those
def maxCals(data: list[list[int]], n: int) -> int:
    sums = getSums(data)
    maxes = []
    while len(maxes) < n:
        m = max(sums)
        maxes.append(m)
        sums.remove(m)
    return sum(maxes)
    
if __name__=='__main__':
    input = 'input.txt'
    data = extract_data(input)
    result = maxCals(data, 3)
    print(f'Max Calories: {result}')