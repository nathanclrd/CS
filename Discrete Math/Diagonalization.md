
| Topic                                                                           |
| :------------------------------------------------------------------------------ |
| [[#1. Core Definitions]]                                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Eigenvalues & Eigenvectors]]                         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Multiplicities]]                                     |
| [[#2. Key Polynomials]]                                                         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Characteristic Polynomial]]                          |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Minimal Polynomial ($\pi_A$)]]                       |
| [[#3. Theoretical Properties]]                                                  |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Similar Matrices]]                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Polynomial Lemma]]                                   |
| [[#4. Criteria for Diagonalization]]                                            |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Corollaries & Applications]]                         |
| [[#5. Practical Algorithm]]                                                     |
| [[#6. Solved Example: Computing the Basis]]                                     |
| [[#1. Valeurs Propres et Polynôme Caractéristique]]                             |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1. Critère de valeur propre]]                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2. Invariance par similitude]]                       |
| [[#2. Vecteurs Propres et Multiplicités]]                                       |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#3. Lien colonnes $S$ / vecteurs propres]]            |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4. Inégalité des multiplicités]]                     |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#5. Déterminant et valeurs propres]]                  |
| [[#3. Polynôme Minimal]]                                                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#6. Propriété de divisibilité (1)]]                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#7. Unicité du polynôme minimal]]                     |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#8. Propriété de divisibilité (2)]]                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#9. Polynôme de matrice et vecteur propre]]           |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#10. Racines du polynôme minimal]]                    |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#11. Cas des valeurs propres simples (Corollaire 1)]] |
| [[#4. Diagonalisation]]                                                         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#12. Théorème de Diagonalisation (Critères)]]         |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#13. Condition suffisante (Corollaire 2)]]            |

Tags: #math #linear_algebra #matrices #eigenvalues #diagonalization

# Linear Algebra: Diagonalization

## 1. Core Definitions

> [!INFO] Definition: Diagonalizable Matrix A 
> matrix $A \in \mathbb{C}^{m \times m}$ is **diagonalizable** if there exists an invertible matrix $S \in \mathbb{C}^{m \times m}$ such that $S^{-1}AS$ is a diagonal matrix.
> 
> **Why is this useful?** It simplifies calculating matrix powers. If $A = S\Delta S^{-1}$ where $\Delta = \text{diag}(\lambda_1, \dots, \lambda_m)$, then:
> 
> $$A^n = S \Delta^n S^{-1} = S \cdot \text{diag}(\lambda_1^n, \dots, \lambda_m^n) \cdot S^{-1}$$

### Eigenvalues & Eigenvectors

- **Eigenvalue (**$\lambda$**):** A complex number is a _vp_ (valeur propre) if there is a non-zero vector $x$ such that $Ax = \lambda x$.
    
- **Eigenvector (**$x$**):** The vector $x$ associated with $\lambda$.
    
- **Eigenspace (**$E_\lambda(A)$**):** The set of all eigenvectors for $\lambda$ (plus the zero vector).
    
    $$E_{\lambda}(A) = \{x \in \mathbb{C}^m : Ax = \lambda x\} = \text{Ker}(A - \lambda I)$$

### Multiplicities

> [!WARNING] Crucial Distinction Do not confuse the two types of multiplicity. For a matrix to be diagonalizable, these two numbers **must be equal** for every eigenvalue.

1. **Algebraic Multiplicity (**$\alpha_\lambda$**):** The multiplicity of $\lambda$ as a root of the _characteristic polynomial_.
    
2. **Geometric Multiplicity (**$d_\lambda$**):** The dimension of the eigenspace $E_\lambda(A)$.
    
    - **Calculation:** $d_\lambda = m - \text{rank}(A - \lambda I_m)$
        
    - **The Inequality:** $1 \le d_\lambda \le \alpha_\lambda$
        

## 2. Key Polynomials

### Characteristic Polynomial

$$P_A(X) = \det(A - X I_m)$$

- Roots = Eigenvalues of $A$.
    
- Degree = $m$ (size of the matrix).
    
- **Properties:**
    
    - $\det(A) = \prod_{i=1}^m \lambda_i$
        
    - $\text{tr}(A) = \sum_{i=1}^m \lambda_i$

	- $\text{tr}(A) = \sum_{i=1}^m A_{ii}$

> [!QUOTE] Theorem: Cayley-Hamilton Every square matrix cancels its own characteristic polynomial.
> 
> $$P_A(A) = 0$$
> 
> _Note: This does **not** mean replacing_ $X$ _with_ $A$ _inside the determinant formula directly (which would give 0)._

### Minimal Polynomial ($\pi_A$)

The monic polynomial of the lowest degree such that $\pi_A(A) = 0$.

- **Uniqueness:** There is exactly one minimal polynomial for $A$.
    
- **Divisibility:** $\pi_A$ divides the characteristic polynomial $P_A$.
    
- **Roots:** The zeros of $\pi_A$ are exactly the eigenvalues of $A$.
    

## 3. Theoretical Properties

### Similar Matrices

If $A$ and $B$ are similar (i.e., $B = S^{-1}AS$), they share the **same characteristic polynomial**.

- Consequently, they have the **same eigenvalues** with the **same algebraic multiplicities**.
    

### Polynomial Lemma

For any polynomial $P \in \mathbb{C}[X]$ and any eigenvector $x$ associated with $\lambda$:

$$P(A)x = P(\lambda)x$$

_This property is useful for proving that if_ $\pi(A)=0$_, then_ $\pi(\lambda)=0$_._

## 4. Criteria for Diagonalization

> [!SUMMARY] The Diagonalization Theorem 
> For a matrix $A \in \mathbb{C}^{m \times m}$, the following statements are equivalent:
> 
> 1. $A$ is diagonalizable.
>     
> 2. $A$ possesses $m$ linearly independent eigenvectors.
>     
> 3. The sum of geometric multiplicities equals $m$.
>     
> 4. **For every eigenvalue** $\lambda$**, the geometric multiplicity equals the algebraic multiplicity (**$d_\lambda = \alpha_\lambda$**).**
>     

### Corollaries & Applications

> [!TIP] Shortcuts & Context
> 
> - **Distinct Roots:** If $A$ has $m$ distinct eigenvalues (all simple roots), then $A$ is automatically diagonalizable.
>     
> - **Minimal Polynomial:** $A$ is diagonalizable $\iff$ its minimal polynomial has only **simple roots**.
>     
> - **Real Symmetric Matrices:** Any real symmetric matrix ($A = A^T$) is diagonalizable (and by an orthogonal matrix, orthogonal meaning that $A^T = A^{-1}$).
>     
> - **Graph Theory:** Since the adjacency matrix of an **undirected graph** is symmetric, it is always diagonalizable.
>     

## 5. Practical Algorithm

> [!EXAMPLE] How to Diagonalize
> 
> 1. **Find Eigenvalues:** Compute roots of $\det(A - X I_m) = 0$.
>     
> 2. **Check Dimensions & Find Basis:** For each eigenvalue $\lambda_i$, calculate the eigenspace basis.
>     
>     - **How to do this:** Solve the linear system $(A - \lambda_i I)x = 0$.
>         
>     - **Result:** The "free variables" in your solution will give you the basis vectors.
>         
>     - _If_ $\dim(E_{\lambda_i}) < \alpha_{\lambda_i}$ _for any_ $\lambda$_, STOP. It is not diagonalizable._
>         
> 3. **Construct** $S$**:** Collect all basis vectors found in step 2 into a single matrix columns.
>     
> 4. **Result:** $S$ is your transition matrix such that $S^{-1}AS = D$.
>
## 6. Solved Example: Computing the Basis

**Matrix:**

$$A = \begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}$$

**Step 1: Eigenvalues** Compute $\det(A - XI) = (1-X)^2 - 9$. Roots are $\lambda_1 = 4$ and $\lambda_2 = -2$.

**Step 2: Basis for** $\lambda_1 = 4$ We must solve $(A - 4I)v = 0$.

$$A - 4I = \begin{pmatrix} 1-4 & 3 \\ 3 & 1-4 \end{pmatrix} = \begin{pmatrix} -3 & 3 \\ 3 & -3 \end{pmatrix}$$

The system is:

$$\begin{cases} -3x + 3y = 0 \\ 3x - 3y = 0 \end{cases} \implies -3x = -3y \implies x = y$$

Since $y$ can be anything, we choose $y=1$. Then $x=1$. **Basis Vector 1:** $v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$

**Step 3: Basis for** $\lambda_2 = -2$ We must solve $(A - (-2)I)v = 0 \implies (A + 2I)v = 0$.

$$A + 2I = \begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix}$$

The system is:

$$3x + 3y = 0 \implies x = -y$$

We choose $y=1$. Then $x=-1$. **Basis Vector 2:** $v_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$

# 7 . Démonstrations : Diagonalisation

Ce document recense les **13 démonstrations** du chapitre sur la **Diagonalisation** tirées du cours _Mathématiques pour l'informatique 2_.

> [!INFO] Légende
> 
> - $A$ désigne une matrice de $\mathbb{C}^{m \times m}$.
>     
> - $\chi_A(X) = \det(A - XI_m)$ désigne le polynôme caractéristique.
>     
> - $\pi_A$ désigne le polynôme minimal.
>     
> - Les démonstrations sont masquées par défaut. **Cliquez sur la flèche pour les révéler.**
>     

## 1. Valeurs Propres et Polynôme Caractéristique

### 1. Critère de valeur propre

> [!important] Proposition 
> Un nombre complexe $\lambda$ est valeur propre de $A$ si et seulement si il est racine du polynôme caractéristique de $A$ (c'est-à-dire $\det(A - \lambda I_m) = 0$).

> [!example]- Démonstration 
> $\lambda$ est valeur propre de $A$ $\iff$ Il existe $x \neq 0$ tel que $Ax = \lambda x$ $\iff$ Le système homogène $(A - \lambda I_m)x = 0$ admet une solution non nulle. $\iff$ La matrice $A - \lambda I_m$ n'est pas inversible (le système n'est pas de Cramer). $\iff \det(A - \lambda I_m) = 0$. $\iff \lambda$ est racine du polynôme caractéristique.

### 2. Invariance par similitude

> [!important] Proposition 
> Si $A$ et $B$ sont semblables (i.e., $B = S^{-1}AS$), alors elles ont le même polynôme caractéristique.

> [!example]- Démonstration
>  Calculons le polynôme caractéristique de $S^{-1}AS$ :
> 
> $$\begin{aligned} \det(S^{-1}AS - X I_m) &= \det(S^{-1}AS - X S^{-1}I_m S) \\ &= \det(S^{-1}(A - X I_m)S) \\ &= \det(S^{-1}) \cdot \det(A - X I_m) \cdot \det(S) \end{aligned}$$
> 
> Comme les scalaires commutent et $\det(S^{-1})\det(S) = \det(S^{-1}S) = \det(I) = 1$, on obtient :
> 
> $$= \det(A - X I_m)$$

## 2. Vecteurs Propres et Multiplicités

### 3. Lien colonnes $S$ / vecteurs propres

> [!important] Lemme 
> La $j$-ème colonne de $S^{-1}AS$ est égale à $\lambda e_j$ si et seulement si la $j$-ème colonne de $S$ est un vecteur propre de $A$ relatif à $\lambda$.

> [!example]- Démonstration
>  Notons $c_j$ la $j$-ème colonne de $S$.
> 
> - La $j$-ème colonne de $AS$ est $A c_j$.
>     
> - D'autre part, regardons $S(S^{-1}AS)$. Si la $j$-ème colonne de $S^{-1}AS$ est $\lambda e_j$, alors la $j$-ème colonne de $S(S^{-1}AS)$ est $S(\lambda e_j) = \lambda S e_j = \lambda c_j$.
>     
> 
> Ainsi, $A c_j = \lambda c_j$, ce qui signifie que $c_j$ est un vecteur propre associé à $\lambda$.

### 4. Inégalité des multiplicités

> [!important] Proposition 
> La multiplicité géométrique d'une valeur propre $\lambda$ ($\dim E_\lambda$) est inférieure ou égale à sa multiplicité algébrique (dans $\chi_A$).

> [!example]- Démonstration 
> Soit $d = \dim E_\lambda(A)$. Soit $(x_1, ..., x_d)$ une base de l'espace propre $E_\lambda(A)$. On complète cette famille en une base $(x_1, ..., x_m)$ de $\mathbb{C}^m$. Soit $S$ la matrice inversible dont les colonnes sont ces vecteurs.
> 
> D'après le lemme précédent, comme les $d$ premières colonnes sont des vecteurs propres pour $\lambda$, la matrice $B = S^{-1}AS$ est de la forme :
> 
> $$B = \begin{pmatrix} \lambda I_d & * \\ 0 & M' \end{pmatrix}$$
> 
> Le polynôme caractéristique est :
> 
> $$\det(B - X I_m) = \det(\lambda I_d - X I_d) \cdot \det(M' - X I_{m-d}) = (\lambda - X)^d \cdot Q(X)$$
> 
> Le facteur $(\lambda - X)$ apparaît au moins $d$ fois, donc la multiplicité algébrique est au moins $d$.

### 5. Déterminant et valeurs propres

> [!important] Proposition
>  Le déterminant de $A$ est égal au produit de ses valeurs propres (comptées avec multiplicités).

> [!example]- Démonstration
>  On sait que $\chi_A(X) = \prod_{i=1}^m (\lambda_i - X)$. En évaluant ce polynôme en $0$ :
> 
> $$\chi_A(0) = \det(A - 0 \cdot I_m) = \det(A)$$
> 
> D'autre part, en remplaçant $X$ par $0$ dans le produit :
> 
> $$\prod_{i=1}^m (\lambda_i - 0) = \prod_{i=1}^m \lambda_i$$
> 
> D'où l'égalité.

## 3. Polynôme Minimal

### 6. Propriété de divisibilité (1)

> [!important] Lemme 
> Si $\pi$ est un polynôme minimal de $A$ et $P$ un polynôme annulateur ($P(A)=0$), alors $\pi$ divise $P$.

> [!example]- Démonstration
>  Effectuons la division euclidienne de $P$ par $\pi$ :
> 
> $$P = Q\pi + R \quad \text{avec} \quad \deg(R) < \deg(\pi)$$
> 
> Évaluons en $A$ :
> 
> $$P(A) = Q(A)\pi(A) + R(A)$$
> 
> Comme $P(A)=0$ et $\pi(A)=0$, on obtient $R(A)=0$. $R$ est donc un polynôme annulateur de degré strictement inférieur à celui du polynôme minimal. Par définition du polynôme minimal, $R$ doit être nul. Donc $P = Q\pi$, et $\pi$ divise $P$.

### 7. Unicité du polynôme minimal

> [!important] Proposition
>  Il existe un **unique** polynôme minimal de $A$ (unitaire).

> [!example]- Démonstration 
> Soient $P$ et $Q$ deux polynômes minimaux (donc unitaires et de même degré minimal). D'après le lemme précédent, $P$ divise $Q$ et $Q$ divise $P$. Comme ils sont unitaires, ils sont nécessairement égaux : $P=Q$.

### 8. Propriété de divisibilité (2)

> [!important] Proposition 
> Le polynôme minimal divise le polynôme caractéristique.

> [!example]- Démonstration 
> C'est une conséquence directe du **Théorème de Cayley-Hamilton** (admis : $\chi_A(A) = 0$). Puisque $\chi_A$ est un polynôme annulateur, le polynôme minimal le divise (d'après le lemme de divisibilité).

### 9. Polynôme de matrice et vecteur propre

> [!important] Lemme 
> Pour tout $P \in \mathbb{C}[X]$ et toute valeur propre $\lambda$ de $A$ associée au vecteur propre $x$, on a :
> 
> $$P(A)x = P(\lambda)x$$

> [!example]- Démonstration
> 
> 1. **Pour les puissances** : Montrons par récurrence que $A^k x = \lambda^k x$.
>     
>     - $k=0$ : $Ix = x = 1 x$. Ok.
>         
>     - Hérédité : $A^{k+1}x = A(A^k x) = A(\lambda^k x) = \lambda^k (Ax) = \lambda^k (\lambda x) = \lambda^{k+1} x$.
>         
> 2. **Pour le polynôme** : Soit $P = \sum a_k X^k$.
>     
>     $$P(A)x = (\sum a_k A^k) x = \sum a_k (A^k x) = \sum a_k \lambda^k x = (\sum a_k \lambda^k) x = P(\lambda) x$$

### 10. Racines du polynôme minimal

> [!important] Proposition 
> Les racines du polynôme minimal sont exactement les valeurs propres de $A$.

> [!example]- Démonstration 
> Soit $\pi$ le polynôme minimal.
> 
> **(**$\Rightarrow$**)** Si $\lambda$ est racine de $\pi$, alors $\lambda$ est racine de $\chi_A$ (car $\pi$ divise $\chi_A$), donc c'est une valeur propre.
> 
> **(**$\Leftarrow$**)** Soit $\lambda$ une valeur propre et $x \neq 0$ un vecteur propre associé. On sait que $\pi(A) = 0$. D'après le lemme précédent : $0 = \pi(A)x = \pi(\lambda)x$. Comme $x \neq 0$, on a nécessairement $\pi(\lambda) = 0$.

### 11. Cas des valeurs propres simples (Corollaire 1)

> [!important] Corollaire
>  Si toutes les valeurs propres de $A$ sont simples, alors le polynôme minimal est égal au polynôme caractéristique (au signe près).

> [!example]- Démonstration
>  Si $A$ a $m$ valeurs propres simples $\lambda_1, ..., \lambda_m$, alors :
> 
> $$\chi_A(X) = \prod (X - \lambda_i)$$
> 
> (au signe près). Le polynôme minimal $\pi$ doit admettre toutes les valeurs propres comme racines, donc le polynôme $\prod (X - \lambda_i)$ divise $\pi$. Comme $\pi$ divise $\chi_A$, et qu'ils sont unitaires (au signe près pour $\chi$), ils sont égaux.

## 4. Diagonalisation

### 12. Théorème de Diagonalisation (Critères)

> [!important] Théorème 
> Les conditions suivantes sont équivalentes :
> 
> 1. $A$ est diagonalisable.
>     
> 2. $A$ possède $m$ vecteurs propres linéairement indépendants.
>     
> 3. La somme des multiplicités géométriques vaut $m$.
>     
> 4. Pour chaque valeur propre, la multiplicité géométrique égale la multiplicité algébrique.
>     

> [!example]- Démonstration 
> **(1** $\Rightarrow$ **2)** : Si $A$ est diagonalisable, $S^{-1}AS = D$. Les colonnes de $S$ sont des vecteurs propres (Lemme 3). Comme $S$ est inversible, ses colonnes sont indépendantes.
> 
> **(2** $\Rightarrow$ **3)** : Soit $m_i$ le nombre de vecteurs propres linéairement indépendants associés à $\lambda_i$ qu'on a trouvés. On a $\sum m_i = m$. Or $m_i \le \dim(E_{\lambda_i}) \le \text{mult alg}(\lambda_i)$. La somme des mult alg vaut $m$. Donc toutes les inégalités sont des égalités. Donc $\sum \dim(E_{\lambda_i}) = m$.
> 
> **(3** $\Rightarrow$ **4)** : On sait que $\dim(E_{\lambda_i}) \le \alpha_i$ et $\sum \alpha_i = m$. Si on avait une inégalité stricte pour un $i$, la somme serait $< m$, ce qui contredit l'hypothèse. Donc $\forall i, \dim(E_{\lambda_i}) = \alpha_i$.
> 
> **(4** $\Rightarrow$ **1)** : On recolle les bases de chaque espace propre $E_{\lambda_i}$. Comme la somme des dimensions vaut $m$, on obtient $m$ vecteurs. On montre qu'ils sont indépendants (car des vecteurs propres de VP distinctes sont indépendants). On forme la matrice $S$ avec ces vecteurs, elle est inversible et diagonalise $A$.

### 13. Condition suffisante (Corollaire 2)

> [!important] Corollaire 
> Si $A$ possède uniquement des valeurs propres simples, alors $A$ est diagonalisable.

> [!example]- Démonstration 
> Si toutes les multiplicités algébriques valent 1. Comme $1 \le \text{mult géo} \le \text{mult alg} = 1$, alors la multiplicité géométrique vaut toujours 1. La condition 4 du théorème précédent est vérifiée.