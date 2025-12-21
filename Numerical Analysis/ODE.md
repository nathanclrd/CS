| Topic |
| :--- |
| [[#Table of Contents]] |
| [[#1. Introduction to Initial Value Problems (IVP)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Definition]] |
| [[#2. Stability of Differential Equations]] |
| [[#3. Explicit Euler Method]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Formula]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Error Analysis]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Stability Region]] |
| [[#4. Higher-Order Taylor Methods]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Second-Order Method]] |
| [[#5. Implicit Euler Method]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Formula]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Characteristics]] |
| [[#6. Runge-Kutta Methods]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Concept]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Classical Runge-Kutta 4 (RK4)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Summary of RK]] |

**Tags:** #NumericalAnalysis #ODE #Math #Simulation

**Course:** Numerical Analysis 2025

**Lecturer:** Quentin Louveaux
## Table of Contents

 [[#1. Introduction to Initial Value Problems (IVP)]]
    
 [[#2. Stability of Differential Equations]]
    
 [[#3. Explicit Euler Method]]
    
 [[#4. Higher-Order Taylor Methods]]
    
 [[#5. Implicit Euler Method]]
    
[[#6. Runge-Kutta Methods]]
## 1. Introduction to Initial Value Problems (IVP)

### Definition

The goal is to find a function $x(t)$ starting from $t_0$ and increasing. An **Initial Value Problem** is defined as an ordinary differential equation paired with an initial condition:

$$\begin{cases} x'(t) = f(x(t), t) \\ x(t_0) = x_0 \end{cases}$$

- **Without initial condition:** The solution is determined only up to a constant.
    
- **With initial condition:** The solution is determined uniquely.
    

## 2. Stability of Differential Equations

Before choosing a numerical method, one must understand the stability of the equation itself. Stability concerns what a small perturbation in the initial condition implies for the solution.

> [!abstract] **Definition: Local Stability** A differential equation $x'(t) = f(x(t), t)$ is:
> 
> - **Stable** locally at $(x(t), t)$ if the Jacobian $J(x(t), t) = \frac{\partial f}{\partial x} < 0$.
>     
> - **Unstable** locally if the Jacobian $J(x(t), t) > 0$.
>     

If an equation is unstable, small errors (like those introduced by numerical discretization) will be amplified during iterations, making it nearly impossible to solve numerically.

## 3. Explicit Euler Method

This is the simplest method, based on discretizing time ($t_0, t_1, t_2...$) and truncating the Taylor expansion at the first order.

### Formula

For a step size $h = t_{i+1} - t_i$:

$$\overline{x}_{i+1} = \overline{x}_i + h f(\overline{x}_i, t_i)$$
![[Explicit-Euler-Example.png]]
### Error Analysis

The global error ($EG_i$) at step $i$ decomposes into the previous error propagated and the new local error ($EL_i$):

$$EG_i = (1 + hJ_i)EG_{i-1} + EL_i$$

- **Local Error (**$EL_i$**):** $-\frac{h^2}{2}x''(\xi_i)$ (Proportional to $h^2$).
    
- **Jacobian (**$J_i$**):** $\frac{\partial f}{\partial x}(\zeta_i, t_i)$.
    

### Stability Region

For the error not to grow, we generally need $|1 + hJ_i| < 1$.

> [!fail] **Stability Constraint** For a stable equation ($J < 0$), the Explicit Euler method is stable only if the step size $h$ satisfies:
> 
> $$-2 < hJ_i < 0$$

If the equation is very stable (large negative $J$), $h$ must be chosen to be very small, which is computationally expensive (a characteristic of **stiff equations**).

## 4. Higher-Order Taylor Methods

To improve accuracy, one can use higher-order terms of the Taylor expansion rather than truncating after the first derivative.

### Second-Order Method

$$\overline{x}_{i+1} = \overline{x}_i + h f(\overline{x}_i, t_i) + \frac{h^2}{2} \left( \frac{\partial f}{\partial x}(\overline{x}_i, t_i)f(\overline{x}_i, t_i) + \frac{\partial f}{\partial t}(\overline{x}_i, t_i) \right)$$

> [!warning] **Drawbacks**
> 
> - Requires knowledge of the analytic form of $f$.
>     
> - Involves heavy symbolic differentiation (calculating derivatives of $f$ with respect to $x$ and $t$).
>     
> - In practice, only the first-order method (Euler) is used directly in this form.
>     

## 5. Implicit Euler Method

This method extends Euler's approach but writes the Taylor expansion around $t_{i+1}$ instead of $t_i$.

### Formula

$$\overline{x}_{i+1} = \overline{x}_i + h f(\overline{x}_{i+1}, t_{i+1})$$

### Characteristics

- **Implicit:** The unknown $\overline{x}_{i+1}$ appears on both sides. A nonlinear equation must be solved at each step (e.g., using Newton's method).
    
- **Unconditional Stability:** The method is stable if $|\frac{1}{1-hJ_i}| < 1$. For a stable equation ($J<0$), this holds for **any** step size $h$.
    
- **Usage:** Very convenient for stiff equations where Explicit Euler requires impractically small steps.
    

## 6. Runge-Kutta Methods

**Runge-Kutta** methods aim to achieve the accuracy of higher-order Taylor methods by numerically approximating the derivatives, avoiding symbolic differentiation.

### Concept

They evaluate the function $f$ at multiple points to capture the slope's behavior.

- **RK2 (Second Order):** Copies Taylor expansion up to order 2.
    
- **RK4 (Fourth Order):** Copies Taylor expansion up to order 4 with an error term of $\mathcal{O}(h^5)$.
    

### Classical Runge-Kutta 4 (RK4)

> [!example] **RK4 Algorithm**
> 
> $$\overline{x}_{i+1} = \overline{x}_i + \frac{1}{6}(K_1 + K_2 + K_3 + K_4)$$
> 
> Where the slopes $K$ are defined as:
> 
> 1. $K_1 = h f(\overline{x}_i, t_i)$
>     
> 2. $K_2 = h f(\overline{x}_i + \frac{1}{2}K_1, t_i + \frac{1}{2}h)$
>     
> 3. $K_3 = h f(\overline{x}_i + \frac{1}{2}K_2, t_i + \frac{1}{2}h)$
>     
> 4. $K_4 = h f(\overline{x}_i + K_3, t_i + h)$
>     
![[Runge-kutta-example.png]]
### Summary of RK

- Numerical approximation of Taylor expansion.
    
- Flexibility in choosing coefficients (weights).
    
- Requires multiple evaluations of $f$ (4 evaluations for RK4), which can be costly if $f$ is expensive to compute.