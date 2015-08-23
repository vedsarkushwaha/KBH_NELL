from read_data import read_graph_nodes,read_relation_name
import os
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize

'''
 * python file which matches verbs
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

def chk_line(line):
	if len(line)==0:
		return 0
	lst=line.split('\t')
	if len(lst)<3:
		return 0
	for i in lst:
		if len(i)<1:
			return 0
	return 1

def node_matching(relations,user_query,dict1):
	stemmer=SnowballStemmer('english')
	user_query_list=map(str,map(stemmer.stem,word_tokenize(user_query)))
	user_query_set=set(user_query_list)
	ans_found=0
	r=[]
	#print user_query_list
	#print relations
	for j in relations:
		#get the subject and object for j
		i='concept:'+''.join(j.split(" "))+'/scores.tsv'
		source_list=[]
		target_list=[]
		score_list=[]
		#print j
		with open(os.path.join('nell_pca_svo_pra',i),'r') as fp:
			for line in fp:
				if(chk_line(line)):
					n1,n2,score=map(float,line.split('\t')[:3])
					if score>1:
						#print n1,n2
						source_list.append(n1)
						target_list.append(n2)
						score_list.append(score)
		#convert node to human readable forms
		source_list=read_graph_nodes(dict1,source_list)
		target_list=read_graph_nodes(dict1,target_list)
		#if any of source list and target list is in user_query_set and 60 % of other user query text matches with the relation j, then print that relation
		#this is where we use similarity technique
		for i in range(len(source_list)):
			#print source_list[i].split(":")[2],target_list[i].split(":")[2]
			if stemmer.stem(source_list[i].split(":")[2]) in user_query_list and stemmer.stem(target_list[i].split(":")[2]) in user_query_list:
				#print source_list[i],target_list[i]
				#get both nodes info, get relation from graph, check 60% matching with user query
				relation_info=map(str,map(stemmer.stem,word_tokenize(j)))
				relation_info.extend(map(str,map(stemmer.stem,(source_list[i].split(":")[1:]))))
				relation_info.extend(map(str,map(stemmer.stem,(target_list[i].split(":")[1:]))))
				relation_info_set=set(relation_info)
				#print relation_info_set,user_query_set
				#print len(relation_info_set.intersection(user_query_set)),len(relation_info_set)/2
				if len(relation_info_set.intersection(user_query_set))>len(relation_info_set)*0.4:
					r.append(j)
					ans_found=1
	return r

if __name__=="__main__":
	relations=read_relation_name('nell_pca_svo_pra')
	
	dict1={}
	with open(os.path.join('nell_pca_svo_graph','node_dict.tsv'),'r') as fp:
		for line in fp:
			line=line.rstrip('\n')
			n_id,name=line.split('\t')
			dict1[int(n_id)]=name
			
	user_query=raw_input("Enter the query: ")
	r=node_matching(relations,user_query,dict1)
	if(len(r)==0):
		print 'Not found anything relevant'
	else:
		for i in r:
			print i
