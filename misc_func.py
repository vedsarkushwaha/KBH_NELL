from nltk.corpus import stopwords
from nltk import word_tokenize,pos_tag
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import csv
import pickle

'''
 * python file containing MISC functions
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

def remove_stopwords(lst):
	sw = stopwords.words("english")
	fltr=[]
	for i in lst:
		if i not in sw:
			fltr.append(i)
	return fltr

def lst1_in_lst2(lst1,lst2):
	"""
		if lst1 in lst2 return 1 else return 0
	"""
	for i in lst1:
		if not i in lst2:
			return 0
	return 1

def convert_svo(fname):
	stemmer=SnowballStemmer('english')
	optname=fname[:-4]+str("_modi.csv")
	lst=[]
	opfname=open(optname,'w')
	with open(fname) as fp:
		for line in fp:
			line=line.strip('\n')
			tmp=line.split('\t')
			tmp[0]=remove_stopwords(map(str,map(stemmer.stem,word_tokenize(tmp[0]))))
			tmp[1]=map(str,map(stemmer.stem,word_tokenize(tmp[1])))
			tmp[2]=remove_stopwords(map(str,map(stemmer.stem,word_tokenize(tmp[2]))))
			#opfname.write(str(tmp[0])+","+str(tmp[1])+","+str(tmp[2])+"\n")
			lst.append(tmp)
			#print tmp
	with open(optname,'wb') as f:
		pickle.dump(lst,f)

if __name__=="__main__":
	convert_svo("svo_file.tsv")
