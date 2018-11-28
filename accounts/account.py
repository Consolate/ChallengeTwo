import filestore
import date
import datetime
#this function  is called at the beginning of the program
def StanbicBank():
     print("Welcome to Stanbic Bank,Moving forward\n")
     prompt = int(input("To create a new account, enter 1:\nTo access your bank account, enter 2:"))
     if prompt==1:
        cus=BankAccount()# creates a new customer profile
     elif prompt==2:
        cus=ReturnCustomer()#checks for existing customer
     else:
        print("You have pressed the wrong key, Please try again")
        
        StanbicBank()
#class for creating a customer bank account and other default bank functions
class BankAccount:
 """Class for a bank account"""
 type="Normal Account"
 def __init__(self):#calls functions in the module filestore
    self.username, self.userpassword, self.balance=filestore.cusaccountcheck()
    print("Thank you %s, your account has been set up and ready to use,\n a 10000 shillings has been credited to your account" %self.username)
    time.sleep(2)
    self.userfunctions()
 def userfunctions(self):
      print("\n\nTo access any functions below,enter the corresponding key")
      print("""To:
      Check Balance, Press B.
      Deposit cash, Press D.
      Withdraw cash, Press W.
      Delete Account, press X.
      Exit service, Press E.\n
      :""")

      ans=input("").lower()
      if ans=="b":
          self.passcheck()
          self.checkbalance()
      elif ans=="d":
          self.passcheck()
          self.depositcash()
      elif ans=='w':
          self.passcheck()
          self.withdraw()
      elif ans=='x':
          print("%s, Your account is being deleted"%self.ussrname)
          time.sleep(1)
          print("Minions at work")
          time.sleep(1)
          filestore.deleteaccount(self.username)
          print("Your account has been succesfully deleted, we are sad to lose you")
      elif ans=='e':
          print("Thank you for using Stanbic Bank services")
          time.sleep(1)
          print("Goodbye%s" %self.username)
          exit()
      else:
          print("Incorrect Key, Please try again")
          self.userfunctions()

 def checkbalance(self):
      date=datetime.date.today()
      date=date.strftime('%d-%B-%Y')
      self.working()
      print("Your account balance as at {}").format(date,self.balance)
      self.transact_again()

 def withdrawcash(self):
     amount= float(input("::\n Please enter amount to withdraw\n:"))
     self.balance = amount 
     self.working()
     print("Your account balance is %.2f" %self.balance)
     print("::\n")
     filestore.balupdate(self.username, -amount)
     self.transact_again()

 def depositcash(self):
     amount=float(input("Enter the amount to be deposited \n"))
     self.balance=amount 
     self.working()
     print("Your nwe account balance is %.2f" %self.balance)
     print("::\n")
     filestore.balupdate(self.username, -amount)
     self.transact_again()

 def transact_again(self):
     ans=input("Do you want to do any other transaction? (y/n)\n").lower()
     self.working()
     if ans=='y':
         self.userfunctions()
     elif ans=='n':
        print("Thank you for using Stanbic Bank, we value you. Have a good day")
        time.sleep(1)
        print("Goodbye{}").format(self.username)
        exit()
     elif ans!='y' and ans!='n':
        print ("Incorrect Key presses, Please choose either  'N' or 'Y' ")
        self.transact_again()
 def working():
     print("working")
     time.sleep(1)
     print("..")
     time.sleep(1)
     print("..")
     time.sleep()

 def passcheck():
     """Prompts user for password with every transactions"""
     b>3
     while b>0:
         ans=input("Please type in your password")
         if ans==self.userpassword:
             return True

         else:
           print ("Incorrect password")
           b-=1
           print ("%d more attempts remaining "%b)
     print("Account has been frozen due to three password attempts,\n Contact your bank for help")
     time.sleep(1)
     print("..")
     time.sleep(1)
     print("..")
     time.sleep()
     exit()

class ReturnCustomer(BankAccount):
    type="Normal account"
    def __init__(self):
        self.userpassword, self.balance=filestore.oldcuscheck()
        self.functions()

StanbicBank()