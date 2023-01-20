import dt
import SplitList


def BorrowCostume():
    flag = False
    while flag == False:
        print("select one of these from the table: ")
        print()
        for i in range(len(SplitList.nameofthecustome)):
            print("\tEnter", i, "to borrow a Costume", SplitList.nameofthecustome[i])

        try:
            print()
            a = int(input("My Choice is: "))
            try:
                if(int(SplitList.Quantity[a]) > 0):

                    print("Costume is available")

                    cost = SplitList.CostumeCost[a]

                    while (True):
                        FirstName = input("Enter the First Name: ")
                        if FirstName.isalpha():
                            break
                        print("Please insert Valid Name")
                    while(True):
                        LastName = input("Enter the Last Name:  ")
                        if LastName.isalpha():
                            break
                        print("Please insert valid lastName")

                    text = "Borrow by-"+FirstName+".txt"
                

                    with open(text, "w+") as link:
                        link.write(
                            "----------Cutome management software------------\n")
                        link.write("                     \n")
                        link.write("---------Details of Borrower---------\n")
                        link.write("\n Borrowed By: "+FirstName+" "+LastName+"\n")
                        link.write("    Date: "+dt.getDate() +
                                   "     Time:"+dt.getTime()+"\n")
                        link.write(
                            "\n S.N. \t\t Name of Custome \t         CostumeBrand \n")

                    with open(text, "a") as f:
                        f.write(
                            "1. \t\t"+SplitList.nameofthecustome[a]+"\t\t "+SplitList.CostumeBrand[a]+"\n")

                    
                    SplitList.Quantity[a] = int(SplitList.Quantity[a])-1
                 
                    with open("costumes_store.txt", "w+") as f:
                        for i in range(len(SplitList.nameofthecustome)):
                            f.write(SplitList.nameofthecustome[i]+","+SplitList.CostumeBrand[i] +
                                    ","+str(SplitList.Quantity[i])+"," + "$" + SplitList.CostumeCost[i]+"\n")

                   
                    loop = True
                    total = 1 
                    while loop == True:
                        print()
                        selection = input(
                            FirstName+" Do you want to Borrow more Costumes? But You can't borrow same Costume twice. Input Y for yes and N for no.")
                        if(selection.upper() == "Y"):
                            total += 1
                            print("Please choose an option below")
                            print()

                        
                            for i in range(len(SplitList.nameofthecustome)):
                                print("\tEnter", i, "to borrow a Costume",
                                      SplitList.nameofthecustome[i])
                            print()
                            a = int(input("My Choice is: "))  # asking choice
                            if(int(SplitList.Quantity[a]) > 0):

                               
                                cost = float(cost) + \
                                    float(SplitList.CostumeCost[a])

                                print("Requested Costume is Available")
                                with open(text, "a") as f:
                                    f.write(
                                        str(total)+".""\t\t"+SplitList.nameofthecustome[a]+"\t\t  "+SplitList.CostumeBrand[a]+"\n")

                               
                                SplitList.Quantity[a] = int(SplitList.Quantity[a])-1

                              
                                with open("costumes_store.txt", "w+") as improve:
                                    for i in range(len(SplitList.nameofthecustome)):
                                        improve.write(SplitList.nameofthecustome[i]+","+SplitList.CostumeBrand[i] +
                                                      ","+str(SplitList.Quantity[i])+"," + "$" + SplitList.CostumeCost[i]+"\n")

                            else:
                                loop = False
                                break

                        elif(selection.upper() == "N"):
                            print()
                          
                            print()
                            with open(text, "a")as update_cost:
                                update_cost.write(
                                    "\n Total Borrow Price: $" + str(cost))
                            with open(text, "r") as read:
                                display = read.read()
                                print(display)
                            loop = False
                            flag = True
                        else:
                            print("Please choose as instructed")
                        print("\n !!!Thank You For Borrowing Costume From us.")
                else:
                    print(
                        "Sorry!!! the selected Costume is not available at this moment. Please come back later")

            except IndexError:
                print("")
                print("Please choose Costume according to their number.")
        except ValueError:
            print("")
            print("Please selcect accordingly.")
