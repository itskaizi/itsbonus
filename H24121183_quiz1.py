#使用者輸入芮氏規模
value = float(input("Please input a Richter scale value : "))

joules = 10**(1.5*value + 4.8) #計算使用者輸入的芮氏規模換算的焦耳值
tnt = joules / (4.184 * 10**9) #計算使用者輸入的芮氏規模換算的幾噸TNT
lunch = joules / 2930200 #計算使用者輸入的芮氏規模換算的營養午餐數量


print("Equivalence in Joules:", joules) #印出焦耳值
print("Equivalence in tons of TNT:", tnt) #印出幾噸TNT
print("Equivalence in the number of nutritious lunches:", lunch) #印出營養午餐數量