| Topic                                                                                |
| :----------------------------------------------------------------------------------- |
| [[#1. Formal Polynomials]]                                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Basic Definitions]]                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Operations on $\mathbb{K}[X]$]]                           |
| [[#2. Euclidean Division]]                                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Theorem and Algorithm]]                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Divisibility]]                                            |
| [[#3. GCD and Arithmetic]]                                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#GCD (Greatest Common Divisor)]]                           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Euclid's Algorithm & Bézout]]                             |
| [[#4. Polynomial Functions and Roots]]                                               |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Evaluation]]                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Zeros (Roots)]]                                           |
| [[#5. Formal Differentiation]]                                                       |
| [[#6. Fundamental Theorem of Algebra (FTA)]]                                         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Consequences (Corollaries)]]                              |
| [[#7. Polynomials with Real Coefficients]]                                           |
| [[#1. Opérations et Degré]]                                                          |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Intégrité de $\mathbb{K}[X]$]]                            |
| [[#2. Division Euclidienne]]                                                         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Théorème d'Existence et d'Unicité]]                       |
| [[#3. Arithmétique des Polynômes]]                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Théorème de Gauss]]                                       |
| [[#4. Dérivées et Taylor]]                                                           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Formule de Taylor]]                                       |
| [[#5. Zéros et Fonctions Polynomiales]]                                              |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Caractérisation des Zéros]]                               |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Conséquences du Théorème Fondamental de l'Algèbre (TFA)]] |
| [[#6. Cas Réel ($\mathbb{R}[X]$)]]                                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Zéros conjugués]]                                         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Produit de facteurs conjugués]]                           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Factorisation dans $\mathbb{R}[X]$]]                      |

# Synthesis: Polynomials ($\mathbb{K}[X]$)

#mathematics #computerscience #algebra #polynomials #obsidian

> [!abstract] Context 
> This document is a detailed synthesis of the course on polynomials. 
> **Notation**: $\mathbb{K}$ denotes one of the following sets: $\mathbb{C}, \mathbb{R}, \mathbb{Q}$ or $\mathbb{Z}_m$ (where $m$ is prime). $\mathbb{K}_0$ denotes $\mathbb{K} \setminus \{0\}$.

## 1. Formal Polynomials

### Basic Definitions

> [!definition] Polynomial 
> A polynomial with coefficients in $\mathbb{K}$ is an expression of the form:
> 
> $$P = p_0 + p_1 X + p_2 X^2 + \dots + p_d X^d$$
> 
> - $p_i \in \mathbb{K}$ are the **coefficients**.
>     
> - $X$ is the **indeterminate**.
>     
> - The set of polynomials is denoted by $\mathbb{K}[X]$.
>     

**Degree (**$\deg(P)$**)**:

- If $P \neq 0$, the degree $d$ is the largest integer such that $p_d \neq 0$.
    
- $p_d$ is the **leading coefficient**.
    
- **Convention**: $\deg(0) = -\infty$.
    

> [!note] Sequential Representation 
> A polynomial can be viewed as a finite sequence of coefficients: $P = (p_0, p_1, \dots, p_d, 0, 0, \dots)$.

### Operations on $\mathbb{K}[X]$

Let $P = \sum p_i X^i$ and $Q = \sum q_i X^i$.

1. **Addition**: $P+Q = \sum (p_i + q_i)X^i$.
   
2. **Product**: $P \cdot Q = \sum c_k X^k$ with $c_k = \sum_{i=0}^k p_i q_{k-i}$.    

3. **Scalar Multiplication**: $kP = \sum (kp_i)X^i$ (for $k \in \mathbb{K}$).


> [!important] Properties of Degree For $P, Q \in \mathbb{K}[X]$ and $k \in \mathbb{K}_0$:
> 
> 1. $\deg(P+Q) \leq \max(\deg(P), \deg(Q))$
>     
> 2. $\deg(P \cdot Q) = \deg(P) + \deg(Q)$
>     
> 3. $\deg(kP) = \deg(P)$
>     

> [!tip] Integrity
>  $\mathbb{K}[X]$ is an **integral domain**:
>   If $P \cdot Q = 0$, then $P=0$ or $Q=0$. _Proof_: If $P, Q \neq 0$, then $\deg(P \cdot Q) = \deg(P) + \deg(Q) \geq 0$, therefore $P \cdot Q \neq 0$.

## 2. Euclidean Division

### Theorem and Algorithm

> [!theorem] Euclidean Division
>  For any $P, D \in \mathbb{K}[X]$ with $D \neq 0$, there exist **unique** polynomials $Q$ (quotient) and $R$ (remainder) such that:
> 
> $$P = Q \cdot D + R \quad \text{and} \quad \deg(R) < \deg(D)$$

**Calculation Method (Algorithm)**: We proceed by successive elimination of the highest degree terms of the dividend, similar to integer division.

> [!example] Example in $\mathbb{Q}[X]$ 
> Division of $P = 6X^5 + X^4 - X^3 + 2X - 1$ by $D = 2X^2 + X - 3$.
> 
> - We seek to eliminate $6X^5$ by multiplying $D$ by $3X^3 \dots$
>     
> - Final result:
>     
>     - Quotient $Q = 3X^3 - X^2 + \frac{9}{2}X - \frac{15}{4}$
>         
>     - Remainder $R = \frac{77}{4}X - \frac{49}{4}$
>         

### Divisibility

> [!definition] Divisibility 
> $D$ **divides** $P$ if the remainder of the Euclidean division of $P$ by $D$ is zero ($R=0$). In other words, there exists $Q$ such that $P = Q \cdot D$.

## 3. GCD and Arithmetic

### GCD (Greatest Common Divisor)

> [!definition] GCD 
> A GCD of $P$ and $Q$ is a polynomial $D$ such that:
> 
> 1. $D$ divides $P$ and $D$ divides $Q$.
>     
> 2. Any polynomial dividing both $P$ and $Q$ also divides $D$.
>     

_Note_: The GCD is defined up to a non-zero multiplicative constant. We often normalize it by taking the leading coefficient equal to 1.

### Euclid's Algorithm & Bézout

As with integers, we use Euclid's algorithm (successive divisions) to find the GCD.

> [!theorem] Bézout's Identity
>  Let $D$ be a GCD of $P$ and $Q$. There exist $A, B \in \mathbb{K}[X]$ such that:
> 
> $$A \cdot P + B \cdot Q = D$$

> [!theorem] Gauss's Lemma 
> If $D$ divides $PQ$ and $D$ and $P$ are coprime (GCD = 1), then $D$ divides $Q$.

## 4. Polynomial Functions and Roots

### Evaluation

For $P \in \mathbb{K}[X]$ and $k \in \mathbb{K}$, we denote $P(k)$ the value obtained by replacing $X$ with $k$.

- **Induced function**: $f: \mathbb{K} \to \mathbb{K}, k \mapsto P(k)$.
    

> [!warning] Warning 
> Two different formal polynomials can induce the same function (e.g., in $\mathbb{Z}_2[X]$, $X^2$ and $X$ induce the same function because $0^2=0$ and $1^2=1$). However, for $\mathbb{K} \in \{\mathbb{C}, \mathbb{R}, \mathbb{Q}\}$, the equality of functions implies the equality of polynomials.

### Zeros (Roots)

> [!definition] Zero of a polynomial 
> $k \in \mathbb{K}$ is a zero (or root) of $P$ if $P(k) = 0$.
> 
> **Equivalence**: $k$ is a root of $P \iff (X-k)$ divides $P$.

**Multiplicity**: $k$ is a root of multiplicity $\alpha$ if $(X-k)^\alpha$ divides $P$ but $(X-k)^{\alpha+1}$ does not divide $P$.

## 5. Formal Differentiation

> [!definition] Derivative
>  If $P = \sum p_i X^i$, then the derivative polynomial is:
> 
> $$DP = P' = \sum i \cdot p_i X^{i-1}$$

**Properties**:

- **Linearity**: $D(kP + lQ) = kDP + lDQ$.
    
- **Leibniz Rule**: $D^n(PQ) = \sum_{i=0}^n C_n^i D^i P \cdot D^{n-i} Q$.
    
- **Taylor's Formula** (for $\mathbb{K} \in \{\mathbb{C}, \mathbb{R}, \mathbb{Q}\}$):
    
    $$P = \sum_{i=0}^{\deg(P)} \frac{D^i P(k)}{i!} (X-k)^i$$

> [!tip] Link Roots 
> - Derivatives (For $\mathbb{K} \in \{\mathbb{C}, \mathbb{R}, \mathbb{Q}\}$) $k$ is a root of multiplicity $\alpha$ of $P$ if and only if:
> 
> $$P(k) = 0, \quad P'(k) = 0, \quad \dots, \quad P^{(\alpha-1)}(k) = 0 \quad \text{and} \quad P^{(\alpha)}(k) \neq 0$$

## 6. Fundamental Theorem of Algebra (FTA)

> [!theorem] Fundamental Theorem of Algebra (d'Alembert-Gauss) 
> Every polynomial in $\mathbb{C}[X]$ of degree $d \geq 1$ has exactly $d$ roots in $\mathbb{C}$ (counted with multiplicity).
> 
> **Factorization in** $\mathbb{C}[X]$:
> 
> $$P = p_d (X - k_1)^{\alpha_1} \dots (X - k_m)^{\alpha_m}$$
> 
> where $\sum \alpha_i = d$.

### Consequences (Corollaries)

1. **Uniqueness**: Two polynomials having the same zeros with the same multiplicities are proportional.
    
2. **Identification**: If two polynomials of degree $\le d$ take the same values at $d+1$ points, they are equal.
    
3. **Polynomial/Function Equivalence**: On $\mathbb{C}, \mathbb{R}, \mathbb{Q}$, $P=Q \iff \forall k, P(k)=Q(k)$.
    

## 7. Polynomials with Real Coefficients

Although $\mathbb{R} \subset \mathbb{C}$, polynomials in $\mathbb{R}[X]$ have specific properties regarding their complex roots.

> [!theorem] Conjugate Roots
>  If $P \in \mathbb{R}[X]$ and if $c \in \mathbb{C}$ is a root of $P$, then its conjugate $\bar{c}$ is also a root of $P$ with the same multiplicity. (This only works in $\mathbb{C}$)

> [!summary] Factorization in $\mathbb{R}[X]$ 
> Every polynomial in $\mathbb{R}[X]$ decomposes into a product:
> 
> - Of degree 1 factors: $(X - r_i)$ (real roots).
>     
> - Of irreducible degree 2 factors: $(X^2 + aX + b)$ with $\Delta = a^2 - 4b < 0$ (pairs of complex conjugate roots).
>     
> 
> $$P = \lambda \prod (X-r_i) \prod (X^2+a_j X + b_j)$$

# 8. Démonstrations : Polynômes

Ce document recense les démonstrations du chapitre sur les polynômes ($\mathbb{K}[X]$) tirées du cours _Mathématiques pour l'informatique 2_.

> [!INFO] Légende
> 
> - $\mathbb{K}$ désigne $\mathbb{C}, \mathbb{R}, \mathbb{Q}$ ou $\mathbb{Z}_m$ (m premier).
>     
> - Les démonstrations sont masquées par défaut. **Cliquez sur la flèche pour les révéler.**
>     

## 1. Opérations et Degré

### Intégrité de $\mathbb{K}[X]$

> [!important] Corollaire : Intégrité 
> Si $P, Q \in \mathbb{K}[X]$ sont tels que $P \cdot Q = 0$, alors $P=0$ ou $Q=0$.

> [!example]- Démonstration Nous procédons par la **contraposée**.
> 
> Supposons que $P$ et $Q$ soient deux polynômes **non nuls**.
> 
> 1. Si $P \neq 0$ et $Q \neq 0$, alors $\deg(P) \geq 0$ et $\deg(Q) \geq 0$.
>     
> 2. D'après la propriété du degré du produit :
>     
>     $$\deg(P \cdot Q) = \deg(P) + \deg(Q) \geq 0$$
> 3. Un polynôme de degré $\geq 0$ n'est pas le polynôme nul. Donc $P \cdot Q \neq 0$.
>     
> 
> La contraposée est donc vraie : si le produit est nul, l'un des facteurs est nécessairement nul.

## 2. Division Euclidienne

### Théorème d'Existence et d'Unicité

> [!important] Théorème : Division Euclidienne 
> Pour tous polynômes $P, D \in \mathbb{K}[X]$ avec $D \neq 0$, il existe des polynômes **uniques** $Q, R \in \mathbb{K}[X]$ tels que :
> 
> $$P = Q \cdot D + R \quad \text{et} \quad \deg(R) < \deg(D)$$

> [!example]- Démonstration de l'Existence 
> On procède par **récurrence sur le degré de** $P$.
> 
> **Cas de base :** Si $\deg(P) < \deg(D)$, il suffit de choisir $Q=0$ et $R=P$. La condition sur le degré est satisfaite.
> 
> **Hypothèse de récurrence :** Supposons que $\deg(P) \ge \deg(D)$ et que le résultat est vrai pour tout polynôme de degré strictement inférieur à celui de $P$.
> 
> **Hérédité :** Soient $p$ et $d$ les coefficients dominants de $P$ et $D$ respectivement. Considérons le polynôme $P'$ défini par :
> 
> $$P' = P - \frac{p}{d} X^{\deg(P)-\deg(D)} D$$
> 
> Par construction, le terme de plus haut degré de $P$ est annulé. Donc $\deg(P') < \deg(P)$.
> 
> Par hypothèse de récurrence, il existe $Q', R'$ tels que $P' = Q'D + R'$ avec $\deg(R') < \deg(D)$.
> 
> En remplaçant $P'$ dans l'expression de $P$ :
> 
> $$P = \left( Q'D + R' \right) + \frac{p}{d} X^{\deg(P)-\deg(D)} D$$$$P = \left( Q' + \frac{p}{d} X^{\deg(P)-\deg(D)} \right) D + R'$$
> 
> En posant $Q = Q' + \frac{p}{d} X^{\deg(P)-\deg(D)}$ et $R = R'$, on a bien $P = QD + R$ avec la condition de degré sur $R$ respectée.

> [!example]- Démonstration de l'Unicité
Supposons qu'il existe deux couples $(Q_1, R_1)$ et $(Q_2, R_2)$ tels que :
> 
> 1. $P = Q_1 D + R_1$ avec $\deg(R_1) < \deg(D)$
>     
> 2. $P = Q_2 D + R_2$ avec $\deg(R_2) < \deg(D)$
>     
> 
> En soustrayant les deux égalités, on obtient :
> 
> $$0 = (Q_1 - Q_2)D + (R_1 - R_2) \iff (Q_1 - Q_2)D = R_2 - R_1$$
> 
> Raisonnons sur les degrés :
> 
> - Si $Q_1 \neq Q_2$, alors $\deg((Q_1 - Q_2)D) = \deg(Q_1 - Q_2) + \deg(D) \geq \deg(D)$.
>     
> - Or, $\deg(R_2 - R_1) \leq \max(\deg(R_1), \deg(R_2)) < \deg(D)$.
>     
> 
> On aurait donc une égalité entre un polynôme de degré $\geq \deg(D)$ et un polynôme de degré $< \deg(D)$, ce qui est **impossible**.
> 
> Donc nécessairement $Q_1 = Q_2$. L'égalité devient $0 \cdot D = R_2 - R_1$, d'où $R_1 = R_2$.

## 3. Arithmétique des Polynômes

### Théorème de Gauss

> [!important] Théorème de Gauss Si $P, Q, D \in \mathbb{K}[X]$ sont tels que $D$ divise $PQ$ et que $D$ et $P$ sont premiers entre eux, alors $D$ **divise** $Q$.

> [!example]- Démonstration
> 
> 1. Puisque $D$ et $P$ sont premiers entre eux, d'après le **Théorème de Bézout**, il existe $A, B \in \mathbb{K}[X]$ tels que :
>     
>     $$AD + BP = 1$$
> 2. On multiplie cette égalité par $Q$ :
>     
>     $$ADQ + BPQ = Q$$$$(AQ)D + B(PQ) = Q$$
> 3. Par hypothèse, $D$ divise $PQ$, donc il existe $S$ tel que $PQ = SD$. L'équation devient :
>     
>     $$(AQ)D + B(SD) = Q$$$$D(AQ + BS) = Q$$
> 4. On a écrit $Q$ comme un multiple de $D$, donc $D$ divise $Q$.
>     

## 4. Dérivées et Taylor

### Formule de Taylor

> [!important] Formule de Taylor (pour $\mathbb{K} = \mathbb{C}, \mathbb{R}$ ou $\mathbb{Q}$) 
> Pour tout $P \in \mathbb{K}[X]$ et tout $k \in \mathbb{K}$ :
> 
> $$P = \sum_{i=0}^{\deg(P)} \frac{D^i P(k)}{i!} (X-k)^i$$

> [!example]- Démonstration Soit $P = \sum_{n=0}^d p_n X^n$.
> 
> 1. On utilise l'astuce d'écriture $X = (X-k) + k$ et le **Binôme de Newton** :
>     
>     $$P = \sum_{n=0}^d p_n ((X-k) + k)^n = \sum_{n=0}^d p_n \sum_{i=0}^n C_n^i (X-k)^i k^{n-i}$$
> 2. On intervertit les sommes (sommation sur le triangle d'indices $0 \le i \le n \le d$) :
>     
>     $$P = \sum_{i=0}^d \left( \sum_{n=i}^d p_n C_n^i k^{n-i} \right) (X-k)^i$$
> 3. Il faut identifier le coefficient devant $(X-k)^i$. Calculons la dérivée $i$-ème de $P$ évaluée en $k$ :
>     
>     $$D^i P = D^i \left( \sum_{n=0}^d p_n X^n \right) = \sum_{n=i}^d p_n \frac{n!}{(n-i)!} X^{n-i}$$
>     
>     En évaluant en $k$ et en divisant par $i!$ :
>     
>     $$\frac{D^i P(k)}{i!} = \frac{1}{i!} \sum_{n=i}^d p_n \frac{n!}{(n-i)!} k^{n-i} = \sum_{n=i}^d p_n C_n^i k^{n-i}$$
> 4. On reconnait exactement le coefficient trouvé à l'étape 2. CQFD.
>     

## 5. Zéros et Fonctions Polynomiales

### Caractérisation des Zéros

> [!important] Proposition 
> $k$ est un zéro de $P$ si et seulement si $P(k) = 0$.

> [!example]- Démonstration 
> Effectuons la division euclidienne de $P$ par $(X-k)$ (polynôme de degré 1).
> 
> $$P = Q(X-k) + R \quad \text{avec} \quad \deg(R) < 1$$
> 
> Puisque $\deg(R) < 1$, $R$ est un polynôme constant, notons-le $c$.
> 
> En évaluant l'égalité en $k$ :
> 
> $$P(k) = Q(k)(k-k) + c \implies P(k) = c$$
> 
> - Si $k$ est un zéro (au sens de la définition), alors $(X-k)$ divise $P$, donc le reste $R$ (et donc $c$) est nul. Donc $P(k)=0$.
>     
> - Réciproquement, si $P(k)=0$, alors $c=0$, donc $R=0$, donc $(X-k)$ divise $P$.
>     

### Conséquences du Théorème Fondamental de l'Algèbre (TFA)

> [!important] Corollaire 1 : Mêmes zéros 
> Deux polynômes de $\mathbb{K}[X]$ ($\mathbb{K} = \mathbb{C}, \mathbb{R}, \mathbb{Q}$) ayant les mêmes zéros complexes avec les mêmes multiplicités sont **égaux à une constante multiplicative près**.

> [!example]- Démonstration
> 
> - Si les deux sont nuls : trivialement égaux.
>     
> - Si l'un est nul et l'autre non : impossible car ils n'auraient pas les mêmes zéros (le nul en a une infinité ou aucun selon la définition, le non-nul en a un nombre fini).
>     
> - Si les deux sont non nuls : Cela découle directement de la forme factorisée donnée par le TFA : $P = p \prod (X-k_i)^{\alpha_i}$ et $Q = q \prod (X-k_i)^{\alpha_i}$. Donc $P = \frac{p}{q} Q$.
>     

> [!important] Corollaire 2 : Égalité sur $d+1$ points 
> Deux polynômes de degré $d$ prenant les mêmes valeurs en $d+1$ arguments sont **égaux**.

> [!example]- Démonstration 
> Soient $P$ et $Q$ deux polynômes tels que $\deg(P) \le d$, $\deg(Q) \le d$ et $P(x_i) = Q(x_i)$ pour $d+1$ points distincts.
> 
> Considérons le polynôme différence $D = P - Q$.
> 
> - Son degré est au plus $d$.
>     
> - Il s'annule en $d+1$ points (les $x_i$).
>     
> 
> Si $D$ n'était pas nul, il aurait au plus $\deg(D) \le d$ zéros (par le TFA ou ses conséquences). Or il en a $d+1$. C'est une contradiction. Donc $D = 0$, soit $P = Q$.

> [!important] Corollaire 3 : Polynôme vs Fonction 
> Deux polynômes sont égaux si et seulement si leurs fonctions polynomiales induites sont égales.

> [!example]- Démonstration 
> ($\Rightarrow$) Immédiat. ($\Leftarrow$) Si les fonctions sont égales, elles prennent la même valeur partout sur $\mathbb{K}$. Comme $\mathbb{K}$ ($\mathbb{R}, \mathbb{C}, \mathbb{Q}$) contient une infinité de points, les polynômes coïncident sur une infinité de points. Le polynôme différence $P-Q$ a donc une infinité de zéros. Le seul polynôme ayant une infinité de zéros est le polynôme nul. Donc $P=Q$.

## 6. Cas Réel ($\mathbb{R}[X]$)

### Zéros conjugués

> [!important] Lemme 1 
> Si $P \in \mathbb{R}[X]$ et si $c \in \mathbb{C}$ est un zéro de $P$, alors son conjugué $\bar{c}$ est aussi un zéro de $P$.

> [!example]- Démonstration
>  Soit $P = \sum p_i X^i$ avec $p_i \in \mathbb{R}$. Supposons $P(c) = 0$.
> 
> Calculons $P(\bar{c})$ :
> 
> $$P(\bar{c}) = \sum p_i (\bar{c})^i = \sum p_i \overline{c^i}$$
> 
> Comme les $p_i$ sont réels, $p_i = \overline{p_i}$. Donc :
> 
> $$P(\bar{c}) = \sum \overline{p_i} \overline{c^i} = \overline{\sum p_i c^i} = \overline{P(c)}$$
> 
> Puisque $P(c) = 0$, alors $\overline{P(c)} = \overline{0} = 0$. Donc $P(\bar{c}) = 0$.

### Produit de facteurs conjugués

> [!important] Lemme 2 
> Pour tout $c \in \mathbb{C}$, le polynôme $(X-c)(X-\bar{c})$ appartient à $\mathbb{R}[X]$.

> [!example]- Démonstration 
> Posons $c = a + ib$ avec $a, b \in \mathbb{R}$.
> 
> $$(X-c)(X-\bar{c}) = X^2 - (c + \bar{c})X + c\bar{c}$$
> 
> Or :
> 
> - $c + \bar{c} = (a+ib) + (a-ib) = 2a \in \mathbb{R}$
>     
> - $c\bar{c} = (a+ib)(a-ib) = a^2 + b^2 \in \mathbb{R}$
>     
> 
> Les coefficients sont réels, donc le polynôme est dans $\mathbb{R}[X]$.

### Factorisation dans $\mathbb{R}[X]$

> [!important] Proposition 
> Tout polynôme de $\mathbb{R}[X]$ se factorise en produit de polynômes de degré 1 et de polynômes de degré 2 à discriminant négatif.

> [!example]- Démonstration
> 
> 1. Soit $P \in \mathbb{R}[X]$. Considérons ses racines dans $\mathbb{C}$.
>     
> 2. D'après le **Lemme 1**, les zéros sont :
>     
>     - Des réels $r_1, ..., r_k$.
>         
>     - Des complexes non réels $c_1, ..., c_l$ et leurs conjugués $\overline{c_1}, ..., \overline{c_l}$.
>         
> 3. Par le **Théorème Fondamental de l'Algèbre**, $P$ se factorise dans $\mathbb{C}[X]$ :
>     
>     $$P = p (X-r_1)\cdots(X-r_k) (X-c_1)(X-\overline{c_1}) \cdots (X-c_l)(X-\overline{c_l})$$
>     
>     où $p$ est le coefficient dominant.
>     
> 4. On regroupe les paires conjuguées en posant $Q_j = (X-c_j)(X-\overline{c_j})$.
>     
> 5. D'après le **Lemme 2**, $Q_j \in \mathbb{R}[X]$ et est de degré 2.
>     
> 6. Comme $c_j$ n'est pas réel, $Q_j$ n'a pas de racine réelle, donc son discriminant $\Delta$ est strictement négatif.
>     
> 7. La factorisation finale dans $\mathbb{R}[X]$ est donc :
>     
>     $$P = p \prod_{i=1}^k (X-r_i) \prod_{j=1}^l Q_j$$