#!/usr/bin/env python3

from lib.book import Book

import io
import sys

class TestBook:
    '''Book in book.py'''

def test_has_title_and_page_count():
    '''has the title and page_count passed into __init__, and values can be set to a new instance.'''
    book = Book("And Then There Were None", 272, 1939)
    assert book.title == "And Then There Were None"
    assert book.page_count == 272
    assert book.publication_year == 1939

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Flipping the page...wow, you read fast!\n")

def test_book_checkout_checkin():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    assert book.checkout() == True
    assert book.checkout() == False  
    assert book.checkin() == True
    assert book.checkin() == False  

def test_book_attributes():
    book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    assert book.title == "To Kill a Mockingbird"
    assert book.author == "Harper Lee"
    assert book.publication_year == 1960
    
