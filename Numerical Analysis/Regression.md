| Topic |
| :--- |
| [[#1. La Régression Linéaire]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#📝 Le Critère des Moindres Carrés]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ La Résolution (Équations Normales)]] |
| [[#2. La Régression Non-Linéaire (Générale)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚙️ L'Algorithme]] |
| [[#3. Régression Polynomiale et Choix de la Base]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#⚠️ Le problème de la base standard]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 La solution : Polynômes Orthogonaux]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#🔎 Quel degré choisir ?]] |
| [[#4. Prétraitement des Données (Linéarisation)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#💡 L'idée intuitive]] |
| [[#🏆 Tableau Récapitulatif]] |

# Chapitre 2 : Régression et Approximation (Synthèse Clarifiée)

> [!summary] Le problème en bref 
> On dispose d'un nuage de points (données expérimentales) et on cherche la fonction qui représente le mieux le phénomène sous-jacent.
> 
> Contrairement à l'**interpolation** qui oblige la courbe à passer _exactement_ par tous les points (au risque de faire des zigzags inutiles, le "sur-apprentissage"), la **régression** cherche une courbe simple qui passe _au plus près_ des points, en acceptant une certaine erreur pour lisser le bruit.

## 1. La Régression Linéaire

_L'approche "la droite la plus proche"._

### 💡 L'idée intuitive

Vos points semblent alignés mais forment un "nuage" un peu dispersé à cause des erreurs de mesure. On cherche la droite $y = ax + b$ qui minimise la distance globale entre la droite et tous les points.

### 📝 Le Critère des Moindres Carrés

Pour définir "la plus proche", on minimise la somme des carrés des erreurs verticales. On cherche $a$ et $b$ qui minimisent la fonction $E$ :

$$E(a, b) = \sum_{i=1}^n (ax_i + b - u_i)^2$$

_Pourquoi le carré ?_ Pour pénaliser fortement les gros écarts et éviter que les erreurs positives et négatives ne s'annulent.

### ⚙️ La Résolution (Équations Normales)

Le minimum se trouve là où la dérivée est nulle. On annule les dérivées partielles par rapport à $a$ et $b$. Cela nous donne un système linéaire simple à résoudre :

$$\begin{pmatrix} \sum x_i^2 & \sum x_i \\ \sum x_i & n \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} \sum x_i u_i \\ \sum u_i \end{pmatrix}$$

> [!check] Points forts
> 
> - **Lissage** : Élimine efficacement le bruit expérimental.
>     
> - **Simple** : Calcul très rapide (système $2 \times 2$).
>     

> [!fail] Points faibles
> 
> - **Rigide** : Ne fonctionne que si le phénomène est réellement linéaire.
>     
> - **Sensible** : Un seul point aberrant (_outlier_) très loin des autres peut "tirer" la droite vers lui et fausser le résultat (à cause du carré de l'erreur).
>     

## 2. La Régression Non-Linéaire (Générale)

_L'approche "sur mesure"._

### 💡 L'idée intuitive

Si les points suivent une courbe (parabole, exponentielle...), une droite ne suffit pas. On choisit une famille de fonctions de base (ex: $1, \ln(x), x^2, \cos(x)$) et on cherche la meilleure combinaison linéaire de ces fonctions.

### ⚙️ L'Algorithme

On cherche la fonction $f(x) = a_1 \phi_1(x) + \dots + a_m \phi_m(x)$ qui minimise l'erreur. Cela revient encore à résoudre un système linéaire (les **équations normales**) pour trouver les coefficients $a_j$.

> [!important] Règle d'or 
> Les fonctions de base $\phi_j(x)$ doivent être **linéairement indépendantes** (aucune ne doit être une combinaison des autres), sinon le système n'a pas de solution unique.

## 3. Régression Polynomiale et Choix de la Base

_Le piège des polynômes._

### ⚠️ Le problème de la base standard

On pourrait penser qu'utiliser $1, x, x^2, x^3, \dots$ est naturel. C'est une **erreur numérique** courante.

- **Problème** : Ces fonctions se ressemblent trop sur l'intervalle $[0,1]$.
    
- **Conséquence** : Le système d'équations devient "mal conditionné" (instable). Une toute petite erreur de calcul change complètement le résultat.
    

### 💡 La solution : Polynômes Orthogonaux

Au lieu de $x^k$, on utilise des polynômes spéciaux (comme ceux de **Tchebychev**) qui sont "orthogonaux" entre eux (très différents les uns des autres).

- **Avantage magique** : La matrice du système devient **diagonale**.
    
- **Simplicité** : Chaque coefficient $a_i$ se calcule indépendamment des autres. Ajouter un degré supérieur ne change pas les coefficients déjà calculés !
    

### 🔎 Quel degré choisir ?

On ne connaît pas le degré du polynôme idéal à l'avance. **L'Algorithme de choix de degré :**

1. Calculer la régression pour le degré $k=0, 1, 2, \dots$
    
2. Pour chaque degré, calculer la **variance** $\sigma_k^2$ (l'erreur moyenne restante).
    
3. La variance diminue toujours quand le degré augmente.
    
4. **Critère d'arrêt** : On s'arrête quand la variance ne diminue plus _significativement_ (on atteint un plateau). Aller plus loin serait du sur-apprentissage.
    

## 4. Prétraitement des Données (Linéarisation)

_L'astuce "changement d'échelle"._

### 💡 L'idée intuitive

Parfois, il est plus simple de transformer les données pour qu'elles forment une ligne droite, plutôt que d'essayer de courber le modèle.

**Exemple : Loi de puissance** Si on soupçonne une relation du type $y = C x^a$ (ex: taille en fonction de l'âge).

1. On passe aux logarithmes : $\ln(y) = \ln(C x^a) = \ln(C) + a \ln(x)$.
    
2. On pose $Y = \ln(y)$, $X = \ln(x)$, $A = \ln(C)$.
    
3. L'équation devient $Y = A + aX$ : c'est une **droite** !
    
4. On fait une simple régression linéaire sur les logs pour trouver $a$ et $A$.
    

## 🏆 Tableau Récapitulatif

|Méthode|Objectif|À retenir|Quand l'utiliser ?|
|---|---|---|---|
|**Interpolation**|Passer _exactement_ par tous les points.|Risque d'oscillations fortes (effet Runge) si le degré est élevé.|Données très précises (tables), pas de bruit.|
|**Régression Linéaire**|Trouver la _tendance_ droite.|Minimise les moindres carrés. Système simple.|Données bruitées, tendance proportionnelle.|
|**Régression Polynomiale**|Trouver une courbe lisse.|**Danger** : Ne pas utiliser la base $1, x, x^2$. Utiliser des polynômes orthogonaux.|Phénomènes complexes mais lisses.|
|**Linéarisation (Log)**|Ajuster des lois de puissance/expo.|Transforme le problème en régression linéaire.|Phénomènes physiques ou biologiques à croissance rapide.|