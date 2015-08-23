from nltk import word_tokenize,pos_tag
from nltk.corpus import stopwords
from read_ppdb import read_ppdb
from nltk.util import ngrams
from math import ceil

########PPDB DATABSE##########

'''
 * python file to drive the program using PPDB word distribution
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
	ppdb_lex=read_ppdb('ppdb/ppdb-1.0-s-lexical')
	print "loading lexical paraphrase"
	ppdb_otm=read_ppdb('ppdb/ppdb-1.0-s-o2m')
	print "loading one-to-phrasal paraphrase"
	ppdb_mto=read_ppdb('ppdb/ppdb-1.0-s-m2o')
	print "loading phrasal-to-one paraphrase"
	ppdb_mtm=read_ppdb('ppdb/ppdb-1.0-s-phrasal')
	print "loading one-to-many paraphrase"
	user_query=raw_input("Enter the query")
	ppdb_lex_match_sen=[]
	ppdb_lex_match_sen.append(user_query)
	for i in ppdb_lex:
		if i[1] in user_query:# and user_query[user_query.index(i[1])-1]==' ' and user_query[user_query.index(i[1])+1]==' ':
			tmp=user_query
			ppdb_lex_match_sen.append(tmp.replace(i[1],i[2]))
	ppdb_otm_match_sen=[]
	ppdb_otm_match_sen.append(user_query)
	for i in ppdb_otm:
		if i[1] in user_query:# and user_query[user_query.index(i[1])-1]==' ' and user_query[user_query.index(i[1])+1]==' ':
			tmp=user_query
			ppdb_otm_match_sen.append(tmp.replace(i[1],i[2]))
	ppdb_mto_match_sen=[]
	ppdb_mto_match_sen.append(user_query)
	for i in ppdb_mto:
		if i[1] in user_query:# and user_query[user_query.index(i[1])-1]==' ' and user_query[user_query.index(i[1])+1]==' ':
			tmp=user_query
			ppdb_mto_match_sen.append(tmp.replace(i[1],i[2]))
	ppdb_mtm_match_sen=[]
	ppdb_mtm_match_sen.append(user_query)
	for i in ppdb_mtm:
		if i[1] in user_query:# and user_query[user_query.index(i[1])-1]==' ' and user_query[user_query.index(i[1])+1]==' ':
			tmp=user_query
			ppdb_mtm_match_sen.append(tmp.replace(i[1],i[2]))
	for i in ppdb_lex_match_sen:
		print i
	for i in ppdb_otm_match_sen:
		print i
	for i in ppdb_mto_match_sen:
		print i
	for i in ppdb_mtm_match_sen:
		print i
