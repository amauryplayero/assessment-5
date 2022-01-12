log_file = open("um-server-01.txt")

#declaring a function with def named sales_reports with an parameter of log_file
def sales_reports(log_file):
    #starting a for loop with index[i]=line in log_file
    for line in log_file:
        #removes space between lines 
        line = line.rstrip()
        #printing first three characters on line starting on index of 0
        day = line[0:3]
        # if day equals to Tuesday, it will print the whole line in the loop.
        # if day == "Tue":
            # print(line)

#calling the function passing in the argument
# sales_reports(log_file)

# -------

def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
