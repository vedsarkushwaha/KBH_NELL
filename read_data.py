import os,pickle
from wordsegment import segment
from nltk import word_tokenize,pos_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from misc_func import lst1_in_lst2,remove_stopwords

'''
 * python file to read data from PPDB, Knowledge Graphs
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

def read_ppdb(fname):
	"""
		fname is the name of ppdb file
		return the sorted list in alphabatical order
		 where lst[0] is pos_tag
		 lst[1] is source word/paraphrase
		 lst[2] is target word/paraphrase
 	"""
	lst=[]
	with open(fname) as fp:
		for line in fp:
			tmp1,tmp2,tmp3=line.split('|||')[:3]
			tmp1=tmp1.strip(' ')
			tmp2=tmp2.strip(' ')
			tmp3=tmp3.strip(' ')
			lst.append([tmp1,tmp2,tmp3])
	#lst.sort()t
	return lst

def get_relation_fname(rel_str):
	return "concept:"+''.join(rel_str.split(' '))

def read_graph_nodes(dict1,node_list):
	"""
		fname is the file name which contains nodes of the graph
		node_list contains encrypted nodes from the pra
		
		This function will convert encrypted node_list to humain readable form
		
		return the converted list of nodes in the same order
		if any node is not convertable, then will return -1
	"""
	#print fname
	#dict1={}
	#with open(fname,'r') as fp:
	#	for line in fp:
	#		line=line.rstrip('\n')
	#		n_id,name=line.split('\t')
	#		dict1[int(n_id)]=name
	human_readable_node_list=[]
	for node in node_list:
		if int(node) in dict1:
			#print 'found'
			human_readable_node_list.append(dict1[node])
		else:
			human_readable_node_list.append('-1')
	return human_readable_node_list
	
def read_relation_name(folder_name):
	"""
		This function will look inside the folder folder_name and fetch out all relations where relations are the name of inside folder names. Here each folder name should have name format "concept:relation".
		
		return the list of relations
	"""
	#print folder_name
	folder_list=[]
	#print folder_name
	tmp=[x[0] for x in os.walk(folder_name)]
	#print tmp
	for name in tmp[1:]:
		#print name
		folder_list.append(' '.join(segment(name.split(':')[1])))
	return folder_list[1:]

def read_nell_relations():
	"""
		this function will read relations from nell graph
		
		return the list of relations
	"""
	rel=os.walk("nell/relations")
	relation=[]
	for i in rel:
		trel=i[2]
	for i in trel:
		relation.append(' '.join(segment(i.split(':')[1])))
	return relation

def read_from_file(fname,verb_list,w_list):
	"""
		fname is the name of svo file from where subject and object will be fetched
		verb_list is the list of verbs from user query
		w_list is the total words in the user query
		
		return ...
	"""
	#print str(fname)
	stemmer=SnowballStemmer('english')
	
	verb_list=map(str,map(stemmer.stem,verb_list))
	tmpword_list=remove_stopwords(map(str,map(stemmer.stem,w_list)))
	word_list=[]
	for i in tmpword_list:
		word_list.extend(i.split('_'))
	print verb_list,word_list
	filter_svo_list=[]
	print "svo loading..."
	with open(fname,'r') as f:
		svo_lst=pickle.load(f)
	print "svo loading completed"
	#print verb_list,word_list
	#with open(fname) as fp:
	for verb in verb_list:
		for tmp in svo_lst:
			if verb in tmp[1]:
				#chk the statement
				if lst1_in_lst2(tmp[0],word_list) and lst1_in_lst2(tmp[2],word_list):
					filter_svo_list.append(tmp)
	print "searching completed"
	return filter_svo_list
	
def get_node(rel_fname,usr_query):
	ans=[]
	#ele=get_ele(usr_query)
	score=0
	stemmer=SnowballStemmer('english')
	#print rel_fname
	#usr_query=remove_stopwords(map(str,map(stemmer.stem,word_tokenize(usr_query))))
	with open("nell/relations/"+rel_fname,'r') as fp:
		for line in fp:
			tmp=None
			#print line
			s,o=(line.strip('\n')).split('\t')
			#ts=remove_stopwords(map(str,map(stemmer.stem,[' '.join(x.split('_')) for x in s.split(':')[1:]])))
			ts=[' '.join(x.split('_')) for x in s.split(':')[1:]]
			#print ts
			if ts[0] in usr_query and ts[1] in usr_query:
				tmp=[o.split(':')[1:],'4']
			elif ts[0] in usr_query:
				tmp=[o.split(':')[1:],'1']
			elif ts[1] in usr_query:
				tmp=[o.split(':')[1:],'3']
			if tmp is not None:
				ans.append(tmp)
			tmp=None
			#print ts
			#ts=remove_stopwords(map(str,map(stemmer.stem,[' '.join(x.split('_')) for x in o.split(':')[1:]])))
			ts=[' '.join(x.split('_')) for x in o.split(':')[1:]]
			if ts[0] in usr_query and ts[1] in usr_query:
				tmp=[s.split(':')[1:],'4']
			elif ts[0] in usr_query:
				tmp=[s.split(':')[1:],'1']
			elif ts[1] in usr_query:
				tmp=[s.split(':')[1:],'3']
			if tmp is not None:
				ans.append(tmp)
			#print ts
			#print usr_query
	return ans
