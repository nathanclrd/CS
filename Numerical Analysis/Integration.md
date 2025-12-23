| Topic |
| :--- |
| [[#1. Les Formules de Newton-Cotes]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#A. La Règle du Trapèze (Ordre 1)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#B. La Règle de Simpson (Ordre 3)]] |
| [[#2. La Méthode de Romberg]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 L'Algorithme]] |
| [[#3. La Quadrature de Gauss-Legendre]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 Le Principe]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#✨ La Magie de Gauss]] |
| [[#🏆 Synthèse Comparative]] |

# Chapitre : Intégration Numérique

> [!summary] Le problème en bref
>  On cherche à calculer l'intégrale définie (l'aire sous la courbe) d'une fonction $f$ entre $a$ et $b$ :
> 
> $$I = \int_a^b f(x) dx$$
> 
> **Le défi** :
> 
> 1. On ne connaît pas la primitive analytique de $f$ (ou elle est impossible à calculer, ex: $e^{-x^2}$).
>     
> 2. On veut une valeur numérique précise en utilisant un nombre limité d'évaluations de $f$.
>     

## 1. Les Formules de Newton-Cotes

_L'approche "On découpe et on relie les points"._

L'idée est de remplacer la fonction compliquée $f(x)$ par un **polynôme d'interpolation** (droite, parabole...) passant par des points équidistants, qu'on sait intégrer facilement.

### A. La Règle du Trapèze (Ordre 1)

On relie $f(a)$ et $f(b)$ par une droite. L'aire est celle d'un trapèze.

$$I \approx \frac{b-a}{2} [f(a) + f(b)]$$

- **Précision** : Exacte pour les droites (polynômes degré 1). Erreur en $h^2$.
    

### B. La Règle de Simpson (Ordre 3)

On utilise 3 points ($a$, le milieu $m$, et $b$) et on les relie par une parabole.

$$I \approx \frac{b-a}{6} [f(a) + 4f(m) + f(b)]$$

- **Précision** : Exacte pour les polynômes de degré 3 (surprise ! on gagne un degré gratuit par symétrie). Erreur en $h^4$.
    

> [!info] Méthodes Composites
>  En pratique, on ne fait pas ça sur tout l'intervalle $[a,b]$ d'un coup. On découpe l'intervalle en $n$ petits morceaux et on applique la règle (Trapèze ou Simpson) sur chaque morceau.

## 2. La Méthode de Romberg

_L'approche "Recyclage intelligent"._

### 💡 L'idée intuitive

C'est exactement le même principe que **l'Extrapolation de Richardson** pour les dérivées, mais appliqué aux intégrales. On sait que l'erreur de la méthode du Trapèze composite décroît proprement en $h^2, h^4, h^6 \dots$

### 📝 L'Algorithme

On construit un tableau triangulaire $R_{i,j}$ :

1. **Colonne 1** : On calcule l'intégrale avec la méthode du **Trapèze** pour $1, 2, 4, 8 \dots$ sous-intervalles.
    
2. **Colonnes suivantes** : On combine les résultats pour éliminer mathématiquement les termes d'erreur.
    
    - La colonne 2 correspond en fait à la méthode de **Simpson**.
        
    - La colonne 3 correspond à la méthode de **Boole** (degré 5).
        

> [!check] Résultat 
> On obtient une précision extrême très rapidement en combinant des estimations "médiocres" (Trapèzes).

## 3. La Quadrature de Gauss-Legendre

_L'approche "Le choix optimal"._

### 💡 L'idée intuitive

Dans Newton-Cotes, on force les points d'évaluation à être **équidistants** (ex: 0, 0.5, 1). Ce n'est pas optimal ! Gauss s'est posé la question : _"Si j'ai le droit de choisir n'importe quels points_ $x_i$ _dans l'intervalle, où dois-je les placer pour minimiser l'erreur ?"_

### 📝 Le Principe

L'intégrale est approximée par une somme pondérée :

$$I \approx \sum_{i=1}^n w_i f(x_i)$$

- **Les points** $x_i$ : Ce sont les racines des **Polynômes de Legendre**.
    
- **Les poids** $w_i$ : Ils sont calculés spécifiquement pour chaque point.
    

### ✨ La Magie de Gauss

Avec $n$ points, on peut intégrer exactement n'importe quel polynôme de degré $2n-1$.

- _Newton-Cotes (Simpson)_ avec 3 points intègre exactement jusqu'au degré 3.
    
- _Gauss_ avec 3 points intègre exactement jusqu'au degré 5.
    

> [!example] Exemple (sur [-1, 1] avec 2 points) 
> Au lieu de prendre -1 et 1, Gauss dit de prendre $\pm \frac{1}{\sqrt{3}} \approx \pm 0.577$.
> 
> $$I \approx 1 \cdot f\left(-\frac{1}{\sqrt{3}}\right) + 1 \cdot f\left(\frac{1}{\sqrt{3}}\right)$$
> 
> Cette simple formule donne le résultat **exact** pour n'importe quelle cubique !

## 🏆 Synthèse Comparative

|Méthode|Points d'évaluation|Précision (Ordre)|Quand l'utiliser ?|
|---|---|---|---|
|**Trapèze**|Équidistants|Faible ($h^2$)|Pour une estimation rapide ou données tabulées.|
|**Simpson**|Équidistants|Moyenne ($h^4$)|Le standard "bon à tout faire".|
|**Romberg**|Équidistants (raffinés)|Très Haute (Variable)|Quand on veut une haute précision et qu'on peut recalculer $f$ à volonté.|
|**Gauss-Legendre**|**Racines de Legendre** (Optimaux)|**Maximale** ($2n-1$)|Quand calculer $f(x)$ coûte très cher (on veut le moins d'appels possible).|