list1 = []
Qdict = {}

while True:
    print("menu".upper())
    print("press 1 for add questions")
    print("press 2 for view questions")
    print("press 3 for delete questions")
    print("press 4 for exit")
    ask1 = input("Which operation you want to perform: ")
    if ask1.isdigit():
        ask1 = int(ask1)
        if 1<=ask1<=4:
            if ask1 == 1:
                quesDict = {}
                addQuen = int(input("Enter Question number: "))
                addQue = input("Enter Your Question: ")
                addOp1 = input("Enter Option 1: ")
                addOp2 = input("Enter Option 2: ")
                addAns = input("Enter right answer: ")

                quesDict[addQuen] = {'question':addQuen,'option1':addOp1,'option2':addOp2,'answer':addAns}
                list1.append(quesDict)
            if ask1 == 2:
                for key,value in quesDict.items():
                    print(f"{addQuen}.{addQue}")
                    print(f"A. {value['option1']}")
                    print(f"B. {value['option2']}")
                    print(f"Right Answer: {value['answer']}")


