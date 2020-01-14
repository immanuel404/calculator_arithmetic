# calculator with all buttons
# By Emmanuel.O

import simplegui
import math

# intialize globals
digit_one = 0
digit_two = 0

# event handlers for calculator with a store and operand

def add():
    """ add operand to store"""
    global digit_one, digit_two
    maths = digit_one + digit_two
    print "computing... complete, answer is:",maths
def sub():
    """ subtract operand from store"""
    global digit_one, digit_two
    maths = digit_one - digit_two
    print "computing... complete, answer is:",maths
def mult():
    """ multiply store by operand"""
    global digit_one, digit_two
    maths = digit_one * digit_two
    print "computing... complete, answer is:",maths
def div():
    """ divide store by operand"""
    global digit_one, digit_two
    maths = digit_one / digit_two
    print "computing... complete, answer is:",maths
def enter_one(t):
    """ enter a new operand"""
    global digit_one
    digit_one = int(t)
    print digit_one
def enter_two(t):
    """ enter a new operand"""
    global digit_two
    digit_two = int(t)
    print digit_two
    
# create frame
frame = simplegui.create_frame("Calculator",300,300)

# register event handlers and create control elements
frame.add_input("Enter First Digit", enter_one, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)
frame.add_input("Enter Second Digit", enter_two, 100)

# get frame rolling
frame.start()
