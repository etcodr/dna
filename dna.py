import sys, csv, re

def main():
    # check that there are 3 CLIs
    n = len(sys.argv)
    if n != 3:
        print('Usage: python3 dna.py data.csv sequence.csv')
        sys.exit(1)

    # declare empty list to hold csv contents
    info = list()
    # open csv file, read into memory, populate list w/ contents
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            info.append(line)

    # open sequence file and read into memory
    with open(sys.argv[2], 'r') as txtfile:
        data = txtfile.read()

    # intitialize list to hold STR counts from sequence file
    lst = ['Sequence']
    # slice csv coloumn names to only include STR names
    regexes = info[0][1:]
    # for each STR name run the function to count STR length in sequence
    for i in range(len(regexes)):
        lst.append(findstr(data, regexes[i]))

    # compare sequence to each row in csv file
    for row in info:
        if row[0] == 'name':
            continue
        if row[1:] == lst[1:]:
            print(row[0])
            sys.exit(0)

    print('No match')
    sys.exit(0)

# function to count STRs
def findstr(data, regex):
    count_str = 0
    # compile regex and assign to variable p
    p = re.compile(rf'({regex})\1*')
    # create an iterator from the sequence using the regex
    iterator = p.finditer(data)
    # loop through iterator and populate match with groups that match regex
    match = [match for match in iterator]
    # set match to the longest STR
    for i in range(len(match)):
        if match[i].group().count(regex) > count_str:
            count_str = match[i].group().count(regex)
    return str(count_str)

main()