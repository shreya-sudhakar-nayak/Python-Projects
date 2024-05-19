import random
import sys
import json

print("WELCOME TO STARCARE HOSPITAL!")
b=str(input("Date: "))

Patients={}
q=int(input("Number of patients today: "))
for w in range(q):
    f=str(input("Patient Name: "))
    a=str(input("Time: "))
    c=str(input("Enter Status: "))
    if c=="new patient":
        c1=("New File No: ",random.randrange(11000000,11500000))
        print(c1)
        d=int(input("Phone Number: "))
        e=int(input("Patient Registration No(4-digit): "))
        g=int(input("Age :"))
        if g<18:
            y=str(input("Parent Name: "))
        else:
            y=str(input("Parent/Spouse Name: "))
            h=str(input("Nationality: "))
            i=str(input("Resident Card No: "))
    elif c=="existing patient":
        print("File No: ",random.randrange(10000000,11000000))
        print("Phone Number: ",random.randrange(91000000,99999999))
        e1=("Patient Registration No: ",random.randrange(1000,9999))
        print("Age: ",random.randrange(1,80))
        print("Resident Card No: ",random.randrange(1000000,9999999))
    else:
        sys.exit('''THANK YOU FOR USING STARCARE HEALTH SERVICES!
                    KEEP CARING...''')

    j=str(input("Department: "))
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
    k=str(input("Doctor: "))
    print("You have Registered with ",k)
    print("Token No: ",random.randrange(1,100))
    print("Room Number: ",random.randrange(101,509,2))
    l=15.000
    m=0
    n=str(input("Company: "))
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
        x=0
        z="Not a Partner of this Corporation"
    print("Registration Fee : OMR 15.000")
    print("Partner: ",z)
    print("Discounted Fee: ","OMR",x)
    print("Total R.O.: ",l-x)
    o=str(input("Payment Method: "))
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

if c=="New Patient":
        Patients[e]=f
else:
    if c=="Existing Patient":
        Patients[e1]=f
            
print("Patients today: ")
print(json.dumps(Patients,indent=1))

r=str(input("More Patients?: "))
if r=="n" or r=="NO":
    sys.exit('''THANK YOU FOR USING STARCARE HEALTH SERVICES!
                KEEP CARING...''')
elif r=="y" or r=="YES":
    q1=int(input("Number of patients today: "))
    for w1 in range(q1-q):
        f1=str(input("Patient Name: "))
        a1=str(input("Time: "))
        c1=str(input("Enter Status: "))
        if c2=="New Patient":
            c11=("New File No: ",random.randrange(11000000,11500000))
            d1=int(input("Phone Number: "))
            e2=int(input("Patient Registration No(4-digit): "))
            g1=int(input("Age: "))
            if g1<18:
                y1=str(input("Parent Name: "))
            else:
                y1=str(input("Parent/Spouse Name: "))
                h1=str(input("Nationality: "))
                i1=str(input("Resident Card No: "))
        elif c3=="Existing Patient":
            print("File No: ",random.randrange(10000000,11000000))
            print("Phone Number: ",random.randrange(91000000,99999999))
            e3=("Patient Registration No: ",random.randrange(1000,9999))
            print("Age: ",random.randrange(1,80))
            print("Resident Card No: ",random.randrange(1000000,9999999))
        else:
            if c1=="Done." or "Khalas!":
                sys.exit('''THANK YOU FOR USING STARCARE HEALTH SERVICES!
                         KEEP CARING...''')

        j1=str(input("Department: "))
        if j1=="paediatrics" or j1=="PAEDIATRICS":
            print("Doctors available are:")
            print("DR. Saraswati Sharma")
            print("DR. Lyanna D'Souza")
        elif j1=="gynaecology" or j1=="GYNAECOLOGY":
            print("Doctors available are:")
            print("DR. Saif Qureshi")
            print("DR. Nandita Jain")
        elif j1=="cardiology" or j1=="CARDIOLOGY":
            print("Doctor available are:")
            print("DR. Anuradha Khanna")
            print("DR. Suzzane Terence")
            print("DR. Lilly Singh")
        elif j1=="ophthalmology" or j1=="OPHTHALMOLOGY":
            print("Doctors available are:")
            print("DR. Ankita Dutta")
            print("DR. Jason Gerald Silva")
        elif j1=="dermatology" or j1=="DERMATOLOGY":
            print("Doctors available are:")
            print("DR. Sarthak Singh")
            print("DR. Maha Abdul Ali")
        elif j1=="neurology" or j1=="NEUROLOGY":
            print("Doctors Available are:")
            print("DR. Prachi Chauhan")
            print("DR. Akshay Kulkarni")
        else:
            if j1=="general" or j1=="GENERAL":
                print("Doctors Available are:")
                print("DR. Mohammed Ayman")
                print("DR. Niya Khan")
                print("DR. Geeta Damodharan")
        k1=str(input("Doctor: "))
        print("You have Registered with ",k1)
        print("Token No: ",random.randrange(1,100))
        print("Room Number: ",random.randrange(101,509,2))
        l1=15.000
        m1=0
        n1=str(input("Company: "))
        if n1=="macfin" or n1=="MACFIN":
            x1=l*0.2
            z1=n1
        elif n=="saud bahwan" or n=="SAUD BAHWAN":
            x1=l*0.1
            z1=n1
        elif n=="starcare" or n=="STARCARE":
            x1=l*0.3
            z1=n1
        elif n=="aster" or n=="ASTER":
            x1=l*0.4
            z1=n1
        elif n=="suhail bahwan" or n=="SUHAIL BAHWAN":
            x1=l*0.1
            z1=n1
        else:
            x1=0
            z1="Not a Partner of this Corporation"
        print("Registration Fee : OMR 15.000")
        print("Partner:",z1)
        print("Discounted Fee:","OMR",x1)
        print("Total R.O.:",l-x1)
        o1=str(input("Payment Method:"))
        p1=random.randrange(10000000,99999999)
        if j1=="paediatrics" or j1=="PAEDIATRICS":
            print("Invoice No:","3 -","PD -",p1)
        elif j1=="gynaecology" or j1=="GYNAECOLOGY":
            print("Invoice No:","7 -","GY -",p1)
        elif j1=="cardiology" or j1=="CARDIOLOGY":
            print("Invoice No:","1 -","CD -",p1)
        elif j1=="ophthalmology" or j1=="OPHTHALMOLOGY":
            print("Invoice No:","5 -","OP -",p1)
        elif j1=="dermatology" or j1=="DERMATOLOGY":
            print("Invoice No:","9 -","DM -",p1)
        elif j1=="neurology" or j1=="NEUROLOGY":
            print("Invoice No:","4 -","NR -",p1)
        else:
            if j1=="general" or j1=="GENERAL":
                print("Invoice No:","2 -","GN -",p1)
else:
    sys.exit('''THANK YOU FOR USING STARCARE HEALTH SERVICES!
                KEEP CARING...''')

if c2=="New Patient":
        Patients[e2]=f1
else:
    if c3=="Existing Patient":
        Patients[e3]=f1

print("Patients today:")
print(json.dumps(Patients,indent=1))

s=str(input("Delete patient record/s? "))
if s=="n" or s=="NO":
    sys.exit('''THANK YOU FOR USING STARCARE HEALTH SERVICES!
                KEEP CARING...''')
elif s=="y" or s=="YES":
    t=int(input("Record: "))
    for t in Patients:
        del Patients[t]
else:
    sys.exit('''THANK YOU FOR USING STARCARE HEALTH SERVICES!
                KEEP CARING...''')
    
print("Patients today:")
print(json.dumps(Patients,indent=1))

print("THANK YOU FOR USING STARCARE HEALTH SERVICES!")
print("KEEP CARING.....")
