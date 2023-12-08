"""
https://adventofcode.com/2023/day/3
"""

file = open("day_03_input.txt", "r")

data = file.readlines()


data_matrix = []

for line in data:
    row = []
    for i in range(len(line)):
        if line[i] != "\n":
            row.append(line[i])
    data_matrix.append(row)


#part 1 ----------------------------------------------------------------------------------

def isspecialchar(char):
    return (not char.isalnum()) and (char != ".")

total = 0

for i in range(len(data_matrix)):
    for j in range(len(data_matrix[i])):
        if data_matrix[i][j].isdigit() and (j == 0 or not data_matrix[i][j-1].isdigit()):
            x = 0
            number = data_matrix[i][j]
            for k in range(len(data_matrix[i]))[j+1:]:
                if data_matrix[i][k].isdigit():
                    x += 1
                    number = number + data_matrix[i][k]
                else:
                    break
            surroundings = []
            for row in data_matrix[max(i-1,0):i+2]:
                surroundings += row[max(j-1,0):j+2+x]
            if any(isspecialchar(char) for char in surroundings):
                total += int(number)
        
print(total)


#part 2 ----------------------------------------------------------------------------------  

gear_ratio_sum = 0

for i in range(len(data_matrix)):
    for j in range(len(data_matrix[i])):
        if data_matrix[i][j] == "*":
            partnumbers = []
            for row in data_matrix[max(i-1,0):i+2]:
                for k in range(len(row[max(j-1,0):j+2])):
                    if row[max(j-1,0)+k].isdigit():                           
                        if k == 0 or (k > 0 and not row[max(j-1,0)+k-1].isdigit()): #avoid double counting
                            partnumber = row[j-1+k]
                            for l in range(len(row[:j-1+k])):                       #look back
                                if row[j-2-l+k].isdigit():
                                    partnumber = row[j-2-l+k] + partnumber
                                else:
                                    break
                            for m in range(len(row[j+k:])):                         #look forward
                                if row[j+k+m].isdigit():
                                    partnumber = partnumber + row[j+k+m]
                                else:
                                    break
                            partnumbers.append(partnumber)
            if len(partnumbers) == 2:
                gear_ratio_sum += int(partnumbers[0]) * int(partnumbers[1])

print(gear_ratio_sum)    

