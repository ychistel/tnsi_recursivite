import pyxel

class Disque:
    
    def __init__(self,i,n):
        assert 0 < i < 10,"erreur nombre disques entre 1 et 10"
        self.numero = i
        self.couleur = 16-i
        self.poteau = 1
        self.largeur = 4+i*4
        self.hauteur = 6
        self.x = 20 + (self.poteau-1)*42 - (self.largeur-4)//2
        self.y = 128-(n+1-i)*self.hauteur

class Poteau:
    
    def __init__(self,i):
        assert 0<i<4
        self.numero = i
        self.largeur = 4
        self.hauteur = 54
        self.x = 20 + (i-1)*42
        self.y = 74
        self.couleur = 4
        
class Tour_Hanoi:
    
    def __init__(self,n,solution):
        
        self.disques = [Disque(i,n) for i in range(1,n+1)]
        self.poteaux = [Poteau(i) for i in range(1,4)]
        self.etat = [n,0,0]
        self.etapes = solution
        self.suivant = False
        # taille de la fenetre 128x128 pixels
        pyxel.init(128, 128, title="Tours de Hanoi")
        
        # Lancement de la boucle de jeu
        pyxel.run(self.update,self.draw)

    # Etats du jeu
    def update(self):
        
        if self.suivant:
            if len(self.etapes) > 0:
                self.etapes.pop(0)
            self.suivant = False
        else:
            if len(self.etapes) > 0:
                num_disk,poteau_debut,poteau_fin = self.etapes[0]
                #print(num_disk,poteau_debut,poteau_fin)            
                if self.disques[num_disk-1].y > 60 and self.disques[num_disk-1].x == self.poteaux[poteau_debut-1].x-(self.disques[num_disk-1].largeur-4)//2:
                    self.disques[num_disk-1].y -= 2
                elif self.disques[num_disk-1].y == 60 and self.disques[num_disk-1].x < self.poteaux[poteau_fin-1].x-(self.disques[num_disk-1].largeur-4)//2 and poteau_debut < poteau_fin:
                    self.disques[num_disk-1].x += 2
                elif self.disques[num_disk-1].y == 60 and self.poteaux[poteau_fin-1].x-(self.disques[num_disk-1].largeur-4)//2 < self.disques[num_disk-1].x and poteau_debut > poteau_fin:
                    self.disques[num_disk-1].x -= 2
                elif self.disques[num_disk-1].y < 122-self.etat[poteau_fin-1]*self.disques[num_disk-1].hauteur and self.disques[num_disk-1].x == self.poteaux[poteau_fin-1].x-(self.disques[num_disk-1].largeur-4)//2:
                    self.disques[num_disk-1].y += 2
                else:
                    self.suivant = True
                    self.disques[num_disk-1].poteau = poteau_fin
                    self.etat[poteau_fin-1] += 1
                    self.etat[poteau_debut-1] -= 1    
                
    # Dessin des états du jeu
    def draw(self):
        pyxel.cls(0)
        for poteau in self.poteaux:
            pyxel.rect(poteau.x,poteau.y,poteau.largeur,poteau.hauteur,poteau.couleur)
        for disk in self.disques:
            pyxel.rect(disk.x,disk.y,disk.largeur,disk.hauteur,disk.couleur)