# Introduction to Python Programming
# Lesson 09 Assignment
# Sample Solution

test_scores = { }
name = input("Please enter a student name (-999 quits): ")

while name != '-999':
    score = eval(input("Please enter the students score: "))
    test_scores[name] = score

    print()
    name = input("Please enter a student name (-999 quits): ")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
search_name = input("Which student's score would you like to see (-999 quits): " )

while search_name != '-999':
    if search_name in test_scores:
        print (search_name, "\t", test_scores[search_name])
    else:
        print (search_name, "not found in list")

    print()
    print()

    search_name = input("Which student's score would you like to see (-999 quits): " )


