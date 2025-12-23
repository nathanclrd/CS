| Topic |
| :--- |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1. Chapitre : Outils d'analyse (1 démonstration)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2. Chapitre : Diagonalisation (13 démonstrations)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#3. Chapitre : Espaces Vectoriels (11 démonstrations)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4. Chapitre : Polynômes (11 démonstrations)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1. Les Définitions (À savoir mot pour mot)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2. Les "Gros" Théorèmes & Démonstrations (Le cœur de la théorie)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#3. Les "Questions Application" en Théorie]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Résumé pour ta "Nuit Blanche" :]] |

### 1. Chapitre : Outils d'analyse (1 démonstration)

Ce chapitre contient beaucoup de définitions et de résultats admis (comme le Théorème de Taylor), mais une seule démonstration complète est fournie.

- **Unicité de l'approximation polynomiale** (Proposition, points 1 et 2)1.
    

### 2. Chapitre : Diagonalisation (13 démonstrations)

Ce chapitre est très dense en démonstrations fondamentales pour l'algèbre linéaire.

- **Critère de valeur propre** : $\lambda$ est valeur propre ssi il est racine du polynôme caractéristique2.
    
- **Invariance du polynôme caractéristique** par similitude (matrices semblables)3.
    
- **Lien entre colonnes et vecteurs propres** : La $j$-ème colonne de $S^{-1}AS$ est $\lambda e_j$ ssi la $j$-ème colonne de $S$ est un vecteur propre4.
    
- **Inégalité des multiplicités** : Multiplicité géométrique $\le$ Multiplicité algébrique5.
    
- **Formule du déterminant** : Le déterminant est le produit des valeurs propres6.
    
- **Propriété du polynôme minimal (1)** : Il divise tout polynôme annulateur7.
    
- **Unicité du polynôme minimal**8.
    
- **Propriété du polynôme minimal (2)** : Il divise le polynôme caractéristique (conséquence de Cayley-Hamilton)9.
    
- **Lemme sur les polynômes de matrices** : Si $Ax=\lambda x$, alors $P(A)x = P(\lambda)x$10.
    
- **Racines du polynôme minimal** : Ce sont exactement les valeurs propres11.
    
- **Cas des valeurs propres simples (1)** : Si toutes les VP sont simples, le polynôme minimal égale le caractéristique (au signe près)12.
    
- **Théorème de diagonalisation** : Preuve des équivalences (A diagonalisable $\iff$ somme des multiplicités géométriques = m $\iff$ mult. alg. = mult. géo)13.
    
- **Cas des valeurs propres simples (2)** : Si A a des VP simples, elle est diagonalisable14.
    

### 3. Chapitre : Espaces Vectoriels (11 démonstrations)

Les démonstrations ici concernent la structure fondamentale des espaces de dimension finie.

- **Propriétés de la dépendance linéaire** (Points 1 et 5 : vecteur nul dépendant et ajout d'un vecteur dépendant)15.
    
- **Structure de sous-espace vectoriel (SEV)** : Un SEV est un espace vectoriel16.
    
- **Enveloppe linéaire** : C'est le plus petit SEV contenant l'ensemble17.
    
- **Critère de sous-espace vectoriel** : Stabilité par combinaison linéaire18.
    
- **Lemme fondamental** : Taille d'une partie libre $\le$ taille d'une partie génératrice19.
    
- **Théorème d'équipotence des bases** : Toutes les bases ont le même nombre d'éléments20.
    
- **Théorème de complétion (Corollaires)** : Toute partie génératrice contient une base / Toute partie libre est incluse dans une base21.
    
- **Dimension d'un sous-espace** : $\dim(F) \le \dim(E)$ et égalité ssi $F=E$22.
    
- **Théorème de décomposition** : Unicité des composantes dans une base23.
    
- **Composition des matrices de changement de base**24.
    
- **Inverse de la matrice de changement de base**25.
    

### 4. Chapitre : Polynômes (11 démonstrations)

Plusieurs preuves techniques (Leibniz, Binôme de Newton) sont laissées en exercice, mais les propriétés structurelles sont démontrées.

- **Intégrité** : $\mathbb{K}[X]$ est intègre26.
    
- **Division euclidienne** : Existence et unicité27.
    
- **Théorème de Gauss** : Si $D$ divise $PQ$ et $D \land P = 1$, alors $D$ divise $Q$28.
    
- **Formule de Taylor** pour les polynômes29.
    
- **Racine et évaluation** : $k$ est racine ssi $P(k)=0$30.
    
- **Conséquence du TFA (1)** : Deux polynômes ayant les mêmes racines sont égaux à une constante près31.
    
- **Conséquence du TFA (2)** : Deux polynômes égaux en $d+1$ points sont égaux32.
    
- **Conséquence du TFA (3)** : Égalité formelle $\iff$ Égalité des fonctions polynomiales33.
    
- **Lemme sur les complexes (1)** : Si $c$ est racine, son conjugué $\bar{c}$ l'est aussi (pour $P \in \mathbb{R}[X]$)34.
    
- **Lemme sur les complexes (2)** : Le produit $(X-c)(X-\bar{c})$ est un polynôme réel35.
    
- **Factorisation dans $\mathbb{R}[X]$** : Décomposition en facteurs de degré 1 et 236.





C'est une excellente stratégie. J'ai extrait et compilé **toutes** les questions théoriques posées dans les examens de ton fichier (de Janvier 2019 à Janvier 2025).

Puisque tu veux être sûr de ne rien rater, voici la liste exhaustive, classée par récurrence. Si tu maîtrises cette liste, tu couvres 100% de l'historique des examens.

### 1. Les Définitions (À savoir mot pour mot)

Ces définitions reviennent systématiquement (2 à 3 points "gratuits" à chaque examen).

- **Vecteurs linéairement indépendants (Libre) / Dépendants (Lié) :** (Très fréquent : Jan 19, Sept 19, Août 21, Août 23, Jan 24, Jan 25)
    
- **Approximation polynomiale au voisinage d'un point :** (Jan 22, Août 22, Jan 23, Jan 24, Jan 25)
    
- **Valeur propre, Vecteur propre & Polynôme caractéristique :** (Jan 19, Jan 23, Jan 25)
    
- **Matrice diagonalisable :** (Jan 19)
    
- **Partie génératrice, Base & Dimension.**
    
- **Image et Noyau d'une matrice.**
    
- **Combinaison linéaire / Enveloppe linéaire.**
    
- **Multiplicité d'un zéro (algébrique) vs Multiplicité géométrique.**
    
- **PGCD de deux polynômes.**
    
- **Fonction exponentielle** (Définition par série).
    

### 2. Les "Gros" Théorèmes & Démonstrations (Le cœur de la théorie)

Il y a presque toujours une démonstration de cours à faire (4 à 6 points). Voici les "stars" du cours :

#### **Top Priorité (Tombent très souvent)**

1. **Division Euclidienne des polynômes :**
    
    - **Énoncé complet.**
        
    - **Preuve de l'Unicité** (Jan 21, Août 22).
        
    - **Preuve de l'Existence** (Jan 22).
        
    - _Conseil :_ Apprends les deux, mais l'unicité tombe plus souvent.
        
2. **Lien Valeur Propre / Polynôme Caractéristique :**
    
    - **Preuve :** Démontrer qu'un nombre $\lambda$ est valeur propre ssi c'est une racine du polynôme caractéristique ($\det(A-\lambda I)=0$). (Sept 19, Jan 23, Jan 25).
        
3. **Indépendance linéaire et Combinaison linéaire :**
    
    - **Preuve :** Soit une famille libre $x_1, \dots, x_n$. Montrer que la famille $x_1, \dots, x_n, y$ est liée **si et seulement si** $y$ est combinaison linéaire des $x_i$. (Jan 19, Jan 21, Jan 23).
        
4. **Matrices Semblables ($A = S^{-1}BS$) :**
    
    - **Preuve :** Deux matrices semblables ont le même polynôme caractéristique (et donc les mêmes valeurs propres avec mêmes multiplicités).
        
    - **Contre-exemple :** Montrer que la réciproque est fausse (deux matrices peuvent avoir les mêmes VP sans être semblables, ex: Identité et une matrice triangulaire). (Jan 22, Août 22).
        
5. **Diagonalisation et Vecteurs Propres :**
    
    - **Preuve :** Si $A$ est diagonalisable par $S$, alors les colonnes de $S$ sont des vecteurs propres de $A$.
        
    - **Corollaire :** Une matrice de taille $m$ est diagonalisable ssi elle possède $m$ vecteurs propres linéairement indépendants. (Jan 23, Jan 24).
        

#### **Seconde Priorité (Tombent régulièrement)**

- **Théorème de Taylor-Lagrange :** Énoncé complet + Expliquer comment il permet d'estimer le reste (l'erreur). (Jan 19, Août 24, Jan 25).
    
- **Lemme de Gauss (Polynômes) :** Si $S$ divise $TU$ et est premier avec $T$, alors $S$ divise $U$. (Jan 19, Août 23, Jan 24).
    
- **Théorème du Rang :** Énoncé + Illustration avec une matrice donnée. (Août 21, Août 23, Jan 24).
    
- **Théorème de Steinitz :** Énoncé + Application (Août 24).
    

### 3. Les "Questions Application" en Théorie

Parfois, une question de théorie demande une petite application directe :

- **Trace et Déterminant :** Comment calculer la trace et le déterminant à partir des valeurs propres ? (Somme et Produit des VP). (Jan 21, Jan 22, Août 22, Jan 25).
    
- **Puissances de matrices :** Décrire la méthode pour calculer $A^n$ via la diagonalisation ($A^n = S D^n S^{-1}$) et donner l'avantage par rapport au calcul direct. (Août 23).
    
- **Racines et Conjugués :** Preuve que pour un polynôme réel, si $z$ est racine, alors $\bar{z}$ l'est aussi. (Jan 21).
    

### Résumé pour ta "Nuit Blanche" :

Si tu dois trier, voici l'ordre d'apprentissage :

1. **Définitions :** VP/Vecteur propre, Indépendance linéaire, Approx polynomiale.
    
2. **Preuves :** Unicité Division Euclidienne, Lien VP/Racine polynôme, Matrices semblables (mêmes VP).
    
3. **Théorèmes :** Taylor (énoncé + reste), Théorème du rang.
    

Tout est dans ton fichier `corriges-math-info2(1).pdf`. Concentre-toi sur les pages de correction "Théorie" de 2022, 2023 et 2024, c'est la matière la plus fraîche.