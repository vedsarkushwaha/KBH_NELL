from wordsegment import segment
import os

'''
 * python file which creates dictionary for relations
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

def create_dict():
	relation_name=[x[2] for x in os.walk("nell/relations")][0]
	sub_table={}
	obj_table={}
	for r in relation_name:
		lst=[]
		r_name=' '.join(segment(r.split(':')[1]))
		print r_name
		with open("nell/relations/"+r) as fp:
			for line in fp:
				line=line.rstrip('\n')
				sub,obj=line.split('\t')
				sub=' '.join((sub.split(":")[2]).split('_'))
				obj=' '.join((obj.split(":")[2]).split('_'))
				if sub in sub_table:
					tmp=sub_table[sub]
					tmp=tmp.union([r_name])
					sub_table[sub]=tmp
					#print("y")
				else:
					sub_table[sub]=set([r_name])
				if obj in obj_table:
					tmp=obj_table[obj]
					tmp=tmp.union([r_name])
					obj_table[obj]=tmp
					#print("yy")
				else:
					obj_table[obj]=set([r_name])
				#print len(sub_table[sub]),len(obj_table[obj])
	return sub_table,obj_table
	
def create_dict_adva():
	relation_name=[x[2] for x in os.walk("nell/relations")][0]
	sub_table={}
	obj_table={}
	for r in relation_name:
		lst=[]
		r_name=' '.join(segment(r.split(':')[1]))
		print r_name
		with open("nell/relations/"+r) as fp:
			for line in fp:
				line=line.rstrip('\n')
				sub,obj=line.split('\t')
				sub=sub.split(":")[1:]
				obj=obj.split(":")[1:]
				for tmp in sub:
					tmpsb=''.join(tmp.split('_'))
					tmpsb=segment(tmpsb)
					for sb in tmpsb:
						if sb in sub_table:
							tmp=sub_table[sb]
							tmp=tmp.union([r_name])
							sub_table[sb]=tmp
							#print("y")
						else:
							sub_table[sb]=set([r_name])
				for tmp in obj:
					tmpob=''.join(tmp.split('_'))
					tmpob=segment(tmpob)
					for ob in tmpob:
						if ob in obj_table:
							tmp=obj_table[ob]
							tmp=tmp.union([r_name])
							obj_table[ob]=tmp
							#print("yy")
						else:
							obj_table[ob]=set([r_name])
	return sub_table,obj_table
