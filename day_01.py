
file = open("day_01_input.txt", "r")

data = file.readlines()

# first part:

cal_vals = 0

for line in data:
    digits_seen = 0    
    for character in line:        
        if character in ["0","1","2","3","4","5","6","7","8","9"]:
            digits_seen += 1
            if digits_seen == 1:
                first = character
            last = character
    cal_vals += int(first + last)

print(cal_vals)


# second part:

cal_vals2 = 0

for line in data:
    digits_seen = 0
    number = None
    for i in range(len(line)):
        if line[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            number = int(line[i])
        elif line[i:i+3] == "one":
            number = 1
        elif line[i:i+3] == "two":
            number = 2
        elif line[i:i+5] == "three":
            number = 3
        elif line[i:i+4] == "four":
            number = 4
        elif line[i:i+4] == "five":
            number = 5
        elif line[i:i+3] == "six":
            number = 6
        elif line[i:i+5] == "seven":
            number = 7
        elif line[i:i+5] == "eight":
            number = 8
        elif line[i:i+4] == "nine":
            number = 9
        if number != None:
            digits_seen += 1
            if digits_seen == 1:
                first = number
            last = number
    cal_vals2 += int(str(first) + str(last))

print(cal_vals2)


        
