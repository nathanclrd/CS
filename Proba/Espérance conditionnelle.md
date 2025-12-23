| Topic |
| :--- |
| [[#Tags: #Probabilités #EspéranceConditionnelle #ThéorèmeEspéranceTotale #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 6]] |
| [[#6.1 Approche Discrète]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Fonction de masse conditionnelle]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Espérance et Variance conditionnelles (valeurs)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Espérance conditionnelle (variable aléatoire)]] |
| [[#6.2 Approche Continue]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Densité conditionnelle]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Espérance conditionnelle]] |
| [[#6.4 Théorème de l'Espérance Totale]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Variance Totale]] |
| [[#6.5 Propriétés et Indépendance]] |

## Tags: #Probabilités #EspéranceConditionnelle #ThéorèmeEspéranceTotale #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 6

# Chapitre 6 : Espérance conditionnelle - une première approche

Ce chapitre introduit une notion fondamentale pour modéliser la dépendance entre variables aléatoires : l'espérance conditionnelle. Elle permet de mettre à jour la "valeur moyenne" attendue d'une variable $Y$ lorsqu'on dispose d'une information partielle (la valeur de $X$).

## 6.1 Approche Discrète

Soit $(X, Y)$ un couple aléatoire discret de supports respectifs $(x_j)_j$ et $(y_k)_k$.

### Fonction de masse conditionnelle

Si on observe que l'événement $\{X = x_j\}$ est réalisé, la distribution de $Y$ change.

> [!def] Fonction de masse conditionnelle 
> La probabilité que $Y$ prenne la valeur $y_k$ sachant que $X = x_j$ est :
> 
> $$p_{Y|X=x_j}(y_k) = \mathbb{P}(Y=y_k | X=x_j) = \frac{\mathbb{P}(X=x_j, Y=y_k)}{\mathbb{P}(X=x_j)} = \frac{p_{jk}}{p_{j\bullet}}$$
> 
> _(Valide uniquement si_ $\mathbb{P}(X=x_j) > 0$_)_.

Cela définit une nouvelle variable aléatoire (notée $Y | X=x_j$) dont la somme des probabilités vaut bien 1.

### Espérance et Variance conditionnelles (valeurs)

Pour une valeur fixée $x_j$ de $X$, l'espérance conditionnelle est un **nombre réel**.

> [!def] Espérance conditionnelle (valeur)
> 
> $$\mathbb{E}[Y | X=x_j] = \sum_k y_k \cdot \mathbb{P}(Y=y_k | X=x_j)$$

> [!def] Variance conditionnelle (valeur)
> 
> $$Var[Y | X=x_j] = \mathbb{E}[ (Y - \mathbb{E}[Y|X=x_j])^2 | X=x_j ]$$
> 
> _Formule pratique (Koenig-Huygens conditionnel)_ :
> 
> $$Var[Y | X=x_j] = \mathbb{E}[Y^2 | X=x_j] - (\mathbb{E}[Y | X=x_j])^2$$

### Espérance conditionnelle (variable aléatoire)

Si on ne fixe pas $x_j$ à l'avance, $\mathbb{E}[Y|X]$ devient une **variable aléatoire** qui est fonction de $X$. Elle prend la valeur $\mathbb{E}[Y|X=x_j]$ lorsque $X$ prend la valeur $x_j$.

> [!def] Variable Aléatoire $\mathbb{E}[Y|X]$
>  C'est la v.a. définie par :
> 
> - **Valeurs possibles** : L'ensemble des $\mathbb{E}[Y | X=x_j]$.
>     
> - **Probabilités** : La probabilité d'obtenir la valeur $\mathbb{E}[Y | X=x_j]$ est $\mathbb{P}(X=x_j)$.
>     

## 6.2 Approche Continue

Soit $(X, Y)$ un couple aléatoire continu de densité jointe $f(x, y)$.

### Densité conditionnelle

> [!def] Densité conditionnelle 
> La densité de $Y$ sachant que $X=x$ est définie par :
> 
> $$f_{Y|X=x}(y) = \frac{f(x, y)}{f_X(x)}$$
> 
> _(Valide là où la densité marginale_ $f_X(x) > 0$_)_.

On retrouve la densité jointe par la règle du produit : $f(x, y) = f_{Y|X=x}(y) \cdot f_X(x)$.

### Espérance conditionnelle

Comme dans le cas discret, c'est l'espérance calculée avec la densité conditionnelle.

> [!def] Formule continue
> 
> $$\mathbb{E}[Y | X=x] = \int_{-\infty}^{+\infty} y \cdot f_{Y|X=x}(y) \, dy$$

La variable aléatoire $\mathbb{E}[Y|X]$ est la v.a. qui prend la valeur $\mathbb{E}[Y|X=x]$ avec la densité $f_X(x)$.

## 6.4 Théorème de l'Espérance Totale

C'est le résultat central du chapitre, analogue à la loi des probabilités totales. L'espérance de l'espérance conditionnelle redonne l'espérance "brute".

> [!important] Théorème de l'Espérance Totale (T.E.T.) 
> Si $Y$ admet une espérance, alors :
> 
> $$\mathbb{E}[\mathbb{E}[Y|X]] = \mathbb{E}[Y]$$

**Interprétation pratique** : Pour calculer $\mathbb{E}[Y]$, il est souvent plus facile de conditionner par $X$ (si la loi de $Y$ dépend de $X$) puis de moyenner sur toutes les valeurs possibles de $X$.

- **Cas Discret** : $\mathbb{E}[Y] = \sum_j \mathbb{E}[Y | X=x_j] \cdot \mathbb{P}(X=x_j)$
    
- **Cas Continu** : $\mathbb{E}[Y] = \int_{-\infty}^{+\infty} \mathbb{E}[Y | X=x] \cdot f_X(x) \, dx$
    

### Variance Totale

Il existe une formule similaire pour décomposer la variance de $Y$.

> [!tip] Formule de la Variance Totale
> 
> $$Var[Y] = \mathbb{E}[Var[Y|X]] + Var[\mathbb{E}[Y|X]]$$
> 
> _La variance totale est la somme de :_
> 
> 1. _La moyenne des variances locales (dispersion intra-groupe)._
>     
> 2. _La variance des moyennes locales (dispersion inter-groupe)._
>     

## 6.5 Propriétés et Indépendance

L'espérance conditionnelle capture la dépendance. Si les variables sont indépendantes, le conditionnement ne change rien.

> [!summary] Propriétés Clés
> 
> 1. **Indépendance** : Si $X$ et $Y$ sont indépendantes, alors la connaissance de $X$ n'apporte rien :
>     
>     $$\mathbb{E}[Y|X] = \mathbb{E}[Y]$$
> 2. **Fonctionnelle** : $\mathbb{E}[Y|X]$ est une fonction de $X$ (et non de $Y$).
>     
> 3. **Linéarité** : $\mathbb{E}[aY_1 + bY_2 | X] = a\mathbb{E}[Y_1|X] + b\mathbb{E}[Y_2|X]$.
>     
> 4. **Sortie des constantes connues** : Si $h(X)$ est une fonction de $X$, alors elle agit comme une constante une fois $X$ connu :
>     
>     $$\mathbb{E}[h(X) \cdot Y | X] = h(X) \cdot \mathbb{E}[Y | X]$$