Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bài 7.1 
x = 6
s = 1 + x + x**3/3 + x**5/5
print(s)
1634.2
>>> #bài 7.2
result = 1+2
print('result',result)
result 3
original_result= result
result = result + 1
print('result',result)
result 4
original_result= result
result = result * 2
original_result= result
print('result',result)
result 8
result = result ** 3
original_result= result
print('result',result)
result 512
result = result + 8
original_result= result
print('result',result)
result 520
result = result % 7
original_result= result
print('result',result)
result 2
result = result // 2
original_result= result
print('result',result)
result 1
#bài 7.3
result= 5
print('result',result)
result 5
result -= 1
print('result',result)
result 4
result += 3
print('result',result)
result 7
result = - result
print('result',result)
result -7
result = True
print('not result',not result)
not result False
#Bài 7.4
x = 10
y = 4
print('x = %d, y =%d'%(x,y))
x = 10, y =4
equivelence = x==y
print('x==y is', equivelence)
x==y is False
equivelence = x!=y
print('x!=y is', equivelence)
x!=y is True
equivelence = x>y
print('x>y is', equivelence)
x>y is True
equivelence = x<y
print('x<y is', equivelence)
x<y is False
equivelence = x<=y
print('x<=y is', equivelence)
x<=y is False
#Bài tập 7.5
x = 15
y = 12
print('binary of x =',bin(x),',binary of y =',bin(y))
binary of x = 0b1111 ,binary of y = 0b1100
print('x&y =',bin(x&y))
x&y = 0b1100
print('x/y =',bin(x/y))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print('x/y =',bin(x/y))
TypeError: 'float' object cannot be interpreted as an integer
print('x/y =',bin(x|y))
x/y = 0b1111
print('x^y =',bin(x^y))
x^y = 0b11
print('~x =',bin(~x))
~x = -0b10000
print('x << 2',bin(x << 2))
x << 2 0b111100
print('y >> 2',bin(y >> 2))
y >> 2 0b11
#bài 7.6
x = True
y = False
print('x and y:',x and y)
x and y: False
print('x or y:',x or y)
x or y: True
print('not x:',not x)
not x: False
print('x is y:',x is y)
x is y: False
print('x is not y:',x is not y)
x is not y: True
# bài 7.7
đổi tiền
so_tien_muon_doi = float(input("Số tiền muốn đổi :"))
so_to_1 = so_tien_muon_doi // 500000
tien_con_lai = so_tien_muon_doi%500000
print('Số tờ 500,000 :', so_to_1)
so_to_2 = tien_con_lai//200000
tien_con_lai = tien_con_lai%200000
print('Số tờ 200,000 :', so_to_2)
so_to_3 = tien_con_lai//100000
tien_con_lai = tien_con_lai%100000
print('Số tờ 100,000 :',so_to_3)
so_to_4 = tien_con_lai//50000
tien_con_lai = tien_con_lai%50000
print('Số tờ 50,000 :', so_to_4)
tien_con_lai = tien_con_lai*1
print('Tiền còn lại :', tien_con_lai)
