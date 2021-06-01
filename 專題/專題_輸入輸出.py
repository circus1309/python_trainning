print("請輸入你的姓名")
name = input()
print("請輸入一個部位")
part = input()
print("請輸入一個數字")
number = input()
number = int(number)
sentence = "%s你的%s是%d公分"
print(sentence % (name, part, number) )