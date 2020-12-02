

def main():
    fin = open("input.in", "r")
    input = [int(line.strip()) for line in fin.readlines() if line.strip()]
    for x in input: 
        for y in input:
            for z in input:
                if(x+y+z == 2020):
                    print(x*y*z)

if __name__ == "__main__":
    main()