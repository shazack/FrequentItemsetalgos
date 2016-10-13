# -*- coding: utf-8 -*- 
import random
from string import lowercase as letters
import sys
import itertools
from collections import Counter
from collections import defaultdict
from itertools import chain
from collections import OrderedDict
import math
import sys
import os
sys.setrecursionlimit(15000)
class Toivenon:
	def __init__(self):
		self.iteration=0
		self.combi2=[]
		self.combi1=[]

	def execute(self,input,support):
		#STEP 1 : pick a random sample and work on them
		
		def toiven():
			self.iteration = self.iteration + 1
			
			print str(self.iteration)
			p=0.4
			print p
			freq=[]
			sortuple=[]
			myList=[]
			myList2=[]
			fin=[]
			fin1=[]
			infreq=[]
			maincount={}
			mainlist=[]
			
			num_lines = sum(1 for line in open(input))
			num = num_lines * 40 / 100
			with open(input, "rb") as f:
				myList1 = [(line.rstrip('\n').split(',')) for line in f.readlines()]

			#sorting the list lexicographically
			for i in myList1:
				myList2.append(tuple(sorted(i)))
			mainlist=list(chain(*myList2))
			maincount=Counter(mainlist)
			random_choice = random.sample(myList2,num)
			f.close()
			
			#Step 2 : Perform apriori on it 
			#calculate frequent itemset for singletons
			randomlist=list(chain(*random_choice))
			newsupport=int(support)*8/10*40/100
			# Finding the count of each frequent item
			myList = Counter(randomlist)
			for key in myList:
				if myList[key]>=(newsupport):
					freq.append(key)
				else:
					infreq.append(key)
			fin = list(itertools.combinations(freq,2))
			fin1 = list(itertools.combinations(freq,3))
			#count the pairs greater than new threshold in self.combi is in the random sample
			countlist=[]
			freq1=[]
			countdict={}
			final=[]
			maincombi=[]
			maincombi1=[]
			newfreq=[]
			def subsettuplevalid(a,b):
				for i in b:
					if sorted(i)==sorted(a):
						return tuple(i)
			for line in random_choice:
				self.combi = sorted(list(itertools.combinations(line,2)))
				self.combi2 = sorted(list(itertools.combinations(line,3)))
				for pair in fin:
						countlist.append(subsettuplevalid(pair,self.combi))
				for pair in fin1:
						countlist.append(subsettuplevalid(pair,self.combi2))
			countdict= Counter(tuple(countlist))
			for k,v in countdict.iteritems(): 
				if k != None:
					if v>=newsupport:
						freq.append(k)

					else:
						infreq.append(k) 


			negborder=[]
			combi1=[]
			clist=[]
			cdict=[]
			dlist=[]
			ddict={}
			freqmain=[]
			newfreq=[]
			newfreq1=[]
			newfreq2=[]
			#constructing negative border
			#if items are single elements cos every empty set is a freq set#imm subset are in freq
			def nCr(n,r):
				f = math.factorial
				return f(n) / f(r) / f(n-r)
			for i in infreq:
				if len(i)==1:
					negborder.append(i)
				elif len(i) > 1:
					l=len(i)
					combi1 = sorted(list(itertools.combinations(i,l-1)))
					flag=0
					for elem in combi1:
						elem=list(elem)
						for e in elem:
							#print str(e)+"<---e"
							if e in freq:
								flag=flag+1
								#print flag
								if flag==nCr(l,l-1):
									negborder.append(i)
									#print "negborder append"+str(negborder)
								
			#print"\n"
			#print "neg border"
			#print negborder
			#print "\n"
			#check if items in negborder exist in main file
			#if any item in the negborder is found to be frequent in the main file
			#repeat toivenon
			def subsettuplevalid(a,b):
					a=list(a)
					for i in b:
						i=list(i)
						#print i,a
						if i==a:
							return a
			#filtering false positives
			#check if count in main file is greater than original support
			#print"new place"
			#print maincount
			#print "freq with false positives"
			#print freq

			for i in freq:
				if len(i)==1:
                    #print i
					for k,v in maincount.iteritems():
						if k==i:
							if int(v) >= int(support):
								newfreq.append(i)
								#print "newfreq append"+str(newfreq)
				elif len(i) > 1:
					for j in myList2:
						maincombi = sorted(list(itertools.combinations(j,2)))
						maincombi1 = sorted(list(itertools.combinations(j,3)))
						if i in maincombi:
							dlist.append(i)
						if i in maincombi1:
							dlist.append(i)
							#print "dlist append"+str(dlist)
			#print"dlist"
			#print dlist
			ddict=Counter(dlist)
			
			#print "ddict"
			#print ddict
			

			for k,v in ddict.iteritems():
				if int(v) >= int(support):
					newfreq2.append(list(k))
			#print "newfreq2"
			#print newfreq2
					#print "newfreq append"+str(newfreq)
			len2=[]
			len3=[]
			if len(infreq) == 0:
				#print "filterd stuff"
				print sorted(newfreq)
				for i in newfreq2:
					if len(i)==2:
						len2.append(i)
					elif len(i)==3:
						len3.append(i)
				print sorted(len2)
				if len(len3)!=0:
					print sorted(len3)
			for i in newfreq:
				newfreq1.append(list(i))
			#print "newfreq1"
			#print newfreq1



			neglen= len(negborder)
			flag1=0
			for i in negborder:
				if len(i)==1:
					for k,v in maincount.iteritems():
						if k==i:
							if int(v) >= int(support):
								toiven()
							else:
								flag1=flag1+1
								if flag1 == neglen:
									#print "INSIDE1"
									print sorted(newfreq1)
									#print newfreq2
									for i in newfreq2:
										if len(i)==2:
											len2.append(i)
										elif len(i)==3:
											len3.append(i)
									print sorted(len2)
									if len(len3)!=0:
										print sorted(len3)
									#return
				elif len(i)> 1:
					for j in myList2:
						maincombi = sorted(list(itertools.combinations(j,2)))
						maincombi1 = sorted(list(itertools.combinations(j,3)))
						if i in maincombi:
							clist.append(i)
						if i in maincombi1:
							clist.append(i)

			cdict=Counter(tuple(clist))
			#print cdict
			for k,v in cdict.iteritems():
				if int(v) >= int(support):
					toiven()
					 
				else:
					flag1=flag1+1
					if flag1 == neglen:
						#print "INSIDE2"
						print sorted(newfreq1)
						#print newfreq2
						for i in newfreq2:
							if len(i)==2:
								len2.append(i)
							elif len(i)==3:
								sorted(len3.append(i))
						print len2
						if len(len3)!=0:
							print sorted(len3)
						return 
				


			#print "finally workssss  -NOT!"
			#print newfreq
		toiven()






		
if __name__ == '__main__':
	toi = Toivenon()
	toi.execute(sys.argv[1],sys.argv[2])