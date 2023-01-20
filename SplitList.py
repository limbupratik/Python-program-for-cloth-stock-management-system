def listOfCostume():

    global nameofthecustome
    global CostumeBrand
    global Quantity
    global CostumeCost

    nameofthecustome = []
    CostumeBrand = []
    Quantity = []
    CostumeCost = []

    with open("./store.txt", "r") as f:
        lines = f.readlines()
        Empty_list = []

        for z in lines:
            remove = z.strip('\n')
            Empty_list.append(remove)
        for i in range(len(Empty_list)):
            customelist = Empty_list[i].split(',')
            value = 0
            for b in customelist:
                if(value == 0):
                    nameofthecustome.append(b)
                elif(value == 1):
                    CostumeBrand.append(b)
                elif(value == 2):
                    Quantity.append(b)
                elif(value == 3):
                    CostumeCost.append(b.strip('$'))
                value += 1


listOfCostume()
