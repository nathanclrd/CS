| Topic |
| :--- |
| [[#1. Introduction & Context]] |
| [[#2. Definition of Approximation (Order $n$)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Interpretation]] |
| [[#3. Properties]] |
| [[#4. Taylor's Theorem (Existence)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Special Case: Polynomials]] |
| [[#5. Differentiability vs. Approximation]] |
| [[#6. Remainder Estimation (Error Analysis)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Practical Application (Bounding)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Useful Formula (Lagrange Error Bound)]] |
| [[#7. Example: Cosine Function]] |
| [[#1. Approximation Polynomiale]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Unicité de l'approximation]] |

Tags: #math #analysis #polynomials #taylor
# Linear Algebra: Approximation



## 1. Introduction & Context

The goal is to approximate the values of a function $f: A \to \mathbb{R}$ in the neighborhood of a point $a$ using polynomials. While linear approximation (tangents) is useful locally, complex curves (like sine) require higher-degree polynomials for better precision.

> [!INFO] Core Concept
> 
> We seek a polynomial $P$ such that the difference between $f(x)$ and $P(x)$ becomes negligible faster than $(x-a)^n$ as $x$ approaches $a$.

## 2. Definition of Approximation (Order $n$)

Let $f$ be a function defined on an interval containing $a$. A polynomial $P \in \mathbb{R}_n[X]$ (degree $\le n$) is an **approximation of** $f$ **at order** $n$ **at point** $a$ if:

$$\lim_{x \to a} \frac{f(x) - P(x)}{(x - a)^n} = 0$$

### Interpretation

- We write $f(x) = P(x) + r(x)$, where the remainder $r(x)$ is $o((x-a)^n)$.
    
- This means the error $|r(x)|$ is very small relative to the distance $|x-a|^n$.
    
- Since $|x-a|^n$ shrinks rapidly for $|x-a| < 1$, a higher $n$ generally yields a better local approximation.
    

## 3. Properties

> [!ABSTRACT] **Proposition: Uniqueness & Consistency**
> 
> 1. **Uniqueness:** If an approximation of order $n$ exists, it is **unique**.
>     
> 2. **Consistency:** If $f$ has an approximation of order $n$, it automatically has an approximation for any order $i \le n$.
>     

**Note on Order 0 and 1:**

- Approximation at **order 0** $\iff f$ is **continuous** at $a$.
    
- Approximation at **order 1** $\iff f$ is **differentiable** at $a$ (Tangent line).
    

## 4. Taylor's Theorem (Existence)

How do we find this polynomial? If the function is sufficiently smooth, we use derivatives.

> [!thm] Theorem: Taylor Polynomial
> 
> If $f$ is $n$ times differentiable on an interval $I$ containing $a$, then the approximation of order $n$ exists and is given by:
> 
> $$P_n(X) = \sum_{i=0}^{n} \frac{(D^{i}f)(a)}{i!} (X - a)^i$$
> 
> _Where_ $(D^{i}f)(a))$ _denotes the_ $i$_-th derivative of_ $f$ _evaluated at_ $a$_._

### Special Case: Polynomials

If $f$ is itself a polynomial of degree $d$:

- **If** $n < d$**:** The approximation is the truncated Taylor series.
    
- **If** $n \ge d$**:** The approximation is $f$ itself (exact fit, remainder is 0).
    

## 5. Differentiability vs. Approximation

> [!WARNING] Crucial Distinction
> 
> Differentiability ($n$ times) $\implies$ Existence of Approximation (order $n$).
> 
> However, the reciprocal is **FALSE** for $n \ge 2$.

Counter-Example:

Consider the function:

$$f(x) = \begin{cases} x^3 \sin(1/x) & \text{if } x \neq 0 \\ 0 & \text{if } x = 0 \end{cases}$$

- **Approximation:** It admits $P(x) = 0$ as an approximation of **order 2** at $a=0$ (the limit condition holds).
    
- **Differentiability:** It is **not** two times differentiable at 0. (The first derivative exists, but the second derivative limit does not defined).
    

## 6. Remainder Estimation (Error Analysis)

To trust an approximation, we must bound the error $r_n(x) = f(x) - P_n(x)$.

> [!thm] Theorem: Taylor-Lagrange
> 
> Let $f$ be $n+1$ times differentiable on an interval $I$. For any distinct $x, a \in I$, there exists a real number $u$ strictly between $a$ and $x$ such that:
> 
> $$r_n(x) = \frac{(D^{n+1}f)(u)}{(n+1)!} (x - a)^{n+1}$$

Using the fact that 
$r_n : A \to \mathbb{R}, x \mapsto f(x) - P_n(X)$ is
$$lim_{x\to a} \frac{r_n(x)}{(x-a)^n} = 0$$

we can deduce

$$|r_n(x)| \leq c|x-a|^n$$
or even
$$|r_n(x)| \leq c|x-a|^{n+1}$$
when f is sufficently differentiable
### Practical Application (Bounding)

If we can bound the $(n+1)$-th derivative by a constant $M$ (i.e., $|(D^{n+1})(t)| \le M$ for all $t$ between $a$ and $x$), then:

$$|r_n(x)| \le \frac{M}{(n+1)!} |x - a|^{n+1}$$
### Useful Formula (Lagrange Error Bound)

In practice, we use the following inequality to frame the error $R(x)$:

$$\frac{m_{n+1}}{(n+1)!} |x-a|^{n+1} \quad \le \quad |R(x)| \quad \le \quad \frac{M_{n+1}}{(n+1)!} |x-a|^{n+1}$$

**Where:**

- **$a$**: The center of expansion.
    
- **$m_{n+1}$ / $M_{n+1}$**: The **minimum** and **maximum** values of the derivative $|f^{(n+1)}(u)|$ on the interval between $a$ and $x$.
    
- **$|x-a|$**: The **distance from the center**, chosen based on the context:
    
    - **For a specific point estimation:** Use the **Fixed Distance** (simply calculate $|x_{target} - a|$).
        
    - **For an interval upper bound (Majoration):** Use the **Maximum Radius** (the distance of the point in the interval _farthest_ from $a$).
        
    - **For an interval lower bound (Minoration):** Use the **Minimum Radius** (the distance of the point in the interval _closest_ to $a$; use 0 if $a$ is inside the interval).

## 7. Example: Cosine Function

Goal: Approximate $f(x) = \cos(x)$ at $a = \frac{\pi}{2}$.

Derivatives:

1. $f'(x) = -\sin(x) \implies -1$  
    
2. $f''(x) = -\cos(x) \implies 0$  
    
3. $f'''(x) = \sin(x) \implies 1$  
    
4. $f^{(4)}(x) = \cos(x) \implies 0$  
    

**Approximations:**

- **Order 1:** $-(x - \frac{\pi}{2})$  
    
- **Order 3:** $-(x - \frac{\pi}{2}) + \frac{1}{6}(x - \frac{\pi}{2})^3$  
    
- **Order 5:** $-(x - \frac{\pi}{2}) + \frac{1}{6}(x - \frac{\pi}{2})^3 - \frac{1}{120}(x - \frac{\pi}{2})^5$  
    

Error at Order 5:

Using Taylor-Lagrange, since derivatives of cosine are always $\le 1$ in magnitude:

$$|r_5(x)| \le \frac{1}{6!} \left| x - \frac{\pi}{2} \right|^6$$
# 8. Démonstrations : Outils d'Analyse

Ce document recense l'unique démonstration formelle du chapitre **Outils d'Analyse** tirée du cours _Mathématiques pour l'informatique 2_.

> [!INFO] Légende
> 
> - $f$ désigne une fonction de $A \subseteq \mathbb{R}$ vers $\mathbb{R}$.
>     
> - $P$ désigne un polynôme.
>     
> - La démonstration est masquée par défaut. **Cliquez sur la flèche pour la révéler.**
>     

## 1. Approximation Polynomiale

### Unicité de l'approximation

> [!important] Proposition
> 
> 1. Si $f$ admet une approximation polynomiale à l'ordre $n$ en $a$, alors celle-ci est **unique**.
>     
> 2. Si $f$ admet une approximation polynomiale à l'ordre $n$ en $a$, alors $f$ admet une approximation à l'ordre $i$ en $a$ pour tout $i \le n$.
>     

> [!example]- Démonstration **Point 1 : Unicité** Supposons que $P \in \mathbb{R}_n[X]$ est une approximation à l'ordre $n$ en $a$. On a $\lim_{x \to a} \frac{f(x) - P(x)}{(x-a)^n} = 0$.
> 
> Cela implique que pour tout $i < n$ :
> 
> $$\lim_{x \to a} \frac{f(x) - P(x)}{(x-a)^i} = \lim_{x \to a} \left( \frac{f(x) - P(x)}{(x-a)^n} \cdot (x-a)^{n-i} \right) = 0 \cdot 0 = 0$$
> 
> Écrivons $P$ dans la base $((X-a)^n, \dots, 1)$ : $P = \sum_{j=0}^n c_j (X-a)^j$. Pour montrer l'unicité de $P$, il suffit de montrer l'unicité des coefficients $c_j$.
> 
> Procédons de proche en proche pour $i$ allant de 0 à $n$.
> 
> Pour $i=0$ :
> 
> $$\lim_{x \to a} (f(x) - P(x)) = 0 \implies \lim_{x \to a} (f(x) - c_0) = 0 \implies c_0 = \lim_{x \to a} f(x)$$
> 
> $c_0$ est déterminé de manière unique par $f$.
> 
> Supposons $c_0, \dots, c_{i-1}$ déterminés de manière unique. On sait que $\lim_{x \to a} \frac{f(x) - P(x)}{(x-a)^i} = 0$. Or $P(x) = \sum_{j=0}^{i-1} c_j(x-a)^j + c_i(x-a)^i + \sum_{j=i+1}^n c_j(x-a)^j$.
> 
> Donc :
> 
> $$\frac{f(x) - P(x)}{(x-a)^i} = \frac{f(x) - \sum_{j=0}^{i-1} c_j(x-a)^j}{(x-a)^i} - c_i - \sum_{j=i+1}^n c_j(x-a)^{j-i}$$
> 
> En passant à la limite $x \to a$, les termes de la somme pour $j > i$ tendent vers 0 (car $(x-a)^{j-i} \to 0$). On obtient :
> 
> $$0 = \lim_{x \to a} \frac{f(x) - \sum_{j=0}^{i-1} c_j(x-a)^j}{(x-a)^i} - c_i$$
> 
> D'où :
> 
> $$c_i = \lim_{x \to a} \frac{f(x) - \sum_{j=0}^{i-1} c_j(x-a)^j}{(x-a)^i}$$
> 
> Le coefficient $c_i$ est donc déterminé de manière unique par $f$ et les coefficients précédents (déjà uniques).
> 
> **Point 2 : Existence aux ordres inférieurs** On a vu dans la preuve précédente que si $\lim_{x \to a} \frac{f(x) - P(x)}{(x-a)^n} = 0$, alors pour tout $i \le n$, $\lim_{x \to a} \frac{f(x) - P(x)}{(x-a)^i} = 0$.
> 
> Considérons le polynôme tronqué $P_i(X) = \sum_{j=0}^i c_j(X-a)^j$. On a :
> 
> $$\frac{f(x) - P_i(x)}{(x-a)^i} = \frac{f(x) - P(x)}{(x-a)^i} + \frac{P(x) - P_i(x)}{(x-a)^i}$$
> 
> Le premier terme tend vers 0. Le second terme est $\frac{\sum_{j=i+1}^n c_j(x-a)^j}{(x-a)^i} = \sum_{j=i+1}^n c_j(x-a)^{j-i}$, qui tend aussi vers 0 quand $x \to a$.
> 
> Donc $P_i$ est bien une approximation de $f$ à l'ordre $i$.