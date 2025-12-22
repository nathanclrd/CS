| Topic |
| :--- |
| [[#1. Dépendance Linéaire]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1. Propriétés élémentaires]] |
| [[#2. Sous-Espaces Vectoriels (SEV)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2. Structure de SEV]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#3. Enveloppe Linéaire]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4. Critère de Sous-Espace Vectoriel]] |
| [[#3. Dimension et Bases]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#5. Lemme Fondamental]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#6. Équipotence des bases]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#7. Corollaires de la Complétion]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#8. Dimension d'un SEV]] |
| [[#4. Composantes et Changement de Base]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#9. Unicité des composantes]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#10. Composition des matrices de changement de base]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#11. Inverse de la matrice de changement de base]] |

# Démonstrations : Espaces Vectoriels

Ce document recense les démonstrations du chapitre sur les **Espaces Vectoriels** tirées du cours _Mathématiques pour l'informatique 2_.

> [!INFO] Légende
> 
> - $E$ désigne un espace vectoriel sur un corps $\mathbb{K}$.
>     
> - Les démonstrations sont masquées par défaut. **Cliquez sur la flèche pour les révéler.**
>     

## 1. Dépendance Linéaire

### 1. Propriétés élémentaires

> [!important] Proposition
> 
> 1. Un vecteur $e$ est linéairement dépendant si et seulement si $e=0$.
>     
> 2. Soient $x_1, ..., x_n$ des vecteurs linéairement indépendants et $e$ un vecteur. Les vecteurs $x_1, ..., x_n, e$ sont linéairement dépendants si et seulement si $e \in \rangle x_1, ..., x_n \langle$.
>     

> [!example]- Démonstration (Point 1) **(**$\Leftarrow$**)** Le vecteur $0$ est linéairement dépendant car on peut écrire la combinaison linéaire non triviale : $1 \cdot 0 = 0$.
> 
> **(**$\Rightarrow$**)** Si $e$ est linéairement dépendant, il existe un scalaire $k \in \mathbb{K}$ **non nul** tel que $k \cdot e = 0$. Comme on est dans un corps, cela implique $k=0$ ou $e=0$. Puisque $k \neq 0$, on a nécessairement $e=0$.

> [!example]- Démonstration (Point 2) **(**$\Leftarrow$**)** Si $e$ est combinaison linéaire des $x_i$, on écrit $e = \sum k_i x_i$. Alors $\sum k_i x_i + (-1)e = 0$. C'est une combinaison linéaire nulle avec au moins un coefficient non nul ($-1$), donc la famille est liée.
> 
> **(**$\Rightarrow$**)** Supposons qu'il existe une relation de dépendance :
> 
> $$k_1 x_1 + ... + k_n x_n + k e = 0$$
> 
> avec les scalaires non tous nuls.
> 
> Si $k = 0$, alors $\sum k_i x_i = 0$. Comme les $x_i$ sont indépendants, tous les $k_i$ seraient nuls, ce qui contredit l'hypothèse (scalaires non tous nuls). Donc $k \neq 0$. On peut diviser par $k$ :
> 
> $$e = - \frac{k_1}{k} x_1 - ... - \frac{k_n}{k} x_n$$
> 
> Donc $e$ est bien combinaison linéaire des $x_i$.

## 2. Sous-Espaces Vectoriels (SEV)

### 2. Structure de SEV

> [!important] Proposition Un sous-espace vectoriel $F$ de $E$ (muni des opérations induites) est un espace vectoriel.

> [!example]- Démonstration Soit $F$ un SEV de $E$.
> 
> 1. **Opérations internes** : Par définition d'un SEV, l'addition et la multiplication scalaire sont stables (internes) à $F$.
>     
> 2. **Neutre** : Le vecteur $0$ appartient à $F$ (c'est la combinaison linéaire vide).
>     
> 3. **Opposé** : Pour tout $f \in F$, son opposé $-f = (-1) \cdot f$ appartient à $F$ par stabilité de la multiplication scalaire.
>     
> 4. **Axiomes** : Les propriétés d'associativité, commutativité, distributivité, etc., sont vraies pour tous vecteurs de $E$, donc a fortiori pour ceux de $F$.
>     

### 3. Enveloppe Linéaire

> [!important] Proposition L'enveloppe linéaire $\rangle A \langle$ est le plus petit (au sens de l'inclusion) sous-espace vectoriel contenant $A$.

> [!example]- Démonstration
> 
> 1. **C'est un SEV** : Une combinaison linéaire de combinaisons linéaires est encore une combinaison linéaire. Donc $\rangle A \langle$ est stable par combinaisons linéaires.
>     
> 2. **Il contient** $A$ : Tout vecteur $a \in A$ s'écrit $1 \cdot a$, donc $a \in \rangle A \langle$.
>     
> 3. **C'est le plus petit** : Tout SEV contenant $A$ doit contenir toutes les combinaisons linéaires des éléments de $A$ (par définition de la stabilité). Donc tout SEV contenant $A$ contient nécessairement $\rangle A \langle$.
>     

### 4. Critère de Sous-Espace Vectoriel

> [!important] Proposition Une partie $F$ de $E$ est un SEV si et seulement si :
> 
> 1. $0 \in F$
>     
> 2. $\forall x, y \in F, \forall k, l \in \mathbb{K} \implies kx + ly \in F$
>     

> [!example]- Démonstration **Condition nécessaire** : Immédiate par définition.
> 
> **Condition suffisante** : Montrons par récurrence que $F$ contient toute combinaison linéaire finie.
> 
> - **Base (**$n=0$**)** : La combinaison vide vaut $0$, qui est dans $F$ par (1).
>     
> - **Hérédité** : Supposons que $F$ contient les combinaisons de $n-1$ vecteurs. Soit $S = \sum_{i=1}^n k_i x_i = \underbrace{(\sum_{i=1}^{n-1} k_i x_i)}_{=u \in F \text{ (H.R.)}} + k_n x_n$. On a $S = 1 \cdot u + k_n x_n$. D'après la condition (2) avec $x=u, y=x_n$, on a $S \in F$.
>     
> 
> $F$ est donc stable par combinaisons linéaires et contient $0$, c'est un SEV.

## 3. Dimension et Bases

### 5. Lemme Fondamental

> [!important] Lemme Si $E$ admet une partie génératrice finie de taille $p$, alors toute partie libre de $E$ est de taille au plus $p$.

> [!example]- Démonstration On procède par l'absurde. Soit $G$ une partie génératrice de taille $p$ et $L$ une partie libre. Supposons que $|L| \ge p+1$.
> 
> Les vecteurs de $L$ sont dans $E$, donc ils sont tous combinaisons linéaires des vecteurs de $G$. Nous avons donc $p+1$ vecteurs qui sont combinaisons linéaires de $p$ vecteurs.
> 
> D'après le **Théorème de Steinitz** (admis ou vu précédemment : "Si $n+1$ vecteurs sont CL de $n$ vecteurs, ils sont liés"), les vecteurs de $L$ sont linéairement dépendants.
> 
> Ceci contredit le fait que $L$ est une partie libre.

### 6. Équipotence des bases

> [!important] Théorème Toutes les bases d'un espace vectoriel de dimension finie ont le même nombre d'éléments.

> [!example]- Démonstration Soient $B$ et $B'$ deux bases finies.
> 
> 1. $B$ est libre et $B'$ est génératrice. D'après le lemme fondamental : $|B| \le |B'|$.
>     
> 2. $B'$ est libre et $B$ est génératrice. D'après le lemme fondamental : $|B'| \le |B|$.
>     
> 
> Conclusion : $|B| = |B'|$. Ce nombre commun est la **dimension**.

### 7. Corollaires de la Complétion

> [!important] Corollaires
> 
> 1. Toute partie génératrice contient une base.
>     
> 2. Toute partie libre est incluse dans une base.
>     

> [!example]- Démonstration Ces résultats découlent du **Théorème de la base incomplète** (admis : pour toute famille libre $L$ et génératrice $G$, il existe une base $B$ telle que $L \subseteq B \subseteq L \cup G$).
> 
> 1. **Génératrice contient base** : On applique le théorème avec $L = \emptyset$. Il existe une base $B$ telle que $\emptyset \subseteq B \subseteq G$.
>     
> 2. **Libre incluse dans base** : On applique le théorème avec $G = E$. Il existe une base $B$ telle que $L \subseteq B \subseteq E$.
>     

### 8. Dimension d'un SEV

> [!important] Proposition Si $F$ est un SEV de $E$ (dimension finie) :
> 
> 1. $\dim(F) \le \dim(E)$
>     
> 2. $\dim(F) = \dim(E) \iff F = E$
>     

> [!example]- Démonstration Soit $B_F$ une base de $F$.
> 
> 1. **Inégalité** : $B_F$ est une famille libre dans $F$, donc c'est une famille libre dans $E$. On peut la compléter en une base $B_E$ de $E$. Donc $|B_F| \le |B_E|$, d'où $\dim(F) \le \dim(E)$.
>     
> 2. **Égalité** :
>     
>     - ($\Leftarrow$) Trivial.
>         
>     - ($\Rightarrow$) Si $\dim(F) = \dim(E)$, alors $|B_F| = |B_E|$. Comme $B_F \subseteq B_E$ (par construction de la complétion) et qu'ils ont le même cardinal fini, on a nécessairement $B_F = B_E$. Ainsi, la base de $F$ engendre tout $E$. Donc $E \subseteq F$. Comme $F \subseteq E$, on a $F=E$.
>         

## 4. Composantes et Changement de Base

### 9. Unicité des composantes

> [!important] Théorème Pour toute base $B=(b_1, ..., b_m)$ et tout vecteur $x$, les scalaires $x_i$ tels que $x = \sum x_i b_i$ sont uniques.

> [!example]- Démonstration **Existence** : Car $B$ est génératrice.
> 
> **Unicité** : Supposons deux écritures : $x = \sum x_i b_i = \sum y_i b_i$.
> 
> Par soustraction : $\sum (x_i - y_i) b_i = 0$.
> 
> Comme $B$ est une famille **libre**, la seule combinaison linéaire nulle est la triviale. Donc pour tout $i$, $x_i - y_i = 0 \implies x_i = y_i$.

### 10. Composition des matrices de changement de base

> [!important] Proposition $\mathcal{M}(B, B'') = \mathcal{M}(B', B'') \times \mathcal{M}(B, B')$

> [!example]- Démonstration On compare les colonnes des deux matrices. Soit $B=(b_1, ..., b_m)$.
> 
> 1. La $j$-ème colonne de $\mathcal{M}(B, B'')$ est, par définition, le vecteur des composantes de $b_j$ dans la base $B''$ : $\Psi_{B''}(b_j)$.
>     
> 2. Regardons le produit matriciel à droite. La $j$-ème colonne est : $\mathcal{M}(B', B'') \times (\text{$j$-ème colonne de } \mathcal{M}(B, B'))$ $= \mathcal{M}(B', B'') \times \Psi_{B'}(b_j)$.
>     
> 3. Or, la formule de changement de base dit que pour tout vecteur $v$ (ici $v=b_j$) : $\Psi_{B''}(v) = \mathcal{M}(B', B'') \Psi_{B'}(v)$.
>     
> 
> Les colonnes sont donc identiques deux à deux.

### 11. Inverse de la matrice de changement de base

> [!important] Corollaire $\mathcal{M}(B', B) = (\mathcal{M}(B, B'))^{-1}$

> [!example]- Démonstration On applique la proposition précédente avec $B'' = B$.
> 
> $$\mathcal{M}(B', B) \times \mathcal{M}(B, B') = \mathcal{M}(B, B) = I_m$$
> 
> (La matrice de passage d'une base vers elle-même est l'identité).
> 
> De même $\mathcal{M}(B, B') \times \mathcal{M}(B', B) = I_m$. Donc les matrices sont inverses l'une de l'autre.