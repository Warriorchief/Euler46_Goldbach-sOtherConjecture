#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:53:03 2017

@author: christophergreen
Goldbach's other conjecture Problem 46
It was proposed by Christian Goldbach that every odd composite number can 
be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math
def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
    
def assemble(maximum):
    primes=[];
    comps=[];
    twicesqs=[]
    j=2
    while j<=maximum:
        if is_prime(j):
            primes.append(j);
        else:
            comps.append(j);
        j+=1
    k=1;
    while k<=math.ceil(math.sqrt(maximum/2)):
        twicesqs.append(2*k**2);
        k+=1;
    oddcomps=[];
    l=0;
    while l<len(comps):
        if comps[l]%2==1:
            oddcomps.append(comps[l]);
        l+=1;
    sums=[];
    a=0;
    while a<len(primes):
        b=0;
        while b<len(twicesqs):
            sums.append(primes[a]+twicesqs[b]);
            b+=1;
        a+=1;
    sums.sort()
    sums=set(sums);       
    sums=list(sums);
    return (oddcomps,primes,twicesqs,sums);


def main(maximum):
    z=assemble(maximum);
    l=len(z[0]);
    print("there are",l,"odd composites below",maximum);
    i=0;
    counter=0;
    while i<l:
        if z[0][i] in z[3]:
            counter+=1;
        else:
            print("didn't find match for",z[0][i]);
            return z[0][i];
        i+=1;
    print("found match for everything, so counter should be same as number of primes, which is",l,". Counter is",counter);
    return;
    
    
#main(10000)  #--> didn't find match for 5777 CORRECT