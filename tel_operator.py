#!/usr/bin/python3

import unittest
operators = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}} #Declare multiple operators with thier respective price lists in nested dictionary
'''
format for manipulating operators
operators = {'Operator A':{'prefix' : 'price', 'prefix2':'price2'.....................},'Opearor B':{'prefix' : 'price', 'prefix2':'price2'.....................}...............................}
'''
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
##########################################################################################(UNIT TESTS)#########################################################################################
#####################################################################################################################################################################################
print ('#### UNIT TESTS #####')
class MyTest(unittest.TestCase):
    
    def test1(self):									#TEST for Single operator and single pricelist
        operator_t1 = {'Operator A' : {'4678':'3.4'}}
        num = '467845687'
        self.assertEqual(cheap(num, operator_t1),('Operator A','3.4'))
													
    def test2(self):									#Test for Multiple operators with single price list
        operator_t2 = {'Operator A' : {'46732': '1.1'}, 'Operator B':{'4673':'1.0'}}
        num = '46732456'
        self.assertEqual(cheap(num, operator_t2),('Operator B','1.0'))

    def test3(self):									#Test for single operator with multiple price list
        operator_t3 = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}}
        num = '46332456'
        self.assertEqual(cheap(num, operator_t3),('Operator A','1.3'))

    def test4(self):									#Test for multiple operators with multiple price list
        operator_t4 = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}, 'Operator B':{'4673':'1.0','46':1.9} }
        num = '46332456'
        self.assertEqual(cheap(num, operator_t4),('Operator A','1.3'))
        num = '467321234'
        self.assertEqual(cheap(num, operator_t4),('Operator B','1.0'))

    def test5(self):  									#Test if the there is no prefix matches in the available operator
        operator_t5 = {'Operator A' : {'46732': '1.1','463':'1.3','376':'2.2'}}
        num = '676332456'
        self.assertEqual(cheap(num, operator_t5),('',''))	
			
    def test6(self):									#Test if the longest prefix of mobile number matches the price list
        operator_t6 = {'Operator A' : {'46732': '1.1','467':'1.3','376':'2.2','467325':'5300','4673':'333'}}
        num = '46732514443'
        self.assertEqual(cheap(num, operator_t6),('Operator A','5300'))

    def test7(self):									#Test for selecting the cheapest and finalizing with multiple conditions
        operator_t7 = {'Operator A' : {'46732': '1.1','467':'1.3','376':'2.2','467325':'5300','4673':'333'},'Operator B':{'4673':'1.0','46':'0.9'},'Operator C':{'463':'1.1','467325':'0.01','4673258':'0.02'}}
        num = '467314443'
        self.assertEqual(cheap(num, operator_t7),('Operator B','1.0'))
        num = '463882792'
        self.assertEqual(cheap(num, operator_t7),('Operator B','0.9'))
        num = '4673251234'
        self.assertEqual(cheap(num, operator_t7),('Operator C','0.01'))
        num = '4673258123'
        self.assertEqual(cheap(num, operator_t7),('Operator C','0.02'))

if __name__ == '__main__':
    unittest.main()
 






