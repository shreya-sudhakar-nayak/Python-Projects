#PATIENT RECORD SYSTEM

import random

print("WELCOME TO STARCARE HOSPITAL!")
a=str(input("Time:"))
b=str(input("Date:"))
print("New Patient or Existing Patient?")
c=str(input("Enter Status:"))
if c=="New Patient":
    print("New File No:",random.randrange(11000000,11500000))
else:
    if c=="Existing Patient":
        print("File No:",random.randrange(10000000,11000000))
d=int(input("Phone Number:"))
e=int(input("Patient Registration No:"))
f=str(input("Patient Name:"))
g=int(input("Age:"))
if g<18:
    y=str(input("Parent Name:"))
else:
    y=str(input("Parent/Spouse Name:"))
h=str(input("Nationality:"))
i=str(input("Resident Card No:"))
j=str(input("Department:"))
if j=="paediatrics" or j=="PAEDIATRICS":
    print("Doctors available are:")
    print("DR. Saraswati Sharma")
    print("DR. Lyanna D'Souza")
elif j=="gynaecology" or j=="GYNAECOLOGY":
    print("Doctors available are:")
    print("DR. Saif Qureshi")
    print("DR. Nandita Jain")
elif j=="cardiology" or j=="CARDIOLOGY":
    print("Doctor available are:")
    print("DR. Anuradha Khanna")
    print("DR. Suzzane Terence")
    print("DR. Lilly Singh")
elif j=="ophthalmology" or j=="OPHTHALMOLOGY":
    print("Doctors available are:")
    print("DR. Ankita Dutta")
    print("DR. Jason Gerald Silva")
elif j=="dermatology" or j=="DERMATOLOGY":
    print("Doctors available are:")
    print("DR. Sarthak Singh")
    print("DR. Maha Abdul Ali")
elif j=="neurology" or j=="NEUROLOGY":
    print("Doctors Available are:")
    print("DR. Prachi Chauhan")
    print("DR. Akshay Kulkarni")
else:
    if j=="general" or j=="GENERAL":
        print("Doctors Available are:")
        print("DR. Mohammed Ayman")
        print("DR. Niya Khan")
        print("DR. Geeta Damodharan")
k=str(input("Doctor:"))
print("You have Registered with;",k)
print("Token No:",random.randrange(1,100))
if k=="DR. Saraswati Sharma":
    print("Room No: 101")
elif k=="DR. Lyanna D'Souza":
    print("Room No: 103")
elif k=="DR. Saif Qureshi":
    print("Room No: 105")
elif k=="DR. Nandita Jain":
    print("Room No: 107")
elif k=="DR. Anuradha Khanna":
    print("Room No: 201")
elif k=="DR. Suzzane Terence":
    print("Room No: 204")
elif k=="DR. Lilly Singh":
    print("Room No: 207")
elif k=="DR. Ankita Dutta":
    print("Room No: 301")
elif k=="DR. Jason Gerald Silva":
    print("Room No: 304")
elif k=="DR. Sarthak Singh":
    print("Room No: 307")
elif k=="DR. Maha Abdul Ali":
    print("Room No: 401")
elif k=="DR. Prachi Chauhan":
    print("Room No: 404")
elif k=="DR. Akshay Kulkarni":
    print("Room No: 407")
elif k=="DR. Mohammed Ayman":
    print("Room No: 501")
elif k=="DR. Niya Khan":
    print("Room No: 504")
elif k=="DR. Geeta Damodharan":
    print("Room No: 507")

l=15.000
m=0
n=str(input("Company:"))
if n=="macfin" or n=="MACFIN":
   x=l*0.2
   z=n
elif n=="saud bahwan" or n=="SAUD BAHWAN":
    x=l*0.1
    z=n
elif n=="starcare" or n=="STARCARE":
    x=l*0.3
    z=n
elif n=="aster" or n=="ASTER":
     x=l*0.4
     z=n
elif n=="suhail bahwan" or n=="SUHAIL BAHWAN":
    x=l*0.1
    z=n
else:
    x=n
    z="Not a Partner of this Corporation"
print("Registration Fee : OMR 15.000")
print("Partner:",n)
print("Discounted Fee:","OMR",x)
print("Total R.O.:",l-x)
o=str(input("Payment Method:"))
p=random.randrange(10000000,99999999)

if j=="paediatrics" or j=="PAEDIATRICS":
    print("Invoice No:","3 -","PD -",p)
elif j=="gynaecology" or j=="GYNAECOLOGY":
    print("Invoice No:","7 -","GY -",p)
elif j=="cardiology" or j=="CARDIOLOGY":
    print("Invoice No:","1 -","CD -",p)
elif j=="ophthalmology" or j=="OPHTHALMOLOGY":
    print("Invoice No:","5 -","OP -",p)
elif j=="dermatology" or j=="DERMATOLOGY":
    print("Invoice No:","9 -","DM -",p)
elif j=="neurology" or j=="NEUROLOGY":
    print("Invoice No:","4 -","NR -",p)
else:
    if j=="general" or j=="GENERAL":
        print("Invoice No:","2 -","GN -",p)
import json        
MENU={"Time":a,"Date":b,"status":c,"phone number":d,"patient registration number":e,"Name":f,"age":g,"Parent/spouse name":y,"Nationality":h,"Resident card number":i,"department":j,"Doctor":k,"company":n,"payment method":o}
print("PATIENT RECORD:")
print(json.dumps(MENU,indent=2))
print("THANK YOU FOR USING STARCARE HEALTH SERVICES!")
print("KEEP CARING.....")








      
          
