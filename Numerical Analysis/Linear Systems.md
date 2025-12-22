| Topic |
| :--- |
| [[#1. Direct Methods]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Gaussian Elimination]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Pivoting Strategies]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#LU Decomposition]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#The Inverse Matrix ($A^{-1}$)]] |
| [[#2. Error Analysis & Stability]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Matrix Norms & Condition Number]] |
| [[#3. Sparse Matrices]] |
| [[#Iterative Methods]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#General Framework (Fixed-Point Iteration)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Standard Decomposition]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Deriving the Matrix $G$ (Two Equivalent Forms)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#**A. Jacobi Method**]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#**B. Gauss-Seidel Method**]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Convergence Criteria]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#**Condition 1: Spectral Radius (Necessary & Sufficient)**]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#**Condition 2: Diagonal Dominance (Sufficient)**]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Summary Table]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Relaxation]] |

> [!ABSTRACT] Chapter Overview 
> This note covers the numerical resolution of linear systems $Ax=b$. It contrasts **direct methods** (Gaussian elimination, LU) with **iterative methods** (Jacobi, Gauss-Seidel), analyzes computational complexity, and discusses numerical stability through **conditioning**.

## 1. Direct Methods

Direct methods attempt to solve the system in a finite number of steps.

### Gaussian Elimination

The goal is to triangularize the matrix to solve the system via backward substitution.

**Algorithm Steps:**

1. **Triangularization:** Transform $A$ into an upper triangular matrix using elementary row operations.
    
2. **Backward Substitution:** Solve for variables starting from $x_n$ up to $x_1$.
    

> [!INFO] Complexity
> 
> - **Triangularization:** $\approx \frac{2}{3}n^3$ operations.
>     
> - **Backward Substitution:** $\approx n^2$ operations.
>     
> - **Total:** $O(n^3)$.
>     

### Pivoting Strategies

If a pivot element $a_{ii}$ is 0 or very close to 0, it causes numerical instability (division by zero or amplification of roundoff errors).

- **Partial Pivoting:** Swap rows to use the largest element in the current column (in absolute value) as the pivot.
    
- **Complete Pivoting:** Swap rows and columns to find the largest element in the remaining submatrix. Slower ($O(n^3)$ comparison overhead) but most stable.
    

### LU Decomposition

Factorize matrix $A$ into a lower triangular matrix $L$ and an upper triangular matrix $U$ such that $A = LU$.

**Workflow:**

1. Decompose $A \to L, U$ (Cost: $\frac{2}{3}n^3$).
    
2. Solve $Ly = b$ (Forward substitution, Cost: $n^2$).
    
3. Solve $Ux = y$ (Backward substitution, Cost: $n^2$).
    

> [!TIP] Why use LU? 
> While the initial cost is similar to Gaussian elimination, LU is superior if you need to solve $Ax=b$ for **multiple different vectors** $b$. You only pay the $\frac{2}{3}n^3$ cost once, and each new solution costs only $2n^2$.

### The Inverse Matrix ($A^{-1}$)

> [!DANGER] Critical Rule **Never** compute the inverse of a matrix explicitly!
> 
> - Computing $A^{-1}$ is computationally expensive ($\approx \frac{5}{3}n^3$ or more).
>     
> - It is numerically unstable.
>     
> - It destroys sparsity (inverse of a sparse matrix is usually dense).
>     
> - **Always** solve $Ax=b$ directly or use LU decomposition.
>     

## 2. Error Analysis & Stability

We must account for errors in the data and roundoff errors during computation.

### Matrix Norms & Condition Number

To measure errors, we use vector norms ($||x||$) and compatible matrix norms ($||A||$). Common norms: $L_1$ (max column sum), $L_2$ (spectral norm), $L_\infty$ (max row sum).

**The Condition Number (**$\kappa(A)$**)**

The condition number measures how sensitive the function (solving the linear system) is to changes in the input. It acts as an **error magnification factor**.

$$\kappa(A) = ||A|| \cdot ||A^{-1}||$$

**Key Properties:**

- **Magnification:** If input data has a relative error of $\epsilon$, the solution can have a relative error up to $\kappa(A) \cdot \epsilon$.
    
- **Range:** $\kappa(A) \ge 1$.
    
- **Interpretation:**
    
    - **Well-conditioned:** Stable. Small errors in data yield small errors in the solution.
        
    - **Ill-conditioned :** Unstable. Tiny errors (like roundoff or measurement noise) can result in massive errors in the final solution.
        
- **The Residual Trap:** For ill-conditioned systems, a small residual ($r = b - Ax \approx 0$) does **not** guarantee that the computed $x$ is close to the true solution.
    

> [!example]
> 
> Perturbation Bounds If we solve $(A + \delta A)x = b + \delta b$, the relative error on the solution $\delta x$ is bounded by:
> 
> $$\frac{||\delta x||}{||x||} \le \kappa(A) \frac{||\delta b||}{||b||} \quad \text{and} \quad \frac{||\delta x||}{||x + \delta x||} \le \kappa(A) \frac{||\delta A||}{||A||}$$
> 
> 
> 
> 
## 3. Sparse Matrices

A matrix is **sparse** if it contains mostly zeros (e.g., Internet adjacency matrix).

- **Operation:** Matrix-vector multiplication ($Av$) is very cheap for sparse matrices.
    

> [!failure] The Problem with Gaussian Elimination 
> Gaussian elimination causes **fill-in**:
>  zero elements become non-zero during row operations. A sparse matrix can become fully dense, destroying memory and speed advantages.

## Iterative Methods

### General Framework (Fixed-Point Iteration)

To solve $Ax = b$, we rewrite the system by introducing a matrix $Q$ (easy to invert) to create a fixed-point form.

We write $Ax = b$ as:

$$Qx = Qx - Ax + b$$$$Qx = (Q - A)x + b$$

This leads to the **iteration formula**:

$$x^{(k+1)} = Q^{-1}((Q-A)x^{(k)} + b)$$

This fits the general form $x^{(k+1)} = G x^{(k)} + c$, where:

- $G = Q^{-1}(Q-A) = I - Q^{-1}A$ is the **Iteration Matrix**.
    
- $c = Q^{-1}b$ is the constant vector.
    

### Standard Decomposition

For a matrix $A$, we define (Slide 89):

- $D$: Diagonal part.
    
- $L$: Strictly Lower triangular part.
    
- $U$: Strictly Upper triangular part.
    

$$A = L + D + U$$

### Deriving the Matrix $G$ (Two Equivalent Forms)

### **A. Jacobi Method**

- **Matrix Choice:** $Q = D$ (Diagonal only).
    

**Form 1: Using the remainder (Q-A)**

$$G_{Jac} = Q^{-1}(Q-A) = D^{-1}\left[ -(L+U) \right] = -D^{-1}(L+U)$$

**Form 2: Using the Identity (**$I - Q^{-1}A$**)**

$$G_{Jac} = I - D^{-1}A$$

_(Use this form if asked to compute "I minus D inverse A")_

### **B. Gauss-Seidel Method**

- **Matrix Choice:** $Q = L + D$ (Lower Triangle + Diagonal).
    

**Form 1: Using the remainder (Q-A)**

$$G_{GS} = Q^{-1}(Q-A) = (L+D)^{-1}\left[ -U \right] = -(L+D)^{-1}U$$

**Form 2: Using the Identity (**$I - Q^{-1}A$**)**

$$G_{GS} = I - (L+D)^{-1}A$$

_(Use this form to find eigenvalues generally)_

### Convergence Criteria

Convergence depends entirely on the properties of $G$. The error vector $e^{(k)} = x^{(k)} - x$ evolves as $e^{(k+1)} = G e^{(k)}$.

### **Condition 1: Spectral Radius (Necessary & Sufficient)**

The method converges for **any** initial vector $x^{(0)}$ if and only if the spectral radius of $G$ is strictly less than 1.

$$\rho(G) < 1$$

- $\rho(G) = \max_i |\lambda_i(G)|$ (The largest absolute eigenvalue of G).
    
- **To test convergence:** Calculate eigenvalues of $G$ by solving $\det(G - \lambda I) = 0$.
    

### **Condition 2: Diagonal Dominance (Sufficient)**

If $A$ is strictly diagonally dominant, then $\rho(G) < 1$ automatically for both methods.

$$|a_{ii}| > \sum_{j \neq i} |a_{ij}|$$

- _Note:_ If this fails, the method might still converge. You **must** check Condition 1.
    

### Summary Table

| Method           | Splitting Matrix $Q$ | Iteration Matrix $G$ | Practical Algorithm (Scalar)                 |
| ---------------- | -------------------- | -------------------- | -------------------------------------------- |
| **Jacobi**       | $D$                  | $I - D^{-1}A$        | Use $x^{(k)}$ to compute entire $x^{(k+1)}$. |
| **Gauss-Seidel** | $L+D$                | $I - (L+D)^{-1}A$    | Use new $x_j^{(k+1)}$ as soon as available.  |
### Relaxation

- Introduce a parameter $\omega$ to speed up convergence (Over-relaxation, $\omega > 1$) or stabilize divergence (Under-relaxation, $\omega < 1$).
    
- If $\omega = 1$, it is equivalent to Gauss-Seidel.