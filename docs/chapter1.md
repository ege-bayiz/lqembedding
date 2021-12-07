# Linear-Quadratic Embedding of Finite Dynamic Games #
## Analysis ##
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.js" integrity="sha384-9Nhn55MVVN0/4OFx7EE5kpFBPsEMZxKTCnA+4fqDmg12eCTqGi6+BB2LjY8brQxJ" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/contrib/auto-render.min.js" integrity="sha384-kWPLUVMOks5AQFrykwIup5lo0m3iMkkHrD0uJ4H5cjeGihAutqP0yW0J6dpFiVkI" crossorigin="anonymous" onload="renderMathInElement(document.body);"></script>

### Linear Embeddability of Games ###
Not all games are linear embeddable. In fact most games are not. In this chapter, we present a wide subclass of games which are not linearly embeddable.

Suppose that the our game has finite state space $$X$$ and suppose that $$a,b,c,d,e,\in X$$. Now suppose that this game has distinct actions $$u,v\in U = \prod_i U^i$$. Then if we have the following dynamics:

- $$a \xrightarrow^u b$$
- $$c \xrightarrow^u b$$
- $$a \xrightarrow^v d$$
- $$c \xrightarrow^v e$$

Then the game is not linearly embeddable since if it were, the first two dynamics above would yield

$$
\mathbf{A} f(a) - f(c) = 0  
$$

But from the last two dynamic we have

$$
\mathbf{A} f(a) - f(c) = f(d) - f(e)   
$$

Therefore $$f(d) = f(e)$$. Which contradicts our requirement of the embedding functions to be injective. In other words, if anywhere in the game there are two states which map to the same state under the same action, then if those states map to different states under different actions then the game is not linearly embeddable. notice that this immediately eliminates a large class of games.

Notice that despite the above result limits the number of linearly embeddable games significantly, our example game tic-tac-toe is still linearly embeddable. Indeed we can find a linear embedding for it. To do this we first enumerate each cell as follows:

![PCA plot of the semi-one-hot embedding](assets/images/TTT_embedding.png =256x256)


[Previous page](problem.md) | [Next page](results.md)

[Home](README.md)
