| Topic |
| :--- |
| [[#Definition]] |
| [[#Several know problems]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Graph coloring]] |
| [[#Methods]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#DPLL]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2. CDCL (Conflict-Driven Clause Learning)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#3. Resolution Method]] |

## Definition

SAT Solving is the concept of using a computer to determine whether a given boolean formula is satisfiable of not.
SAT Solving is a NP-Complete problem, meaning it can only be solved in exponential time in the worst case.

## Several know problems

### Graph coloring
Given a undirected graph, a graph coloring assigns a color to each node such that every adjacent nodes have a different colour. A graph coloring using at most K color is called a **K-coloring**. The graph coloring problem asks if such a k-coloring graph exists.

#### Applications
Compilers : How to assign $n$ variables to $m$ registers with $n>m$ ?
Just consider the n variables as
nodes, draw an edge between variables used at the same time, color with m colors

#### Theorem
Every finite planar graph can be colored using only 4 colors
**Variables:** Let $x_{i,c}$ be a boolean variable meaning "Node $i$ has color $c$".

**Clauses (Constraints):**

1. **At least one color per node:** For every node $i$: $(x_{i,1} \lor x_{i,2} \lor ... \lor x_{i,k})$
    
2. **At most one color per node:** For every node $i$ and distinct colors $c, c'$: $(\neg x_{i,c} \lor \neg x_{i,c'})$
    
3. **Adjacent nodes have different colors:** For every edge $(i, j)$ and every color $c$: $(\neg x_{i,c} \lor \neg x_{j,c})$


## Methods
### DPLL
#### Idea
Give a set of clauses S, we split on a variable than we use resolution rule 

##### Example

![[Pasted image 20251212173006.png]]

#### Algorithm

The function $DPLL(S)$ works as follows:

1. **Unit Propagation (Unit Clause Rule):** If $S$ contains a unit clause $\{l\}$ (a clause with only one literal), this literal _must_ be true.
    
    - Remove all clauses containing $l$ (they are now satisfied).
        
    - Remove $\neg l$ from all clauses where it appears (it cannot be true).
        
    - Repeat until no unit clauses remain.
        
2. **Pure Literal Elimination:** If a literal $l$ occurs in $S$ but its negation $\neg l$ does not, assign $l$ to true.
    
    - Remove all clauses containing $l$.
        
3. **Termination Check:**
    
    - If $S$ is empty (no clauses left): Return **SAT**.
        
    - If $S$ contains an empty clause ($\bot$): Return **UNSAT** (contradiction found).
        
4. **Splitting (Branching):**
    
    - Choose an unassigned variable $p$ (Heuristics like MOMs or DLIS are used here).
        
    - **Try:** `DPLL(S \cup \{p\})`.
        
    - **If that returns SAT:** Return **SAT**.
        
    - **Else:** Return `DPLL(S \cup \{\neg p\})`.
#### Pseudo Code
![[Pasted image 20251212175416.png]]
#### Instructions
-  **Propagate**: finds unit clauses repeatedly and pushes literals on the stack.
   Returns ⊥ iff unsatisfied clause
- **Decide**: chose one non assigned literal,pushes on stack. 
  Returns ⊥ iff no literal
- **Backtrack**: backtrack (pops literals from stack) until the last decision and adds the opposite literal as propagated

### 2. CDCL (Conflict-Driven Clause Learning)

#### Idea

CDCL is an extension of DPLL used in modern solvers. Instead of standard backtracking (going back one level), it learns from mistakes to prune the search space more effectively.

#### Key Differences from DPLL:

1. **Implication Graph:** CDCL maintains a graph that tracks _why_ a literal was set to true (which decision or propagation caused it).
    
2. **Conflict Analysis & Clause Learning:** When a conflict (empty clause) occurs, the solver analyzes the Implication Graph to find the root cause.
    
    - It generates a **Learned Clause** (or "Conflict Clause") that prevents this specific combination of assignments from happening again.
        
    - This clause is added to the formula $S$.
        
3. **Non-Chronological Backtracking (Backjumping):** Instead of backtracking to the immediate previous level, CDCL jumps back multiple levels to the highest decision level involved in the conflict.
    
4. **Restarts:** Occasionally, the solver forgets current assignments (but keeps learned clauses) and restarts to avoid getting stuck in hard regions of the search space.
    
#### Pseudo-Code
![[Pasted image 20251212175155.png]]
#### Instructions
- **Propagate**: finds unit clauses repeatedly
	and pushes literals on the stack. Returns ⊥
	iff unsatisfied clause
- **Decide**: choses one non assigned literal,
	pushes on stack. Returns ⊥ iff no literal
- **Analyse**: analyses the conflict from
	propagate, creates conflict clause, adds it in
	the set of clauses
- **Backtrack**: backtracks (pops literals from
	stack) until conflict clause is unit
### 3. Resolution Method

#### Idea

Instead of assigning values, we derive new clauses implied by the existing ones until we either find a contradiction or cannot derive anything new.

#### The Resolution Rule

Given two clauses $C_1$ and $C_2$ where $p \in C_1$ and $\neg p \in C_2$:

$$\frac{C \lor p, \quad D \lor \neg p}{C \lor D}$$

Here, $p$ and $\neg p$ are complementary literals. $C \lor D$ is called the **resolvent**.