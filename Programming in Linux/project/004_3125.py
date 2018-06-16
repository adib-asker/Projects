#!/usr/bin/python
import sys
import os
import re
import sys
import pymysql

from xml.dom.minidom import parse, parseString

# convert to xhtml
# use: java -jar tagsoup-1.2.jar --files html_file
def html_to_xml(fn):
   os.system("java -jar tagsoup-1.2.jar --files "+fn)
   xhtml_fn = fn.replace('.html','.xhtml')
   return xhtml_fn

def get_text(e):
    if len(e.childNodes) > 1:
        aElem = e.childNodes[1]
        return aElem.firstChild.toxml()

    return e.firstChild.nodeValue

# remove leading and trailing whitespace chars
def remove_white_space(str):
   p = re.compile(r'\s+')
   new = p.sub(' ',str)   # a lot of \n\t\t\t\t\t\t
   return new.strip()

# replace but these chars including ':'
def replace_non_alpha_numeric(s):
   p = re.compile(r'[^a-zA-Z0-9\.()-]+')
   new = p.sub('',s)
   return new.strip()

def extract_text(cell_list):
   lst=[]
   for cell in cell_list:
       text=get_text(cell);
       text=remove_white_space(text)
       text=replace_non_alpha_numeric(text)
       lst.append(text)
   return lst


def insert_to_table(cur, tbl, lst):
   sql = "INSERT INTO "+tbl+" (id, issue, volume, price, diff, percent) VALUES (%s, '%s', %s, %s, %s, %s)" % (lst[0], lst[1], lst[2], lst[3], lst[4], lst[5])
   cur.execute(sql)

def select_from_db(cur, tbl):
   sql = "SELECT * FROM " + tbl
   cur.execute(sql)

   while True:
       row = cur.fetchone()
       if row == None:
           break
       print(row)


def main():
   html_fn = sys.argv[1]
   fn = html_fn.replace(".html","");
   xhtml_fn = html_to_xml(html_fn)

   dom = parse(xhtml_fn)

   #initialize connection to database
   #conn = pymysql.connect(host="dbserver", user="ucid",passwd="password")
   conn = pymysql.connect(host="localhost", user="root", passwd="mysql")
   conn.select_db("ucid")
   #(re)create the table
   cur = conn.cursor()
   query_text = "DROP TABLE IF EXISTS " + fn
   cur.execute(query_text)
   query_text = "CREATE TABLE `"+fn+"` ( `id` int(11) NOT NULL AUTO_INCREMENT,\
                                            `issue` varchar(255) COLLATE utf8_bin NOT NULL,\
                                            `volume` int(11) NOT NULL,\
                                            `price` float NOT NULL,\
                                            `diff` float NOT NULL,\
                                            `percent` float NOT NULL,\
                                                PRIMARY KEY (id))"
   cur.execute(query_text)

   #extract values and insert them into database
   table = None
   for tbl in dom.getElementsByTagName('table'):
       if tbl.getAttribute('class') == 'mdcTable':
           table = tbl
           break

   row_list = table.getElementsByTagName('tr')
   for row in row_list[1:]:
       #print row.toxml()
       cell_list = row.getElementsByTagName('td')
       text_list = extract_text(cell_list)
       insert_to_table(cur, fn, text_list)

   #read the values back from the database
   # display the table on the screen
   select_from_db(cur, fn)
   conn.commit()
   cur.close()
   conn.close()

# end of main()

if __name__ == "__main__":
    main()
