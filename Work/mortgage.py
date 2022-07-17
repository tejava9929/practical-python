# mortgage.py
#
# Exercise 1.7

#원금
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
month = 0
while principal>0 :
    principal = principal*(1+rate/12)-payment
    total_paid += payment
    if month>=extra_payment_start_month and month<=extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    if principal<0 :
        total_paid += principal
        principal = 0
    month += 1
    print(f'month {month}: Paid ${total_paid:0.2f}, last principal : {principal:0.2f}')
    #python에서 print에서는, 변수 사이에 공백 자동 삽입
    
print('Total paid', total_paid)
print('Months', month)

