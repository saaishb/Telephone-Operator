operators = {'op_a' : {'1':'0.9','268':'5.1','46': '0.17','4620':	'0.0','468':'0.15','4631':'0.15','4673':'0.9','46732': '1.1'} ,
'op_b' : {'1':'0.92','44':'0.5','46': '0.2','467':'1.0','48':'1.2'} ,
    'op_c' :{'467':'0.01', '4676':'0.02'}
}

num = input('Enter the phone number:')
num = num.replace('+', '');
print (num);
size2 = 0;
price2 = 0;
pref2 = 0;
highest_size=0;
high_pref='';
high_price='';
final_price='';
final_operator ='';
high_price2 ='';
k2='';
final_price2 = '';
final_operator2 = '';
for k,operator in sorted(operators.items()):
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
        print (high_pref, x, 'for operator:',k);
        if high_price2 != '':
            if float(x) < float(high_price2):
                final_price = x;
                final_operator = k;
            else:
                final_price = high_price2;
                final_operator= k2;
                
        high_price2 = x;
        k2 = k
        
print (final_operator,final_price) ;
