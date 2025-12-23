| Topic |
| :--- |
| [[#Tags: #Probabilités #Statistiques #LGN #TCL #BorelCantelli #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 7]] |
| [[#7.1 Loi des Grands Nombres (LGN)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Cadre]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Énoncés des LGN]] |
| [[#7.2 Théorème Central Limite (TCL)]] |
| [[#7.3 Lemme de Borel-Cantelli]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Limites d'ensembles]] |

## Tags: #Probabilités #Statistiques #LGN #TCL #BorelCantelli #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 7

# Chapitre 7 : Théorèmes Limites

Ce chapitre présente trois résultats fondamentaux qui décrivent le comportement asymptotique des variables aléatoires (quand le nombre d'observations $n \to \infty$). Ils justifient l'approche fréquentiste des probabilités et l'utilisation de la moyenne empirique en statistiques.

## 7.1 Loi des Grands Nombres (LGN)

On s'intéresse à la **moyenne empirique** $\bar{X}_n$ d'une suite de variables aléatoires indépendantes et identiquement distribuées (i.i.d.) $X_1, X_2, \dots, X_n$.

### Cadre

Soit $X$ une v.a. d'espérance $\mu = \mathbb{E}[X]$ et de variance $\sigma^2 = Var[X]$. On considère $X_1, \dots, X_n$ des v.a. i.i.d. de même loi que $X$.

> [!def] Moyenne Empirique
> 
> $$\bar{X}_n = \frac{1}{n} \sum_{j=1}^n X_j$$

> [!tip] Propriétés de $\bar{X}_n$ (Prop 7.1.2)
> 
> 1. **Espérance** : $\mathbb{E}[\bar{X}_n] = \mu$ (Estimateur sans biais).
>     
> 2. **Variance** : $Var[\bar{X}_n] = \frac{\sigma^2}{n}$.
>     
> 
> _Interprétation : Plus_ $n$ _augmente, plus la variance diminue, donc la distribution de_ $\bar{X}_n$ _se "concentre" autour de_ $\mu$_._

### Énoncés des LGN

Ces lois affirment que la moyenne empirique converge vers l'espérance théorique.

> [!important] Loi Faible des Grands Nombres
>  Pour tout $\epsilon > 0$, la probabilité que l'écart entre la moyenne empirique et l'espérance dépasse $\epsilon$ tend vers 0 :
> 
> $$\lim_{n \to \infty} \mathbb{P}(|\bar{X}_n - \mu| \ge \epsilon) = 0$$
> 
> _Preuve : Repose sur l'inégalité de Bienaymé-Tchebychev._

> [!important] Loi Forte des Grands Nombres 
> La moyenne empirique converge **presque sûrement** vers $\mu$ :
> 
> $$\mathbb{P}\left( \lim_{n \to \infty} \bar{X}_n = \mu \right) = 1$$

_Justification de l'approche fréquentiste :_ Si $X$ est une indicatrice d'un événement $A$ ($X=1$ si $A$ se réalise, $0$ sinon), alors $\bar{X}_n$ est la fréquence d'apparition de $A$. La LGN assure que cette fréquence converge vers la probabilité théorique $p = \mathbb{E}[X] = \mathbb{P}(A)$.

## 7.2 Théorème Central Limite (TCL)

La LGN dit que $\bar{X}_n \to \mu$. Le TCL précise **comment** cette convergence se fait (la forme de la distribution de l'erreur) et à quelle vitesse.

> [!important] Théorème Central Limite (TCL)
>  Soient $X_1, \dots, X_n$ des v.a. i.i.d. d'espérance $\mu$ et de variance $\sigma^2$. La variable centrée réduite associée à la moyenne empirique converge en loi vers une loi normale standard $\mathcal{N}(0, 1)$ :
> 
> $$\lim_{n \to \infty} \mathbb{P}\left( \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \le x \right) = \Phi(x)$$
> 
> où $\Phi$ est la fonction de répartition de la loi normale $\mathcal{N}(0, 1)$.

**Conséquences Pratiques :** Pour $n$ grand ($n \ge 30$ est une règle empirique courante), on a les approximations :

1. $\bar{X}_n \approx \mathcal{N}(\mu, \frac{\sigma^2}{n})$
    
2. La somme $S_n = \sum_{j=1}^n X_j \approx \mathcal{N}(n\mu, n\sigma^2)$
    

> [!example] Approximation de la loi Binomiale (De Moivre - Laplace) 
> Si $Y_n \sim Bin(n, p)$ (somme de $n$ Bernoulli), alors pour $n$ grand :
> 
> $$Y_n \approx \mathcal{N}(np, np(1-p))$$
> 
> On utilise la variable standardisée :
> 
> $$Z_n = \frac{Y_n - np}{\sqrt{np(1-p)}} \approx \mathcal{N}(0, 1)$$

## 7.3 Lemme de Borel-Cantelli

Ce résultat concerne la convergence d'ensembles (événements).

### Limites d'ensembles

Soit $(A_j)_j$ une suite d'événements.

- **Limite Supérieure** ($\limsup A_j$) : L'événement "une infinité de $A_j$ se réalisent".
    
    $$\limsup A_j = \bigcap_{J \ge 1} \bigcup_{j \ge J} A_j$$
- **Limite Inférieure** ($\liminf A_j$) : L'événement "tous les $A_j$ se réalisent à partir d'un certain rang".
    

> [!important] Lemme de Borel-Cantelli 
> Si la somme des probabilités converge ($\sum_{j=1}^{+\infty} \mathbb{P}(A_j) < \infty$), alors :
> 
> $$\mathbb{P}(\limsup A_j) = 0$$
> 
> _Interprétation : Si le nombre moyen d'événements qui se réalisent (_$\sum \mathbb{P}(A_j)$_) est fini, alors la probabilité qu'une infinité d'entre eux se réalisent est nulle._