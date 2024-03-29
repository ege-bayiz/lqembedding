# Linear-Quadratic Embedding of Finite Dynamic Games #
## Problem Statement ##
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.js" integrity="sha384-9Nhn55MVVN0/4OFx7EE5kpFBPsEMZxKTCnA+4fqDmg12eCTqGi6+BB2LjY8brQxJ" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>

In this project we wish to investigate solving finite dynamic games with smooth dynamic game solution methods by embedding the finite dynamic game into a smooth LQ feedback game. That is, given an $$N$$-player finite dynamic game with $$X$$, the set of game states, and $$U^i$$, a finite set of controls available to player $$i$$, we wish to find injective mappings $$f: X \rightarrow \mathbb{R}^n)$$, $$g^i: U^i \rightarrow \mathbb{R}^{m_i}$$ and some linear state transition rule

$$
    \hat{\mathbf{x}}_{t + 1} = \mathbf{A}_t\hat{\mathbf{x}}_t + \sum_i ^ N \mathbf{B}_t^i\hat{\mathbf{u}}_t^i \quad \textrm{where} \quad \hat{\mathbf{x}}_t \in \mathbb{R}^n,\; \hat{\mathbf{u}}_t \in \mathbb{R}^{m_i},
$$

such that

$$
    f(x_{t + 1}) = \mathbf{A}_t f(x_t) + \sum_i ^ N \mathbf{B}_t^ig^i(u_t^i).
$$

Note that if we assume $$X$$ is finite, such embedding is not always possible. If the above embedding is always possible, we refer to the finite game as **linear embeddable**, and we call the above embedding as a **linear embedding**. Given the game is linear embeddable, for it to also be **LQ embeddable**, the objective function should also be preserved under the embeddings given by $$f$$ and $$g$$. That is, we also need to find matrices $$Q^i_t$$ and $$R^{i,j}_t$$ such that if the player $$i$$'s one step cost function at state $$x$$ is $$c_i(t, x, u_1, \dots, u_N)$$ we have

$$
       c_i(t, x, u_1, \dots, u_N) = \frac{1}{2}\bigg(f(x)^\top Q_t^i f(x) + \sum_{j=1}^N g^j(u^j)^\top R_t^{ij} g^j(u^j)\bigg).
$$

Again, not all linear embeddable matrices are LQ embeddable. However, given that the game is LQ embeddable, and we manage to find an LQ embedding for it the resulting smooth dynamic LQ game can be solved using efficient LQ solution methods. However, the optimal player action output from the LQ solution will not necessarily correspond to an action in the finite action sets. Thus we also need to implement partitioning functions $$\hat g^i:\mathbb{R}^{m_i}\rightarrow U^i$$ which maps the action outputs resulting from the LQ problem back to discrete actions. For consistency we require $$\hat g^i(g^i(u)) = u $$ for all $$i \in [N]$$ and $$u \in U^i$$. Thus if the LQ solution for the optimal next action of player $$i$$ is $$\hat g^i (\hat\mathbf{u}^{i*})$$, the discrete action player $$i$$ takes will be $$\hat g^i (\hat\mathbf{u}^{i*})$$. Ideally, we want $$\hat g^i (\hat\mathbf{u}^{i*})$$ to be optimal, however, in general it may not be, and one of our tasks in this project is to characterize when it will be optimal. A pictorial representation of the entire decision making process can be seen in the following figure.

![Embedding diagram](assets/images/Embedding_Model.png)

In our project, we wish to investigate when a finite dynamic game can be LQ embedded. In the following chapter, we attempt to characterize LQ embeddability analytically. After this, we show that an example game, tic-tac-toe, is not LQ embeddable experimentally.

[Previous page](README.md) | [Next page](chapter1.md)

[Home](README.md)
