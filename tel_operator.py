operators = {'Operator A' : {'46732': '1.1'}}

num = input('Enter the phone number:')
num = num.replace('+', '')
num = num.replace('-','')

def cheap(num,operator):
    size2 = price2  = pref2 = 0
    final_price =final_operator =  high_price2 = k2=final_price2 = final_operator2 = ''
    for k,operator in sorted(operators.items()):
        high_pref= high_price=''
        highest_size = 0
        for pref in sorted(operator):
            size = 0;
            price = operator[pref];
            if num.startswith(pref):
               size = len(pref);
               if size > size2:
                   highest_size = size;
                   high_pref = pref;
                   high_price = price;
            size2 = size;
            pref2=pref;
            price2 = price; 
        if highest_size==0:
            print('The price for you number is not available in operator:', k)
        else:
            x = high_price;
            print ('the appropriate prfix is:', high_pref,'and price is:', x, 'for operator:',k)
            if high_price2 != '':
                if float(x) < float(high_price2):
                    final_price = x;
                    final_operator = k;
                else:
                    final_price = high_price2;
                    final_operator= k2;
            else: 
                final_price = x;
                final_operator = k;    
            high_price2 = x;
            k2 = k
    return final_operator, final_price  

def check(num):
    if num.isdigit() != True:
        print("Invalid number!!")
        num = input("Please enter your number again:")
        num = num.replace('+', '')
        num = num.replace('-','')
        check(num)
    else:
        print ('Your mobile number is :', num)
        print ('current operators are:')
        for k in sorted(operators.items()): 
            print(k)
        
        final_operator, final_price = cheap(num,operators)
        if final_price and final_operator:
            print ('The cheapest operator is:',final_operator, 'with price:', final_price)
check(num)
