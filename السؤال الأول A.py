l1=['nihal','reem','jood','leen','lama']
name=input('enter name')
for i in range(5):
     if name in l1:
        print(name,'the user is graduated')
        break
     else:
         print('the user is failed')
         break
