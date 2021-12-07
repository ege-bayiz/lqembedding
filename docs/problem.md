# Linear-Quadratic Embedding of Finite Dynamic Games #
## Problem Statement ##
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.js" integrity="sha384-9Nhn55MVVN0/4OFx7EE5kpFBPsEMZxKTCnA+4fqDmg12eCTqGi6+BB2LjY8brQxJ" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>

In this project we wish to investigate solving finite dynamic games with smooth dynamic game solution methods by embedding the finite dynamic game into a smooth LQ feedback game. That is, given an $N$-player finite dynamic game with \\(X)\\, the set of game states, and $U^i$, a finite set of controls available to player $i$, we wish to find injective mappings \\(f: X \rightarrow \mathbb{R}^n)\\, \\(g^i: U^i \rightarrow \mathbb{R}^{m_i}$ and some linear state transition rule

$$
    \hat{\mathbf{x}}_{t + 1} = \mathbf{A}_t\hat{\mathbf{x}}_t + \sum_i ^ N \mathbf{B}_t^i\hat{\mathbf{u}}_t^i \quad \textrm{where} \quad \hat{\mathbf{x}}_t \in \mathbb{R}^n,\; \hat{\mathbf{u}}_t \in \mathbb{R}^{m_i},
$$

such that

$$
    f(x_{t + 1}) = \mathbf{A}_t f(x_t) + \sum_i ^ N \mathbf{B}_t^ig^i(u_t^i).
$$
