class FishBread:
    def __init__(self, filling, size, price):
        """붕어빵의 속재료, 크기, 가격을 설정합니다."""
        self.filling = filling
        self.size = size
        self.price = price
        
        
    def display_info(self):
        """붕어빵 정보를 표시합니다."""
        print("이 붕어빵은 %s 속이 들어 있고, 크기는 %s이며, 가격은 %s원입니다." % (self.filling, self.size, self.price))


# 붕어빵 인스턴스 생성
fish_bread1 = FishBread("팥", "중", 1000)
fish_bread2 = FishBread("슈크림", "중", 1000)
fish_bread3 = FishBread("반반", "대", 2000)
# 붕어빵 정보 표시
fish_bread1.display_info()
fish_bread2.display_info()
fish_bread3.display_info()



