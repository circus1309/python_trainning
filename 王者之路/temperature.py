val = input("輸入溫度符號(ex: c or f")
val1 = input("請輸入溫度")
if val in ['C','c'] :
    f = 1.8 * float(val1) + 32
    print("轉換後的溫度為: %.2F"%f)
elif val in ['F','f'] :
    c = (float(val1) - 32 /1.8)
    print(sep=("轉換後的溫度為: %.2f"%c))
else: 
    print("錯誤")