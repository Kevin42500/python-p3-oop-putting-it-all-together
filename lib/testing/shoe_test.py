#!/usr/bin/env python3

from lib.shoe import Shoe

import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", 9)
        assert(stan_smith.brand == "Adidas")
        assert(stan_smith.size == 9)

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be an integer\n"

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Your shoe is as good as new!\n")
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()
        assert(stan_smith.condition == "New")

    
def test_shoe_wear_clean():
    shoe = Shoe("Nike", 10, "Red")
    assert shoe.wear() == True
    assert shoe.wear() == False 
    assert shoe.clean() == True
    assert shoe.clean() == False 

def test_shoe_attributes():
    shoe = Shoe("Adidas", 9.5, "Blue")
    assert shoe.brand == "Adidas"
    assert shoe.size == 9.5
    assert shoe.color == "Blue"    
        
        
   
