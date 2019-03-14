# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

### Bonjour Melissa: tu dois ajouter «.py» à ton script pour que je puisse le faire fonctionner

fichier = "missions_JHR.csv" ### Je rebaptise ton fichier pour faire mes tests

url = "https://www.nasa.gov/missions"

entetes = {
	# "User-Agent : Tiffany Toussaint" ### Ici, il manquait une virgule pour séparer les deux éléments de ton dictionnaire; il fallait en outre mettre la clé et la valeur chacune dans leur paire de guillemets
	"User-Agent" : "Tiffany Toussaint",
	"From" : "cg491001@ens.uq-8am.ca"
}

contenu = requests.get(url, headers=entetes)
# page = BeautifulSoup(contenu.text,encode("latin-1").decode("utf-8"),"html.parser") ### Ici, ce n'est pas une virgule qui précède le «encode», mais un point. Par ailleurs, ce truc n'était pas nécessaire puisque l'encodage de la page était parfait 
page = BeautifulSoup(contenu.text,"html.parser")

# print()
# missions = page.find_all(class_="clickable") ### Ici, tu as reproduit l'exemple donné dans la vidéo. Il faut adapter ton script au contenu se trouvant dans la page que tu souhaites moissonner.
### La ligne ci-dessous aurait normalement dû marcher
# missions = page.find("div", id="content").find_all("p")

### Mais ce site est généré par du JavaScript et impossible à moissonner avec les méthodes que je vous ai montrées, malheureusement...
### Si tu fais print(page), tu vas voir que le code HTML que BeautifulSoup peut aller chercher est différent de celui que ton navigateur montre...
print(page)

for mission in missions:
	# print(mission)
	# print(page.find("div", class_"static-landing-page").find_next("url").find_all) ### Il manquait un «égale» ici; mais cette commande n'est pas très utile
	# href = (mission.find("a").["href"].text) ### Ici, le . n'était pas nécessaire avant le ["href"]
	href = (mission.find("a")["href"].text)
	# titre = (mission.find("href").["> <"] ### Pour extraire le nom des missions, c'est dans le contenu de la balise «a» qu'il fallait le trouver
	titre = mission.find("a").text
	infos = [href,titre]
	print("><"*30)

	nasa = open(fichier,"a")
	etoiles = vsc.writer(nasa)
	etoiles.writerow(infos)

### Ton script, corrigé comme je l'ai fait, aurait dû marcher si on avait eu affaire à un site «normal»... Tu ne seras pas pénalisée pour cela...