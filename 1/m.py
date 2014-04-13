# Problem A. Magic Trick

# Read the file into a list of lines
f = open('test.in')
m_in = f.readlines()
new_m_in = []

# Test cases number
test_cases_no = int(m_in[0])
test_case_no = 0

while test_case_no < test_cases_no:

    first_row_no = int(m_in[1+(10*test_case_no)])
    second_row_no = int(m_in[6+(10*test_case_no)])

    first_list = set(m_in[first_row_no+1+(test_case_no*10)].strip("\n").split(" "))
    second_list = set(m_in[second_row_no+6+(test_case_no*10)].strip("\n").split(" "))


    if len(first_list.intersection(second_list)) == 0:
        result = "Volunteer cheated!"
    elif len(first_list.intersection(second_list)) == 1:
        result = str(first_list.intersection(second_list).pop())
    elif len(first_list.intersection(second_list)) > 1:
        result = "Bad magician!"

    print "Case #%s: %s" % (str(test_case_no + 1), result)

    test_case_no += 1