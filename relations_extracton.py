from read_data import read_from_file
from nltk import word_tokenize,pos_tag
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from misc_func import remove_stopwords
from relations_dict import create_dict,create_dict_adva
import sys

'''
 * python file which extract relations from knowledge graph
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

if __name__=="__main__":
	print "graph loading in memory"
	sub,obj=create_dict_adva()
	print "graph loaded in memory"
	verb_tag=['VB','VBD','VBG','VBN','VBP','VBZ']
	while(1):
		query=raw_input()
		stemmer=SnowballStemmer('english')
		w_set=word_tokenize(query)
		p_tag=pos_tag(w_set)
		
		verb_list=[]
		print "user query configured"
	
		for i in p_tag:
			if(i[1] in verb_tag):
				verb_list.append(i[0])
		sub_obj=read_from_file('svo_file_modi.csv',verb_list,w_set)
		"""if len(sub_obj)==0:
			print "Not able to find subject and object in the query"
			sys.exit(0)
		"""
		relation=[]
		for so in sub_obj:
			#check all combinations of so[0] with so[2]
			for i in so[0]:
				for j in so[2]:
					try:
						tmprel=sub[i].intersection(obj[j])
						relation.append(tmprel)
					except KeyError:
						pass
		fil_word=remove_stopwords(w_set)
		tmpfil_word=[]
		for x in fil_word:
			tmpfil_word.extend(x.split('_'))
		print tmpfil_word
		for i in xrange(len(tmpfil_word)):
			for j in xrange(i+1,len(tmpfil_word)):
				#print fil_word[i],fil_word[j]
				try:
					tmprel=sub[tmpfil_word[i]].intersection(obj[tmpfil_word[j]])
					relation.append(tmprel)
				except KeyError:
					pass
		if(len(relation)==0):
			print "Information is not in KB"
		else:
			for i in relation:
				print i
