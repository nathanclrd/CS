| Topic |
| :--- |
| [[#1. Syntax]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1.1 Alphabet]] |
| [[#Lexical]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#1.2 Well-Formed Formulas]] |
| [[#2. Semantics]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2.1 Interpretation (Truth Assignment)]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#2.2 Satisfaction and Validity]] |
| [[#3. Logical Equivalence]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#Key Equivalences (Toolbox)]] |
| [[#4. Normal Forms]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4.1 Definitions]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4.2 CNF and DNF]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#4.3 Algorithm to CNF]] |
| [[#5. Inference: The Resolution Method]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#5.1 The Resolution Rule]] |
| &nbsp;&nbsp;&nbsp;&nbsp;[[#5.2 Proof by Refutation Strategy]] |
| [[#6. Summary of Key Exercise Concepts]] |

## 1. Syntax 

Propositional logic is built from atomic propositions (atoms) and logical connectives.

### 1.1 Alphabet

- **Atoms (Variables):** Denoted by capital letters ($P, Q, R, p_1, p_2, \dots$). These represent statements that can be either True or False.
    
- **Connectives:**
    
    - $\neg$ (Negation, "not")
        
    - $\land$ (Conjunction, "and")
        
    - $\lor$ (Disjunction, "or")
        
    - $\Rightarrow$ (Implication, "if... then")
        
    - $\Leftrightarrow$ (Equivalence, "if and only if")
        
- **Punctuation:** Parentheses $($, $)$.

## Lexical
| **Term**                      | **Definition (Source: Handout 1)**                                                               | **Example**                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------- |
| **Atom** (Atomic Proposition) | The most basic building block. A variable that represents a statement that can be true or false. | $P, Q, R$                                           |
| **Literal**                   | An atom or the negation of an atom.                                                              | $P$ (positive literal), $\neg Q$ (negative literal) |
| **Connective**                | Logical symbols used to combine atoms into complex formulas.                                     | $\land, \lor, \neg, \Rightarrow, \Leftrightarrow$   |
| **Formula **                  | A Well-Formed Formula. A string of symbols constructed recursively from atoms and connectives.   | $(P \land Q) \Rightarrow R$                         |
| **Interpretation**            | A function that assigns a truth value (True/False) to every atom.                                | $I(P) = T, I(Q) = F$                                |
| **Model**                     | An interpretation that makes a specific formula evaluate to **True**.                            | If $I(P)=T$, then $I$ is a model of $P \lor Q$.     |
| **Tautology (Valid)**         | A formula that is True under **all** possible interpretations.                                   | $P \lor \neg P$                                     |
| **Unsatisfiable**             | A formula that is False under **all** possible interpretations (a contradiction).                | $P \land \neg P$                                    |
| **Clause**                    | A disjunction ("or") of literals. Used in CNF.                                                   | $P \lor \neg Q \lor R$                              |
| **Cube**                      | A conjunction ("and") of literals. Used in DNF.                                                  | $P \land \neg Q \land R$                            |

### 1.2 Well-Formed Formulas

A string of symbols is a WFF if it can be constructed using the following recursive rules:

1. Every atom is a WFF.
    
2. If $A$ and $B$ are WFFs, then $(\neg A)$, $(A \land B)$, $(A \lor B)$, $(A \Rightarrow B)$, and $(A \Leftrightarrow B)$ are WFFs.
    

## 2. Semantics

Semantics assigns truth values to formulas.

### 2.1 Interpretation (Truth Assignment)

An **interpretation** $I$ is a function that assigns a truth value $\{T, F\}$ (or $\{1, 0\}$ or $\{\top,\bot\}$) to every atom.

The truth value of a complex formula is determined by standard truth tables:

| $A$ | $B$ | $\lnot{A}$ | $A∧B$ | $A∨B$ | $A⇒B$ | $A⇔B$ |
| --- | --- | ---------- | ----- | ----- | ----- | ----- |
| F   | F   | T          | F     | F     | T     | T     |
| F   | T   | T          | F     | T     | T     | F     |
| T   | F   | F          | F     | T     | F     | F     |
| T   | T   | F          | T     | T     | T     | T     |

> [!NOTE] Implication Nuance Recall from **Tutorial 1**: $A \Rightarrow B$ is False **only** when $A$ is True and $B$ is False. If $A$ is False, the implication is always True.

### 2.2 Satisfaction and Validity

Let $A$ be a formula and $I$ be an interpretation.

- **Satisfaction (**$I(A)$**):** $I$ satisfies $A$ if $A$ evaluates to True under $I$. $I$ is called a **model** of $A$.
    
- **Satisfiable:** A formula is satisfiable if there exists at least one model $I$ such that $I(A)$.
    
- **Unsatisfiable (Contradiction):** A formula is unsatisfiable if for all interpretations $I$, $I(A)$ (always False).
    
- **Valid (Tautology):** A formula is valid ($\models A$) if for all interpretations $I$, $I(A)$ (always True).
    

> [!TIP] Exam Connection Checking if $A$ is a tautology is equivalent to checking if $\neg A$ is unsatisfiable. This is the foundation of **Refutation Proofs**.

## 3. Logical Equivalence

Two formulas $A$ and $B$ are logically equivalent ($A \equiv B$) if they share the exact same truth table.

### Key Equivalences (Toolbox)

You must memorize these for simplification exercises (refer to **Tutorial 1** & **2**).

|   |   |
|---|---|
|**Name**|**Equivalence**|
|**Double Negation**|$\neg \neg A \equiv A$|
|**Idempotence**|$A \land A \equiv A$<br><br>$A \lor A \equiv A$|
|**Commutativity**|$A \land B \equiv B \land A$<br><br>$A \lor B \equiv B \lor A$|
|**Associativity**|$(A \land B) \land C \equiv A \land (B \land C)$|
|**Distributivity**|$A \land (B \lor C) \equiv (A \land B) \lor (A \land C)$<br><br>$A \lor (B \land C) \equiv (A \lor B) \land (A \lor C)$|
|**De Morgan's Laws**|$\neg(A \land B) \equiv \neg A \lor \neg B$<br><br>$\neg(A \lor B) \equiv \neg A \land \neg B$|
|**Implication**|$A \Rightarrow B \equiv \neg A \lor B$|
|**Equivalence**|$A \Leftrightarrow B \equiv (A \Rightarrow B) \land (B \Rightarrow A)$|

## 4. Normal Forms

To apply inference methods like Resolution, we often require specific structures.

### 4.1 Definitions

- **Literal:** An atom ($P$) or its negation ($\neg P$).
    
- **Clause:** A disjunction of literals (e.g., $P \lor \neg Q \lor R$).
    
- **Cube (Term):** A conjunction of literals (e.g., $P \land \neg Q$).
    

### 4.2 CNF and DNF

- **Disjunctive Normal Form (DNF):** A disjunction of cubes.
    
    - Example: $(A \land B) \lor (\neg A \land C)$
        
- **Conjunctive Normal Form (CNF):** A conjunction of clauses.
    
    - Example: $(A \lor B) \land (\neg A \lor C \lor D)$
        
    - _Importance:_ **Resolution** operates heavily on CNF.
        

### 4.3 Algorithm to CNF

To convert any formula to CNF (as practiced in **Tutorial 2**):

1. **Eliminate** $\Leftrightarrow$ **and** $\Rightarrow$**:** Use $A \Rightarrow B \equiv \neg A \lor B$.
    
2. **Push** $\neg$ **inwards:** Use De Morgan's laws and Double Negation until negations only apply to atoms (NNF).
    
3. **Distribute** $\lor$ **over** $\land$**:** Apply distributivity to get the final CNF structure.
    

## 5. Inference: The Resolution Method

Resolution is a refutation-complete inference rule for formulas in CNF.

### 5.1 The Resolution Rule

$$\frac{l \lor A, \quad \neg l \lor B}{A \lor B}$$

Where $l$ is a literal and $\neg l$ is its complement. $A \lor B$ is called the **resolvent**.

### 5.2 Proof by Refutation Strategy

To prove that a Knowledge Base $KB$ entails a conclusion $\alpha$ ($KB \models \alpha$):

1. **Negate the goal:** Assume $\neg \alpha$.
    
2. **Form the set:** $S = KB \land \neg \alpha$.
    
3. **Convert to CNF:** Transform $S$ into a set of clauses.
    
4. **Apply Resolution:** Repeatedly resolve pairs of clauses containing complementary literals to derive new clauses.
    
5. **Check for Empty Clause (**$\square$**):**
    
    - If you derive $\square$, then $S$ is unsatisfiable (contradiction). This proves that the original entailment $KB \models \alpha$ is **Valid**.
        
    - If no new clauses can be generated and $\square$ is not found, $KB \not\models \alpha$.
        

## 6. Summary of Key Exercise Concepts

_From Tutorial Solutions_

- **Pigeonhole Principle:** A classic stress test for propositional logic. Encoding that $n+1$ pigeons fit into $n$ holes results in an unsatisfiable set of clauses. Proving this via Resolution is possible but can be lengthy.
    
- **Tseitin Transformation:** A method to convert formulas to CNF without the exponential blow-up in size that standard distributivity can cause. It introduces fresh variables for sub-formulas to maintain a linear size increase. The resulting formula is **equisatisfiable** (has a model iff the original does) but not strictly logically equivalent.