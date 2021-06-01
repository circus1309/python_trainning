print("請輸入距離")
dist = input() #距離
dist = float(dist) 
print("請輸入時速")
speed = input() #時速
speed = float(speed)
total_hour = (dist / speed) #總小時
day = total_hour / 24 #需要天數
hours = total_hour % 24 #需要小時
mins = (hours - int(hours)) * 60 #需要分鐘
secs = (mins - int(mins)) *60 #需要秒數
print("總共需要天數")
print(int(day))
print("總共需要小時")
print(int(hours))
print("總共需要分鐘")
print(int(mins))
print("總共需要秒數")
print(int(secs))
