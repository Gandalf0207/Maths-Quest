# Maths-Quest

> [!IMPORTANT]
> Pour toute information complémentaire au niveau des droits d'auteur et de distribution, veuillez vous référer à la licence.

> [!IMPORTANT]
> Si vous rencontrez un bug dans le jeu ou si vous souhaitez proposer des idées de mises à jour, merci de suivre les modèles présents [ici](.github/ISSUE_TEMPLATE)

Maths-Quest est un projet étudiant réalisé par 2 élèves en première NSI : **LUBAN Théo** & **PLADEAU Quentin**. Le but de ce projet est de réaliser un petit jeu de labyrinthe et de maths avec le langage de programmation Python et le module de GUI (graphical user interface) Tkinter qui est natif à Python. Le jeu se veut durable et unique, c'est pourquoi le point fort du jeu est l'aléatoire. En effet, que ce soit la génération de la carte ou encore les problèmes mathématiques, toutes les valeurs sont aléatoires. Cela rend donc chaque partie unique !

Notre projet est composé de deux éléments principaux :
- Des Maths
  - Équations du premier degré
  - Volumes
  - Fonctions affines & Equation de droite
  - Système d'équation à 2 inconnues
  - Équation du second degré (polynôme)
  - Dérivation
  - Suites
- Informatique
  - Utilisation du module Python
  - Utilisation du langage LaTeX pour respecter les normes d'écriture mathématique
  - Utilisation des dépendances des modules Python & LaTeX
  - Utilisation du module Git 

<br> </br>
### Comment Jouer ?

#### Résumé :
Le jeu se présente donc sous la forme d'un GUI. Après le lancement du jeu, il vous suffit de vous déplacer sur la carte, à la recherche des personnages non joueurs qui seront là pour vous donner de petits objets, qui plus tard, une fois assemblés, vous permettront d'accéder aux niveaux supérieurs. Le jeu, au lancement, se présente sous deux formes : soit une partie courte (choix entre le niveau de mathématiques de première ou seconde) soit une partie longue (les deux niveaux combinés). Le jeu se termine par l'affrontement d'un boss (2 boss si la partie choisie est longue). Le boss vous pose un problème de maths et vous devez le résoudre. Pour vous aider : le cours que tous les PNJ vous auront donné ainsi que des indices disponibles au nombre de trois. Ce jeu est donc un outil éducatif autour des maths pour les élèves et équipes pédagogiques de première et seconde ou plus.

#### Pas-à-pas :
Exécutez le fichier "Maths-Quest.exe". Après son exécution, vous devriez voir cette fenêtre apparaître : (insérer img fenetre load)
Vous avez donc le choix entre 2 options :
- Une partie courte :
  - Soit autour du programme de seconde en maths
  - Soit autour du programme de première en maths
- Une partie longue :
  - Les deux programmes seront combinés

Une fois votre choix fait, sélectionnez le bouton jouer pour lancer la partie.
Vous arrivez sur une carte qui est générée aléatoirement. (insérer img map nv1). Votre but va être de vous déplacer à l'aide des flèches de votre clavier, afin d'aller à la rencontre des personnages non joueurs (PNJ) qui sont présents sur la carte. Chaque PNJ est unique et vous donnera non seulement une partie de cours de mathématiques mais également un objet qui, une fois assemblé, vous permettra d'ouvrir la porte pour accéder au niveau supérieur. Une fois que vous vous êtes déplacé jusqu'à un PNJ, vous pouvez presser la barre espace pour entamer la discussion avec le personnage. Appuyez sur le bouton suivant à chaque fin de dialogue pour passer au dialogue suivant. Pour obtenir l'objet et la partie du cours, il vous faut discuter jusqu'à la fin du dialogue. Si vous partez avant la fin, il faudra recommencer la discussion. Pour chaque PNJ, un objet différent est donné. Vous ne pouvez donc pas obtenir plusieurs objets d'un même PNJ/niveau. Vous pouvez, si vous le souhaitez, rediscuter avec un PNJ, ils sont sympas ;)

Dès que vous avez obtenu tous les objets des différents PNJ de la carte, vous pouvez observer votre cours complet dans la boîte latérale droite (insérer img box cours). Vous devez vous rendre au début du labyrinthe, l'endroit où vous êtes apparu pour pouvoir assembler la grande clé à partir de tous les objets que vous aurez obtenus. Une fois à côté de la table de fabrication, appuyez sur la touche "c". Vous avez donc fabriqué la grande clé, elle apparaît dans votre inventaire (insérer img inv grande clé nv1 & img craft table).

Vous devez maintenant vous rendre à la porte (insérer img porte map). Une fois à côté de la porte, appuyez sur la barre "espace" pour pouvoir déverrouiller la porte avec la grande clé que vous venez de fabriquer. Une fenêtre va s'ouvrir (la fenêtre peut demander un peu de temps au chargement, max 30s). C'est une fenêtre d'exercice en rapport avec le cours que vous pouvez consulter dans le menu latéral droit (boîte du cours). Veuillez donc lire les consignes et explications en haut de cette nouvelle fenêtre et cliquez sur suivant pour résoudre l'exercice. Une fois que vous avez résolu l'exercice et trouvé une réponse, un choix de trois réponses vous est proposé, vous devez cliquer sur la réponse que vous avez trouvée. Une réponse parmi les trois est juste.
- Si vous avez sélectionné la bonne réponse, cliquez sur suivant et vous passerez au niveau supérieur.
- Si vous avez sélectionné la mauvaise réponse, cliquez également sur suivant jusqu'à ce que la fenêtre se ferme et vous pouvez recommencer l'énigme de la porte.
A noter également que si vous fermez manuellement la fenêtre de l'énigme de la porte, vous devrez en réouvrir une nouvelle et recommencer l'énigme.

Une fois le niveau supérieur atteint, vous pouvez recommencer ! Le cours va s'accumuler sur le menu latéral droit jusqu'au boss, où tout le cours en question vous sera nécessaire. Sur chaque niveau, un cours précis vous sera donné. Le nombre de PNJ est variable selon le niveau où vous vous trouvez.

Quand vous arrivez au niveau du boss, le principe est le même, vous devez vous déplacer jusqu'au boss puis presser la barre "espace" pour pouvoir l'affronter (img boss). Une nouvelle fenêtre va s'ouvrir et vous devrez résoudre un problème reprenant tous les exercices que vous avez eus jusqu'à présent. Des indices sont également à votre disposition, vous pouvez les obtenir en cliquant dessus (insérer img indices). A noter que chaque fois que vous utilisez un indice, vous descendez de score :
- 0 Indice utilisé --> Médaille de diamant
- 1 Indice utilisé --> Médaille d'or
- 2 Indices utilisés --> Médaille d'argent
- 3 Indices utilisés --> Médaille de bronze
Votre score sera affiché à la fin de votre partie.

##### Voilà, vous avez terminé le jeu !

<br> </br>
### Installation :
> [!NOTE]
> Le jeu et le système d'installation ont été développés pour les machines utilisant Windows 10 et plus.
> Si vous utilisez des versions antérieures ou encore un autre système d'exploitation (Linux / MacOS), veillez à ce que chaque élément d'installation soit compatible, téléchargez les éléments en compatibilité avec votre machine.

Afin de pouvoir utiliser le jeu sans soucis, nous vous demandons de bien vouloir suivre pas-à-pas l'installation décrite ci-dessous du projet.

#### 2 modes d'installation :
- Si vous avez reçu par votre professeur un dossier contenant les éléments nécessaires à l'installation, veuillez suivre le PDF d'installation donné avec, vous pouvez également le retrouver [ici](insérer le lien).
- Si vous avez juste à votre disposition ce GitHub, veuillez suivre attentivement l'installation ci-dessous :

  ##### Téléchargement des .exe nécessaires au jeu :
  Vous devez récupérer les 4 .exe qui sont nécessaires à l'installation :
  - [Git](https://git-scm.com/)
  - [Python](https://www.python.org/downloads/release/python-3123/) *Une version récente est préférable*
  - [MikTeX](https://miktex.org/download)
  - [Visual C++ x64](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

  Une fois que vous avez récupéré ces 4 fichiers exécutables, executez-les dans l'ordre de téléchargement 1 par 1.

  ##### Clône du repositorie GitHub:
  Après avoir installer les 4 fichiers executables, vous devez récupérer le projet. Pour ce faire, dans votre invite de commande, exécutez la commande ci-dessous :

  > Clone du dossier contenant le jeu
  ```
  git clone https://github.com/Gandalf0207/Maths-Quest.git
  ```
 
  ##### Téléchargement des dépendances nécessaires au jeu :
  Veillez à redémarrer votre machine si nécessaire pour permettre à votre système de bien intégrer l'installation des logiciels précédents. Après cela, il vous faut installer différentes dépendances nécessaires au bon fonctionnement du jeu.
  Vous avez 2 possibilités de le faire :
  
  - Vous pouvez exécuter simplement le script [Installateur_dépendances](Installateurs/Installateur_dependances.py).
  - Vous pouvez installer manuellement les dépendances. Pour ce faire, ouvrez un terminal (cmd / powershell...) et entrez les commandes suivantes dans l'ordre donné.
    Pour chacune des comande en rapport avec des dépendances Latex, une fenêtre peut s'ouvrir, il vous faut accpeter l'installation

  > Mettre à jour pip 
  ```
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip
  ```
  > Installation de la dépendance : matplotlib
  ```
  pip install matplotlib
  ```
  > Installation extension LaTeX : type1cm.sty
  ```
  mpm --install type1cm
  ```
  > Installation extension LaTeX : type1ec.sty
  ```
  mpm --install cm-super
  ```
  > Installation extension LaTeX : geometry.sty
  ```
  mpm --install geometry
  ```
  > Installation extension LaTeX : underscore.sty
  ```
  mpm --install underscore
  ```
  > Installation extension LaTeX : ttfonts.map
  ```
  mpm --install zhmetrics
  ```

<br>

  Si vous rencontrez des problèmes avec des éléments de l'installation, vérifiez bien que vous respectez les différents éléments de prévention, présents dans les explications de l'installation et ci-dessous.

<br>


> [!NOTE]
> Pour toutes les dépendances LaTeX, un pop-up va s'ouvrir, vous devrez cliquer sur Install pour pouvoir l'installer.

> [!TIP]
> Si vous utilisez une ancienne version de Windows ou bien que vous rencontrez toujours une erreur avec Visual C++ x64, installez également [Visual C++ x86](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

> [!TIP]
> Lorsque vous exécutez une commande **git clone**, assurez-vous que l'emplacement où vous êtes est le bon pour cloner le dossier. La commande **Git clone** n'est possible seulement di vous avez télécharger le .exe git

> [!WARNING]
> Veuillez faire attention au lieu d'installation des logiciels, et si nécessaire vous octroyer les droits en les ajoutant dans le **PATH**.

> [!WARNING]
> Si vous rencontrez un problème lors de l'installation des dépendances, après l'installation des logiciels.exe, veillez à redémarrer votre machine puis à réinstaller les dépendances.

<br> </br>
### Jouer :
Une fois tous les éléments de l'installation faits, vous pouvez profiter du jeu ! Pour le lancer, éxécuter le fichier "Maze-Mahts.exe"

  ##### Les déplacements : 
  - Haut --> Touche '↑'
  - Bas --> Touche '↓'
  - Gauche --> Touche '←'
  - Droite --> Touche '→'

  ##### Parler : 
  - Parler aux pnj --> Touche 'espace'
  - Affronter le boss --> Touche 'espace'

  ##### Autre : 
  - Fabriquer --> Touche 'c'

<br> </br>
### Crédits & Termes et Conditions d'utilisation :

  Merci d'utiliser ce jeu Python Maths-Quest, un projet créé avec passion pour l'amour des mathématiques et du partage de connaissances. Avant de continuer à utiliser ce logiciel, veuillez lire attentivement les conditions suivantes :

  1. Droit d'auteur : Ce jeu est protégé par les lois sur le droit d'auteur et est la propriété intellectuelle de LUBAN Théo & PLADEAU Quentin. Tous les droits qui ne sont pas expressément accordés dans ces conditions sont réservés.
  
  2. Utilisation personnelle : Ce jeu est destiné à un usage personnel et non commercial. Vous pouvez le partager avec des amis et des proches, mais toute distribution à des fins commerciales est strictement interdite sans autorisation préalable.
  
  3. Règlementation française : En utilisant ce jeu, vous acceptez de vous conformer à toutes les lois et réglementations en vigueur en France concernant les droits d'auteur, la propriété intellectuelle et toute autre loi applicable.
  
  4. Librairies open source : Ce jeu utilise des librairies open source telles que Python, Tkinter, Matplotlib, LaTeX, et d'autres. Nous reconnaissons et apprécions le travail des développeurs de ces librairies, et nous nous engageons à respecter les termes de leurs licences respectives. Les informations sur ces licences sont disponibles dans les fichiers correspondants du projet.
          
  5. Crédits : Nous tenons à remercier LUBAN Théo & PLADEAU Quentin pour leur contribution à ce projet. Leurs efforts ont été essentiels pour créer ce jeu. Nous apprécions également le soutien de ESCOUTE Cédric, qui a rendu ce projet possible.
  
  6. Cadre de réalisation : Ce jeu a été développé dans le cadre [du cours de NSI de première]. Nous sommes reconnaissants envers ESCOUTE Cédric pour son soutien et l'enseignement de connaissances ayant servi au projet.
  
  En utilisant ce jeu, vous acceptez ces termes et conditions. Si vous n'acceptez pas ces termes, veuillez ne pas utiliser ce logiciel. Ces termes et conditions peuvent être modifiés à tout moment sans préavis.
  
  Pour toute question ou préoccupation concernant ces termes et conditions, veuillez contacter votre enseignant vous ayant transmis une copie du projet.      

#
__© Tous droits réservés 2024__

*by LUBAN Théo & PLADEAU Quentin*














