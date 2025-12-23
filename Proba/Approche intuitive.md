| Topic |
| :--- |
| [[#Tags: #Probabilités #Mathématiques #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 1]] |
| [[#1.1 Théorie des ensembles]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Opérations ensemblistes]] |
| [[#1.2 Probabilités dans le cas fini équiprobable]] |
| [[#1.3 Analyse combinatoire]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Outils de dénombrement]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Principes additionnels]] |
| [[#1.4 Limites et tentative de généralisation]] |

## Tags: #Probabilités #Mathématiques #ULiège #Synthèse Source: Éléments du calcul des probabilités Chapitre: 1

Ce chapitre introductif pose les bases du langage probabiliste via la théorie des ensembles et explore le cas simple des espaces finis équiprobables (analyse combinatoire), tout en soulignant les limites de cette approche "naïve".

## 1.1 Théorie des ensembles

La modélisation probabiliste commence par définir l'ensemble des résultats possibles comme un ensemble mathématique.

> [!abstract] Définitions de base
> 
> - **Espace fondamental (**$\Omega$**)** : Ensemble de tous les résultats possibles d'une expérience aléatoire.
>     
> - **Élément (**$\omega$**)** : Un résultat particulier ($\omega \in \Omega$).
>     
> - **Événement (**$A$**)** : Un sous-ensemble de $\Omega$ ($A \subseteq \Omega$). C'est une proposition liée au résultat.
>     
> - **Espace des parties (**$\mathcal{P}(\Omega)$**)** : L'ensemble de tous les sous-ensembles possibles de $\Omega$.
>     

### Opérations ensemblistes

Les liens logiques entre événements se traduisent par des opérations sur les ensembles.

|Opération|Notation|Signification|
|---|---|---|
|**Inclusion**|$A \subseteq B$|Si A se réalise, alors B aussi.|
|**Union**|$A \cup B$|A **ou** B (ou les deux).|
|**Intersection**|$A \cap B$|A **et** B.|
|**Complémentaire**|$A^c$|**Non** A (tout sauf A).|
|**Différence**|$A \setminus B$|A mais **pas** B ($A \cap B^c$).|
|**Disjoints**|$A \cap B = \emptyset$|Incompatibles (ne peuvent arriver ensemble).|

> [!tip] Propriétés (Proposition 1.1.12) Les opérations $\cup$ et $\cap$ sont **commutatives**, **associatives** et **distributives**.
> 
> **Lois de Morgan** :
> 
> 1. $(A \cup B)^c = A^c \cap B^c$
>     
> 2. $(A \cap B)^c = A^c \cup B^c$
>     

## 1.2 Probabilités dans le cas fini équiprobable

C'est l'approche historique et intuitive ("mise en bouche").

> [!important] Formule de Laplace (Cas équiprobable) Si l'espace $\Omega$ est fini et que tous les résultats ont la **même chance** d'apparaître (équiprobabilité), la probabilité d'un événement $A$ est :
> 
> $$\mathbb{P}(A) = \frac{\#A}{\#\Omega} = \frac{\text{nombre de cas favorables}}{\text{nombre de cas possibles}}$$

Cette définition ramène le calcul de probabilités à un problème de comptage (dénombrement).

## 1.3 Analyse combinatoire

Cette section fournit les outils pour calculer les cardinaux ($\#A$ et $\#\Omega$) nécessaires à la formule précédente.

### Outils de dénombrement

Le choix de la formule dépend de deux critères : l'**ordre** des éléments est-il important ? Peut-on répéter les éléments (**remise**) ?

> [!summary] Tableau des formules Tirage de $k$ éléments parmi $n$.
> 
> |Contexte|Formule|Nom|
> |---|---|---|
> |**Avec remise**, ordre important|$n^k$|$k$-uplets|
> |**Sans remise**, ordre important|$A_n^k = \frac{n!}{(n-k)!}$|Arrangements|
> |**Sans remise**, ordre **non** important|$\binom{n}{k} = \frac{n!}{k!(n-k)!}$|Combinaisons|
> |**Permutations** (ordre de $n$ éléments)|$n!$|Permutations|

### Principes additionnels

- **Règle de multiplication** : Si une expérience se compose de plusieurs étapes successives indépendantes, on multiplie le nombre de possibilités de chaque étape.
    

> [!example] Paradoxe des anniversaires 
> Dans un groupe de $k$ personnes, quelle est la probabilité que deux personnes aient le même anniversaire ?
> 
> - On passe par l'événement complémentaire : "Toutes les dates sont différentes".
>     
> - $\#\Omega = 365^k$ (avec remise).
>     
> - $\#A^c = A_{365}^k$ (sans remise, car dates différentes).
>     
> - Résultat : $\mathbb{P}(\text{Même anniversaire}) = 1 - \frac{365!}{365^k(365-k)!}$.
>     
> - _Fait notable : Dès 23 personnes, la probabilité dépasse 50%._
>     

## 1.4 Limites et tentative de généralisation

L'approche équiprobable ($\frac{\#A}{\#\Omega}$) présente deux limites majeures discutées à la fin du chapitre :

1. **Situations non-équiprobables** : Parfois, les issues élémentaires n'ont pas la même chance (ex: dé truqué, météo). On tente alors de pondérer chaque issue $\omega_j$ par un poids $p_j$ tel que $\sum p_j = 1$.
    
    $$\mathbb{P}(A) = \sum_{\omega_j \in A} p_j$$
2. **Espaces infinis** : Si $\Omega$ est infini (ex: temps d'attente d'un bus $\Omega = [0, +\infty[$), le comptage est impossible.