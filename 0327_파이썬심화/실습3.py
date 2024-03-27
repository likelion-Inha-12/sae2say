from 실습2 import Account

class SaveAcc(Account):
    def __init__(self,owner,acc_money,interest_r):
        super().__init__(owner,acc_money)
        self.interest_r=interest_r


    def prt_init(self):
        print("%s님의 계좌 잔액은 %d원입니다."%(self.owner,self.acc_money))
        print("이자율: %d" %self.interest_r,"%")
    
    def save(self,save_m):
        if(save_m>=0):
            self.acc_money += save_m
            print("%d원이 입금되었습니다."%save_m)
            interest=self.acc_money*self.interest_r*0.01
            self.acc_money += interest
            print("%s님의 계좌에 %d원의 이자가 추가되었습니다."%(self.owner,interest))

my_acc = SaveAcc("sae2",1000,5)
my_acc.prt_init()
my_acc.save(int(500))
my_acc.draw(int(100))
my_acc.prt_init()


    


