class Data():
    bikename=["CLASSIC","BULLET","THUNDERBIRD","INTERCEPTOR","INTERCEPTOR","HIMALAYAN"]
    bikeprices=["1,01,100","1,12,200","1,12,300","1,11,400","1,12,500","1,12,600"]
    bikenumber=["01","02","03","04","05","06"]
    bikeweight=["100kg","110kg","105kg","110kg","102kg","96kg"]
    bikemileage=["18kmpl","20kmpl","21kmpl","22kmpl","20kmpl","24kmpl"]


class Marketer(Data):
    
    def printmenu(self):
        print("BIKES MENU")
        for i in range(len(Data.bikename)):
                print(i+1,Data.bikename[i])#i+1 bcuz we dont want it to start from 0
    def printdetails(self,name):
         print("{:<15} {:<15} {:<15} {:<15}".format("NAME","PRICE","WEIGHT","MILEAGE"))
         for i in range(len(Data.bikename)):
            if name==Data.bikename[i]:
                print("{:<15} {:<15} {:<15} {:<15}".format(Data.bikename[i],Data.bikeprices[i],Data.bikeweight[i],Data.bikemileage[i]))
                #break bcuz it may prit only one interceptor
         print("WANT TO BUY THIS: ")
         dec=input("TYPE A YES OR NO:")
         if dec== "YES":
             print("CASH PAID THE BIKE IS YOURS NOW")
         else:
             print("THERE ARE MANY OTHERS MODELS")
                                                
class User():    
    def takeinput(self):
       name_of_bike=input("Please select a bike of your chocie: ")
       return name_of_bike    


ob=Marketer()
ob.printmenu()
name=User().takeinput()
while name!= "STOP":
    ob.printdetails(name)
    name=User().takeinput()
    
print("THANKYOU,VISIT AGAIN!!")
