#ΕΡΓΑΣΙΑ 2: Γινομενο πρώτων παραγόντων
while True:
        x=int(input("Dwste enan arithmo sto diasthma [2,1000000]: "))
        while x<2 or x>1000000:
                print("Dokimaste ksana!")
                x=int(input("Dwste enan arithmo sto diasthma [2,1000000]: "))
                
        arithmos=x
#Δημιουργία της λίστας των πρώτων αριθμών μεχρι το 2000.
#Aρχικοποιουμε την λιστα των πρωτων με τον αριθμό 2 που ειναι ο πρώτος πρώτος αριθμός
        prwtoi=[2]
        p=[0]
        i=3



        while i<2000:
                n=0 #metrhths
                for j in range(1,i+1):
                        if i%j==0:
                                n+=1

                if n==2: #Αν ο μετρητης ειναι ίσος με 2, αυτό σημαινει οτι αριθμος διαιρείται με τον εαυτό του και την μονάδα. Άρα ειναι πρώτος.
                        prwtoi.append(i)
                        
                i+=1
                
                

#Η λίστα p λειτουργεί ως μετρητής για καθέναν από τους πρώτους αριθμούς.
        
        
        p=[0]*(len(prwtoi)+1)       
        while x!=1:
                i=0
                while x!=1:
                        if x%prwtoi[i]==0:
                                x=x//prwtoi[i]
                                p[i]+=1
                                i=0
                        else:
                                i+=1

        msg=" "
        for i in range(len(prwtoi)):
                if p[i]!=0:
                        prwtos=str(prwtoi[i])
                        dunamh=str(p[i])
                
                        msg+="("+(prwtos + "**" + dunamh)+")" 

        
        print("To" ,arithmos, "grafetai" ,msg, "ws ginomeno prwtwn arithmwn")
        answer=str(input("Pieste 'ENTER' gia na ksanadwsete arithmo."))
        if answer!="":
                break
        
