| Topic |
| :--- |
| [[#1. La Méthode de la Puissance]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 L'Algorithme]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚠️ Convergence]] |
| [[#2. La Méthode de la Puissance Inverse]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ En pratique (Astuce importante)]] |
| [[#3. Le "Shift" (Décalage Spectral)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| [[#4. Calculer les _autres_ valeurs propres (Déflation)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Pour les matrices symétriques]] |
| [[#5. L'Algorithme QR]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 L'Algorithme]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#✨ Le Résultat Magique]] |

# Chapitre : Calcul Numérique des Valeurs Propres

> [!summary] Le problème en bref 
> On cherche à trouver les scalaires $\lambda$ (valeurs propres) et les vecteurs non nuls $v$ (vecteurs propres) tels que :
> 
> $$Av = \lambda v$$
> 
> **Pourquoi est-ce difficile ?** Contrairement aux systèmes linéaires ($Ax=b$), on ne peut pas isoler l'inconnue facilement. L'approche théorique (calculer le déterminant $\det(A-\lambda I) = 0$ pour trouver le polynôme caractéristique) est **instable et trop coûteuse** pour les grandes matrices ($N > 4$). On utilise donc des méthodes itératives.

## 1. La Méthode de la Puissance

_L'approche "bourrin mais efficace" pour le plus grand élément._

### 💡 L'idée intuitive

Si on multiplie un vecteur arbitraire $w$ par la matrice $A$ encore et encore ($A \cdot A \cdot A \dots w$), le vecteur résultant va finir par s'aligner avec la direction qui "dilate" le plus l'espace : celle correspondant à la valeur propre la plus grande en valeur absolue ($|\lambda_{max}|$).

### 📝 L'Algorithme

1. **Départ** : Choisir un vecteur initial $w^{(0)}$ (au hasard).
    
2. **Itération** :
    
    - Multiplier : $w^{(k)} = A w^{(k-1)}$
        
    - _Normaliser_ (crucial pour éviter que les nombres explosent) : $z^{(k)} = \frac{w^{(k)}}{\|w^{(k)}\|}$
        
3. **Résultat** : La suite converge vers le vecteur propre dominant $v^{(1)}$.
    

### ⚠️ Convergence

La vitesse dépend du ratio $|\lambda_2| / |\lambda_1|$.

- Si $\lambda_1$ est beaucoup plus grand que les autres, ça converge très vite.
    
- Si $\lambda_1 \approx \lambda_2$, la méthode rame.
    

## 2. La Méthode de la Puissance Inverse

_L'approche pour trouver le plus petit élément._

### 💡 L'idée intuitive

Les valeurs propres de l'inverse $A^{-1}$ sont les inverses des valeurs propres de $A$ ($1/\lambda$). La plus _petite_ valeur propre de $A$ devient la plus _grande_ de $A^{-1}$. On applique donc la méthode de la puissance sur $A^{-1}$.

### ⚙️ En pratique (Astuce importante)

On ne calcule **jamais** $A^{-1}$ explicitement (trop cher). Au lieu de calculer $w^{(k+1)} = A^{-1} z^{(k)}$, on résout le système linéaire :

$$A w^{(k+1)} = z^{(k)}$$

(On utilise une décomposition LU de $A$ pour faire cela rapidement à chaque itération).

## 3. Le "Shift" (Décalage Spectral)

_L'approche "ciblage laser"._

### 💡 L'idée intuitive

Si on veut trouver une valeur propre proche d'un nombre $m$ arbitraire, on peut "shifter" la matrice. Les valeurs propres de $A - mI$ sont $\lambda_i - m$. Si on applique la **Puissance Inverse** à $(A - mI)$, on va converger vers la valeur propre pour laquelle $1/(\lambda_i - m)$ est le plus grand, c'est-à-dire celle où $(\lambda_i - m)$ est le plus petit (la plus proche de $m$).

> [!tip] Utilisation 
> Très utile pour accélérer la convergence si on a déjà une estimation grossière de la valeur propre.

## 4. Calculer les _autres_ valeurs propres (Déflation)

Une fois qu'on a trouvé $\lambda_1$, comment trouver $\lambda_2$ ?

### Pour les matrices symétriques

On "retire" l'influence de $\lambda_1$ de la matrice.

$$A_{nouveau} = A - \lambda_1 v^{(1)} (v^{(1)})^T$$

Cette nouvelle matrice a les mêmes valeurs propres que $A$, sauf $\lambda_1$ qui est remplacée par $0$. La méthode de la puissance convergera alors vers $\lambda_2$.

## 5. L'Algorithme QR

_L'approche "tout-en-un" (Le Saint Graal)._

### 💡 L'idée intuitive

C'est la méthode standard pour trouver **toutes** les valeurs propres d'un coup. Elle est basée sur la factorisation $A = QR$ (Q orthogonale, R triangulaire supérieure).

### 📝 L'Algorithme

On génère une suite de matrices $A_0, A_1, A_2 \dots$

1. **Factoriser** : $A_k = Q_k R_k$
    
2. **Recombiner à l'envers** : $A_{k+1} = R_k Q_k$
    

### ✨ Le Résultat Magique

La matrice $A_k$ converge vers une matrice **triangulaire supérieure** (Forme de Schur). Les **valeurs propres** se lisent alors simplement sur la **diagonale** de cette matrice limite.

> [!check] Points forts
> 
> - Très robuste.
>     
> - Donne tout le spectre (toutes les valeurs propres).
>     
> - Préserve la symétrie (si $A$ est symétrique, la limite est diagonale).
>     

> [!fail] Points faibles
> 
> - Coûteux pour les très grandes matrices (complexité $O(N^3)$).
>