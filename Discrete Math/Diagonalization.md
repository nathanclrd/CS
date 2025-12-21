| Topic |
| :--- |
| [[#1. Core Definitions]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Eigenvalues & Eigenvectors]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Multiplicities]] |
| [[#2. Key Polynomials]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Characteristic Polynomial]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Minimal Polynomial ($\pi_A$)]] |
| [[#3. Theoretical Properties]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Similar Matrices]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Polynomial Lemma]] |
| [[#4. Criteria for Diagonalization]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Corollaries & Applications]] |
| [[#5. Practical Algorithm]] |
| [[#6. Solved Example: Computing the Basis]] |

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