import dt
import SplitList


def returncustome():
    SplitList.listOfCostume()
    print()
    Name = input("Input Borrower Name:")
    file = "Borrow by-"+Name+".txt"

    try:
        with open(file, "r") as read:
            borrower = read.read()
            print(borrower)

        doc = "Return by-"+Name+".txt"
        with open(doc, "w+") as info:
            info.write("\n---------------------------Custome management software------------------------\n")
            info.write("                   Returned By: " + Name+"\n")
            info.write("    Date: " + dt.getDate() +
                       "    Time:" + dt.getTime()+"\n\n")
            info.write("S.N.\t\Custome Name \t\tCost\n")

        with open(file, "r") as f:
            lines = f.readlines()
            empty_list = []

            for z in lines:
            
                clear = z.strip('\n')
              
                empty_list.append(clear)

        total = 1
        cost = 0.0
        for i in range(len(SplitList.nameofthecustome)):

            if SplitList.nameofthecustome[i] in borrower:
                with open(doc, "a") as info:
                    info.write(
                        "\n " + str(total) + " " + SplitList.nameofthecustome[i]+"   " + "$" + SplitList.CostumeCost[i])
                    total += 1

                cost = float(cost) + float(SplitList.CostumeCost[i])

              
                SplitList.Quantity[i] = int(SplitList.Quantity[i])+1
             
                with open("store.txt", "w+") as info:
                    for i in range(len(SplitList.nameofthecustome)):
                        info.write(SplitList.nameofthecustome[i]+","+SplitList.CostumeBrand[i]+","+str(
                            SplitList.Quantity[i]) + "," + "$" + SplitList.CostumeCost[i]+"\n")
                with open(doc, "a") as update:
                    update.write(
                        "\n             Total Cost of Borrow:$" + str(cost)
                    )
        CostWithFine = 0.0
        success = False
        while success == False:
            print()
            print()
            print("Is the Costume return on time?")
            ask = input("Press 'y' for Yes and 'n' for No: ")
            if(ask.upper() == "Y"):

                print("By How many days was the Costume returned late ?")
                print()
                day = int(input("Total days: "))

                CostWithFine = float(cost) + float(day*1.9)

                with open(doc, 'a') as Newcost:
                    Newcost.write(
                        "\n                    Total Fine: $ " +
                        str(day*1.5)
                    )
                    Newcost.write(
                        "\n                     Total Cost with Fine: $" +
                        str(CostWithFine)
                    )
                with open(doc, "r") as f:
                    display = f.read()
                    print(display)
                    success = True
            elif(ask.upper() == "N"):
                print()
                with open(doc, "a") as Newcost:
                    Newcost.write(
                        "\n                     Total Return amount: $" +
                        str(cost)
                    )
                with open(doc, "r")as info:
                    display = info.read()
                    print(display)
                    success = True
            else:
                print("!!!Please provide correct input")
    except ValueError:
        print("!!!You Haven't Borrowed any Costumes")
        returncustome()
