operators = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}} #Declare multiple operators with thier respective price lists in nested dictionary

num = input('Enter the phone number:')             #user input of telephoe number
num = num.replace('+', '') #removing + and - if exists in provided input number
num = num.replace('-','')

def cheap(num,operators):            #This function calclates the cheapest and best price for the provided mobile number
    pref = price = price2 = pref2 = final_price =final_operator =  high_price2 = k2=final_price2 = final_operator2 = ''
  
    for k,operator in sorted(operators.items()):
        size2 = 0       #iterate through the multiple operators dictionary
        high_pref= high_price=''
        highest_size = 0
        for pref in sorted(operator):            #iterate through the price list of individual operator
            size = 0;
            price = operator[pref];
            if num.startswith(pref):
               size = len(pref);
               if size > size2:                #repetetive comparisions with previous values of price list iterations to check the longest prefix that matches the provided number in a single operator
                   highest_size = size;
                   high_pref = pref;
                   high_price = price;

            size2 = size;
            pref2=pref;                    #storing the current values to make them reusable in the next iteration
            price2 = price;
        if highest_size != 0:                #if the preix in the current operator doesnot match the provided input's number
            #print (' Sorry! The price for you number is not available in:', k)
        #else:
            x = high_price;
            #print ('The appropriate prfix is:', high_pref,'and price is:', x, 'for operator:',k)
            if high_price2 != '':                         

                if float(x) < float(high_price2):    #repetative comparisions with previous values of operators iterations to check which operator has the cheapest price
                    final_price = x;
                    final_operator = k;
                else:
                    final_price = high_price2;
                    final_operator= k2;
            else:
                final_price = x;
                final_operator = k;  
            high_price2 = x;
            k2 = k                #storing the current values to make them reusable in the next iteration
    return final_operator, final_price

def check(num, operators):                #this function validates whether the mobile number has only numbers and asks the user to enter again in case of invalid input
    if num.isdigit() != True:
        print ("Invalid number!!")
        num = input("Please enter your number again:")       
        num = num.replace('+', '')
        num = num.replace('-','')
        check(num, operators)            #recursive way until the input is valid
    else:
        print ('Your mobile number is :', num)       
        print ('current operators are:')
        for k in sorted(operators.items()):        #optput of the current operators
            print(k)
        final_operator, final_price = cheap(num,operators)        #function call to get the cheapest and best price for the provided number ad operators
        if final_price and final_operator:
            print ('The cheapest operator for the provided input number:',num, 'is:',final_operator, 'with price:', final_price)
        else:
            print ("No operator has the matching price with your mobile number")
       
(check(num, operators)) #function call to validate the input mobile number

###########################################################################################################################################################################################
##########################################################################################UNIT TESTS#########################################################################################
#####################################################################################################################################################################################
print ('#### UNIT TESTS #####')

#TEST for Single operator and single pricelist (T1)
operator_t1 = {'Operator A' : {'4678':'3.4'}}
num = '467845687'
x,y = (cheap(num, operator_t1))
if x == 'Operator A' and y == '3.4':
    print ('Test(T1) passed for single operator and single pricelist')
else:
    print ('something went worng for testing single operator and single pricelist')


#Test for Multiple operators with single price list
operator_t2 = {'Operator A' : {'46732': '1.1'}, 'Operator B':{'4673':'1.0'}}
num = '46732456'
x,y = (cheap(num, operator_t2))
if x == 'Operator B' and y == '1.0':
    print ('Test(T2) passed for Multiple operators with single price list ')
else:
    print ('something went worng for testing Multiple operators with single price list')

#Test for single operator with multiple price list
operator_t3 = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}}
num = '46332456'
x,y = (cheap(num, operator_t3))
if x == 'Operator A' and y == '1.3':
    print ('Test(T3) passed for single operator with multiple price list')
else:
    print ('something went worng for testing single operator with multiple price list ')

#Test for multiple operators with multiple price list
operator_t4 = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}, 'Operator B':{'4673':'1.0','46':1.9} }
num = '46332456'
x,y = (cheap(num, operator_t4))
if x == 'Operator A' and y == '1.3':
    h = True
else:
    print ('something went worng for testing multiple operators with multiple price list')
num = '467321234'
x,y = (cheap(num, operator_t4))
if x == 'Operator B' and y == '1.0':
    j = True
else:
    print ('something went worng for testing multiple operators with multiple price list')

if h == True and j == True:
    print ('Test(T4) passed for multiple operators with multiple price list')
else:
    print ('something went worng for testing multiple operators with multiple price list')

#Test if the there is no prefix matches in the available operator
operator_t5 = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}}
num = '676332456'
x,y = (cheap(num, operator_t5))
if x == '' and y == '':
    print ('Test(T5) passed for no prefix matches in the available operator')
else:
    print ('something went worng for testing no prefix matches in the available operators')

#Test if the longest prefix of mobile number matches the price list
operator_t6 = {'Operator A' : {'46732': '1.1','467':'1.3','376':'2.2','467325':'5300','4673':'333'}}
num = '46732514443'
x,y = (cheap(num, operator_t6))
if x == 'Operator A' and y == '5300':
    print ('Test(T6) passed for longest prefix of mobile number matches the price list')
else:
    print ('something went worng for testing longest prefix of mobile number matches the price list ')

#Test for selecting the cheapest and finalizing with multiple conditions
operator_t7 = {'Operator A' : {'46732': '1.1','467':'1.3','376':'2.2','467325':'5300','4673':'333'},'Operator B':{'4673':'1.0','46':'0.9'},'operator C':{'463':'1.1'}}
num = '467314443'
x,y = (cheap(num, operator_t7))
if x == 'Operator B' and y == '1.0':
    h = True
else:
    print ('something went worng for selecting the cheapest and finalizing with multiple conditions')

num = '463882792'
x,y = (cheap(num, operator_t7))
if x == 'Operator B' and y == '0.9':
    j = True
else:
    print ('something went worng for selecting the cheapest and finalizing with multiple conditions')

if h== True and j == True:
    print ('Test(T7) passed for selecting the cheapest and finalizing with multiple conditions')
