class Calculate:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def div(self):
        try:
            result = self.num1 / self.num2
            return result
        except:
            return "0으로 나눌 수 없습니다."
    

a, b = map(int, input("a, b 입력 :").split())

# 객체 생성
calc = Calculate(a, b)
# 객체의 add 메소드 호출

add_ab = calc.add()
sub_ab = calc.add()
mul_ab = calc.mul()
div_ab = calc.div()


print(add_ab, sub_ab, mul_ab, div_ab)
