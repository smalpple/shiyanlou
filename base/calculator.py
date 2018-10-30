#!/usr/bin/env python3

import sys 

def compute_money(money):
	money = money - 3500
	tax = 0
	if money <= 1500:
		tax = money * 0.03
	elif money > 1500 and money <= 4500:
		tax = money * 0.1 - 105
	elif money > 4500 and money <= 9000:
		tax = money * 0.2 - 555
	elif money > 9000 and money <= 35000:
		tax = money * 0.25 - 1005
	elif money > 35000 and money <= 55000:
		tax = money * 0.3 - 2755
	elif money > 55000 and money <= 80000:
		tax = money * 0.35 - 5505
	elif money > 80000:
		tax = money * 0.45 - 13505
	if tax <= 0 :
		tax = 0
	tax=format(tax,'.2f')
	return tax


if __name__ == '__main__':
	money = sys.argv[1]
	#print(money)
	try:
		money = int(money)
		print(compute_money(money))
	except:
		print('Parameter Error')

