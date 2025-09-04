total_minutes= input("please type the number of minutes: \n")
int_minutes= int(total_minutes)
hours= int_minutes // 60
minutes= int_minutes % 60
print("This course is:"+str(hours)+"hours and "+str(minutes)+"minutes long")