| Topic |
| :--- |
| [[#1. La Méthode du Point Fixe]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 Principe]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 Formulations possibles (Exemple)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚠️ Condition de Convergence (Rigoureuse)]] |
| [[#2. La Méthode de Newton (Newton-Raphson)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 Principe]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#🔑 La Matrice Jacobienne $J_F$]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ L'Algorithme Complet]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚖️ Analyse Critique]] |
| [[#3. La Méthode Quasi-Newton (Méthode de Broyden)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 Principe]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 Formule de Mise à Jour de Broyden]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ L'Algorithme]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚖️ Analyse Critique]] |
| [[#🏆 Synthèse Comparée]] |

# Chapitre : Systèmes d'Équations Non Linéaires

> [!summary] Le problème en bref 
> On cherche un vecteur $\vec{x} = (x_1, x_2, \dots, x_n)$ qui satisfait un système d'équations :
> 
> $$F(\vec{x}) = \vec{0}$$
> 
> **Exemple Fil Rouge du cours :** Intersection d'un cercle et d'une hyperbole :
> 
> $$\begin{cases} x^2 + y^2 - 4 = 0 \\ xy - 1 = 0 \end{cases} \implies F(\vec{x}) = \begin{pmatrix} x^2+y^2-4 \\ xy-1 \end{pmatrix}$$

## 1. La Méthode du Point Fixe

### 💡 Principe

On transforme $F(\vec{x}) = \vec{0}$ en $\vec{x} = G(\vec{x})$. On itère : $\vec{x}_{k+1} = G(\vec{x}_k)$.

### 📝 Formulations possibles (Exemple)

Pour notre système, on peut isoler les variables de plusieurs façons :

- **Formulation 1 (Simple)** : $x = \sqrt{4-y^2}$ et $y = 1/x$.
    
- **Formulation 2 (Plus stable)** : $x = \sqrt{4-y^2}$ et $y = y + \frac{1}{2}(xy-1)$ (exemple de relaxation).
    

### ⚠️ Condition de Convergence (Rigoureuse)

La convergence dépend de la **Matrice Jacobienne** de $G$, notée $J_G(\vec{x})$.

$$J_G(\vec{x}) = \begin{pmatrix} \frac{\partial G_1}{\partial x} & \frac{\partial G_1}{\partial y} \\ \frac{\partial G_2}{\partial x} & \frac{\partial G_2}{\partial y} \end{pmatrix}$$

**Critère de convergence :** La méthode converge localement si le **rayon spectral** (la plus grande valeur propre en module) de la Jacobienne au point fixe $\bar{x}$ est strictement inférieur à 1 :

$$\rho(J_G(\bar{x})) < 1$$

_En pratique, une condition suffisante est que la norme matricielle_ $\|J_G\| < 1$_._

## 2. La Méthode de Newton (Newton-Raphson)

### 💡 Principe

On linéarise la fonction $F$ autour de $\vec{x}_k$ en utilisant la série de Taylor au premier ordre :

$$F(\vec{x}) \approx F(\vec{x}_k) + J_F(\vec{x}_k)(\vec{x} - \vec{x}_k)$$

On cherche $\vec{x}$ tel que cette approximation s'annule.

### 🔑 La Matrice Jacobienne $J_F$

C'est la matrice des dérivées partielles de $F$. Pour notre exemple :

$$F(x,y) = \begin{pmatrix} x^2+y^2-4 \\ xy-1 \end{pmatrix} \implies J_F(x,y) = \begin{pmatrix} 2x & 2y \\ y & x \end{pmatrix}$$

### ⚙️ L'Algorithme Complet

À chaque itération $k$ :

1. **Calculer** le résidu $-F(\vec{x}_k)$ et la Jacobienne $J_F(\vec{x}_k)$.
    
2. **Résoudre** le système linéaire pour trouver le déplacement $\vec{d}_k$ (ne pas inverser la matrice !) :
    
    $$J_F(\vec{x}_k) \cdot \vec{d}_k = -F(\vec{x}_k)$$
3. **Mise à jour** :
    
    $$\vec{x}_{k+1} = \vec{x}_k + \vec{d}_k$$

### ⚖️ Analyse Critique

- **Avantage** : Convergence **quadratique** (le nombre de décimales exactes double à chaque étape).
    
- **Coût** : Résoudre un système linéaire à chaque étape coûte cher ($O(n^3)$ opérations).
    
- **Robustesse** : Diverge si la Jacobienne est singulière (déterminant nul) ou si le point de départ est trop loin.
    

## 3. La Méthode Quasi-Newton (Méthode de Broyden)

### 💡 Principe

Pour éviter de calculer et recalculer la Jacobienne $J_F$ (coûteux ou impossible analytiquement), on utilise une matrice approximation $A_k$ que l'on met à jour à chaque itération. On impose que $A_k$ satisfasse l'**équation de la sécante multidimensionnelle** :

$$A_k(\vec{x}_k - \vec{x}_{k-1}) = F(\vec{x}_k) - F(\vec{x}_{k-1})$$

### 📝 Formule de Mise à Jour de Broyden

On cherche à minimiser le changement dans la matrice ($min \|A_k - A_{k-1}\|$) tout en respectant l'équation de la sécante. Cela donne la formule de mise à jour de rang 1 :

$$A_k = A_{k-1} + \frac{(\vec{y}_{k-1} - A_{k-1}\vec{d}_{k-1}) \cdot \vec{d}_{k-1}^T}{\vec{d}_{k-1}^T \cdot \vec{d}_{k-1}}$$

**Définitions :**

- $\vec{d}_{k-1} = \vec{x}_k - \vec{x}_{k-1}$ (le déplacement effectué)
    
- $\vec{y}_{k-1} = F(\vec{x}_k) - F(\vec{x}_{k-1})$ (le changement de la fonction)
    

### ⚙️ L'Algorithme

1. **Initialisation** : Choisir $\vec{x}_0$ et une matrice $A_0$ (souvent l'Identité $I$ ou $J_F(\vec{x}_0)$).
    
2. **Itération** :
    
    - Résoudre $A_k \vec{d}_k = -F(\vec{x}_k)$.
        
    - $\vec{x}_{k+1} = \vec{x}_k + \vec{d}_k$.
        
    - Calculer $\vec{y}_k = F(\vec{x}_{k+1}) - F(\vec{x}_k)$.
        
    - Mettre à jour $A_{k+1}$ avec la formule de Broyden.
        

### ⚖️ Analyse Critique

- **Avantage** : Plus besoin de calculer les dérivées partielles. Une seule évaluation de $F$ par étape.
    
- **Convergence** : **Superlinéaire** (très rapide, mais théoriquement moins que Newton).
    
- **Coût** : $O(n^2)$ si on utilise la formule de Sherman-Morrison pour mettre à jour directement l'inverse de la matrice.
    

## 🏆 Synthèse Comparée

| Caractéristique        | Newton                                | Quasi-Newton (Broyden)          | Point Fixe                             |
| ---------------------- | ------------------------------------- | ------------------------------- | -------------------------------------- |
| **Vitesse**            | Quadratique (+++)                     | Superlinéaire (++)              | Linéaire (+)                           |
| **Dérivées**           | Requises (Jacobienne exacte)          | Non requises (Approximation)    | Non requises                           |
| **Coût par itération** | Élevé (Système linéaire + Jacobienne) | Moyen (Mise à jour matricielle) | Faible                                 |
| **Stabilité**          | Sensible au point de départ           | Moyenne                         | Dépend fortement de la formulation $G$ |