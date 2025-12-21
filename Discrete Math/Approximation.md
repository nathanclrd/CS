| Topic                                                              |
| :----------------------------------------------------------------- |
| [[#1. Introduction & Context]]                                     |
| [[#2. Definition of Approximation (Order $n$)]]                    |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Interpretation]]                        |
| [[#3. Properties]]                                                 |
| [[#4. Taylor's Theorem (Existence)]]                               |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Special Case: Polynomials]]             |
| [[#5. Differentiability vs. Approximation]]                        |
| [[#6. Remainder Estimation (Error Analysis)]]                      |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Practical Application (Bounding)]]      |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Useful Formula (Lagrange Error Bound)]] |
| [[#7. Example: Cosine Function]]                                   |

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