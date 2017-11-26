# Commands
RM := rm -f

# Run to clean and rebuild xml files
all: clean dblp-query gen-html

clean: 
	$(RM) *.xml

dblp-query:
	wget http://dblp.org/search/publ/api?q=author%3AIvan_Beschastnikh%3A -O ivan.xml
	wget http://dblp.org/search/publ/api?q=author%3AAndrew_Warfield%3A -O andy.xml
	wget http://dblp.org/search/publ/api?q=author%3AWilliam_Aiello%3A -O bill.xml
	wget http://dblp.org/search/publ/api?q=author%3AMichael_J._Feeley%3A -O mike.xml
	wget http://dblp.org/search/publ/api?q=author%3ANorman_C._Hutchinson%3A -O norm.xml
	wget http://dblp.org/search/publ/api?q=author%3AAlan_Wagner%3A -O alan.xml

gen-html:
	python parser.py
	cp pub_list.html ../html

.PHONY: all clean
