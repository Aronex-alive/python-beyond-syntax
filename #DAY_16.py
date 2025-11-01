v=int(input("Enter a number :"))
match v:
    case _ if v >0: # for giving codition first make it default case using _ then give condition
        print("Positive Number")
    case _ if v<0:
        print("Negative Number")
    case _:  #default case like else block
        print("Zero")        