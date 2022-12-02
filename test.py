class Challenge:
    @staticmethod
    def end_zeros(num):
        counter = 0
        while num % 10 != num:
            if num % 10 == 0:
                counter += 1
            num /= 10
        return counter


obj = Challenge
print(obj.end_zeros(0))
print(obj.end_zeros(1))
print(obj.end_zeros(10))
print(obj.end_zeros(101))
print(obj.end_zeros(100))
print(obj.end_zeros(10010))
