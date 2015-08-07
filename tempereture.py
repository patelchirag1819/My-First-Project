
i=0
while(i<4):
    temp = input("Enter temp: ")
    temp=int(temp)
    i=i+1
    if temp>=31 and temp<35:
        print ("Sunny Day")
        
    elif temp>35 and temp<40:
        print ("Warn Day")
        
    elif temp>40 and temp<50:
        print ("High Tempereture")
        
    else:
        print("Invalid ")
