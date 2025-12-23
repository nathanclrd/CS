| Topic |
| :--- |
| [[#Tags: #Probabilités #VariablesAléatoires #LoisUsuelles #Espérance #Variance #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 4]] |
| [[#4.1 Définitions Générales]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Loi et Fonction de Répartition]] |
| [[#4.2 Variables Aléatoires Discrètes]] |
| [[#4.3 Variables Aléatoires Continues]] |
| [[#4.5 Espérance et Variance]] |
| [[#4.6 Lois Usuelles]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Lois Discrètes]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Lois Continues]] |

## Tags: #Probabilités #VariablesAléatoires #LoisUsuelles #Espérance #Variance #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 4

# Chapitre 4 : Variables aléatoires

Ce chapitre introduit le concept central de **variable aléatoire** (v.a.), qui permet de traduire les résultats d'une expérience aléatoire en nombres réels (ex: somme de dés, durée de vie, nombre de succès). On distingue principalement deux familles : les variables **discrètes** et **continues**.

## 4.1 Définitions Générales

> [!def] Variable Aléatoire (v.a.) 
> Une variable aléatoire est une application $X: \Omega \to \mathbb{R}$ telle que pour tout intervalle $I$, l'ensemble $\{X \in I\}$ est un événement (appartient à la tribu $\mathcal{F}$).
> 
> _Note_ : On ne s'intéresse plus à $\Omega$ directement, mais aux valeurs que prend $X$ _et avec quelle probabilité._

### Loi et Fonction de Répartition

La **loi** de $X$ est la description complète des probabilités $\mathbb{P}(X \in I)$ pour tout intervalle. Elle est caractérisée par la fonction de répartition.

> [!def] Fonction de Répartition (CDF) 
> Pour toute v.a. $X$, la fonction de répartition $F_X$ est définie par :
> 
> $$F_X(x) = \mathbb{P}(X \le x)$$

> [!tip] Propriétés de $F_X$ (Prop 4.1.9)
> 
> 1. $F_X$ est **croissante**.
>     
> 2. $\lim_{x \to -\infty} F_X(x) = 0$ et $\lim_{x \to +\infty} F_X(x) = 1$.
>     
> 3. Lien avec les probabilités d'intervalles :
>     
>     $$\mathbb{P}(a < X \le b) = F_X(b) - F_X(a)$$$$\mathbb{P}(X > a) = 1 - F_X(a)$$

## 4.2 Variables Aléatoires Discrètes

Une v.a. est **discrète** si elle prend un nombre fini ou dénombrable de valeurs (le **support**).

> [!def] Fonction de Masse 
> La loi est donnée par la fonction de masse $p_X$ :
> 
> $$p_X(x_j) = \mathbb{P}(X = x_j)$$
> 
> **Condition de normalisation** : $\sum_j p_X(x_j) = 1$.

Pour calculer la probabilité d'un ensemble $A$ : $\mathbb{P}(X \in A) = \sum_{x_j \in A} p_X(x_j)$. La fonction de répartition $F_X$ est une fonction en escalier.

## 4.3 Variables Aléatoires Continues

Une v.a. est **continue** si elle peut prendre n'importe quelle valeur dans un intervalle continu. La probabilité qu'elle prenne une valeur _exacte_ est nulle ($\mathbb{P}(X=x)=0$).

> [!def] Densité de Probabilité
>  Une v.a. $X$ est continue s'il existe une fonction intégrable $f \ge 0$ (la densité) telle que :
> 
> $$\mathbb{P}(a \le X \le b) = \int_a^b f(x) dx$$
> 
> **Condition de normalisation** : $\int_{-\infty}^{+\infty} f(x) dx = 1$.

> [!info] Lien Densité / Répartition
> 
> - $F_X(x) = \int_{-\infty}^x f(t) dt$ (Primitive)
>     
> - $f(x) = F_X'(x)$ (Dérivée, là où elle existe)
>     

## 4.5 Espérance et Variance

L'espérance est la valeur moyenne théorique ("centre de gravité" de la distribution).

> [!summary] Formules de l'Espérance $\mathbb{E}[X]$
> 
> |Type|Formule|
> |---|---|
> |**Discret**|$\mathbb{E}[X] = \sum_j x_j \cdot \mathbb{P}(X=x_j)$|
> |**Continu**|$\mathbb{E}[X] = \int_{-\infty}^{+\infty} x \cdot f(x) dx$|
> |**Fonction** $g(X)$|$\mathbb{E}[g(X)] = \sum g(x_j)p(x_j)$ ou $\int g(x)f(x)dx$|

> [!tip] Propriétés de l'Espérance (Linéarité)
> 
> 1. $\mathbb{E}[X + Y] = \mathbb{E}[X] + \mathbb{E}[Y]$
>     
> 2. $\mathbb{E}[\alpha X] = \alpha \mathbb{E}[X]$
>     
> 3. $\mathbb{E}[c] = c$ (pour une constante $c$)
>     
> 4. **Monotonie** : Si $X \le Y$, alors $\mathbb{E}[X] \le \mathbb{E}[Y]$.
>     

La variance mesure la **dispersion** autour de la moyenne.

> [!def] Variance et Écart-Type 
> **Variance** : $Var[X] = \mathbb{E}[(X - \mathbb{E}[X])^2]$ **Formule de Koenig-Huygens** (Calcul pratique) :
> 
> $$Var[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$
> 
> **Écart-type** : $\sigma_X = \sqrt{Var[X]}$

> [!tip] Propriétés de la Variance
> 
> 1. $Var[X] \ge 0$.
>     
> 2. $Var[X + c] = Var[X]$ (Invariance par translation).
>     
> 3. $Var[\alpha X] = \alpha^2 Var[X]$ (Homogénéité quadratique).
>     

> [!important] Inégalité de Bienaymé-Tchebychev
>  Pour toute v.a. $X$ d'espérance $\mu$ et de variance $\sigma^2$, et tout $r > 0$ :
> 
> $$\mathbb{P}(|X - \mu| \ge r\sigma) \le \frac{1}{r^2}$$
> 
> _Interprétation : La probabilité de s'éloigner de la moyenne de plus de_ $r$ _écarts-types est faible._

## 4.6 Lois Usuelles

### Lois Discrètes

|Loi|Notation|Support|$\mathbb{P}(X=k)$|Espérance|Variance|
|---|---|---|---|---|---|
|**Uniforme**|$Unif(\{1..n\})$|$\{1,..,n\}$|$\frac{1}{n}$|$\frac{n+1}{2}$|$\frac{n^2-1}{12}$|
|**Bernoulli**|$Bern(p)$|$\{0,1\}$|$p$ (si $k=1$)|$p$|$p(1-p)$|
|**Binomiale**|$Bin(n,p)$|$\{0,..,n\}$|$\binom{n}{k}p^k(1-p)^{n-k}$|$np$|$np(1-p)$|
|**Géométrique**|$Geom(p)$|$\mathbb{N}^*$|$(1-p)^{k-1}p$|$\frac{1}{p}$|$\frac{1-p}{p^2}$|
|**Poisson**|$Pois(\lambda)$|$\mathbb{N}$|$e^{-\lambda}\frac{\lambda^k}{k!}$|$\lambda$|$\lambda$|

_Notes :_

- **Binomiale** : Nombre de succès en $n$ essais indépendants.
    
- **Géométrique** : Nombre d'essais pour obtenir le 1er succès (Propriété : **Sans mémoire**).
    
- **Poisson** : Événements rares (approxime Binomiale si $n$ grand, $p$ petit).
    

### Lois Continues

|Loi|Notation|Support|Densité $f(x)$|Espérance|Variance|
|---|---|---|---|---|---|
|**Uniforme**|$\mathcal{U}([a,b])$|$[a,b]$|$\frac{1}{b-a}$|$\frac{a+b}{2}$|$\frac{(b-a)^2}{12}$|
|**Exponentielle**|$Exp(\lambda)$|$\mathbb{R}^+$|$\lambda e^{-\lambda x}$|$\frac{1}{\lambda}$|$\frac{1}{\lambda^2}$|
|**Normale**|$\mathcal{N}(\mu, \sigma^2)$|$\mathbb{R}$|$\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$|$\mu$|$\sigma^2$|

_Notes :_

- **Exponentielle** : Durée de vie sans vieillissement (**Sans mémoire**).
    
- **Normale** : Courbe en cloche. On utilise la transformation $Z = \frac{X-\mu}{\sigma} \sim \mathcal{N}(0,1)$ pour utiliser les tables.