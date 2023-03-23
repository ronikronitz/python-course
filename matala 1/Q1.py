# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 13:53:12 2023

@author: ronik
"""



def revword(word):
    word=word[::-1]
    return word.lower()

def countword(myFile):
    counter=1
    myF=open(myFile)
    first_line=True
    for line in myF:
        if first_line:
            word=line.rstrip()
            first_line=False
        else:
            myList=[]
            line=line.split()
            for char in line:
                myList.append(revword(char))
            for match in myList:
                if match==word:
                    counter+=1
    return (counter)
        
            
        
    

