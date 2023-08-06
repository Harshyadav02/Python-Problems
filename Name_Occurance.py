'''Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop
to find the most prolific committer.'''


# Opening mbox-short file 
file = open('mbox-short.txt','r')

# Dictionary which will hold the names and the counts of sender
name_count = {}

for line in file:
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            committer = words[1]
            name_count[committer] = name_count.get(committer, 0) + 1
print(name_count)


file.close()




