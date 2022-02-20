def valid(pin):
 if len(pin)==4 or len(pin)==6:  
       return print('True')
 else: print('False')    


valid("1234") 
valid("45135")
valid("89abc1")
valid("900876")
valid(" 4983")
valid("")