# RAILWAY RESERVATION PROJECT
import csv
import sys
import random
def employee():
    a=open("emp.csv","r")
    data=csv.reader(a)
    
    l=[]
    l1=[]
    for i in data:
        l.append(i[0])
        l1.append(i[1])
    b=input("Enter emp id:")
    if b in l:
        x=l.index(b)
        c=input("Enter emp code:")
        if l1[x]==c:
            print("You logged in")
        else:
            print("Invalid emp code")
            sys.exit()
    else:
        print("Invalid emp id")
        sys.exit()
    a.close()
    f=open("paschim.csv","r")
    g=open("Unchara exp.csv","r")
    h=open("SHATABDI.csv","r")
    i=open("mks.csv","r")
    print("WELCOME DEAR EMPLOYEE")
    d=input("Do you want to know the passangers? y/n")
    if d.lower()=="y":
        print('''The trains available are:
                     1.)UNCHARA EXP
                     2.)SHATABDI
                     3.)MKS SUP FAST
                     4.)PASCHIM EXP''')
        e=int(input("Enter your option  (1,2,3,4)  :"))
        count1=0
        count2=0
        count3=0
        count4=0
        if e==1:
            file1=csv.reader(g)
            for A in file1:
                if A!=[]:
                    print(A)
                    count1=count1+1
            print("Number of passengers=",count1)
        elif e==2:
            file2=csv.reader(h)
            for B in file2:
                if B!=[]:
                    print(B)
                    count2=count2+1
            print("Number of passengers=",count2)
        elif e==3:
            file3=csv.reader(i)
            for C in file3:
                if C!=[]:
                    print(C)
                    count3=count3+1
            print("Number of passengers=",count3)
        elif e==4:
            file4=csv.reader(f)
            for D in file4:
                if D!=[]:
                    print(D)
                    count4=count4+1
            print("Number of passengers=",count4)
            
        else:
            print("wrong input")
        print("Thank You")
        
    else:
        print("ok")
        print("Thank You")
    f.close()
    g.close()
    h.close()
    i.close()
    z1=input("Do you wish to update any record (y/n):  ")
    if z1.lower()=="y":
        print('''YOU CAN UPDATE :
              1.)DATE OF TRAVEL
              2.)ARRIVAL DESTINATION
              3.)TIME OF DEPARTURE''')
        a1=open("paschim.csv","r")
        a2=open("Unchara exp.csv","r")
        a3=open("SHATABDI.csv","r")
        a4=open("mks.csv","r")
    
        z2=int(input("Enter your choice(1,2,3)  :"))
        z5=input("Token Number:  ")
        print('''The trains available are:
                     1.)UNCHARA EXP
                     2.)SHATABDI
                     3.)MKS SUP FAST
                     4.)PASCHIM EXP''')
        z3=int(input("Enter your option  (1,2,3,4)  :"))
        if z2==1:
            z4=input("Enter new date of travel:")
            lst=[]
            if z3==1:
                data1=list(csv.reader(a2))
                for i in data1:
                    k=data1.index(i)
                    if z5 in i:
                        data1[k][10]=z4
                    if i!=[]:
                        lst.append(i)
                t=open("Unchara exp.csv","w")        
                x1=csv.writer(t)
                x1.writerows(lst)
                t.close()
               
            
            elif z3==2:
                data2=list(csv.reader(a1))
                for j in data2:
                    k=data2.index(j)
                    if z5 in j:
                        data2[k][10]=z4
                    if j!=[]:
                        lst.append(j)
                v=open("SHATABDI.csv","w")        
                x2=csv.writer(v)
                x2.writerows(lst)
                v.close()
                
            elif z3==3:
                data3=list(csv.reader(a4))
                for m in data3:
                    k=data3.index(m)
                    if z5 in m:
                        data3[k][10]=z4
                    if m!=[]:
                        lst.append(m)
                x=open("mks.csv","w")        
                x3=csv.writer(x)
                x3.writerows(lst)
                x.close()
            else:
                data4=list(csv.reader(a1))
                for l in data4:
                    k=data4.index(l)
                    if z5 in l:
                        data4[k][10]=z4
                    if l!=[]:
                        lst.append(l)
                z=open("paschim.csv","w")        
                x4=csv.writer(z)
                x4.writerows(lst)
                z.close()
                   
        elif z2==2:
            z6=input("Enter new Arrival destination:")
            lst1=[]
            if z3==1:
                data1=list(csv.reader(a2))
                for i in data1:
                    k=data1.index(i)
                    if z5 in i:
                        data1[k][12]=z6
                    if i!=[]:
                        lst1.append(i)
                t=open("Unchara exp.csv","w")        
                x1=csv.writer(t)
                x1.writerows(lst1)
                t.close()
               
            elif z3==2:
                data2=list(csv.reader(a1))
                for j in data2:
                    k=data2.index(j)
                    if z5 in j:
                        data2[k][12]=z6
                    if j!=[]:
                        lst1.append(j)
                v=open("SHATABDI.csv","w")        
                x2=csv.writer(v)
                x2.writerows(lst1)
                v.close()
            elif z3==3:
                data3=list(csv.reader(a4))
                for m in data3:
                    k=data3.index(m)
                    if z5 in m:
                        data3[k][12]=z6
                    if m!=[]:
                        lst1.append(m)
                x=open("mks.csv","w")        
                x3=csv.writer(x)
                x3.writerows(lst1)
                x.close()
            else:
                data4=list(csv.reader(a1))
                for l in data4:
                    k=data4.index(l)
                    if z5 in l:
                        data4[k][12]=z6
                    if l!=[]:
                        lst1.append(l)
                z=open("paschim.csv","w")        
                x4=csv.writer(z)
                x4.writerows(lst1)
                z.close()
                
        else:
            z7=input("Enter new time:")
            lst2=[]
            if z3==1:
                data1=list(csv.reader(a2))
                for i in data1:
                    k=data1.index(i)
                    if z5 in i:
                        data1[k][13]=z7
                    if i!=[]:
                        lst2.append(i)
                t=open("Unchara exp.csv","w")        
                x1=csv.writer(t)
                x1.writerows(lst2)
                t.close()
               
            elif z3==2:
                data2=list(csv.reader(a1))
                for j in data2:
                    k=data2.index(j)
                    if z5 in j:
                        data2[k][13]=z7
                    if j!=[]:
                        lst2.append(j)
                v=open("SHATABDI.csv","w")        
                x2=csv.writer(v)
                x2.writerows(lst2)
                v.close()
            elif z3==3:
                data3=list(csv.reader(a4))
                for m in data3:
                    k=data3.index(m)
                    if z5 in m:
                        data3[k][13]=z7
                    if m!=[]:
                        lst2.append(m)
                x=open("mks.csv","w")        
                x3=csv.writer(x)
                x3.writerows(lst2)
                x.close()
            else:
                data4=list(csv.reader(a1))
                for l in data4:
                    k=data4.index(l)
                    if z5 in l:
                        data4[k][13]=z7
                    if l!=[]:
                        lst2.append(l)
                z=open("paschim.csv","w")        
                x4=csv.writer(z)
                x4.writerows(lst2)
                z.close()
            print("Thank You!!!!!")
            a1.close()
            a2.close()
            a3.close()
            a4.close()
    else:
        print("Thank You")
        
    v1=str(input("Do you wish to view specific record  (y/n)  :"))
    if v1.lower()=="y":
        print('''The trains available are:
                     1.)UNCHARA EXP
                     2.)SHATABDI
                     3.)MKS SUP FAST
                     4.)PASCHIM EXP''')
        v2=int(input("Enter your option  (1,2,3,4)  :"))
        v3=input("Token Number:")
        if v2==1:
            with open("Unchara exp.csv","r") as v4:
                file1=list(csv.reader(v4))
                flag=0
                for i in file1:
                    if v3 in i:
                        print(i)
                        flag=1
                        break
                if flag==0:
                    print("Invalid Token")
        elif v2==2:
            with open("SHATABDI.csv","r") as v4:
                file1=list(csv.reader(v4))
                flag=0
                for i in file1:
                    if v3 in i:
                        print(i)
                        flag=1
                        break
                if flag==0:
                    print("Invalid Token")
        elif v2==3:
            with open("mks.csv","r") as v4:
                file1=list(csv.reader(v4))
                flag=0
                for i in file1:
                    if v3 in i:
                        print(i)
                        flag=1
                        break
                if flag==0:
                    print("Invalid Token")
        else:
            with open("paschim.csv","r") as v4:
                file1=list(csv.reader(v4))
                flag=0
                for i in file1:
                    if v3 in i:
                        print(i)
                        flag=1
                        break
                if flag==0:
                    print("Invalid Token")
        print("THANK YOU!!!")
    else:
        print("THANK YOU!!!!")
        sys.exit()
    
                
                    
                
                        
        
    
                        
                   
                
            
            
       
        
       
def passenger():
    print('''What do you wish to do:
                1.)Reserve a ticket
                2.)Delete your reservatiion''')
    j=int(input("Enter your choice (1,2):"))
    if j==1:
        k=int(input("Enter number of passengers"))
        for i in range(k):
            n1=input("First Name:")
            n2=input("Last Name:")
            n3=input("Gender:")
            n4=input("Date of Birth")
            n5=int(input("Age"))
            n6=input("Nationality")
            n7=input("Email Id:")
            n8=int(input("Mobile No:"))
            n9=input("Address:")
            n10=random.randrange(5000,1000000)
            n11=input("Date of Travel:")
            n12=input("Departure from:")
            n13=input("Arrival at:")
            print('''Time for departure is:
                            11:45 am
                            3:30 pm
                            10:15 pm''')                            
            n14=input("Enter Time:")
            n15=input("Quota    (general/special)  :")
            n16=input("Class   (1s,2s,3s)   :")
            n17=input("Payement Method (Visa,Credit,American Express):")
            n18=200
            if n17.lower()=="visa":
                n18=n18+60
            elif n17.lower=="credit":
                n18=n18+80
            else:
                n18=n18+40
            print('''The trains available are:
                     1.)UNCHARA EXP
                     2.)SHATABDI
                     3.)MKS SUP FAST
                     4.)PASCHIM EXP''')
            l=int(input("Enter the train of your choice (1,2,3,4)    :"))
           
            if l==1:
                r=open("Unchara exp.csv","a")
                E=csv.writer(r)
                E.writerow([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18])
            elif l==2:
                s=open("SHATABDI.csv","a")
                F=csv.writer(s)
                F.writerow([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18])
            elif l==3:
                t=open("mks.csv","a")
                G=csv.writer(t)
                G.writerow([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18])
                
            else:
                q=open("paschim.csv","a")
                H=csv.writer(q)
                H.writerow([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18])
            print("Take a copy of the the below ticket\n")
            print("=====================================================================================================================================================================")
            print("~~~~~~~TICKET~~~~~~~~")
            print("_____________________")
            print("First Name:",n1,"\n","Last Name:",n2,"\n","Gender:",n3,"\n","Date of birth:",n4,"\n","Age:",n5,"\n","Nationality:",n6,"\n","Email ID:",n7,"\n","Mobile NO:",n8,"\n","Address:",n9,"\n","Token NO:",n10,"\n","Date:",n11,"\n","From:",n12,"\n","To:",n13,"\n","Time:",n14,"\n","Quota:",n15,"\n","Class:",n16,"\n","Payement:",n17,"\n","Amount:",n18,"\n")
            print("=====================================================================================================================================================================")
            print("Thank You!!!")
            sys.exit()
    else:
        q=str(input("Enter token number please:"))
        print('''The trains available are:
                     1.)UNCHARA EXP
                     2.)SHATABDI
                     3.)MKS SUP FAST
                     4.)PASCHIM EXP''')
        r=int(input("Enter the train of your choice (1,2,3,4)    :"))
        
        if r==1:
            s=open("Unchara exp.csv","r")
            L1=[]
            data=list(csv.reader(s))
            for i in data:
                if q not in i:
                    if i!=[]:
                        L1.append(i)
            s.close()      
            t=open("Unchara exp.csv","w")        
            x1=csv.writer(t)
            x1.writerows(L1)
            t.close()
        elif r==2:
            u=open("SHATABDI.csv","r")
            L2=[]
            data1=list(csv.reader(u))
            for j in data1:
                if q not in j:
                    if j!=[]:
                        L2.append(j)
            u.close()      
            v=open("SHATABDI.csv","w")        
            x2=csv.writer(v)
            x2.writerows(L2)
            v.close()
        elif r==3:
            w=open("mks.csv","r")
            L3=[]
            data2=list(csv.reader(w))
            for k in data2:
                if q not in k:
                    if k!=[]:
                        L3.append(k)
            w.close()      
            x=open("mks.csv","w")        
            x3=csv.writer(x)
            x3.writerows(L3)
            x.close()
        else:
            y=open("paschim.csv","r")
            L4=[]
            data3=list(csv.reader(y))
            for l in data3:
                if q not in l:
                    if l!=[]:
                        L4.append(l)
                    
            y.close()
            z=open("paschim.csv","w")        
            x4=csv.writer(z)
            x4.writerows(L4)
            z.close()
        print("Thank You")
       

def Viewer():
    print('''~~~~~~WELCOME TO BANGALORE CENTRAL RAILWAY~~~~~~
______________________________________________________________________

        STARTED IN 1988 THE RAILWAY HAS ALWAYS FOCUSSED TO PROVIDE THE BEST OF THE FACILITIES
        TO ITS PASSENGERS.
        THIS INTERACTIVE SYSTEM IS PURELY DEVELOPED TO MAKE PROVISIONS LIKE TICKET REGISTRATION,
        CANCELLATION AND UPDATION A WORK UNDER OUR FINGER TIPS.
        HOPE THIS WILL HELP YOU.  TEL:93563210
        THANK YOU:)
        HAVE A SAFE JOURNEY!!!''')
    
    
#MAIN PROGRAM
while(True):
    print("~~~~~~~~~~~~~~~~WELCOME TO BANGALORE CENTRAL RAILWAYS~~~~~~~~~~~~~~")
    print("_________________________________________________________________")
    print('''STATUS AVAILABLE ARE:
                1.)EMPLOYEE
                2.)PASSENGER
                3.)VIEWER''')
    s1=int(input("Enter your choice (1,2,3)   :  "))
    if s1==1:
        employee()
    elif s1==2:
        passenger()
    elif s1==3:
        Viewer()
    else:
        print("WRONG INPUT")
        sys.exit()
          

        
        
                
                

            
            
        
          
