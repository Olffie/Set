# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
ovaal = 0
rechthoek = 1
golf = 2

blauw = 0
groen = 1
rood = 2

leeg = 0
vol = 1
gespikkeld = 2

een = 0
twee = 1
drie = 2

        
class set_kaart:
    def __init__(self, aantal=0, vorm=0, kleur=0, vulling=0):
        self.aantal = aantal
        self.vorm = vorm
        self.kleur = kleur
        self.vulling = vulling
    
    def derde_kaart(self,other):
        kaart_3 = [self.aantal + other.aantal, self.vorm + other.vorm, 
                   self.kleur + other.kleur, self.vulling + other.vulling]
        for i in range(4):
            if kaart_3[i] % 3 == 1:
                kaart_3[i] += 2
            if kaart_3[i] % 3 == 2:
                kaart_3[i] += 1
            
        return kaart_3
        
        
        
        
        

set_stapel = []
for i in range (3):
    for j in range (3):
        for k in range (3):
            for l in range (3):
                set_stapel.append([i,j,k,l])
                


#a = set_stapel.pop(random.randrange(0,len(set_stapel))
                
kleurnaargetal("2","blauw","0","0")
