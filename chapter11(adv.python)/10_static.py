class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  # 8

#Can also be called on an instance
m = MathUtils()
print(m.add(4,5)) # 9