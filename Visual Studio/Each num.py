#num=[1,2,3,4,5]
#num=1+2+3+4+5
#print(num)



#num=["1","2","3","4","5"]
#a=str(input("Let's add each num to the next \n-> "+num[0]))
#print("the total num is: "+num[0])
#for i in range(1,len(num)):
 #   a=input("Let's add each num to the next \n-> "+num[i])
  #  num[0]=num[0]+num[1]
   # print("the total num is: "+num[0])



num=[1,2,3,4,5]
totle=0
print("Let's add each num to the next")
for a in num:
    totle += a
    print(f"-> {totle}")
print(f"\nThe final total num is: {totle}\n")


