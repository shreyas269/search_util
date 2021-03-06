import os
import re
import shelve
from nltk.stem.porter import *


#Search function based on [product(1+lambda*ai)] formula

def search(q):
		stemmer=PorterStemmer()

		tokens=shelve.open('tokens1.db')

		queries=q.split(' ')
		for i in range(len(queries)):
			queries[i]=str(stemmer.stem(queries[i]))


		query_list=[]


		for query in queries:
			if query in tokens.keys():
				v={}
				i=0
				for w in sorted(tokens[query], key=tokens[query].get, reverse=True):
							v[w]=tokens[query][w]	
							i+=1
							if i>10:
								break
				query_list.append(v)

		temp={}
		query_len=len(query_list)
		_lambda=10

		for i in range(query_len):
			for word in query_list[i]:
				if word not in temp.keys():
					temp[word]=(1+_lambda*query_list[i][word])
					for j in range(query_len):
						if i==j:
							continue
						if word in query_list[j].keys():
							temp[word]*=1+_lambda*query_list[j][word]
								

			


		return  sorted(temp,key=temp.get,reverse=True)[:10]






