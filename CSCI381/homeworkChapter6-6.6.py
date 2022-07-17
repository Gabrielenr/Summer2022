# CSCI 381
# Summer 2022
# Homework Chapter 6 - 6.6
# Gabriel Rubio Alvarado

"""Exercise 6.6
(Duplicate Email Address Removal) Write a function that receives a list of email
addresses and displays only the unique addresses. Treat uppercase and lowercase letters the
same. The function should use a set to get the unique email addresses from the list. Test
your function with several different lists."""

email_list1 = ["gabe@gmail.com", "gabrielenr93@gmail.com",
               "gabe@gmail.com", "GABRIELENR93@gmail.com",
               "gabe93@gmail.com", "gabrielenr@gmail.com"]

email_list2 = ["email_1@gmail.com", "email_2@gmail.com",
               "email_3@gmail.com", "EMAIL_3@gmail.com",
               "EMAIL_2@gmail.com", "email_5@gmail.com"]


def emails_received(email_list):
    for i in range(len(email_list)):
        email_list[i] = email_list[i].lower()
    print(list(set(email_list)))


emails_received(email_list2)
emails_received(email_list1)
