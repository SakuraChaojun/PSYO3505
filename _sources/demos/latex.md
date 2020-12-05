# Writing Math Equations in Jupyter

Jupyter allows you to write code, text, mathematical formula and pictures in the same document and others can easily understand your ideas and processes by share this document. You may not familiar how to insert math equations in notebook. So, in this demo, I am going to show how to write formula in Jupyter notebook.

## Latex Overview
First of all, we need change the cell type to markdown. Because latex is not a programming language.

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(1).png" alt="GitHub" title="GitHub,Social Coding" width="450px" height="100px" /> <br>

Once the changes are completed, we can try to enter our first formula. Y=a+bx by typing
```
$ y = a + b x $
```
$ y = a + b x $

You may have noticed that we need to use the \$ in above example, in fact everything between the \$ will be rendered as mathematical symbol.
How about this one: 

```
$$P(A \mid B) = \frac{ P(B \mid A) P(A) }{ P(B) }$$
```
$$P(A \mid B) = \frac{ P(B \mid A) P(A) }{ P(B) }$$

We are not concerned the specifics of Latex wrting rules in here, you may notice that there are two $$ are applying.

Latex gives us two modes in here: inline mode and display mode. In-line mode, also known as in-text mode, inlays formulas into regular text, along with text. The display mode is to separate the formulas into a single line and center them. By using single \$ means inline mode and $$ for display mode.

```
In here we using single character $ y = a + b x $ inlays into text
```
In here we using single character $ y = a + b x $ inlays into text

## Common mathematical symbols
Exponents and subscripts can be implemented with ^ and _ followed by the corresponding character like:

```
a_{1}
x^{2}
\sum_{i=1}^{N}
```
$a_{1}$ $x^{2}$ $\sum_{i=1}^{N}$

\sqrt for square root and  \sqrt[n] for n'th root
```
\sqrt[4]{x^2+y^2}
```
$\sqrt[4]{x^2+y^2}$

Vectors are usually variables with little arrows at the top. This can be obtained by  \vec. The commands \overrightarrow and \overleftarrow are useful for defining A vector from A to B. Such as:

```
\overrightarrow{AB}*\vec A
```
$\overrightarrow{AB}*\vec A$

For example, summation can be done using the \sum command, product operations can be done using \prod, and integration can be done using the \int command. Some examples are as follows

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(2).png" alt="GitHub" title="GitHub,Social Coding" width="550px" height="300px" /> <br>

Based on above details we can try to write a simple calculus formula

```
$$ f(x) = \sum_{i=0}^{N} \int_{a}^{b} g(t,i) \text{d}t \tag{a}$$
```
$$ f(x) = \sum_{i=0}^{N} \int_{a}^{b} g(t,i) \text{d}t \tag{a}$$

## Matrix

The command used to generate the matrix is as follows:
```
$$\begin{matrix}
...
\end{matrix}$$
```

... means LaTeX matrix commands, in which each line ends with \ and the elements of the matrix are separated by &. Examples are as follows:

```
$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix} \tag{3-1}
$$
```
$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix} \tag{3-1}
$$

The matrix shown above is not very beautiful, you can put brackets on the matrix

```
$$
\left [
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
\right ] \tag{3-3}
$$
```
$$
\left [
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
\right ] \tag{3-3}
$$

If you have too many matrix elements, you can use  \cdots ... \ddots ⋱ \vdots ⋮ And so on ellipsis to define the matrix

```
$$
\begin{bmatrix}
1 & 2 & \cdots & 4 \\
7 & 6 & \cdots & 5 \\
\vdots & \vdots & \ddots & \vdots \\
8 & 9 & \cdots & 10
\end{bmatrix} \tag{3-8}
$$
```
$$
\begin{bmatrix}
1 & 2 & \cdots & 4 \\
7 & 6 & \cdots & 5 \\
\vdots & \vdots & \ddots & \vdots \\
8 & 9 & \cdots & 10
\end{bmatrix} \tag{3-8}
$$

## Learn More

Latex also has many more methods and techniques, but I will not elaborate on them in here because of space limitations. You can download above pdf like ‘cheat sheet’ for latex.

In addition, I highly recommend a good online cooperative website 'overleaf' (Easy to use ,online and collaborative latex editor).  Unlike cocalc, this website focus on the academic paper (especially for science or engineering) writing. 

Cheers!


## References:
[1][LATEX Mathematical Symbols](https://www.caam.rice.edu/~heinken/latex/symbols.pdf) <br>
[2][Learn How to Write Markdown & LaTeX in The Jupyter Notebook](https://towardsdatascience.com/write-markdown-latex-in-the-jupyter-notebook-10985edb91fd) <br>
[3][Mathematical Python](https://www.math.ubc.ca/~pwalls/math-python/jupyter/latex/)




