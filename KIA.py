print("==========KOTOKA INTERNATIONAL AIRPORT CHECK-IN SYSTEM================")\

passenger_details={}

print("1. Check In Passenger\n2. View Daily Statistics\n3. View Flight Summary\n4. Close Check-In")


while True:
    choice=input("Enter Choice: ") 
    if choice == '1':
        name=input("Enter Passenger Name: ")
        id=input("Enter Passenger ID: ")
        nationality=input("Enter Passenger Nationality: ")
        age=int(input("Enter Passenger Age: "))
        destination=input("Enter Destination: ")

        print(" ")
        print("=====TICKET SECTION=====")

        print("1. First Class\n2. Economy Class\n3. Business Class  ")
        ticket_class=int(input("Enter Ticket Class: "))
        print(" ")
        
        print("=====BAGGAGE SECTION=====")

        luggage=int(input("Enter Number of Bags: "))
        if luggage < 0:
            print("Invalid Number of Bags")
        count=1
        total_charge1=0
        total_weight=0
        for i in range(1,luggage+1):
            weight= int(input(f"Enter Weight of Bag {count}: "))
            total_weight+=weight
            count +=1
            if ticket_class == 1 and weight > 40:
                print(f"Bag {i} exceeds the allowable limit")
                print("Allowed is 40kg and Ghs30 for Each Extra Kg")
                allowed_1= 40
                extra= weight-allowed_1
                charge_1= 30*extra
                print(f"Extra Charge for Bag {i} is {charge_1}")
                total_charge1 += charge_1
        print(f"Total Cost for all extra luggage is {total_charge1}")
        print(" ")

        print("====PASSENGER ELIGIBILITY=====")
        print(' ')

        if len(id)==0:
            print("No Access, Passport Number Not Provided")
        elif age<= 0:
            print("No Access, Invalid Age")
        elif len(destination)==0:
            print("No Access, No Destination Provided")
        elif luggage < 1:
            print("No Access, Invalid Number of Bags")
        security2= None
        security1= None
        if luggage > 5:
            print("Security Inspection Required")
            security1= "Security Inspection Required"
        elif weight > 50:
            print(" Manual Security Inspection Required")
            security2="Manual Security Inspection Required"
        else:
            print("===========================" \
        "Passenger Successfully Checked In" \
        "===================================")
        security_status=security1 or security2
        if security1 and security2:
            eligibility_to_board = "NO"
        elif security1 or security2:
            eligibility_to_board= "NO"
        else:
            eligibility_to_board= "YES"


        passenger_details["NAME"]=name
        passenger_details["PASSPORT NUMBER"]=id
        passenger_details["AGE"]=age
        passenger_details["NATIONALITY"]=nationality
        passenger_details["DESTINATION"]=destination
        passenger_details["BOARDING CLASS"]=ticket_class
        passenger_details["NUMBER OF BAGS"]=luggage
        passenger_details["TOTAL EXTRA LUGGAGE COST"]=total_charge1
        passenger_details["TOTAL LUGGAGE WEIGHT"]=total_weight
        passenger_details["SECURITY STATUS"]=security_status
        passenger_details["ElIGIBILITY TO BOARD"]=eligibility_to_board
        print(passenger_details)


            
