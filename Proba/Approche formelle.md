| Topic                                                                                   |
| :-------------------------------------------------------------------------------------- |
| [[#Tags: #Probabilités #Kolmogorov #Conditionnement #Bayes #ULiège #Synthèse]]          |
| [[#3.1 Mesure de probabilité]]                                                          |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#La $\sigma$-algèbre (Le domaine de définition)]]             |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Axiomes de Kolmogorov]]                                      |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Propriétés fondamentales et théoriques]]                     |
| [[#3.2 Retour sur le cas fini]]                                                         |
| [[#3.3 Probabilités conditionnelles]]                                                   |
| [[#3.4 Indépendance d'événements]]                                                      |
| [[#3.5 Loi des probabilités totales]]                                                   |
| [[#3.6 Formule de Bayes]]                                                               |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Exemple : L'énigme des chaussettes (Bayes III)]]             |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1. Preuve des règles de calcul (Prop 3.1.7)]]                |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2. Preuve que la probabilité conditionnelle est une mesure]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#3. Retour sur le cas fini équiprobable (Slide 15)]]          |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4. Probabilité d'une union dénombrable (Slide 17)]]          |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#5. Preuves sur l'indépendance]]                              |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#6. Preuve de la Loi des probabilités totales]]               |

## Tags: #Probabilités #Kolmogorov #Conditionnement #Bayes #ULiège #Synthèse

Source: Éléments du calcul des probabilités Chapitre: 3

# Chapitre 3 : Approche formelle des probabilités

Ce chapitre développe le formalisme rigoureux des probabilités basé sur la théorie de la mesure (Axiomatique de Kolmogorov, 1933). Il permet de dépasser le cadre intuitif du cas équiprobable pour traiter des situations générales.

## 3.1 Mesure de probabilité

Pour définir une probabilité, il faut d'abord définir précisément l'ensemble des événements auxquels on peut attribuer une probabilité. C'est le rôle de la **tribu** (ou $\sigma$-algèbre).

### La $\sigma$-algèbre (Le domaine de définition)

Soit $\Omega$ l'espace fondamental. Une famille $\mathcal{F}$ de sous-ensembles de $\Omega$ est une $\sigma$-algèbre si elle vérifie trois propriétés de stabilité :

> [!abstract] Définition : $\sigma$-algèbre ($\mathcal{F}$)
> 
> 1. **L'espace entier** : $\Omega \in \mathcal{F}$.
>     
> 2. **Complémentaire** : Si $A \in \mathcal{F}$, alors $A^c \in \mathcal{F}$.
>     
> 3. **Union dénombrable** : Si $(A_j)_{j}$ est une suite d'éléments de $\mathcal{F}$, alors $\bigcup_j A_j \in \mathcal{F}$.
>     

_Conséquences_ : $\emptyset \in \mathcal{F}$ et $\mathcal{F}$ est stable par intersection dénombrable. _Exemple_ : La $\sigma$-algèbre de **Borel** sur $\mathbb{R}$ est celle engendrée par les intervalles.

### Axiomes de Kolmogorov

Une fois l'espace mesurable $(\Omega, \mathcal{F})$ défini, on définit la probabilité comme une fonction.

> [!def] Définition : Mesure de probabilité Une application $\mathbb{P}: \mathcal{F} \to [0,1]$ est une probabilité si :
> 
> 1. **Normalisation** : $\mathbb{P}(\Omega) = 1$.
>     
> 2. $\sigma$**-additivité** : Pour toute suite $(A_j)_{j}$ d'événements **deux à deux disjoints** (incompatibles) :
>     
>     $$\mathbb{P}\left(\bigcup_{j} A_j\right) = \sum_{j} \mathbb{P}(A_j)$$

Le triplet $(\Omega, \mathcal{F}, \mathbb{P})$ est appelé un **espace probabilisé**.

### Propriétés fondamentales et théoriques

Outre les règles de calcul de base, l'axiomatique implique des propriétés de convergence essentielles pour l'analyse.

> [!tip] Règles de calcul (Proposition 3.1.7)
> 
> - **Vide** : $\mathbb{P}(\emptyset) = 0$.
>     
> - **Complémentaire** : $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$.
>     
> - **Monotonie** : Si $A \subseteq B$, alors $\mathbb{P}(A) \le \mathbb{P}(B)$.
>     
> - **Union quelconque** : $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$.
>     

> [!important] Propriétés de continuité et bornes
> 
> 1. **Sous-additivité (Inégalité de Boole)** : Pour toute suite d'événements $(A_j)$ (pas nécessairement disjoints) :
>     
>     $$\mathbb{P}\left(\bigcup_{j} A_j\right) \le \sum_{j} \mathbb{P}(A_j)$$
> 2. **Continuité de la mesure** : Si une suite d'événements est croissante ($A_n \subseteq A_{n+1}$) vers $A$ (c'est-à-dire $A = \bigcup A_n$), alors :
>     
>     $$\lim_{n \to \infty} \mathbb{P}(A_n) = \mathbb{P}(A)$$
>     
>     _Ceci est également vrai pour les suites décroissantes (_$A_n \supseteq A_{n+1}$_) vers l'intersection._
>     

## 3.2 Retour sur le cas fini

Le formalisme général englobe les cas vus au Chapitre 1.

- **Mesure de Laplace** (cas équiprobable) : $\mathbb{P}(A) = \frac{\#A}{\#\Omega}$.
    
- **Cas pondéré** : $\mathbb{P}(A) = \sum_{\omega \in A} p(\omega)$.
    

## 3.3 Probabilités conditionnelles

Cette notion permet de mettre à jour la probabilité d'un événement $A$ sachant qu'un événement $B$ s'est réalisé.

> [!def] Définition Si $\mathbb{P}(B) > 0$, la probabilité conditionnelle de $A$ sachant $B$ est :
> 
> $$\mathbb{P}(A|B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$$

> [!important] Formules du produit (Probabilités composées)
> 
> **Cas simple (2 événements)** :
> 
> $$\mathbb{P}(A \cap B) = \mathbb{P}(A|B) \cdot \mathbb{P}(B)$$
> 
> **Généralisation (**$n$ **événements)** : Pour une suite d'événements $A_1, \dots, A_n$ :
> 
> $$\mathbb{P}(A_1 \cap \dots \cap A_n) = \mathbb{P}(A_1) \cdot \mathbb{P}(A_2 | A_1) \cdot \mathbb{P}(A_3 | A_1 \cap A_2) \cdot \dots \cdot \mathbb{P}(A_n | A_1 \cap \dots \cap A_{n-1})$$
> 
> _C'est la règle de la chaîne, très utile pour calculer la probabilité d'une séquence temporelle d'événements._

**Propriété fondamentale** : Si on fixe $B$, l'application $\mathbb{P}(\cdot|B)$ est elle-même une mesure de probabilité. Elle vérifie donc toutes les règles (complémentaire, union, etc.).

## 3.4 Indépendance d'événements

L'indépendance signifie que la réalisation de $B$ n'influence pas la probabilité de $A$.

> [!def] Définition Deux événements $A$ et $B$ sont **indépendants** (noté $A \perp\!\!\perp B$) si :
> 
> $$\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$$

_Équivalent à_ $\mathbb{P}(A|B) = \mathbb{P}(A)$ _(si_ $\mathbb{P}(B) > 0$_)._

> [!warning] Indépendance mutuelle (pour $n$ événements) Pour que des événements $A_1, \dots, A_n$ soient mutuellement indépendants, il ne suffit pas qu'ils le soient deux à deux. Il faut que la règle du produit fonctionne pour **tous** les sous-groupes possibles d'indices $J \subseteq \{1, \dots, n\}$ :
> 
> $$\mathbb{P}\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} \mathbb{P}(A_j)$$

## 3.5 Loi des probabilités totales

C'est un outil puissant pour calculer la probabilité d'un événement $A$ en le décomposant selon les scénarios possibles (une partition).

> [!important] Théorème Soit $(B_j)_j$ une **partition** de $\Omega$ (événements disjoints dont l'union fait $\Omega$, avec $\mathbb{P}(B_j)>0$). Alors pour tout événement $A$ :
> 
> $$\mathbb{P}(A) = \sum_{j} \mathbb{P}(A | B_j) \cdot \mathbb{P}(B_j)$$

_Interprétation_ : C'est une moyenne pondérée des probabilités conditionnelles.

## 3.6 Formule de Bayes

La formule de Bayes permet d'"inverser" le conditionnement : calculer $\mathbb{P}(B|A)$ alors qu'on connait $\mathbb{P}(A|B)$. C'est la base de l'inférence (diagnostic, apprentissage).

> [!summary] Les Formules de Bayes
> 
> **Formule Simple (I)** :
> 
> $$\mathbb{P}(B|A) = \frac{\mathbb{P}(A|B) \cdot \mathbb{P}(B)}{\mathbb{P}(A)}$$
> 
> **Formule avec Probabilités Totales (II & III)** : Si $\{B_j\}$ est une partition de l'espace :
> 
> $$\mathbb{P}(B_k | A) = \frac{\mathbb{P}(A | B_k) \cdot \mathbb{P}(B_k)}{\sum_{j} \mathbb{P}(A | B_j) \cdot \mathbb{P}(B_j)}$$

### Exemple : L'énigme des chaussettes (Bayes III)

_Contexte (vu au cours)_ : Adam, Benjamin et David ont retrouvé une chaussette noire. Qui l'a perdue ?

- **Données** :
    
    - Adam (A) : 3 chaussettes noires, 5 colorées. Risque de perte $\times 2$. ($P(A) = 1/2$)
        
    - Benjamin (B) : 2 chaussettes noires, 7 colorées. Risque normal. ($P(B) = 1/4$)
        
    - David (D) : 4 chaussettes noires, 3 colorées. Risque normal. ($P(D) = 1/4$)
        
- **Probabilités de tirer une noire (N)** :
    
    - $P(N|A) = 3/8$
        
    - $P(N|B) = 2/9$
        
    - $P(N|D) = 4/7$
        
- **Résolution (Qui est le propriétaire ?)** :
    
    $$P(A|N) = \frac{P(N|A)P(A)}{P(N)} = \frac{\frac{3}{8} \cdot \frac{1}{2}}{\frac{3}{8}\cdot\frac{1}{2} + \frac{2}{9}\cdot\frac{1}{4} + \frac{4}{7}\cdot\frac{1}{4}} \approx 0.49$$
    
    _Conclusion : C'est probablement Adam._
    

# 3.7 Démonstrations et Notes de cours (Tableau)

Cette section regroupe les démonstrations transcrites directement depuis les notes manuscrites des diapositives ("photos des tableaux").

### 1. Preuve des règles de calcul (Prop 3.1.7)

_Notes manuscrites du slide 12 (Partie 1)_

**a) Complémentaire :** $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$

- On sait que $A \cup A^c = \Omega$.
    
- $A$ et $A^c$ sont disjoints ($A \cap A^c = \emptyset$).
    
- Par l'axiome de $\sigma$-additivité : $\mathbb{P}(\Omega) = \mathbb{P}(A \cup A^c) = \mathbb{P}(A) + \mathbb{P}(A^c)$.
    
- Comme $\mathbb{P}(\Omega)=1$, on a $1 = \mathbb{P}(A) + \mathbb{P}(A^c)$, d'où le résultat.
    

**b) Ensemble vide :** $\mathbb{P}(\emptyset) = 0$

- $\emptyset = \Omega^c$.
    
- Donc $\mathbb{P}(\emptyset) = 1 - \mathbb{P}(\Omega) = 1 - 1 = 0$.
    

**c) Monotonie : Si** $A \subseteq B$**, alors** $\mathbb{P}(A) \le \mathbb{P}(B)$

- On décompose $B$ en union disjointe : $B = A \cup (B \setminus A)$.
    
- Donc $\mathbb{P}(B) = \mathbb{P}(A) + \mathbb{P}(B \setminus A)$.
    
- Comme une probabilité est toujours positive ($\mathbb{P}(B \setminus A) \ge 0$), on a $\mathbb{P}(B) \ge \mathbb{P}(A)$.
    
- _Note_ : On déduit aussi $\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A)$.
    

**d) Union quelconque :** $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$

- On décompose l'union : $A \cup B = A \cup (B \cap A^c)$. (C'est une union disjointe).
    
- Donc $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B \cap A^c)$.
    
- Or, on sait que $B = (A \cap B) \cup (B \cap A^c)$ (aussi disjointe).
    
- Donc $\mathbb{P}(B) = \mathbb{P}(A \cap B) + \mathbb{P}(B \cap A^c)$, ce qui implique $\mathbb{P}(B \cap A^c) = \mathbb{P}(B) - \mathbb{P}(A \cap B)$.
    
- En remplaçant dans la première équation : $\mathbb{P}(A \cup B) = \mathbb{P}(A) + [\mathbb{P}(B) - \mathbb{P}(A \cap B)]$.
    

### 2. Preuve que la probabilité conditionnelle est une mesure

_Notes manuscrites du slide 25 (Partie 1)_

On veut montrer que $\mathbb{P}(\cdot | B)$ vérifie les axiomes de Kolmogorov.

1. **Bornes** : $0 \le \mathbb{P}(A|B) \le 1$.
    
    - Car $A \cap B \subseteq B$, donc par monotonie $\mathbb{P}(A \cap B) \le \mathbb{P}(B)$.
        
    - Le quotient est donc $\le 1$.
        
2. **Normalisation** : $\mathbb{P}(\Omega | B) = 1$.
    
    - $\mathbb{P}(\Omega | B) = \frac{\mathbb{P}(\Omega \cap B)}{\mathbb{P}(B)} = \frac{\mathbb{P}(B)}{\mathbb{P}(B)} = 1$.
        
3. $\sigma$**-additivité** :
    
    - Soit $(A_j)$ une suite d'événements deux à deux disjoints.
        
    - $\mathbb{P}(\bigcup_j A_j | B) = \frac{\mathbb{P}((\bigcup_j A_j) \cap B)}{\mathbb{P}(B)}$.
        
    - Par distributivité : $(\bigcup_j A_j) \cap B = \bigcup_j (A_j \cap B)$.
        
    - Comme les $A_j$ sont disjoints, les $(A_j \cap B)$ le sont aussi.
        
    - Donc $\mathbb{P}(\bigcup_j (A_j \cap B)) = \sum_j \mathbb{P}(A_j \cap B)$.
        
    - On divise tout par $\mathbb{P}(B)$ : $\sum_j \frac{\mathbb{P}(A_j \cap B)}{\mathbb{P}(B)} = \sum_j \mathbb{P}(A_j | B)$.
        

**Conséquence** : $\mathbb{P}(A^c|B) = 1 - \mathbb{P}(A|B)$.

### 3. Retour sur le cas fini équiprobable (Slide 15)

Soit $\Omega = \{\omega_1, \dots, \omega_n\}$ et $\mathbb{P}(\{\omega_j\}) = p$.

- **Valeur de** $p$ : $\mathbb{P}(\Omega) = \sum \mathbb{P}(\{\omega_j\}) = np = 1 \implies p = 1/n$.
    
- **Probabilité de** $A$ : $\mathbb{P}(A) = \sum_{\omega \in A} \frac{1}{n} = \frac{\#A}{n}$.
    

### 4. Probabilité d'une union dénombrable (Slide 17)

On veut montrer que la mesure équiprobable $\mathbb{P}(A) = \frac{\#A}{\#\Omega}$ vérifie l'additivité pour une suite $(A_k)$ disjointe.

1. $\mathbb{P}(\bigcup_k A_k) = \frac{\#(\bigcup_k A_k)}{\#\Omega}$.
    
2. Comme les $A_k$ sont disjoints, $\#(\bigcup_k A_k) = \sum_k \#A_k$.
    
3. Donc $\mathbb{P}(\bigcup_k A_k) = \frac{\sum_k \#A_k}{\#\Omega}$.
    
4. Par linéarité : $\sum_k \frac{\#A_k}{\#\Omega} = \sum_k \mathbb{P}(A_k)$.
    

### 5. Preuves sur l'indépendance

_Notes manuscrites du slide 10 (Partie 2)_

**a) Si** $\mathbb{P}(B)=0$**, alors** $A$ **et** $B$ **sont indépendants**

- $A \cap B \subseteq B \implies 0 \le \mathbb{P}(A \cap B) \le \mathbb{P}(B) = 0$. Donc $\mathbb{P}(A \cap B)=0$.
    
- $\mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(A) \cdot 0 = 0$.
    

**b)** $A \perp\!\!\perp B \iff A \perp\!\!\perp B^c$

- $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$.
    
- Si $A \perp\!\!\perp B$, alors $\mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(A)(1-\mathbb{P}(B)) = \mathbb{P}(A)\mathbb{P}(B^c)$.
    

### 6. Preuve de la Loi des probabilités totales

_Notes manuscrites du slide 21 (Partie 2)_

Soit $(B_j)$ une partition de $\Omega$.

- $A = A \cap \Omega = A \cap (\bigcup_j B_j) = \bigcup_j (A \cap B_j)$.
    
- Les $(A \cap B_j)$ sont disjoints.
    
- $\mathbb{P}(A) = \sum_j \mathbb{P}(A \cap B_j) = \sum_j \mathbb{P}(A | B_j) \mathbb{P}(B_j)$.