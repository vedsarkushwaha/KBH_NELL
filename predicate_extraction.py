from read_data import read_graph_nodes,read_relation_name
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

if __name__=="__main__":
	relations=read_relation_name('nell_pca_svo_pra')
	
	dict1={}
	with open(os.path.join('nell_pca_svo_graph','node_dict.tsv'),'r') as fp:
		for line in fp:
			line=line.rstrip('\n')
			n_id,name=line.split('\t')
			dict1[int(n_id)]=name
	
	user_query=raw_input("Enter the query: ")
	ans_found=0
	#print relations
	for j in relations:
		if j in user_query: #this is where we use paraphrasing
			#print the answer. node convert. etc
			#read relation nodes obtained by PRA
			i='concept:'+''.join(j.split(" "))+'/scores.tsv'
			source_list=[]
			target_list=[]
			score_list=[]
			with open(os.path.join('nell_pca_svo_pra',i),'r') as fp:
				for line in fp:
					if(chk_line(line)):
						n1,n2,score=map(float,line.split('\t')[:3])
						if score>1:
							source_list.append(n1)
							target_list.append(n2)
							score_list.append(score)
				#convert node to human readable forms
			source_list=read_graph_nodes(dict1,source_list)
			target_list=read_graph_nodes(dict1,target_list)
			#match nodes with user query
			for ii in xrange(len(source_list)):
				print source_list[ii].split(":")[2]+' '+j+' '+target_list[ii].split(":")[2]+' '+str(score_list[ii])
			ans_found=1
	if ans_found==0:
		print 'Not found anything relevant'
