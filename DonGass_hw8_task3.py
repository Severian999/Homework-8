# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 20:51:15 2017

@author: Don Gass
"""

def whoDishonest(club1, club2, club3):
    """
    return sorted list of Strings, the names
    that appear in more than one of the
    String lists club1, club2, club3
    """
    myset = (set(club1) & set(club2)) | (set(club1) & set(club3)) | \
            (set(club2) & set(club3))
    return sorted(list(myset))

#    
club1 = ["JOHN","JOHN","FRED","PEG"]
club2 = ["PEG","GEORGE"]
club3 = ["GEORGE","DAVID"]

print(whoDishonest(club1, club2, club3))

club1 = ["DOUG","DOUG","DOUG","DOUG","DOUG"]
club2 = ["BOBBY","BOBBY"]
club3 = ["JAMES"]

print(whoDishonest(club1, club2, club3))

club1 = ["BOBBY"]
club2 = ["BOB","BOBBY"]
club3 = ["BOB"]

print(whoDishonest(club1, club2, club3))

club1 = ["BOBBY","HUGH","LIZ","GEORGE"]
club2 = ["ELIZABETH","WILL"]
club3 = ["BOB","BOBBY","BOBBY","PAM","LIZ","BOBBY","BOBBY","WILL"]

print(whoDishonest(club1, club2, club3))

club1 = ["JAMES","HUGH","HUGH","GEORGE","ELIZABETH","ELIZABETH","HUGH","DAVID","ROBERT","DAVID","BOB","BOBBY","PAM","JAMES","JAMES"]
club2 = ["BOBBY","ROBERT","GEORGE","JAMES","PEG","JAMES","DAVID","JOHN","LIZ","SANDRA","GEORGE","JOHN","GEORGE","ELIZABETH","LIZ","JAMES"]
club3 = ["ROBERT","ROBERT","ROBERT","SANDRA","PAM","BOB","LIZ","GEORGE"]

print(whoDishonest(club1, club2, club3))

club1 = ["LIZ","WILL","JAMES"]
club2 = ["JOHN","ROBERT","GEORGE","LIZ","PEG","HUGH","BOB","BOBBY","ROBERT","ELIZABETH","DAVID"]
club3 = ["PAM","DAVID","SANDRA","GEORGE","JOHN","ROBERT","SANDRA","GEORGE"]

print(whoDishonest(club1, club2, club3))

club1 = ["PEG","ROBERT","PAM","JOHN","DAVID","JOHN","ROBERT","GEORGE","HUGH","WILL","JAMES","JAMES","BOBBY","BOBBY","SANDRA"]
club2 = ["SANDRA","BOB","PAM","JAMES","WILL","DAVID","BOBBY","GEORGE","WILL","LIZ","BOBBY","ROBERT","WILL","BOB","BOBBY","ELIZABETH","HUGH"]
club3 = ["WILL","PEG","ELIZABETH","DAVID","HUGH","BOBBY","JOHN","SANDRA","ELIZABETH","ELIZABETH","SANDRA","GEORGE","PAM","ELIZABETH","BOBBY","DAVID","PAM"]

print(whoDishonest(club1, club2, club3))