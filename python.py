

user_Name="saikumar"
password=123

num1=str(input("enter a username"))
num2=int(input("enter password"))

while True:


     if num1==user_Name and num2==password:

         print("""


          1)checkbalance
          2)deposit
          3)withdraw
          4)Ministatement
          5)Quit


       """)
         option=int(input("please enter your option"))

         amount=50000

         if option==1:
             print(amount)

         elif option==2:
             deposit=float(input("enter the amount"))
             amount=amount+deposit
             print("your total amount",amount)

             break

         elif option==3:
             withdraw=float(input("enter the amount you withdraw"))
             amount=amount-withdraw
             print("the withdraw amount is",amount)

             break
         elif option==4:
              print("your name",user_Name)
              print("your total amount is",amount)

              break
         elif option==5:
             print("exit")

         else:
             print("please provide the correct information")











-
