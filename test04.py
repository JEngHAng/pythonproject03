wide = float(input("กรุณาใส่ความกว้าง : "))
hight = float(input("กรุณาใส่ความสูง : "))
long = float(input("กรุณาใส่ความยาว : "))
compile = ((wide + long) * hight) * 2 + (wide * long) * 2
if compile%5 == 0 :
    compile0 = int(compile/5)
else :
    compile0 = int(compile/5)+1
print ("-------------------------------------------")
print (f"ต้องใช้สี {compile0} แกลอน")
print ("-------------------------------------------")
print ("ต้องใช้สี",compile0,"แกลอน")
print ("-------------------------------------------")
print ("ต้องใช้สี "+str(compile0)+" แกลอน")
print ("-------------------------------------------")
print ("ต้องใช้สี {} แกลอน".format(compile0))
print ("-------------------------------------------")
print ("ต้องใช้สี %d แกลอน"%(compile0))
print ("-------------------------------------------")