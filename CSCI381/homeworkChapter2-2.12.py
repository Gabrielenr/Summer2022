# CSCI 381
# Summer 2022
# Homework Chapter 2 - 2.12
# Gabriel Rubio Alvarado

""" Exercise 2.12
(Hourly Wage Calculator) Every year, if an employee receives a good job performance
review, they get a raise of 3% on their wages. In turn, if they receive a suboptimal performance
review, their wages are deducted by 3%. Consider an employee starting with an hourly wage
of $10. Calculate how much this employee is earning after 5 years of consistent good reviews
and after 2 years of bad reviews. Use the following formula to calculate these wages:
        w = o(1 + p)^n
where
        w is the new hourly wage,
        o is the original hourly wage,
        p is the percentage increase or decrease, and
        n is the number of years with an increase or decrease in hourly wage. """

initial_wage = 10

good_review_wage = initial_wage * ((1 + 0.03) ** 5)
bad_review_wage = initial_wage * ((1 - 0.03) ** 2)

print("Employee hourly wage after 5 years of good reviews:", "${:.2f}".format(good_review_wage))
print("Employee hourly wage after 2 years of bad reviews:", "${:.2f}".format(bad_review_wage))





