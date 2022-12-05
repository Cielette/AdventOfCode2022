#!/usr/bin/env python3

def main():
    one_elf_total = 0
    elf = []
    elf_group = []
    with open('Calorie.txt', 'r') as f:
        for line in f:
            elf_group.append(line.strip())
    for i in range(len(elf_group)):
        if elf_group[i] == "":
            elf.append(one_elf_total)
            one_elf_total = 0
        else:
            one_elf_total += int(elf_group[i])
    print(f"The highest calorie count is: {max(elf)}!")
    
if __name__ == "__main__":
    main()
