#Time Pass

# Sachin Chaudhari Toll PVT Limited....!!

print("Welcome To Sachin Chaudhari Toll PVT.")
Vehicle= input("What Type Of Vehicle You Are Driving? bike , car , truck ? ")
if Vehicle=="car":
    car =input("What Is Your car Wheel Type? 4W , 3W ? ")
    if car=="4W":
        print("You Need To Pay $20.")
        if car=="3W":
            print("You Need To Pay $15.")
        
elif Vehicle== "truck":
    truck=input("How Many Wheels Your truck Have? 12W , 8W , 6W ? ")
    if truck=="12W":
        charge=50
        print("You Charge To Pay $50.")    
    if truck=="8W":
     charge= 40
     print("Charge Need To Pay $40.")
    if truck=="6W":
     charge=30
     print("Charge Need To Pay $30.")
    loaded=input("Your truck Is Loaded? Y or N :-")
    if loaded=="Y":               
     charge += 20
     print("You Need To Give Extra Charge Amount Of $20.")
     
    print(f"Total Amount You Need To Pay Is {charge}. ") 
                
else:
    print("bikers will be not charged any $, You can go...")



