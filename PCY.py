# -*- coding: utf-8 -*- 
from string import lowercase as letters
import sys
import itertools
from collections import Counter
from collections import defaultdict
from itertools import chain
from collections import OrderedDict

class Pcy1:
	def __init__(self):
		self.intermediate={}
		self.dmap = []
		self.freq=[]
		self.combi=[]
		self.combi1=[]
		self.lst=[]
		self.lst1=[]
		self.lst2=[]
		self.hashlist=[]
		self.bucket=[]
		self.intermediate1={}
		self.bitmaplist1=[]
		self.sortuple=[]
		self.countdict={}
		self.countlist=[]	

		
	def execute(self,input,bucket,support):
	#STEP 1:
		#reading buckets as a list of tuples
		with open(input) as f:
   	      	  myList = [(line.rstrip('\n').split(',')) for line in f.readlines()]
     	
		#print myList
	
		#converting input into numbers

		def modifyval(tup):
   		  self.lst=list(tup)
		  #print self.lst
		  for j in self.lst:
       			ind=self.lst.index(j)
			self.lst[ind]=ord(j)-96
		  self.lst1.append(tuple(self.lst))
 
		for i in myList:
			self.sortuple = tuple(sorted(i))
			modifyval(self.sortuple)
		#print "list in integers"				
		#print self.lst1	
		
	#STEP 2: Finding frequent items across tuples for each item		

		self.lst2=list(chain(*self.lst1))
		# Finding the count of each frequent item
		self.lst2 = Counter(self.lst2)
		for key in self.lst2:
			if self.lst2[key]>=support:
				self.freq.append(key)
		print "frequent items" 
		for k in self.freq:
			a=str(unichr(k+96))
			self.bucket.append(a)
		#printing in character
		print self.bucket
	
		h=2
	#STEP 3: Finding combinations for each tuple in the list
		def  candi(h):
			finalist=[]
			bitmaplist=[]
			intermediate={}
			fin=[]
			final2=[]
			countdict={}
			countlist=[]
			def frequent_items(key,value):
				intermediate.setdefault(key, [])
				intermediate[key].append(value)
				

			#self.lst1 is the integer list 
			#taking each tuple as a list and summing the values that get hashed in each bucket (+1 for each value being hashed)
			def hashing_fn(list1):
				for i in list1:
					i=list(i)
					sum1=sum(i)
					key=sum1%bucket
					frequent_items(key,1)

			# Updating the bucket count
				for key in intermediate:
					sum2=sum(intermediate[key])
					self.intermediate1.setdefault(key, [])
					self.intermediate1[key]=sum2
		
			#Hashing is done for each tuple in terms of combi of 2 - make 2 as h
			for i in self.lst1:
				self.combi = list(itertools.combinations(i,h))
				# we take one line-combinations at a time and generate hash fn
				hashing_fn(self.combi)
			print self.intermediate1	
			#Updating the bitmap list to find out frequent buckets
			for key,value in self.intermediate1.iteritems():
				#print key,value
				if value>=support:
					bitmaplist.append(1)
				else:
					bitmaplist.append(0)
				
			#print "bitmap"
			#print bitmaplist
			flag=0
			for i in bitmaplist:
				if i==1:
					flag=1
			if flag==0:
				return -1
		#step 5	
			#check for each pair of items if each of them are frequent items and if they hash to the same bitmap
			def subsetvalid(list1,list2):
				for item in list1:
					if item not in list2:
						return False
				return True

			for i in self.lst1:
				self.combi = list(itertools.combinations(i,h))
				for j in self.combi:
					j=list(j)
					sum3=sum(j)
					key=sum3%bucket
					k=subsetvalid(j,self.freq)
					if bitmaplist[key]==1 and int(k):
						j=tuple(j)
						finalist.append(j)
				finalist = list(OrderedDict.fromkeys(finalist))

			def modifyback(tup):
				self.lst=list(tup)
				for j in self.lst:
					ind=self.lst.index(j)
					self.lst[ind]=str(unichr(j+96))
				fin.append((self.lst))
			for i in finalist:
				modifyback(i)
			#print "Candidate pairs:"
			#print fin
			def subsettuplevalid(a,b):
				for i in b:
					i=list(i)
					if i==a:
						return tuple(i)
			
			
			#checking against the entire file
			with open(input) as f:
				for line in f:
					myList1 = line.rstrip('\n').split(',')
					myList1=sorted(myList1)
					self.combi = sorted(list(itertools.combinations(myList1,h)))
					for pair in fin:
						countlist.append(subsettuplevalid(pair,self.combi))
					#print self.countlist	
		
			countdict= Counter(tuple(countlist))
			#print countdict
			for k in countdict:	
				if countdict[k]>=support and k != None :
					final2.append(list(k))
			#print "final pairs"
			print("\n")
			print final2
			print("\n")
			return 1	
		while h>1 and h<4:
			a=candi(h)
			if a == -1:	
				break
			h=h+1
						
						
						
		
if __name__ == '__main__':
	pc = Pcy1()
	pc.execute(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))






