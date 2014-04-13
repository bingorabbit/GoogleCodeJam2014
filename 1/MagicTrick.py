'''
Google Code Jam 2014
Problem A. Magic Trick
Author: Ibrahim A. Mohamed
email: bingorabbit@gmail.com
'''

try:
    # Read the file into a list of lines
    f = open('test.in')
    m_in = f.readlines()
    new_m_in = []

    # Test cases number
    test_cases_no = int(m_in[0])
    test_case_no = 0

    # For each test case
    while test_case_no < test_cases_no:

        # Get the numer of the row in which the chosen number resides in both deck of cards.
        first_row_no = int(m_in[1+(10*test_case_no)])
        second_row_no = int(m_in[6+(10*test_case_no)])

        # Get the row itself to compare.
        first_list = set(m_in[first_row_no+1+(test_case_no*10)].strip("\n").split(" "))
        second_list = set(m_in[second_row_no+6+(test_case_no*10)].strip("\n").split(" "))

        # Compare and set the result for each case
        # Volunteer Cheated!
        if len(first_list.intersection(second_list)) == 0:
            result = "Volunteer cheated!"
        # Number resides in both decks
        elif len(first_list.intersection(second_list)) == 1:
            result = str(first_list.intersection(second_list).pop())
        # Magician rearranged the cards in a wrong manner
        elif len(first_list.intersection(second_list)) > 1:
            result = "Bad magician!"

        # Print each case's output
        print "Case #%s: %s" % (str(test_case_no + 1), result)

        # Continue to loop.
        test_case_no += 1
except IOError:
    print "Please be sure that you have added the test sample/input data in the right place."
