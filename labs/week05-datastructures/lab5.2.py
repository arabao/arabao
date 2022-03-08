# program stores months of the year in a tuple
# and from that tuple creates annother tuple with just the summer months
# and prints the summer months one at a time
# Auther: Tosin Araba

months = ("January",
             "February",
             "March",
             "April",
             "May",
             "June",
             "July",
             "August",
             "September",
             "October",
             "November",
             "December"
)
summer = months[4:7]
for month in summer:
    print (month)