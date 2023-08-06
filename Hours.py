'''  Problem Statment 

Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts'''

# Variable declartion 

file_data = [] 
Time_data = []
Hours = {}   # dictionary to hold hours(key) and number of count(value)
Hours_count = 1
Hours_timing = []

# Opening the file mbox-short 
with open("mbox-short.txt", "r") as file:
    file_data = file.readlines()



for line in file_data:
    if line.startswith("From "):
        time = line.split()[5]
        Time_data.append(time);
       
for time in Time_data:
    hour = time.split(":")[0]
    Hours_timing.append(hour)

    # condtion to check if the hour repeats
    if hour in Hours:
        Hours[hour] += 1
    else :
        Hours[hour] = Hours_count 

# Printig the final output
print(Hours)



