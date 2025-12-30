| Topic                                                                   |
| :---------------------------------------------------------------------- |
| [[#1. La Méthode Naïve (Différence Avant)]]                             |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]]                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚠️ Analyse de l'Erreur (Le "V" de la mort)]] |
| [[#2. Les Différences Centrales]]                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]]                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 La Formule]]                              |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#✨ Pourquoi c'est mieux ?]]                   |
| [[#3. Dérivées d'Ordre Supérieur]]                                      |
| [[#4. Extrapolation de Richardson]]                                     |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]]                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 L'Algorithme]]                            |
| [[#🏆 Synthèse Comparative]]                                            |

# Chapitre : Différenciation Numérique

> [!summary] Le problème en bref
>  On cherche à calculer la dérivée $f'(x)$ d'une fonction en un point donné, mais :
> 
> 1. On n'a pas la formule analytique de $f$ (c'est une "boîte noire", un résultat de simulation, ou des mesures).
>     
> 2. L'ordinateur ne peut pas faire tendre $h$ vers 0 (limite mathématique).
>     
> 
> **Le dilemme** : Si $h$ est grand, l'approximation mathématique est mauvaise (**erreur de troncature**). Si $h$ est trop petit, l'ordinateur fait des erreurs de calcul énormes (**erreur d'arrondi**).

## 1. La Méthode Naïve (Différence Avant)

_L'approche "définition mathématique"._

### 💡 L'idée intuitive

On applique bêtement la définition de la dérivée avec un $h$ fixe.

$$f'(x) \approx \frac{f(x+h) - f(x)}{h}$$

### ⚠️ Analyse de l'Erreur (Le "V" de la mort)

L'erreur totale est la somme de deux ennemis :

1. **Erreur de Troncature** (Maths) : Proportionnelle à $h$ (Ordre 1). Plus $h$ est petit, mieux c'est.
    
2. **Erreur d'Arrondi** (Machine) : Proportionnelle à $1/h$. Plus $h$ est petit, plus on divise par un petit nombre, et plus le "bruit" numérique explose.
    

> [!fail] Conséquence
>  On ne peut jamais atteindre la précision machine (16 chiffres). On plafonne souvent à 8 chiffres corrects, même avec le $h$ optimal (qui est souvent autour de $\sqrt{\epsilon_{machine}} \approx 10^{-8}$).

## 2. Les Différences Centrales

_L'approche "symétrique"._

### 💡 L'idée intuitive

Au lieu de regarder juste devant ($x$ et $x+h$), on regarde de part et d'autre ($x-h$ et $x+h$). La pente de la corde symétrique est une bien meilleure approximation de la tangente.

### 📝 La Formule

$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$$

### ✨ Pourquoi c'est mieux ?

- **Ordre 2** : L'erreur mathématique diminue en $h^2$. (Si on divise $h$ par 10, l'erreur est divisée par 100 !).
    
- **Annulation d'erreurs** : Les termes d'erreur d'ordre pair s'annulent grâce à la symétrie.
    

## 3. Dérivées d'Ordre Supérieur

On peut généraliser pour calculer la dérivée seconde $f''(x)$. En combinant les développements de Taylor de $f(x+h)$ et $f(x-h)$, on obtient la formule classique :

$$f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2}$$

> [!warning] Attention 
> Diviser par $h^2$ rend cette formule encore plus sensible aux erreurs d'arrondi que la dérivée première.

## 4. Extrapolation de Richardson

_L'approche "Magique" pour booster la précision._

### 💡 L'idée intuitive

Si on connaît la forme de l'erreur (par exemple $E \approx C h^2$), on peut calculer la dérivée avec un pas $h$, puis avec un pas $h/2$, et combiner les deux résultats pour **éliminer mathématiquement** le terme d'erreur principal.

### 📝 L'Algorithme

On construit un tableau triangulaire :

1. **Colonne 1** : Calculs avec la méthode des différences centrales pour $h, h/2, h/4 \dots$
    
2. **Colonne 2** : On combine les valeurs de la colonne 1 pour tuer l'erreur en $h^2$.
    
    $$G_{i,1} = \frac{4G_{i,0} - G_{i-1,0}}{3}$$
3. **Colonnes suivantes** : On continue pour tuer l'erreur en $h^4, h^6 \dots$
    

> [!check] Résultat
>  On peut obtenir une dérivée avec **10 à 14 chiffres significatifs** corrects, ce qui est impossible avec les méthodes simples. C'est la technique utilisée par les solveurs professionnels.

## 🏆 Synthèse Comparative

|Méthode|Formule|Ordre (Vitesse)|Précision max|
|---|---|---|---|
|**Naïve** (Avant)|$\frac{f(x+h)-f(x)}{h}$|$O(h)$ (Lent)|~7-8 chiffres|
|**Centrale**|$\frac{f(x+h)-f(x-h)}{2h}$|$O(h^2)$ (Moyen)|~10-11 chiffres|
|**Richardson**|Combinaison linéaire|$O(h^4), O(h^6)...$|~14-15 chiffres|