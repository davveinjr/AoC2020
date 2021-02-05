f = open("Day4.txt", "r")

data = [x.strip() for x in f.readlines()]

f.close()

##Imports:
# byr - Birth Year
# iyr - Issue Year 
# eyr - Expiration Year
# hgt - Height
# hcl - Hair Color
# ecl - Eye Color
# pid - Passport ID
# cid - Country ID

## Part 1
def Part1(data):
    #Parse Data
    #with open("Day4.txt", "r"):
    total_valid = req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    
    current = 0
    for line in data:
        if line == '':
            if current == len(req_fields):
                total_valid += 1
            current = 0
            continue
            
        #split key/value pair, check if in req_fields
        for pair in line.split():
            key, value = pair.split(':')
            if key in req_fields:
                current += 1

    return total_valid

print("Solution to Part 1: %d" % Part1(data))
## Part 2

# def validate():


def Part2(data):

    total_valid = 0
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport = {} 
    current = 0
    for line in data:
        if line == '':
            if current == len(req_fields):
                # Validate the entries using the newly built passport dict   
            current = 0
            continue
            
        #split key/value pair, check if in req_fields
        for pair in line.split():
            key, value = pair.split(':')
            if key in req_fields:
                passport[key] = value
                current += 1

    return total_valid
