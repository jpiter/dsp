# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Q1 Response:

```rm -rf anydirectory``` deletes a directory even if it is not empty


```rm *.txt``` deletes all text files


```cp dir1/file1.txt dir2/``` would copy file1.txt from dir1 to dir2


```touch newfile.txt``` creates new text file


```grep someword *.txt``` searches for the word "someword" in all text files in the directory


```cat > newfile.txt``` creates and opens input to a text file, you have to finish input with CTRL-D


```export``` creates new environment variable


```echo $VAR``` accesses the value of environmental variable VAR


```env``` prints out all environmental(global) variables


```env | grep USER``` finds all environmental variables with a word USER in the name of a variable or in its value


```$|$``` takes the output from the command on the left from | , and "pipes" it to the command on the right


```mv``` renames files and directories


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > Q2 Response:

`ls` lists out all directories and files in working directory


`ls -a` includes directory entries whose name starts with a .


`ls -l` lists directories and file names with details; the total size of all files is displayed in the terminal.


`ls -lh` uses unit suffixes Byte, Kilobyte, etc., to display file size.


`ls -lah` includes directory entries whose name starts with a . with details


`ls -t` sorts directory entries by time modified (most recently modified first) 


`ls -Glp` this combination displays content of the directory with details using colorized input and a backslash(/) after each directory name

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > Q3 Response:

`ls -R` recursively lists all subdirectories encountered

`ls -S` sort files by size

`ls -r` reverses the order of the sort

`ls -m` displays the names as a comma-separated list

`ls -1` displays directory content as one entry per line


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

