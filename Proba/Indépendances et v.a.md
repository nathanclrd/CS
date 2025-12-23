| Topic |
| :--- |
| [[#Tags: #Probabilités #VariablesAléatoires #Indépendance #Covariance #Corrélation #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 5]] |
| [[#5.1 Loi jointe et fonction de répartition]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Cas Discret (Lois bivariées discrètes)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Cas Continu (Lois bivariées continues)]] |
| [[#5.2 Indépendance de variables aléatoires]] |
| [[#5.3 Covariance et Corrélation]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Corrélation]] |

## Tags: #Probabilités #VariablesAléatoires #Indépendance #Covariance #Corrélation #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 5

# Chapitre 5 : Indépendance de variables aléatoires

Ce chapitre étend la notion de probabilité aux **couples aléatoires** $(X, Y)$ (vecteurs bivariés) pour étudier les liens potentiels entre deux variables définies sur le même espace.

## 5.1 Loi jointe et fonction de répartition

On s'intéresse à la distribution conjointe des valeurs prises par le couple $(X, Y)$.

> [!def] Loi jointe & Fonction de Répartition
> 
> - **Loi jointe** : Description des probabilités $\mathbb{P}((X, Y) \in I)$ pour tout rectangle $I \subseteq \mathbb{R}^2$.
>     
> - **Fonction de répartition jointe** :
>     
>     $$F_{X,Y}(x, y) = \mathbb{P}(X \le x \text{ et } Y \le y)$$

### Cas Discret (Lois bivariées discrètes)

Soient $X$ et $Y$ deux v.a. discrètes prenant les valeurs $\{x_j\}$ et $\{y_k\}$.

> [!def] Fonction de masse jointe
> 
> $$p_{X,Y}(x_j, y_k) = p_{jk} = \mathbb{P}(X = x_j \text{ et } Y = y_k)$$
> 
> **Condition de normalisation** : $\sum_j \sum_k p_{jk} = 1$.

> [!tip] Lois marginales (Projection) 
> On retrouve la loi de $X$ (ou $Y$) seule en sommant sur toutes les valeurs possibles de l'autre variable :
> 
> - **Marginale de X** : $p_X(x_j) = \sum_k p_{jk}$
>     
> - **Marginale de Y** : $p_Y(y_k) = \sum_j p_{jk}$
>     

### Cas Continu (Lois bivariées continues)

Le couple $(X, Y)$ est continu s'il existe une densité jointe $f(x, y)$.

> [!def] Densité jointe 
> Une fonction $f: \mathbb{R}^2 \to [0, +\infty[$ telle que pour tout domaine $D$ :
> 
> $$\mathbb{P}((X, Y) \in D) = \iint_D f(x, y) \, dx \, dy$$
> 
> **Condition de normalisation** : $\iint_{\mathbb{R}^2} f(x, y) \, dx \, dy = 1$.

> [!tip] Lois marginales 
> On "intègre" la variable dont on veut se débarrasser :
> 
> - **Densité marginale de X** : $f_X(x) = \int_{-\infty}^{+\infty} f(x, y) \, dy$
>     
> - **Densité marginale de Y** : $f_Y(y) = \int_{-\infty}^{+\infty} f(x, y) \, dx$
>     

## 5.2 Indépendance de variables aléatoires

L'indépendance signifie que connaître la valeur de $X$ n'apporte aucune information sur $Y$ (et inversement).

> [!def] Indépendance (Définition générale)
>  $X$ et $Y$ sont **indépendantes** (noté $X \perp\!\!\perp Y$) si :
> 
> $$F_{X,Y}(x, y) = F_X(x) \cdot F_Y(y) \quad \forall x, y \in \mathbb{R}$$

> [!important] Critères pratiques d'indépendance
> 
> - **Cas Discret** : $X \perp\!\!\perp Y \iff \mathbb{P}(X=x_j, Y=y_k) = \mathbb{P}(X=x_j) \cdot \mathbb{P}(Y=y_k)$ pour tout couple $(j, k)$.
>     
> - **Cas Continu** : $X \perp\!\!\perp Y \iff f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y)$ pour tout $(x, y)$. _(La densité jointe est le produit des densités marginales)._
>     

> [!tip] Espérance d'un produit Si $X$ et $Y$ sont **indépendantes**, alors :
> 
> $$\mathbb{E}[X \cdot Y] = \mathbb{E}[X] \cdot \mathbb{E}[Y]$$
> 
> _Attention : La réciproque est fausse ! (Voir covariance nulle)._
> 
> Plus généralement, si $X \perp\!\!\perp Y$, alors pour toutes fonctions $g, h$ : $\mathbb{E}[g(X)h(Y)] = \mathbb{E}[g(X)]\mathbb{E}[h(Y)]$.

## 5.3 Covariance et Corrélation

Ces outils mesurent le lien linéaire entre deux variables.

> [!def] Covariance 
> La covariance mesure comment deux variables varient ensemble :
> 
> $$Cov[X, Y] = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])]$$
> 
> **Formule de calcul (Koenig-Huygens)** :
> 
> $$Cov[X, Y] = \mathbb{E}[X Y] - \mathbb{E}[X]\mathbb{E}[Y]$$

> [!warning] Lien avec l'indépendance
> 
> - Si $X \perp\!\!\perp Y \implies Cov[X, Y] = 0$ (Variables **non-corrélées**).
>     
> - Si $Cov[X, Y] = 0 \nRightarrow X \perp\!\!\perp Y$ (La covariance ne mesure que la dépendance _linéaire_).
>     

> [!tip] Propriétés de la Covariance (Bilinéarité)
> 
> 1. $Cov[X, Y] = Cov[Y, X]$ (Symétrie).
>     
> 2. $Cov[X, X] = Var[X]$.
>     
> 3. $Cov[aX + b, cY + d] = ac \cdot Cov[X, Y]$.
>     
> 4. **Variance d'une somme** :
>     
>     $$Var[X + Y] = Var[X] + Var[Y] + 2Cov[X, Y]$$
>     
>     _(Si indépendants,_ $Var[X+Y] = Var[X] + Var[Y]$_)_.
>     

### Corrélation

Pour avoir une mesure standardisée (indépendante des unités), on utilise le coefficient de corrélation linéaire.

> [!def] Coefficient de Corrélation ($r$ ou $\rho$)
> 
> $$Corr[X, Y] = \frac{Cov[X, Y]}{\sqrt{Var[X]} \sqrt{Var[Y]}} = \frac{Cov[X, Y]}{\sigma_X \sigma_Y}$$

> [!important] Propriétés de la Corrélation
> 
> 1. **Bornes** : $-1 \le Corr[X, Y] \le 1$ (Inégalité de Cauchy-Schwarz).
>     
> 2. **Interprétation** :
>     
>     - $Corr \approx 1$ : Forte relation linéaire positive ($Y \approx aX+b, a>0$).
>         
>     - $Corr \approx -1$ : Forte relation linéaire négative.
>         
>     - $Corr \approx 0$ : Pas de relation _linéaire_ (mais une relation non-linéaire est possible).
>