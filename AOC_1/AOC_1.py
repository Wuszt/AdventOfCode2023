numbers = ["zero", '0', "one", '1', "two", '2', "three", '3', "four", '4', "five", '5', "six", '6', "seven", '7', "eight", '8', "nine", '9']
file, sum = open("input.txt", "r"), 0
for line in file:
    first, last = '', ''
    for c in range(len(line)):
        for i, value in enumerate(numbers):
            if line[c-len(value):c] == value:
                first = str(int(i / 2)) if first == '' else first
                last = str(int(i / 2))
    sum += int(first + last)
print("sum: " + str(sum))