import num3 

#test for the examples
#The functions work as they should when inputing numbers into the shell,
#but when using print function, the quotation marks indicating
#strings disappear. Thus, I used "\"%s\"" % to manually create quotation marks for strings in the test.
print('Test for product function:')
print('If num1 = “12” and num2 = “11”, the product is ' + "\"%s\"" % num3.product('12','11'))
print('If num1 = “25” and num2 = “25”, the product is ' + "\"%s\"" % num3.product('25','25'))
print('If num1 "20000" and num2 = "425524", the product is ' + "\"%s\"" % num3.product('20000','425524'))
print('\n')

print('Test for StrToInt function:')
print('If num1 = “12”, StrToInt(num1) returns ' + num3.IntToStr(num3.StrToInt('12')))
print('If num1 = “25”, StrToInt(num1) returns ' + num3.IntToStr(num3.StrToInt('25')))
print('If num1 = “20000”, StrToInt(num1) returns ' + num3.IntToStr(num3.StrToInt('20000')))
print('\n')

print('Test for IntToStr function:')
print('If num1 = 12, IntToStr(num1) returns ' +  "\"%s\"" % num3.IntToStr(12))
print('If num1 = 25, IntToStr(num1) returns ' +  "\"%s\"" % num3.IntToStr(25))
print('If num1 = 20000, IntToStr(num1) returns ' +  "\"%s\"" % num3.IntToStr(20000))

