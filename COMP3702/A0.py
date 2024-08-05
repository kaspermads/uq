# -*- coding: utf-8 -*-
"""
Assignment 0 template

For submission, rename this file to "A0.py" 

Answer each question in the corresponding method definition stub below
"""


def Q1(A,B):
    union = A | B
    intersection = A & B
    return union,intersection

print(Q1({1,2,3,4,5},{3,4,5,6,7}))

def Q2(A,B):
    return 'DISJOINT'


def Q3(a,b):
    X = set()
    Y = set()
    G = set()
    return X,Y,G


def Q4(E,n):
    n_successors = set()
    return n_successors


def Q5(inFile,outFile,remove):
    print('Character '+remove+' removed from '+inFile)
    print('Output written to '+outFile)


def Q6(state1,state2):
    print('IMPOSSIBLE')


    