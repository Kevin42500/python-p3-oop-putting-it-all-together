#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        self.worn = False

    def wear(self):
        if not self.worn:
            self.worn = True
            return True
        else:
            return False

    def clean(self):
        if self.worn:
            self.worn = False
            return True
        else:
            return False
