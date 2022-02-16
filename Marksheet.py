#user input
name=input("Enter Name= ")
roll=int(input("Enter seat no= "))
reg=int(input("Enter registration no= "))
center=input("Enter center code= ")
Result= "Pass"
#Theory input
while True:
     phy=int(input("Enter physics marks= "))
     if phy>=0 and phy<=60:
         break
     else:
         print("Invalid entry please enter marks between 0 to 60")

while True:
     m1=int(input("Enter Maths marks= "))
     if m1>=0 and m1<=60:
         break
     else:
         print("Invalid entry please enter marks between 0 to 60") 

while True:
     mech=int(input("Enter Mechanincs marks= "))
     if mech>=0 and mech<=60:
         break
     else:
         print("Invalid entry please enter marks between 0 to 60") 

while True:
     be=int(input("Enter Electronics marks= "))
     if be>=0 and be<=60:
         break
     else:
         print("Invalid entry please enter marks between 0 to 60")    
while True:
     itcp=int(input("Enter ITCP marks= "))
     if itcp>=0 and itcp<=60:
         break
     else:
         print("Invalid entry please enter marks between 0 to 60")    
while True:
     cs=int(input("Enter Communication Skills marks= "))
     if cs>=0 and cs<=60:
         break
     else:
         print("Invalid entry please enter marks between 0 to 60")    

#Lab marks
while True:
     itcpp=int(input("Enter ITCP lab marks= "))
     if itcpp>=0 and itcpp<=50:
         break
     else:
         print("Invalid entry please enter marks between 0 to 50")    

while True:
     bep=int(input("Enter Electronics lab marks= "))
     if bep>=0 and bep<=50:
         break
     else:
         print("Invalid entry please enter marks between 0 to 50")     
while True:
     phyp=int(input("Enter Physics lab marks= "))
     if phyp>=0 and phyp<=50:
         break
     else:
         print("Invalid entry please enter marks between 0 to 50")     
while True:
     mechp=int(input("Enter mechanics lab marks= "))
     if mechp>=0 and mechp<=50:
         break
     else:
         print("Invalid entry please enter marks between 0 to 50")     

#TA marks 
while True:
     tp=int(input("Enter TA physics marks= "))
     if tp>=0 and tp<=40:
         break
     else:
         print("Invalid entry please enter marks between 0 to 40")     
while True:
     tm1=int(input("Enter TA Maths marks= "))
     if tm1>=0 and tm1<=40:
         break
     else:
         print("Invalid entry please enter marks between 0 to 40")   
while True:
     tmech=int(input("Enter TA Mechanincs marks= "))
     if tmech>=0 and tmech<=40:
         break
     else:
         print("Invalid entry please enter marks between 0 to 40")   
while True:
     tbe=int(input("Enter TA Electronics marks= "))
     if tbe>=0 and tbe<=40:
         break
     else:
         print("Invalid entry please enter marks between 0 to 40")   
while True:
     titcp=int(input("Enter TA ITCP marks= "))
     if titcp>=0 and titcp<=40:
         break
     else:
         print("Invalid entry please enter marks between 0 to 40")   
while True:
     tcs=int(input("Enter TA Communication Skills marks= "))
     if tcs>=0 and tcs<=40:
         break
     else:
         print("Invalid entry please enter marks between 0 to 40")   
while True:
     titcpp=int(input("Enter TA ITCP lab marks= "))
     if titcpp>=0 and titcpp<=50:
         break
     else:
         print("Invalid entry please enter marks between 0 to 50")   
while True:
     tbep=int(input("Enter TA Electronics lab marks="))
     if tbep>=0 and tbep<=50:
         break
     else:
          print("Invalid entry please enter marks between 0 to 50")    
while True:
     tphyp=int(input("Enter TA Physics lab marks= "))
     if tphyp>=0 and tphyp<=50:
         break
     else:
          print("Invalid entry please enter marks between 0 to 50")    
while True:
     tmechp=int(input("Enter TA mechanics lab marks= "))
     if tmechp>=0 and tmechp<=50:
         break
     else:
          print("Invalid entry please enter marks between 0 to 50")    

#calculation

#Theory Calculation

mop=tp+phy


if mop<=100 and mop>=80:
    G="A"
    
elif mop<80 and mop>=60:
    G="B"
    
elif mop<60 and mop>=50:
    G="C"
    
elif mop<50 and mop>=40:
    G="D"
    
else:
    G="F" 
    Result="Fail" 

mom1=tm1+m1

if mom1<=100 and mom1>=80:
    G1="A"
elif mom1<80 and mom1>=60:
    G1="B" 
elif mom1<60 and mom1>=50:
    G1="C"
elif mom1<50 and mom1>=40:
    G1="D"
else:
    G1="F"
    Result= "Fail"

momech=tmech+mech

if momech<=100 and momech>=80:
    G2="A"
elif momech<80 and momech>=60:
    G2="B" 
elif momech<60 and momech>=50:
    G2="C"
elif momech<50 and momech>=40:
    G2="D"
else:
    G2="F"
    Result= "Fail"
mobe=tbe+be

if mobe<=100 and mobe>=80:
    G3="A"
elif mobe<80 and mobe>=60:
    G3="B" 
elif mobe<60 and mobe>=50:
    G3="C"
elif mobe<50 and mobe>=40:
    G3="D"
else:
    G3="F"
    Result="Fail"
moitcp=titcp+itcp

if moitcp<=100 and moitcp>=80:
    G4="A"
elif moitcp<80 and moitcp>=60:
    G4="B"
elif moitcp<60 and moitcp>=50:
    G4="C"
elif moitcp<50 and moitcp>=40:
    G4="D"
else:
    G4="F"
    Result="Fail"
mocs=tcs+cs

if mocs<=100 and mocs>=80:
    G5="A"
elif mocs<80 and mocs>=60:
    G5="B" 
elif mocs<60 and mocs>=50:
    G5="C"
elif mocs<50 and mocs>=40:
    G5="D"
else:
    G5='F'
    Result="Fail"
#Marks obtained practical

mophyp=tphyp+phyp

if mophyp<=100 and mophyp>=80:
    G6="A"
elif mophyp<80 and mophyp>=60:
    G6="B" 
elif mophyp<60 and mophyp>=55:
    G6="C"
elif mophyp<55 and mophyp>=50:
    G6="D"
else:
    G6="F"
    Result="Fail"
mobep=tbep+bep

if mobep<=100 and mobep>=80:
    G7="A"
elif mobep<80 and mobep>=60:
    G7="B"
elif mobep<60 and mobep>=55:
    G7="C"
elif mobep<55 and mobep>=50:
    G7="D"
else:
    G7="F"
    Result="Fail"
moitcpp=titcpp+itcpp

if moitcpp<=100 and moitcpp>=80:
    G8="A"
elif moitcpp<80 and moitcpp>=60:
    G8="B"
elif moitcpp<60 and moitcpp>=55:
    G8="C"
elif moitcpp<55 and moitcpp>=50:
    G8="D"
else:
    G8="F"
    Result="Fail"
momechp=tmechp+mechp

if momechp<=100 and momechp>=80:
    G9="A"
elif momechp<80 and momechp>=60:
    G9="B" 
elif momechp<60 and momechp>=55:
    G9="C"
elif momechp<55 and momechp>=50:
    G9="D"
else:
    G9="F"
    Result="Fail"




Tmo=mop+mom1+momech+mobe+moitcp+mocs+mophyp+mobep+moitcpp+momechp

 



M=1000
Percentage=(Tmo/1000)*100
cgpa=Percentage/9.5




print("                      Yeshwantrao Chavan College of Engineering            ")

print('',end='  ')

print('')
print("Name",name,end='                                                            ')
print('Semester = 1')

print("Registration no=",reg,end='                                                ')
print("Seat no =",roll)

print("center code ",center)

print("-------------------------------------------------------------------------------------------------------------------------------------")



print('Sr no  |  Subjects               | TA  | Total Marks  ',end=' || ' ) 
print('TA Marks obtained |  Marks obtained | Total Marks obtained |Grade ')

print("-------------------------------------------------------------------------------------------------------------------------------------")

print('1      |  Physics                | 40  | 100          ',end=' || ')
print(tp,"               | ", phy,"            |",mop,"                  |",G  )

print('2      |  Maths                  | 40  | 100          ',end=' || ')
print(tm1,"               | ", m1,"            |",mom1,"                  |",G1  )

print('3      |  Mechanics              | 40  | 100          ',end=' || ')
print(tmech,"               | ", mech,"            |",momech,"                 |",G2  )

print('4      |  Electronics            | 40  | 100          ',end=' || ')
print(tbe,"               | ", be,"            |",mobe,"                  |",G3  )

print('5      |  communication skills   | 40  | 100          ',end=' || ')
print(tcs,"               | ", cs,"            |",mocs,"                  |",G4  )

print('6      |  ITCP                   | 40  | 100          ',end=' || ')
print(titcp,"               | ", itcp,"            |",moitcp,"                  |",G5  )

print('7      |  ITCP Lab               | 50  | 100          ',end=' || ')
print(titcpp,"               | ", itcpp,"            |",moitcpp,"                  |",G8  )

print('8      |  Electronics lab        | 50  | 100          ',end=' || ')
print(tbep,"               | ", bep,"            |",mobep,"                  |",G7  )

print('9      |  Mechanics lab          | 50  | 100          ',end=' || ')
print(tmechp,"               | ", mechp,"             |",momechp,"                 |",G9  )

print('10     |  Physics Lab            | 50  | 100          ',end=' || ')
print(tphyp,"               | ", phyp,"            |",mophyp,"                  |",G6  )

print("--------------------------------------------------------------------------------------------------------------------------------------")

print("Total marks obtained=",Tmo,end='                               ')
print("Total marks= ",M)

print("Percentage=",Percentage,end='          ')
print("CGPA",cgpa)

print("Result=",Result)