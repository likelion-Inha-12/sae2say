
class Account():
    def __init__(self,owner,acc_money):
        self.owner=owner
        self.acc_money=acc_money

    def save(self,save_m):
        if(save_m>=0):
            self.acc_money += save_m
            print("%d원이 입금되었습니다."%save_m)
        else:
            print("금액은 양수여야 합니다.")
        return self.acc_money
    
    def draw(self,draw_m):
        if (self.acc_money>=draw_m) and (draw_m>=0):
            self.acc_money -= draw_m
            print("%d원이 출금되었습니다."%draw_m)
        else:
            print('출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.')
        return self.acc_money

    def print_acc(self):
        print("%s님의 계좌 잔액은 %d원 입니다."%(self.owner,self.acc_money))


if __name__ =='__main__':

    my_acc=Account("sae2",1000)
    my_acc.print_acc()
    my_acc.save(int(-5500))
    my_acc.draw(int(20000))
    my_acc.print_acc()