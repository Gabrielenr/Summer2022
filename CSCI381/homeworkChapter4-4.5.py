# CSCI 381
# Summer 2022
# Homework Chapter 4 - 4.5
# Gabriel Rubio Alvarado

"""Exercise 4.5
(Fill in the Missing Code) The slope of a line is the number that describes its direction and steepness.
It is calculated by dividing the change in height by the change in length.
Replace the ***s in the calc_slope function so that it returns the slope of a line drawn in a cartesian
coordinate system. The function should receive four integers representing the x and y coordinates of the
beginning and end of the line. For example, if you call the function for a line starting at (1,1) and
ending at (4,5), the function should return 1.33.
 def calc_slope(***):
    delta_x = ***
    delta_y = ***
    slope = ***
    return ***
    """


def calc_slope(x1, x2, y1, y2):
    delta_x = x1 - x2
    delta_y = y1 - y2
    slope = delta_y / delta_x
    return slope


# passing point (1,1) and (4,5)
print(calc_slope(1, 4, 1, 5))
