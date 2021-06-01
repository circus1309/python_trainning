val = input("輸入溫度符號(ex: 30c or 80f")
if val[-1] in ['C','c'] :
    f = 1.8 * float(val[0:-1]) + 32
    print("轉換後的溫度為: %.2fF"%f)
elif val[-1] in ['F','f'] :
    c = (float(val[0:-1]) - 32 /1.8)
    print(sep=("轉換後的溫度為: %.2fC"%c))
else:
    print("error")