# CSCI 381
# Summer 2022
# Homework Chapter 3 - 3.6
# Gabriel Rubio Alvarado

""" Exercise 3.6
(Turing Test) The great British mathematician Alan Turing proposed a simple test
to determine whether machines could exhibit intelligent behavior. A user sits at a computer and does the same text chat
with a human sitting at a computer and a computer operating by itself. The user does not know if the
responses are coming back from the human or the independent computer. If the user can’t distinguish which
responses are coming from the human and which are coming from the computer, then it’s reasonable to say that
the computer is exhibiting intelligence.
Create a script that plays the part of the independent computer, giving its user a simple medical diagnosis.
The script should prompt the user with 'What is your problem?'
When the user answers and presses Enter, the script should simply ignore the user’s input,
then prompt the user again with 'Have you had this problem before (yes or no)?' If
the user enters 'yes', print 'Well, you have it again.' If the user answers 'no', print 'Well, you have it now.'
Would this conversation convince the user that the entity at the other end exhibited
intelligent behavior? Why or why not?"""

input("What is your problem? ")
second_input = input("Have you had this problem before (yes or no)? ")

if second_input.lower() == 'yes':
    print("Well, you have it again")
elif second_input.lower() == 'no':
    print("Well, you have it now")

# This conversation is not enough to prove that the entity exhibited intelligent behavior because it is hard coded
# what to answer depending on the user's input.
