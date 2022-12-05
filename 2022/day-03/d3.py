# d3.py
# Advent of Code - Day 3 - wyattboyer
import string

ALPHA = list(string.ascii_lowercase + string.ascii_uppercase)

def sum_items(items: list[str]) -> int:
    return sum([get_priority(i) for i in items])

def get_priority(item: str) -> int:
    return ALPHA.index(item) + 1

def intersect_p1(data: list[list[str]]) -> list[str]:
    items = []
    for line in data:
        common_item = (set(line[0]).intersection(set(line[1])))
        items.append(list(common_item)[0])
    return items

def intersect_p2(data: list[list[str]]) -> list[str]:
    items = []
    for arr in data:
        sets = [set(l) for l in arr]
        common_item = list(sets[0].intersection(sets[1]).intersection(sets[2]))
        items.append(common_item[0])
    return items
    
def format_p2(raw_txt: str) -> list[list[str]]:
    data = []
    lines = raw_txt.split()
    data = [lines[i*3:(i+1)*3] for i in range(len(lines)//3)]
    return data

def format_p1(raw_txt: str) -> list[list[str]]:
    data = []
    lines = raw_txt.split()
    for l in lines: 
        data.append([l[:len(l)//2], l[len(l)//2:len(l)]])
    return data

def raw_text(filename: str) -> str:
    with open(filename,'r') as f:
        return f.read()

if __name__=='__main__':
    file = 'input.txt'
    raw = raw_text(file)
    # calculate result 1
    data = format_p1(raw)
    items = intersect_p1(data)
    res1 = sum_items(items)
    # calculate result 2
    data = format_p2(raw)
    items = intersect_p2(data)
    res2 = sum_items(items)
    print(f'Result 1: {res1}\nResult 2: {res2}')
    
