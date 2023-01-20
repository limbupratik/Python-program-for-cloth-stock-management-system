import BorrowCostume
import ReturnCustome
import dt
import SplitList


def HereWeGo():
    while(True):
        print()
        print()
        print("------------------------------------------------")
        print("           Custome Management Software          ")
        print("------------------------------------------------")
  
        print("\n")
        
        print("     Enter 1. To Display costume ")
        print("     Enter 2. To Borrow Costume")
        print("     Enter 3. To Return Costume")
        print("     Enter 4. To Exit Program")

        try:
            print()
            print()
            Choice = int(
                input("Enter the option: "))
            print()
            if(Choice == 1):
                print()
                print()
                print("|----------- Custome Details ---------|")
                print("|-----------------------------------------|")
                print()
                with open("./store.txt", "r") as f:
                    lines = f.read()
                    print(lines)

            elif(Choice == 2):
                SplitList.listOfCostume()
                BorrowCostume.BorrowCostume()

            elif(Choice == 3):
                SplitList.listOfCostume()
                ReturnCustome.returncustome()

            elif(Choice == 4):
                print("thank you for using this software! Have a Nice Day...BYE")
                break

            else:
                print(
                    "Select the number from the list")
        except ValueError:
            print("please input valid data.Thank You!!!")


HereWeGo()
