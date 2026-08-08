print("==========KOTOKA INTERNATIONAL AIRPORT CHECK-IN SYSTEM================")\

passenger_details={}
statistics={}
children = 0
adult=0
economy=0
business=0
first_class=0
passengers_inspection=0
total_bags=0
total_passengers=0
total_weight=0
#average_weightperP=total_weight/total_passengers
#average_bagperP=total_bags/total_passengers

print("1. Check In Passenger\n2. View Daily Statistics\n3. View Flight Summary\n4. Close Check-In")


while True:
    choice=input("Enter Choice: ") 
    if choice == '1':
        total_passengers+=1
        name=input("Enter Passenger Name: ")
        id=input("Enter Passenger ID: ")
        nationality=input("Enter Passenger Nationality: ")
        age=int(input("Enter Passenger Age: "))
        if age<18:
            children+=1
        else:
            adult+=1
        destination=input("Enter Destination: ")

        print(" ")
        print("=====TICKET SECTION=====")

        print("1. First Class\n2. Economy Class\n3. Business Class  ")
        ticket_class=int(input("Enter Ticket Class: "))
        if ticket_class == '1':
            first_class+=1
        elif ticket_class =='2':
            economy +=1
        elif ticket_class =='3':
            business+=1
        else:
            print("Invalid Ticket Class")
        print(" ")
        
        print("=====BAGGAGE SECTION=====")

        luggage=int(input("Enter Number of Bags: "))
        if luggage < 0:
            print("Invalid Number of Bags")
        total_bags+=luggage
        count=1
        
        total_charge1=0
        total_charge2=0
        total_charge3=0
        total_charge=total_charge3+total_charge2+total_charge1
        #total_weight=0
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
            elif  ticket_class == 2 and weight > 23:
                print(f"Bag {i} exceeds the allowable limit")
                print("Allowed is 23kg and Ghs30 for Each Extra Kg")
                allowed_2= 23
                extra= weight-allowed_2
                charge_2= 30*extra
                print(f"Extra Charge for Bag {i} is {charge_2}")
                total_charge2 += charge_2
                print(f"Total Cost for all extra luggage is {total_charge2}")
            elif  ticket_class == 3 and weight > 32:
                print(f"Bag {i} exceeds the allowable limit")
                print("Allowed is 40kg and Ghs30 for Each Extra Kg")
                allowed_3= 32
                extra= weight-allowed_3
                charge_3= 30*extra
                print(f"Extra Charge for Bag {i} is {charge_3}")
                total_charge3 += charge_3
                print(f"Total Cost for all extra luggage is {total_charge3}")

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
        if security1 or security2:
            passengers_inspection+=1

        passenger_details["NAME"]=name
        passenger_details["PASSPORT NUMBER"]=id
        passenger_details["AGE"]=age
        passenger_details["NATIONALITY"]=nationality
        passenger_details["DESTINATION"]=destination
        passenger_details["BOARDING CLASS"]=ticket_class
        passenger_details["NUMBER OF BAGS"]=luggage
        passenger_details["TOTAL EXTRA LUGGAGE COST"]=total_charge
        passenger_details["TOTAL LUGGAGE WEIGHT"]=total_weight
        passenger_details["SECURITY STATUS"]=security_status
        passenger_details["ElIGIBILITY TO BOARD"]=eligibility_to_board
        statistics["CHILDREN"]=children
        statistics["ADULTS"]=adult
        statistics["ECONOMY CLASS"]=economy
        statistics["FIRST CLASS"]=first_class
        statistics["BUSINESS CLASS"]=business
        statistics["PASSENGER SENT FOR INSPECTION"]=passengers_inspection
        statistics["TOTAL CHARGES"]=total_charge
        statistics["TOTAL BAGS PROCESSED"]=total_bags
    #average_weightperP=total_weight/total_passengers
    #average_bagperP=total_bags/total_passengers
        print(passenger_details)
    elif choice == '2':
        print(statistics)
    elif choice =='3':
        print("=================")
        print("END OF DAY REPORT")
        print("=================")
        print(' ')
        print(f"PASSENGER PROCESSED: {total_passengers}" )
        print(f"NUMBER OF CHILDREN: {children}")
        print(f"TOTAL BAGS: {total_bags}")
        average_weightperP=total_weight/total_passengers
        average_bagperP=total_bags/total_passengers
        
        print(f"AVERAGE WEIGHT PER PASSENGER: {average_weightperP}")
        print(f"AVERAGE BAG PER PASSENGER: {average_bagperP}")
        print(f"AVERAGE REVENUE FOR LUGGAGE: {total_charge}")
    elif choice =='4':
        userchoice=input("ARE YOU SURE YOU WANT TO CLOSE TODAY'S CHECK-IN? (Y/N): ").capitalize()
        if userchoice == 'Y':
            break
