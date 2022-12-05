# d4.py
# Advent of Code - Day 4 - wyattboyer
#from .. import aocUtils

import re
# remember, match only searches from beginning of the string
# search matches anywhere in the string (perl default, how it should be)

complete_overlap = lambda x: x[0].issubset(x[1]) or x[1].issubset(x[0])
partial_overlap = lambda x: True if len(x[0].intersection(x[1])) > 0 else False


def raw_text(filename: str) -> str:
    with open(filename,'r') as f:
        return f.read()

def format_data(raw_txt: str) -> list[list[set[int]]]:
    data = []
    lines = raw_txt.split()
    for line in lines:
        sections = list(map(int, re.findall(r'(\d+)', line)))
        data.append([set(range(sections[0], sections[1]+1)), set(range(sections[2], sections[3]+1))])
    return data

def find_num_overlaps(data: list[tuple[set[int]]], partial: bool = True) -> int:
    return len(list(filter(partial_overlap if partial else complete_overlap, data)))    

if __name__ == '__main__':
    fn = 'input.txt'
    raw = raw_text(fn)
    data = format_data(raw)
    result1 = find_num_overlaps(data, False)
    result2 = find_num_overlaps(data)
    print(f"Result 1: {result1}\nResult 2: {result2}")
