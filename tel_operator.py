operators = {'Operator A' : {'1':'0.9','268':'5.1','46': '0.17','4620':	'0.0','468':'0.15','4631':'0.15','4673':'0.9','46732': '1.1'} ,
'Operator B' : {'1':'0.92','44':'0.5','46': '0.2','467':'1.0','48':'1.2'} ,
    'Operator C' :{'467':'0.01', '4676':'0.02'}
}

num = input('Enter the phone number:')
num = num.replace('+', '')

def check(num):
    if num.isdigit() != True:
        print("Invalid number!!")
        num = input("Please enter your number again:")
        num = num.replace('+', '')
        check(num)
    else:
        print ('Your mobile number is :', num)
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
                print('not exist in operator:', k)
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
                        
                high_price2 = x;
                k2 = k
                
        print ('The cheapest operator:',final_operator, 'with price:', final_price) 
check(num)
