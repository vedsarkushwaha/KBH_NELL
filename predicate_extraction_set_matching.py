from read_data import read_relation_name
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import os

'''
 * python file to match number of words
 *
 * Copyright 2015 Vedsar
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

def set_matching(relations,user_query,dict1):
	ans_found=0
	#print relations
	stemmer=SnowballStemmer('english')
	user_query_list=map(str,map(stemmer.stem,word_tokenize(user_query)))
	user_query_set=set(user_query_list)
	r=[]
	#print user_query_set
	for j in relations:
		#print j
		relation_list=map(str,map(stemmer.stem,word_tokenize(j)))
		relation_set=set(relation_list)
		#print relation_set
		#print relation_set, user_query_set
		#print relation_set,relation_set.intersection(user_query_set),len(relation_set),len(relation_set.intersection(user_query_set))
		if len(relation_set.intersection(user_query_set))>=0.6*len(relation_set):
			r.append(j)
			ans_found=1
	return r

if __name__=="__main__":
	#print "Reading Relations from Graph"
	relations=read_relation_name('nell_pca_svo_pra')
	dict1={}
	with open(os.path.join('nell_pca_svo_graph','node_dict.tsv'),'r') as fp:
		for line in fp:
			line=line.rstrip('\n')
			n_id,name=line.split('\t')
			dict1[int(n_id)]=name
			
	user_query=raw_input("Enter the query: ")
	r=set_matching(relations,user_query,dict1)
	if(len(r)==int(0)):
		print 'Not found anything relevant'
	else:
		for i in r:
			print i
