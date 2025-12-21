
| Topic                                                                |
| :------------------------------------------------------------------- |
| [[#1. Direct Methods]]                                               |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Gaussian Elimination]]                    |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Pivoting Strategies]]                     |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#LU Decomposition]]                        |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#The Inverse Matrix ($A^{-1}$)]]           |
| [[#2. Error Analysis & Stability]]                                   |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Matrix Norms & Condition Number]]         |
| [[#3. Sparse Matrices]]                                              |
| [[#4. Iterative Methods]]                                            |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Jacobi Method (Simultaneous Update)]]     |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Gauss-Seidel Method (Successive Update)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Convergence Criteria]]                    |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Relaxation]]                              |

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
    
    - **Well-conditioned (**$\kappa \approx 1$**):** Stable. Small errors in data yield small errors in the solution.
        
    - **Ill-conditioned (**$\kappa \gg 1$**):** Unstable. Tiny errors (like roundoff or measurement noise) can result in massive errors in the final solution.
        
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

- **Storage:** Storing all $n^2$ elements is wasteful. Use formats like **Compressed Column Storage (CCS)** (stores values, row indices, and column pointers).
    
- **Operation:** Matrix-vector multiplication ($Av$) is very cheap for sparse matrices.
    

> [!failure] The Problem with Gaussian Elimination 
> Gaussian elimination causes **fill-in**:
>  zero elements become non-zero during row operations. A sparse matrix can become fully dense, destroying memory and speed advantages.

## 4. Iterative Methods

Iterative methods are preferred for huge, sparse matrices because they avoid fill-in. Instead of solving the system directly, they guess a solution and refine it step-by-step.

**Conceptual Approach: Fixed-Point Iteration** We rewrite the system $Ax=b$ into the form $x = G(x)$. To do this, we split the matrix $A$ into a "simple" part $Q$ (easy to invert) and the rest ($Q-A$).

$$Ax = b \implies Qx = (Q-A)x + b$$

This gives the iteration formula:

$$x^{(k+1)} = Q^{-1}((Q-A)x^{(k)} + b)$$

### Jacobi Method (Simultaneous Update)

**Logic:** We isolate $x_i$ in the $i$-th equation. To solve for $x_i^{(k+1)}$, we use the "old" values $x^{(k)}$ for _all_ other variables. All variables are updated simultaneously at the end of the step.

- **Matrix Choice:** $Q = D$ (Diagonal of A).
    
- **Explicit Update:**
    
    $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$$
- **Pros:** Highly parallelizable (each $x_i$ can be computed independently).
    

### Gauss-Seidel Method (Successive Update)

**Logic:** Like Jacobi, we isolate $x_i$ in the $i$-th equation. However, we use the **most recent** information available. For variables $x_1$ through $x_{i-1}$, we have already computed their new values for step $k+1$, so we use them immediately.

- **Matrix Choice:** $Q = L+D$ (Lower triangle of A).
    
- **Explicit Update:**
    
    $$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \underbrace{\sum_{j < i} a_{ij} x_j^{(k+1)}}_{\text{New values}} - \underbrace{\sum_{j > i} a_{ij} x_j^{(k)}}_{\text{Old values}} \right)$$
- **Pros:** Generally converges faster than Jacobi because information propagates immediately.
    

### Convergence Criteria

The error $e^{(k)} = x^{(k)} - x$ evolves as $e^{(k+1)} = (I - Q^{-1}A)e^{(k)}$.

> [!check]
> 
> Convergence Conditions
> 
> 1. **Necessary & Sufficient:** The method converges if and only if the **spectral radius** $\rho(I - Q^{-1}A) < 1$ (all eigenvalues have magnitude < 1).
>     
> 2. **Sufficient Condition:** If $A$ is **strictly diagonally dominant** (the absolute value of the diagonal element is greater than the sum of absolute values of other row elements), both Jacobi and Gauss-Seidel converge.
>     

### Relaxation

- Introduce a parameter $\omega$ to speed up convergence (Over-relaxation, $\omega > 1$) or stabilize divergence (Under-relaxation, $\omega < 1$).
    
- If $\omega = 1$, it is equivalent to Gauss-Seidel.