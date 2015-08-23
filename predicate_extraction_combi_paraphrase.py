from read_data import read_relation_name,read_ppdb
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from predicate_extraction_set_matching import set_matching
from predicate_extraction_node_matching import node_matching
from algo_func import lst1_in_lst2
import os

'''
 * python file to extract predicate
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

def combi_matching(relations, user_query, dict1):
	ans_found=0
	#print user_query
	ans_found=set_matching(relations,user_query,dict1)
	ans_found.extend(node_matching(relations,user_query,dict1))
	return ans_found

def paraphrase(relations,user_query,dict1):
	print "loading lexical paraphrase"
	ppdb_lex=read_ppdb('ppdb/ppdb-1.0-s-lexical')
	print "loading one-to-phrasal paraphrase"
	ppdb_otm=read_ppdb('ppdb/ppdb-1.0-s-o2m')
	print "loading phrasal-to-one paraphrase"
	ppdb_mto=read_ppdb('ppdb/ppdb-1.0-s-m2o')
	print "loading one-to-many paraphrase"
	ppdb_mtm=read_ppdb('ppdb/ppdb-1.0-s-phrasal')
	#user_query paraphrasing using n-grams
	print "lex ppbd"
	user_query_paraphrases=[]
	user_query_paraphrases.append(user_query)
	for i in ppdb_lex:
		if user_query.find(i[1])!=-1:
			if i[1] in user_query.split(' '):
				ind=user_query.split(' ').index(i[1])
				user_query_paraphrases.append(user_query[ind-1:].replace(i[1],i[2]))
	ans_found=[]
	print "number of paraphrases formed"+str(len(user_query_paraphrases))
	print user_query_paraphrases
	for i in user_query_paraphrases:
		ans_found.extend(combi_matching(relations,i,dict1))
	if(len(ans_found) == int(0)):
		print 'Not found anything relevant'
	else:
		for i in ans_found:
			print i
			
	print "one to phrasal"
	user_query_paraphrases=[]
	user_query_paraphrases.append(user_query)
	for i in ppdb_otm:
		if user_query.find(i[1])!=-1:
			if i[1] in user_query.split(' '):
				ind=user_query.split(' ').index(i[1])
				user_query_paraphrases.append(user_query[ind-1:].replace(i[1],i[2]))
	print "number of paraphrases formed"+str(len(user_query_paraphrases))
	print user_query_paraphrases
	ans_found=[]
	for i in user_query_paraphrases:
		ans_found.extend(combi_matching(relations,i,dict1))
	if(len(ans_found) == int(0)):
		print 'Not found anything relevant'
	else:
		for i in ans_found:
			print i
			
	print "phrasal to one"
	user_query_paraphrases=[]
	user_query_paraphrases.append(user_query)
	for i in ppdb_mto:
		if user_query.find(i[1])!=-1:
			if lst1_in_lst2(i[1].split(' '),user_query.split(' ')):
				ind=user_query.split(' ').index(i[1])
				user_query_paraphrases.append(user_query[ind-1].replace(i[1],i[2]))
	print "number of paraphrases formed"+str(len(user_query_paraphrases))
	print user_query_paraphrases
	ans_found=[]
	for i in user_query_paraphrases:
		ans_found.extend(combi_matching(relations,i,dict1))
	if(len(ans_found) == int(0)):
		print 'Not found anything relevant'
	else:
		for i in ans_found:
			print i		
			
	print "phrasal to phrasal"
	user_query_paraphrases=[]
	user_query_paraphrases.append(user_query)
	for i in ppdb_mtm:
		if user_query.find(i[1])!=-1:
			if lst1_in_lst2(i[1].split(' '),user_query.split(' ')):
				ind=user_query.split(' ').index(i[1])
				user_query_paraphrases.append(user_query[ind-1:].replace(i[1],i[2]))
	print "number of paraphrases formed"+str(len(user_query_paraphrases))
	print user_query_paraphrases
	#print user_query
	ans_found=[]
	for i in user_query_paraphrases:
		ans_found.extend(combi_matching(relations,i,dict1))
	if(len(ans_found) == int(0)):
		print 'Not found anything relevant'
	else:
		for i in ans_found:
			print i
	#print user_query_paraphrases
	#user_query paraphrase

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
	paraphrase(relations,user_query,dict1)
