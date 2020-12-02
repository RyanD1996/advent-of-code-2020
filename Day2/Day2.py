
def main():
    fin = open("input.in", "r")
    input = [line.strip() for line in fin.readlines() if line.strip()]
    
    part_a_valids = []
    part_b_valids = []
    for line in input:
        parts = line.split(' ')
        ranges = parts[0].split('-')
        if (parts[2].count(parts[1][0]) >= int(ranges[0]) and parts[2].count(parts[1][0]) <= int(ranges[1])):
            part_a_valids.append(parts)

        if (parts[2][int(ranges[0])-1] == parts[1][0] and parts[2][int(ranges[1])-1] == parts[1][0]):
            continue
        if (parts[2][int(ranges[0])-1] == parts[1][0] or parts[2][int(ranges[1])-1] == parts[1][0]):
            part_b_valids.append(parts)
    print(f'There are {len(part_a_valids)} passwords in part A')
    print(f'There are {len(part_b_valids)} passwords in part B')


if __name__ == "__main__":
    main()