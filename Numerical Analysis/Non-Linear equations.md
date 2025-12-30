| Topic                                            |
| ------------------------------------------------ |
| [[#1. La Méthode de la Bissection (Dichotomie)]] |
| [[#💡 L'idée intuitive]]                         |
| [[#⚠️ Conditions de Convergence]]                |
| [[#⚙️ L'Algorithme]]                             |
| [[#2. La Méthode de Newton-Raphson]]             |
| [[#💡 L'idée intuitive]]                         |
| [[#📝 La Formule à retenir]]                     |
| [[#⚠️ Conditions de Convergence]]                |
| [[#3. La Méthode de la Sécante]]                 |
| [[#💡 L'idée intuitive]]                         |
| [[#⚠️ Conditions de Convergence]]                |
| [[#4. La Méthode du Point Fixe]]                 |
| [[#💡 L'idée intuitive]]                         |
| [[#⚠️ Conditions de Convergence (Le Théorème)]]  |
| [[#🏆 Tableau Récapitulatif : Que choisir ?]]    |

# Chapitre 4 : Résolution d'Équations Non Linéaires (Synthèse Complète)

> [!summary] Le problème en bref On cherche un nombre $x$ (appelé **racine**) qui annule une fonction :
> 
> $$f(x) = 0$$
> 
> Comme on ne peut pas toujours isoler $x$ à la main (ex: $x = \cos(x)$), on utilise des méthodes numériques.

## 1. La Méthode de la Bissection (Dichotomie)

_L'approche "brute mais fiable"._

### 💡 L'idée intuitive

Imaginez que vous cherchez un mot dans un dictionnaire. Vous ouvrez au milieu. Si le mot est avant, vous oubliez la seconde moitié et vous recommencez. On "coupe en deux" l'intervalle indéfiniment.

### ⚠️ Conditions de Convergence

Pour que la méthode fonctionne, il faut impérativement respecter le **Théorème des Valeurs Intermédiaires** :

1. La fonction $f$ doit être **continue** sur l'intervalle $[a, b]$.
    
2. Il doit y avoir un **changement de signe** aux bornes :
    
    $$f(a) \cdot f(b) < 0$$

### ⚙️ L'Algorithme

1. **Départ** : Choisir $a$ et $b$ tels que $f(a)$ et $f(b)$ soient de signes opposés.
    
2. **Milieu** : Calculer $m = \frac{a+b}{2}$.
    
3. **Test** :
    
    - Si $f(a) \cdot f(m) > 0$ (même signe) $\rightarrow$ la racine est dans $[m, b]$. On remplace $a$ par $m$.
        
    - Sinon $\rightarrow$ la racine est dans $[a, m]$. On remplace $b$ par $m$.
        

> [!check] Points forts
> 
> - **Convergence Globale** : Elle converge **toujours** si la condition $f(a)f(b)<0$ est respectée.
>     

> [!fail] Points faibles
> 
> - **Convergence Linéaire** : C'est lent. L'erreur est divisée par 2 à chaque étape.
>     

## 2. La Méthode de Newton-Raphson

_L'approche "formule 1" (rapide mais sensible)._

### 💡 L'idée intuitive

On se place sur la courbe au point $x_n$ et on trace la **tangente**. Là où la tangente coupe l'axe $x$, c'est notre nouveau point.

### 📝 La Formule à retenir

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

### ⚠️ Conditions de Convergence

C'est la méthode la plus capricieuse. Pour converger, il faut :

1. $x_0$ **proche de la solution** : Si on part trop loin, la tangente peut nous envoyer n'importe où. (Convergence Locale).
    
2. **Dérivée non nulle** : Il ne faut jamais que $f'(x_n) \approx 0$ (tangente horizontale), sinon division par zéro !
    
3. **Fonction lisse** : $f$ doit être deux fois dérivable ($\mathcal{C}^2$) et convexe/concave autour de la racine pour garantir la stabilité.
    

> [!check] Points forts
> 
> - **Convergence Quadratique** : Le nombre de décimales correctes **double** à chaque itération (si on est proche du but).
>     

## 3. La Méthode de la Sécante

_Le compromis "Newton sans dérivée"._

### 💡 L'idée intuitive

C'est comme Newton, mais on remplace la tangente par une droite (la **sécante**) qui relie les deux derniers points connus, pour éviter de calculer la dérivée.

### 📝 La Formule

$$x_{i+1} = x_i - f(x_i) \frac{x_i - x_{i-1}}{f(x_i) - f(x_{i-1})}$$

### ⚠️ Conditions de Convergence

1. **Deux points initiaux** : Il faut $x_0$ et $x_1$ proches de la racine.
    
2. **Pas de division par zéro** : Il faut que $f(x_i) \neq f(x_{i-1})$. Si la courbe est plate entre les deux points, ça plante.
    

> [!info] Note sur la vitesse **Convergence Superlinéaire** (ordre $\approx 1.618$) : Plus rapide que la Bissection, un tout petit peu moins que Newton.

## 4. La Méthode du Point Fixe

_L'approche "transformation"._

### 💡 L'idée intuitive

On transforme l'équation $f(x)=0$ sous la forme $x = g(x)$. On réinjecte le résultat dans la fonction en boucle.

### 📝 La Formule

$$x_{k+1} = g(x_k)$$

### ⚠️ Conditions de Convergence (Le Théorème)

C'est la condition la plus stricte. Pour garantir la convergence, la fonction $g$ doit être **contractante** autour de la solution $s$.

$$|g'(x)| < 1 \quad \text{pour tout } x \text{ dans l'intervalle étudié}$$

- Si $|g'(s)| < 1$ : La méthode converge (attraction).
    
- Si $|g'(s)| > 1$ : La méthode diverge (répulsion).
    
- Plus $|g'(s)|$ est proche de 0, plus ça va vite.
    

## 🏆 Tableau Récapitulatif : Que choisir ?

|Méthode|Vitesse (Ordre)|Critère Vital (Convergence)|Quand l'utiliser ?|
|---|---|---|---|
|**Bissection**|🐢 **Linéaire** (Ordre 1)|$f(a)$ et $f(b)$ signes opposés.|Quand on veut être **sûr à 100%** de trouver la solution (fiabilité).|
|**Point Fixe**|🚶 **Linéaire** (Variable)|$|g'(x)|
|**Sécante**|🏃 **Superlinéaire** ($\approx 1.6$)|$x_0, x_1$ proches de la racine.|Quand on veut la vitesse de Newton mais que la dérivée est trop dure à calculer.|
|**Newton**|🚀 **Quadratique** (Ordre 2)|$x_0$ très proche + $f'(x) \neq 0$.|Quand on veut de la **haute précision** et qu'on connaît la dérivée.|

> [!tip] Stratégie Hybride (Le meilleur des deux mondes) Commencez par une **Bissection** pour trouver un petit intervalle sûr, puis lancez **Newton** pour finir le travail en quelques millisecondes.