| Topic |
| :--- |
| [[#Tags: #Analyse #Mathématiques #Séries #Intégrales #ULiège #Synthèse]] |
| [[#2.1 Les suites et séries]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Suites]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Séries]] |
| [[#2.2 L'exponentielle]] |
| [[#2.3 Compléments de calcul intégral]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Intégrale double]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Changement de variable (Détails)]] |

## Tags: #Analyse #Mathématiques #Séries #Intégrales #ULiège #Synthèse

Source: Éléments du calcul des probabilités Chapitre: 2

# Chapitre 2 : Outils d'analyse pour les probabilités

Ce chapitre introduit les fondements d'analyse mathématique nécessaires au développement de la théorie des probabilités (séries, fonction exponentielle, intégrales multiples).

## 2.1 Les suites et séries

Cette section traite de la convergence, notion centrale pour les lois des grands nombres et les séries de probabilités.

### Suites

Une suite est une collection ordonnée d'éléments.

> [!note] Convention de notation
> 
> - **Minuscules** $(x_j)_{j \in \mathbb{N}^*}$ : Suites numériques (réels ou complexes).
>     
> - **Majuscules** $(A_j)_{j \in \mathbb{N}^*}$ : Suites d'ensembles (événements).
>     

**Convergence** : Une suite $(x_j)$ converge vers $x_0$ si pour tout $\epsilon > 0$, il existe un rang $J$ à partir duquel tous les termes sont à une distance inférieure à $\epsilon$ de $x_0$. _Notation :_ $x_j \to x_0$ ou $\lim_{j \to \infty} x_j = x_0$.

> [!important] Théorèmes fondamentaux sur les suites
> 
> 1. **Unicité de la limite** : Si une suite converge, sa limite est unique.
>     
> 2. **Critère de Cauchy** : Une suite converge (dans $\mathbb{C}$ ou $\mathbb{R}$) si et seulement si ses termes se rapprochent arbitrairement les uns des autres quand les indices deviennent grands ($|x_p - x_q| < \epsilon$).
>     
> 3. **Suites monotones** :
>     
>     - Une suite croissante et majorée converge.
>         
>     - Une suite décroissante et minorée converge.
>         

**Limites Supérieure et Inférieure (Détails)** : Ces notions permettent d'étudier le comportement asymptotique de suites qui ne convergent pas nécessairement (elles oscillent).

L'idée est de regarder ce qui se passe "à la fin" de la suite (la queue de la suite à partir de l'indice $j$) :

1. **La suite des "pires cas" (Max)** : On regarde le supremum (le plus grand élément) de la suite à partir de l'indice $j$. Comme on avance dans la suite ($j$ augmente), l'ensemble des valeurs restantes diminue, donc ce maximum ne peut que diminuer (ou rester stable).
    
2. **La suite des "meilleurs cas" (Min)** : On regarde l'infimum (le plus petit élément) à partir de l'indice $j$. Comme on avance, ce minimum ne peut que monter.
    

Pour toute suite bornée, on définit :

- **Limite Supérieure (**$\limsup$**)** : C'est la limite de ces maximums. Elle représente la "borne haute" vers laquelle la suite tend à osciller.
    
    $$\limsup_{j \to \infty} x_j = \lim_{j \to \infty} \left( \sup_{k \ge j} x_k \right)$$
- **Limite Inférieure (**$\liminf$**)** : C'est la limite de ces minimums. Elle représente la "borne basse".
    
    $$\liminf_{j \to \infty} x_j = \lim_{j \to \infty} \left( \inf_{k \ge j} x_k \right)$$

**Théorème** : La suite $(x_j)$ converge si et seulement si ses oscillations s'écrasent, c'est-à-dire si $\limsup x_j = \liminf x_j$.

### Séries

Une série $\sum_{j=1}^{+\infty} x_j$ est la limite de la suite des sommes partielles $S_J = \sum_{j=1}^J x_j$.

> [!warning] Condition nécessaire de convergence 
> Si la série $\sum x_j$ converge, alors le terme général tend vers 0 ($x_j \to 0$). 
> _**La réciproque est fausse (ex: série harmonique_ $\sum 1/j$ _diverge)._**

**Types de convergence** :

1. **Absolue** : $\sum |x_j|$ converge. (Implique la convergence simple).
    
2. **Semi-convergence** : $\sum x_j$ converge mais $\sum |x_j|$ diverge (ex: $\sum (-1)^j/j$).
    

> [!summary] Séries de référence
> 
> | Série | Condition de convergence | Somme (si conv.) |
> |---|---|---|
> | **Géométrique** $\sum_{j=0}^{\infty} z^j$ |  $\|z<1\|$ | $\frac{1}{1-z}$ |
> | **Riemann** $\displaystyle \sum_{j=1}^{\infty} \frac{1}{j^\alpha}$ | $\alpha > 1$ | $\zeta(\alpha)$ |

## 2.2 L'exponentielle

L'exponentielle est définie rigoureusement par une série entière.

> [!def] Définition 
> Pour tout $z \in \mathbb{C}$ :
> 
> $$\exp(z) = e^z = \sum_{j=0}^{+\infty} \frac{z^j}{j!}$$
> 
> Cette série converge absolument pour tout $z$.

**Propriétés clés** :

1. $e^0 = 1$
    
2. **Relation fondamentale** : $e^z e^{z'} = e^{z+z'}$
    
3. **Réel** : Sur $\mathbb{R}$, $x \mapsto e^x$ est strictement croissante, positive, $C^\infty$, et égale à sa dérivée ($De^x = e^x$).
    
4. **Croissance comparée** : L'exponentielle l'emporte sur les polynômes en $+\infty$.
    

## 2.3 Compléments de calcul intégral

Le calcul de probabilités (variables continues) repose sur l'intégration de fonctions de plusieurs variables.

### Intégrale double

L'intégrale d'une fonction continue $f$ sur un domaine $D$ représente le volume sous la surface.

> [!tip] Théorème de Fubini (Calcul pratique) 
> Pour intégrer sur un rectangle $[a,b] \times [c,d]$, on peut intégrer successivement par rapport à une variable puis l'autre. L'ordre n'importe pas pour les fonctions continues.
> 
> $$\iint_{[a,b]\times[c,d]} f(x,y) dx dy = \int_a^b \left( \int_c^d f(x,y) dy \right) dx$$

**Ensembles non rectangulaires** : Si le domaine $E$ est défini par $x \in I$ et $f_1(x) \le y \le f_2(x)$ (ensemble "parallèle à l'axe y"), alors :

$$\iint_E f(x,y) dx dy = \int_I \left( \int_{f_1(x)}^{f_2(x)} f(x,y) dy \right) dx$$

### Changement de variable (Détails)

Lorsque le domaine d'intégration est complexe, on effectue un changement de coordonnées (comme passer de cartésien à polaire) pour simplifier le calcul.

Soit une transformation bijective définie par deux fonctions $\psi_1$ et $\psi_2$ qui transforment les nouvelles coordonnées $(x', y')$ en anciennes coordonnées $(x, y)$ :

$$x = \psi_1(x', y') \quad \text{et} \quad y = \psi_2(x', y')$$

> [!important] Formule du changement de variable
> 
> $$\iint_E f(x,y) dx dy = \iint_{E'} f(\psi_1(x',y'), \psi_2(x',y')) \cdot |\det J| \cdot dx' dy'$$
> 
> **Qu'est-ce que le Jacobien (**$J$**) ?** C'est la matrice des dérivées partielles qui mesure comment la transformation déforme localement l'aire.
> 
> $$J = \begin{pmatrix} \frac{\partial \psi_1}{\partial x'} & \frac{\partial \psi_1}{\partial y'} \\ \frac{\partial \psi_2}{\partial x'} & \frac{\partial \psi_2}{\partial y'} \end{pmatrix}$$
> 
> On multiplie par la **valeur absolue de son déterminant** ($|\det J|$) pour compenser la déformation de l'espace (dilatation ou contraction de l'élément de surface $dx dy$).
> 
> **Exemple classique : Coordonnées Polaires**
> 
> - Transformation : $x = r \cos \theta$, $y = r \sin \theta$.
>     
> - Matrice Jacobienne :
>     
>     $$J = \begin{pmatrix} \cos \theta & -r \sin \theta \\ \sin \theta & r \cos \theta \end{pmatrix}$$
> - Déterminant : $\det J = r \cos^2 \theta - (-r \sin^2 \theta) = r(\cos^2 \theta + \sin^2 \theta) = r$.
>     
> - L'élément d'aire devient : $dx dy \to r dr d\theta$.
>