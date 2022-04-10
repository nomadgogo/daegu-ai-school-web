가격=float(input('가격?'))
부가세율=0.1
부가세=가격*부가세율
print(부가세)


#실습 과제 3/29

name=input("이름을 입력하세요: ")

height_CM=int(input("키(cm)를 입력하세요: "))
height_M=height_CM/100

weight=int(input("몸무게(kg)을 입력하세요: "))

BMI=weight/(height_M**2)

print("%s님의 BMI는 %.1lf 입니다." % (name, BMI))