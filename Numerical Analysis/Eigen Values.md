| Topic |
| :--- |
| [[#1. La Méthode de la Bissection (Dichotomie)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ L'Algorithme]] |
| [[#2. La Méthode de Newton-Raphson]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 La Formule à retenir]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ L'Algorithme]] |
| [[#3. La Méthode de la Sécante]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 La Formule]] |
| [[#4. La Méthode du Point Fixe]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 La Formule]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚠️ Condition de vie ou de mort (Convergence)]] |
| [[#🏆 Tableau Récapitulatif : Que choisir ?]] |

# Chapitre 4 : Résolution d'Équations Non Linéaires (Synthèse Clarifiée)

> [!summary] Le problème en bref 
> On cherche un nombre $x$ (appelé **racine**) qui annule une fonction :
> 
> $$f(x) = 0$$
> 
> Comme on ne peut pas toujours isoler $x$ à la main (ex: $x = \cos(x)$), on utilise des méthodes numériques qui s'approchent de la solution étape par étape.

## 1. La Méthode de la Bissection (Dichotomie)

_L'approche "brute mais fiable"._

### 💡 L'idée intuitive

Imaginez que vous cherchez un mot dans un dictionnaire. Vous ouvrez au milieu. Si le mot est avant, vous oubliez la seconde moitié et vous recommencez avec la première. On "coupe en deux" l'intervalle indéfiniment.

### ⚙️ L'Algorithme

1. **Départ** : Choisir deux points $a$ et $b$ qui encadrent la racine (la fonction doit changer de signe : $f(a)$ et $f(b)$ sont de signes opposés).
    
2. **Milieu** : Calculer le centre $m = \frac{a+b}{2}$.
    
3. **Test** :
    
    - Si $f(a)$ et $f(m)$ ont le même signe $\rightarrow$ la racine est dans l'autre moitié $[m, b]$. On remplace $a$ par $m$.
        
    - Sinon $\rightarrow$ la racine est dans $[a, m]$. On remplace $b$ par $m$.
        
4. **Répéter** jusqu'à ce que l'intervalle soit minuscule.
    

> [!check] Points forts
> 
> - **Indestructible** : Elle converge **toujours** si on a bien encadré la racine au début.
>     
> - **Simple** : Très facile à comprendre.
>     

> [!fail] Points faibles
> 
> - **Très lente** : Il faut beaucoup d'étapes pour gagner de la précision.
>     
> - **Aveugle** : Elle n'utilise pas la forme de la courbe, juste le signe.
>     

## 2. La Méthode de Newton-Raphson

_L'approche "formule 1" (rapide mais sensible)._

### 💡 L'idée intuitive

Au lieu de tâtonner, on se place sur la courbe au point $x_n$ et on trace la **tangente**. Là où la tangente coupe l'axe horizontal, c'est notre nouveau point $x_{n+1}$. On "glisse" le long des tangentes vers la solution.

### 📝 La Formule à retenir

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### ⚙️ L'Algorithme

1. **Départ** : Choisir un point initial $x_0$ (proche de la racine si possible).
    
2. **Calcul** : Appliquer la formule pour trouver le point suivant.
    
3. **Répéter** jusqu'à ce que $x$ ne bouge presque plus.
    

> [!check] Points forts
> 
> - **Extrêmement rapide** (Quadratique) : Une fois proche du but, le nombre de décimales correctes double à chaque étape !
>     

> [!fail] Points faibles
> 
> - **Nécessite la dérivée** $f'(x)$.
>     
> - **Fragile** : Si on part trop loin de la solution, ou si la dérivée est nulle ($f'(x) \approx 0$), la méthode peut partir dans le décor (diverger).
>     

## 3. La Méthode de la Sécante

_Le compromis "Newton sans dérivée"._

### 💡 L'idée intuitive

C'est comme Newton, mais on ne calcule pas la tangente (car on ne veut pas calculer la dérivée). On remplace la tangente par une droite (la **sécante**) qui relie les deux derniers points connus.

### 📝 La Formule

C'est la même que Newton, mais on remplace $f'(x_n)$ par une approximation :

$$x_{i+1} = x_i - f(x_i) \frac{x_i - x_{i-1}}{f(x_i) - f(x_{i-1})}$$

> [!check] Points forts
> 
> - **Pas besoin de dérivée** calculée analytiquement.
>     
> - **Rapide** (Superlinéaire) : Plus rapide que la Bissection, un tout petit peu moins que Newton.
>     

> [!fail] Points faibles
> 
> - Nécessite **2 points** au départ.
>     
> - Moins stable que la Bissection.
>     

## 4. La Méthode du Point Fixe

_L'approche "transformation"._

### 💡 L'idée intuitive

On transforme l'équation $f(x)=0$ sous la forme $x = g(x)$. On injecte une valeur dans $g$, on récupère le résultat, et on le réinjecte dans $g$, encore et encore.

### 📝 La Formule

$$x_{k+1} = g(x_k)$$

### ⚠️ Condition de vie ou de mort (Convergence)

Pour que ça marche, la pente de $g(x)$ ne doit pas être trop raide autour de la solution.

> [!important] Règle d'or
>  La méthode converge si $|g'(x)| < 1$.
> 
> - Si la dérivée est petite (courbe plate), ça converge vite.
>     
> - Si la dérivée est grande (pente raide), ça diverge (on s'éloigne).
>     

## 🏆 Tableau Récapitulatif : Que choisir ?

| Méthode        | Vitesse        | J'ai besoin de...                   | Quand l'utiliser ?                                                            |
| -------------- | -------------- | ----------------------------------- | ----------------------------------------------------------------------------- |
| **Bissection** | 🐢 Lente       | 2 points qui encadrent la racine.   | Quand on veut être **sûr à 100%** de trouver la solution, même si c'est long. |
| **Point Fixe** | 🚶 Variable    | Une fonction $g(x)$ dont $          | g'                                                                            |
| **Sécante**    | 🏃 Rapide      | 2 points de départ.                 | Quand on veut aller vite mais qu'on ne peut pas calculer la dérivée.          |
| **Newton**     | 🚀 Très Rapide | 1 point + la formule de la dérivée. | Quand on veut de la **haute précision** et qu'on connaît la dérivée.          |
|                |                |                                     |                                                                               |

> [!tip] Stratégie Hybride (Le meilleur des deux mondes) 
> En pratique, les logiciels utilisent souvent une **Bissection** au début pour s'approcher de la zone sûre, puis basculent sur **Newton** pour finir très rapidement le travail avec une grande précision.