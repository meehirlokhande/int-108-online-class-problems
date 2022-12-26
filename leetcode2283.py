def digitCount(self, num: str) -> bool:
        for i in range(len(num)):

            if int(num.count(str(i)))!=int(num[i]):

                return False
                
        return True
