Requirement to run this program
=========================================================
Package requirements
-------------------------------
1. python 2.7, if you are using linux then you can install it using the command "sudo-apt-get install python"

2. nltk toolkit, command for linux user "sudo apt-get install python-nltk"
   a. In nltk toolkit, you should install stopwords additionally

3. python wordsegment is used to put spaces between relations.
command to install of linux system "sudo apt-get install python-wordsegment"
-------------------------------
Directory structure requirements
-------------------------------
1. nell
   a. nell directory should contains: subdirectories a) relations
   
2. nell_pca_svo_graph
   a. this directory should contains node_dic.tsv and edge_dict.tsv
   
3. nell_pca_svo_pra
   a. this directory should contains subdirectories as relation name. Basically this directory will be the output of PRA code.

4. svo_file.tsv

5. ppdb
	this directory should contain the following ppdb files
   a. ppdb-1.0-s-lexical
   b. ppdb-1.0-s-m2o
   c. ppdb-1.0-s-o2m
   d. ppdb-1.0-s-phrasal
=========================================================
There are multiple driver file which one can interact to get the results. Two of them are most important.

1. ques_ans.py -> run this file using python command "python ques_ans.py"
This driver will take user query as input and output the answer and the relations. Note that this internally uses SVO triples.

2. predicate_extraction_combi.py -> run this file using python command "python predicate_extraction_combi.py"
This driver file will again take the user query and output relations only. Note that this driver does not uses SVO triples.

There is an further predicate_extraction_read_me file which will guide you how to extract predicate from user queries.
