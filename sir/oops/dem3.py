class Bank:
    accountno: int
    balance: int
    ac_type: str
    p_name: str


    def create_ac(self,acno,bal,ac_type,p_name):
        self.accountno=acno
        self.balance=bal
        self.ac_type=ac_type
        self.p_name=p_name
        print(self.accountno ,self.balance,self.ac_type,self.p_name)

    def deposite(self,amount):
        self.balance+=amount
        print(f"your sbi {self.accountno} has been credited with an amount of {amount} available balance is {self.balance} ")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"your sbi {self.accountno} has been debited with an amount of {amount} available balance is {self.balance}")
        else:
            print("transaction failed insufficient balance ")

obj1= Bank()
obj1.create_ac(1000,49999,"savings","joyan")
obj1.deposite(1000)
obj1.withdraw(1000)