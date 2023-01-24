import numpy as np
import datetime
import csv
fh=open('C:/Users/salam/Downloads/ADE_RT1_Septembre2022_Decembre2022.ics','r')
#print(ress)
#tableau_evenements=np.array([])

evenement=''
code=''
date1=''
debut=''
duree=''
cours=''
typecours=''
salle=''
prof=''
groupe=''
titre=''
continu= True
titre="UID"+";"+"date"+";"+"debut"+";"+"duree"+";"+"cours"+";"+"salle"+";"+"prof"+";"+"groupe"
valeur=[]
liste_valeur_split=[]

while continu:
    line=fh.readline()
    
    
    if "BEGIN:VCALENDAR":
      
        if "BEGIN:VEVENT":
            
                
                
                    
                if line.startswith("UID"):
                    texte=line.split(":")
                    textepart2=texte[1].split("\n")
                    code=textepart2[0]
             
        
                if line.startswith("DTSTART"):

                    texte=line.split(":")
                

                    annee1=texte[1][0:4]
                    mois1=texte[1][4:6]
                    jour1=texte[1][6:8]
                    
                    date1=jour1+'-'+mois1+'-'+annee1
                    
                    heure1=texte[1][9:11]
                    minute1=texte[1][11:13]
                    
                    
                    debut=heure1+':'+minute1
                    
                    
            
                if line.startswith("DTEND"):
                    texte=line.split(":")
                    annee2=texte[1][0:4]
                    mois2=texte[1][4:6]
                    jour2=texte[1][6:8]
                    
                    date2=jour2+"-"+mois2+"-"+annee2
            
                    heure2=texte[1][9:11]
                    minute2=texte[1][11:13]
                    
                    fin=heure2+":"+minute2
                    
            
                if line.startswith("SUMMARY"):
                    texte=line.split(":")
                    textepart2=line.split(" ")
                    textepart3=texte[1].split(" ")
                    textepart4=texte[1].split("\n")
                    #print(texte)
                    cours=textepart4[0]
                    #typecours=textepart3[1]
                    
                    #print(textepart4)
                if line.startswith("LOCATION"):
                    texte=line.split(":")
                    textepart2=texte[1].split("\n")
                    salle=textepart2[0]
                    
                
                if line.startswith("DESCRIPTION"):
                    texte=line.split(":")
                    textepart2=line.split(" ")
                    textepart3=line.split("\\n")
                    groupe=textepart3[2][7:9]
                    prof=textepart3[3]
                    
                
                #duree=heure2-heure1
                   

                if line.startswith("END:VEVENT"):
                    duree=int(heure2)-int(heure1)
                 
                    evenement=code+";"+date1+";"+debut+";"+str(duree)+";"+cours+";"+salle+";"+prof+";"+groupe
                    valeur.append(evenement)
                    
                    
                    
                    
                    #print(evenement)
                        
                if line == '':  
                    print("end of file")
                    break

for j in range (len(valeur)):
    valeur_split=valeur[j].split(",")
    liste_valeur_split.append(valeur_split)
    
    
with open('tableau.csv','a') as file:
    writer=csv.writer(file)
    writer.writerow([titre])
    for i in range (len(liste_valeur_split)):
        writer.writerow(liste_valeur_split[i])
        print(liste_valeur_split[i])
    file.close()            
   
fh.close()  


"""
    if event.startswith('LOCATION'):
        texte1=event.split(";")

    
"""    
    
