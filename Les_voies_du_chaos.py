import pygame
import os
import random
import time


pygame.init()

clock = pygame.time.Clock()
size = width, height = (800, 600)
ecran = pygame.display.set_mode(size)



##IMPORTATION IMAGES
voiture_img = pygame.image.load('Voiture_iso_essai2.png')
poubelle_img = pygame.image.load('poubelle.png')
monstre_bleu_img = pygame.image.load('monstre_bleu.png')
monstre_rose_img = pygame.image.load('monstre_rose.png')
monstre_marron_img = pygame.image.load('monstre_marron.png')
monstre_violet_img = pygame.image.load('monstre_violet.png')
arbre_vert_img = pygame.image.load('arbre_vert.png')
arbre_rose_img = pygame.image.load('arbre_rose.png')
sapin_img = pygame.image.load('sapin.png')
rocher_img = pygame.image.load('rocher.png')
plusieurs_rochers_img = pygame.image.load('plusieurs_rochers.png')
vie_0 = pygame.image.load('vie_0.png')
vie_1 = pygame.image.load('vie_1.png')
vie_2 = pygame.image.load('vie_2.png')
vie_3 = pygame.image.load('vie_2.png')
vie_4 = pygame.image.load('vie_4.png')
vie_5 = pygame.image.load('vie_5.png')
vie_6 = pygame.image.load('vie_6.png')
vie_7 = pygame.image.load('vie_7.png')
vie_8 = pygame.image.load('vie_8.png')
vie_9 = pygame.image.load('vie_9.png')
vie_10 = pygame.image.load('vie_10.png')
image_perdu = pygame.image.load('image_perdu.png')
image_debut = pygame.image.load('image_debut.png')

#liste pour les images de la barre de vie
liste_images_vies = [vie_0 , vie_1 , vie_2 , vie_3 , vie_4 , vie_5 , vie_6 , vie_7 , vie_8 , vie_9 , vie_10]



#CREATION DU FOND
def decor():
    ecran.fill("darkgreen")

    #Séparateurs de route
    pygame.draw.line(ecran,"black",(0,350),(800,600-((0.5*600)/0.87)-350))
    pygame.draw.line(ecran,"black",(0,450),(800,600-((0.5*600)/0.87)-250))
    pygame.draw.line(ecran,"black",(0,550),(800,600-((0.5*600)/0.87)-150))
    pygame.draw.line(ecran,"black",(0,650),(800,600-((0.5*600)/0.87)-50))

    #Axes pour la voiture
    pygame.draw.line(ecran,"darkgrey",(0,400),(800,600-((0.5*600)/0.87)-300),100)
    pygame.draw.line(ecran,"grey",(0,500) , (800,600-((0.5*600)/0.87)-200) ,100)
    pygame.draw.line(ecran,"darkgrey",(0 , 600) , (800 , 600-((0.5*600)/0.87)-100) , 100)



#Fonction d'image aléatoire pour les monstres puis pour le décor
def images_alea():
    liste = [monstre_bleu_img , monstre_marron_img , monstre_rose_img , monstre_violet_img]
    image = random.choice(liste)
    return image

def images_decor_alea():
    liste = [arbre_vert_img , arbre_rose_img , sapin_img , rocher_img , plusieurs_rochers_img]
    image = random.choice(liste)
    return image

##CLASSES
class Voiture:
    X_POS = 40
    Y_POS = 315
    X_POS_2 = 100
    Y_POS_2 = 380
    X_POS_3 = 165
    Y_POS_3 = 445

    def __init__(self):
        self.image = voiture_img
        self.voiture_rect = self.image.get_rect()
        self.voiture_rect.x = self.X_POS
        self.voiture_rect.y = self.Y_POS

        self.voie_1 = True
        self.voie_2 = False
        self.voie_3 = False

    #Fonction pour savoir où doit aller la voiture en fonction des touches appuyées
    def update(self, userInput):

        if self.voie_1 :
            self.go_1()
        if self.voie_2 :
            self.go_2()
        if self.voie_3 :
            self.go_3()

        if userInput[pygame.K_UP] and self.voiture_rect.x != self.X_POS:

            if self.voiture_rect.x == self.X_POS_2:
                self.voie_1 = True
                self.voie_2 = False
                self.voie_3 = False
            else :
                self.voie_1 = False
                self.voie_2 = True
                self.voie_3 = False

        elif userInput[pygame.K_DOWN] and self.voiture_rect.x != self.X_POS_3:

            if self.voiture_rect.x == self.X_POS_2:
                self.voie_1 = False
                self.voie_2 = False
                self.voie_3 = True
            else :
                self.voie_1 = False
                self.voie_2 = True
                self.voie_3 = False


    #Coordonnées pour la voiture en fonction des voies
    def go_1(self):
        self.voiture_rect = self.image.get_rect()
        self.voiture_rect.x = self.X_POS
        self.voiture_rect.y = self.Y_POS

    def go_2(self):
        self.voiture_rect = self.image.get_rect()
        self.voiture_rect.x = self.X_POS_2
        self.voiture_rect.y = self.Y_POS_2

    def go_3(self):
        self.voiture_rect = self.image.get_rect()
        self.voiture_rect.x = self.X_POS_3
        self.voiture_rect.y = self.Y_POS_3


    def draw(self, ecran):
        ecran.blit(self.image, (self.voiture_rect.x, self.voiture_rect.y))

class voie_1():
    OBS_X_POS_1 = 585
    OBS_Y_POS_1 = 35

    def __init__(self):
        self.image = images_alea()
        self.obstacle_rect = self.image.get_rect()
        self.obstacle_rect.x = self.OBS_X_POS_1
        self.obstacle_rect.y = self.OBS_Y_POS_1


    #Fonction pour le déplacement du monstre
    def deplacement(self):
        self.obstacle_rect.x -= x_deplacement
        self.obstacle_rect.y = 370 - (0.5*self.obstacle_rect.x)/0.87

    #Fonction pour afficher l'image
    def draw(self, ecran):
        ecran.blit(self.image, (self.obstacle_rect.x, self.obstacle_rect.y))

class voie_2():
    OBS_X_POS_2 = 650
    OBS_Y_POS_2 = 100

    def __init__(self):
        self.image = images_alea()
        self.obstacle_rect = self.image.get_rect()
        self.obstacle_rect.x = self.OBS_X_POS_2
        self.obstacle_rect.y = self.OBS_Y_POS_2

    def deplacement(self):
        self.obstacle_rect.x -= x_deplacement
        self.obstacle_rect.y = 475 - (0.5*self.obstacle_rect.x)/0.87

    def draw(self, ecran):
        ecran.blit(self.image, (self.obstacle_rect.x, self.obstacle_rect.y))

class voie_3():
    OBS_X_POS_3 = 700
    OBS_Y_POS_3 = 175

    def __init__(self):
        self.image = images_alea()
        self.obstacle_rect = self.image.get_rect()
        self.obstacle_rect.x = self.OBS_X_POS_3
        self.obstacle_rect.y = self.OBS_Y_POS_3

    def deplacement(self):
        self.obstacle_rect.x -= x_deplacement
        self.obstacle_rect.y = 575 - (0.5*self.obstacle_rect.x)/0.87

    def draw(self, ecran):
        ecran.blit(self.image, (self.obstacle_rect.x, self.obstacle_rect.y))

class decor_haut:
    DEC_X_POS_H_R = 445 #Decor _ x _ position _ haut _ rocher
    DEC_Y_POS_H_R = 15
    DEC_X_POS_H_A = 445 #Decor _ x _ position _ haut _ arbre
    DEC_Y_POS_H_A = 5

    def __init__(self):
        self.image = images_decor_alea()
        self.obstacle_rect = self.image.get_rect()
        if self.image == rocher_img or self.image == plusieurs_rochers_img:
            self.obstacle_rect.x = self.DEC_X_POS_H_R
            self.obstacle_rect.y = self.DEC_Y_POS_H_R
        else:
            self.obstacle_rect.x = self.DEC_X_POS_H_A
            self.obstacle_rect.y = self.DEC_Y_POS_H_A

    def deplacement(self):
        self.obstacle_rect.x -= x_deplacement
        self.obstacle_rect.y = 265 - (0.5*self.obstacle_rect.x)/0.87

    def draw(self, ecran):
        ecran.blit(self.image, (self.obstacle_rect.x, self.obstacle_rect.y))

class decor_bas:
    DEC_X_POS_B_R = 750 #Decor _ x _ position _ haut _ rocher
    DEC_Y_POS_B_R = 230
    DEC_X_POS_B_A = 750 #Decor _ x _ position _ haut _ arbre
    DEC_Y_POS_B_A = 210

    def __init__(self):
        self.image = images_decor_alea()
        self.obstacle_rect = self.image.get_rect()
        if self.image == rocher_img or self.image == plusieurs_rochers_img:
            self.obstacle_rect.x = self.DEC_X_POS_B_R
            self.obstacle_rect.y = self.DEC_Y_POS_B_R
        else:
            self.obstacle_rect.x = self.DEC_X_POS_B_A
            self.obstacle_rect.y = self.DEC_Y_POS_B_A

    def deplacement(self):
        self.obstacle_rect.x -= x_deplacement
        self.obstacle_rect.y = 645 - (0.5*self.obstacle_rect.x)/0.87

    def draw(self, ecran):
        ecran.blit(self.image, (self.obstacle_rect.x, self.obstacle_rect.y))


#voie aléatoire
def alea_voie():
    global liste_voies
    if len(liste_voies) != 0 :
        voie = random.choice(liste_voies)
        liste_voies.remove(voie)
        return voie()
    else:
        liste_voies = [voie_1 , voie_2 , voie_3]
        return M_1

#decor aléatoire
def decor_alea():
    liste = [decor_haut , decor_bas]
    cote = random.choice(liste)
    return cote


liste_voies = [voie_1 , voie_2 , voie_3]



#CREATION OBSTACLES UN PAR UN
M_1 = (alea_voie())
M_2 = (alea_voie())
M_3 = (alea_voie())
M_4 = (alea_voie())
M_5 = (alea_voie())

l_obst = [M_1 , M_2 , M_3 , M_4 , M_5]



#CREATION DECOR
Dec_1 = decor_haut()
Dec_2 = decor_bas() #ICI


#Coordonées pour les collisions
voie_2_collision_haut = (80,400)
voie_3_collision_haut = (135,470)


#Initalisation des différentes variables
compteur=0
compteur_temps = 0
vitesse=5 # à augmenter si on veut que ca commence plus lentement
x_deplacement = 3
collision = 100 # points de vie
image_vie = vie_10 # image de la barre de vie au début
decor_plus_existe = 0 #Pour les éléments du décor, afficher s'ils existent
score = 0 #score
run=True

#Préparation de l'affichage du score à la fin
police = pygame.font.SysFont("Times New Roman", 18)

player = Voiture()



#Petit message avant le début de partie
decor()
ecran.blit(image_debut,(0,100))
pygame.display.update()
time.sleep(9)


#Boucle pour la partie
while run:

    #vérification collision
    for i in range(5):

        pos_obstacle = (l_obst[i].obstacle_rect.x , l_obst[i].obstacle_rect.y)

        #si la position de l'obstacle est sur la voie 1 et que la voiture est sur la voie 1
        if pos_obstacle[0] < voie_2_collision_haut[0] and pos_obstacle[1] < voie_2_collision_haut[1] and player.voie_1 == True :

            collision -= 1


        if pos_obstacle[0] >= voie_2_collision_haut[0] and pos_obstacle[1] >= voie_2_collision_haut[1] and pos_obstacle[0] < voie_3_collision_haut[0] and pos_obstacle[1] < voie_3_collision_haut[1] and player.voie_2 == True :

            collision -= 1

        if pos_obstacle[0] >= voie_3_collision_haut[0] and pos_obstacle[1] >= voie_3_collision_haut[1] and player.voie_3 == True :

            collision -= 1


        #recréation des monstres + recréation des décors
        if i==0 and M_1.obstacle_rect.x < 10:
            M_1 = (alea_voie())
            l_obst[i] = M_1
        if i==1 and M_2.obstacle_rect.x < 10:
            M_2 = (alea_voie())
            Dec_2 = decor_haut()
            Dec_2_1 = decor_bas() #Decor pour le bas
            decor_plus_existe += 1
            l_obst[i] = M_2
        if i==2 and M_3.obstacle_rect.x < 10:
            M_3 = (alea_voie())
            Dec_3 = decor_haut()
            Dec_3_1 = decor_bas()
            decor_plus_existe += 1
            l_obst[i] = M_3
        if i==3 and M_4.obstacle_rect.x < 10:
            M_4 = (alea_voie())
            Dec_4 = (decor_alea())()
            decor_plus_existe += 1
            l_obst[i] = M_4
        if i==4 and M_5.obstacle_rect.x < 10:
            M_5 = (alea_voie())
            Dec_1 = (decor_alea())()
            l_obst[i] = M_5



#pour collision = 100 :
    if collision<=100 and collision>=91:
        image_vie = vie_10
    if collision<=90 and collision>=81:
        image_vie = vie_9
    if collision<=80 and collision>=71:
        image_vie = vie_8
    if collision<=70 and collision>=61:
        image_vie = vie_7
    if collision<=60 and collision>=51:
        image_vie = vie_6
    if collision<=50 and collision>=41:
        image_vie = vie_5
    if collision<=40 and collision>=31:
        image_vie = vie_4
    if collision<=30 and collision>=21:
        image_vie = vie_3
    if collision<=20 and collision>=11:
        image_vie = vie_2
    if collision<=10 and collision>= 1:
        image_vie = vie_1
    if collision <= 0 :
        image_vie = vie_0
        ecran.blit(image_vie,(15,15))
        ecran.blit(image_perdu,(0,125))
        #Affichage du score
        score_texte = police.render("Ton score : " + str(score), True, "black")
        score_texteRect = score_texte.get_rect()
        score_texteRect.center = ( width // 2, height // 2 + 50)
        ecran.blit(score_texte, score_texteRect)
        print("Perdu !")
        print("Ton score : ", score)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()


    #Récupération des touches
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    userInput = pygame.key.get_pressed()
    player.update(userInput)


    #Déplacements des monstres et décors
    if compteur == vitesse:
        score += 1
        M_1.deplacement()
        M_2.deplacement()
        M_3.deplacement()
        M_4.deplacement()
        M_5.deplacement()
        Dec_1.deplacement()
        Dec_2.deplacement()
        if decor_plus_existe >= 3:
            Dec_2_1.deplacement()
            Dec_3.deplacement()
            Dec_3_1.deplacement()
            Dec_4.deplacement() # ICI
        compteur=0
        compteur_temps += 1
        if vitesse >= 2 and compteur_temps == 5: #compteur_temps pour pas que ça augmente tout le temps la vitesse
            x_deplacement += 4 #Pour que les monstres de déplacent plus loin d'un coup
            vitesse -= 1 #Augmentation de la vitesse
            compteur_temps=0



    #Affichage de tous les éléments
    decor()
    player.draw(ecran)
    M_1.draw(ecran)
    M_2.draw(ecran)
    M_3.draw(ecran)
    M_4.draw(ecran)
    M_5.draw(ecran)
    Dec_1.draw(ecran)
    Dec_2.draw(ecran)
    if decor_plus_existe >= 3:
        Dec_2_1.draw(ecran)
        Dec_3.draw(ecran)
        Dec_3_1.draw(ecran)
        Dec_4.draw(ecran)

    ecran.blit(image_vie,(15,15))


    pygame.display.update()
    clock.tick(10)
    compteur+=1

pygame.quit()
