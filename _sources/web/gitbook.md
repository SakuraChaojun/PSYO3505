# Use Git book bulid your own page

Using gitbook or juypter book is a good way to present your work to others, and it doesn’t have to be complicated to do so. In this demo, I will still use ‘step by step’ methods to tell you how to build your own page by using Gitbook or jupter book. Before you do this, you need to know some basic git knowledge because both Gitbook and jupter book based on git.

```{tip} You can use DataCamp to learn more about Git.
```

## What is Gitbook

In my opinion, Gitbook is a modern document sharing platform that allows multiple users to collaborate to create, modified , and shared documents. like our textbook use ‘jupyter book’ but gitbook is more user-friendly, and you don’t need spend much time on set up.

### From create an account to your first page

First of all you need an account, this step is not difficult, I suggest you choose ‘sign in with’ Github. so that it is easy to access your page in later.


<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(5).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

After that, you can enter dashboard page.We can click the ‘Edits’ button to go back to the home page, then we click ‘New’ to select a ‘new page’. The default name of the new page is ‘untitled’ and we can easily change this information in later.

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(13).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

In this new page we can select the page template, for demo purposes we select the ‘basic guide’ template. Note that you can also import word, Markdown, and HTML files directly here but unfortunately ipynb files are not supported. This is also a major drawback of Gitbook.

```{warning} Gitbook not support .ipynb fies 
```

After planning the content, we first select how many Heading are needed and then add it. We click the ‘ ^ ’ button to edit heading.

Additionally, We can click the ' + ' in the blank to add the specific block. In common use, we can select Code block, image block or Math block to insert mathematical equations.(For details, you can see my last demo: Writing Math Equations in Jupyter)

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(17).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

Once the content is written, we need to click ‘Save’ in the lower left corner and ‘merge’. Otherwise, our pages won't be saved on Git.

Then we'll choose 'Share' and choose Public from Visibility. The link below is our book, and if you need a specific page you need add page slug (this will be explained below) and we have successfully published the first page so far.

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(25).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

### share and design
If you just want to share a specific page to others, you can click on the '... ' on page and select slug option, here is your link to this page, for example, my book link is https://sakurachaojun.gitbook.io/psyo3505/ and the slug here is 'my - first - page' so this page link is https://sakurachaojun.gitbook.io/psyo3505/my-first-page

We can put multiple pages together and create a group, such as Demo, assignment. we're going to home page select ‘new’ and this time we click ‘new group’ . We can just drag the page in to specific group

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(10).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

```{warning} If the page belongs to a group, the page link requires the group name followed by the slug name like https://sakurachaojun.gitbook.io/psyo3505/demo/latex. page latex belong to group demo 
```
Unfortunately, if you want to make the page fancy, like changing the font color, theme of the page, you have to pay for it. Of course, you don't have to pay to make some basic adjustments, such as changing the font family. These Settings can be found on the design.

## What is jupyter book

Our textbook is based on this platform. It should be noted that jupyter Book is community driven, means you are free to use all the features. but not user-friendly.

### Template book and your first page

```{note} Jupyter Book uses a command-line interface to perform a variety of actions
```

First you need to install Jupyter Book enter the following commands

```
pip install -U jupyter-book
```
Next, Create a repo on Github and pull to the local machine  
```
git pull origin main
```

we create a template book directly. 
```
jupyter-book create mynewbook/
```
In here 'mynewbook' is your path name for example this is my book:

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(20).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

After the creation, we need the Build page. If successful, you will see a '_build' folder generated
```
jupyter-book build mybookname/
```
We using Github Pages to publish our book, the best way is use ghp-import to help our push files to Github.

```
pip install ghp-import
```
then update the seeting for your Github pages site: 

>1. Use the gh-pages branch to host your website.<br>
>2. Choose root directory / if you’re building the book in it’s own repository. Choose /docs directory if you’re building documentation with jupyter-book.

<img src="https://raw.githubusercontent.com/SakuraChaojun/Neural-DataSci-Mybook/master/.gitbook/assets/image%20(21).png" alt="GitHub" title="GitHub,Social Coding" width="750px" height="430px" /> <br>

Then we call ghp push our pages to Github pages:

```
ghp-import -n -p -f _build/html
```
After a few minutes you can access you jupyter book and the link like |https://user.github.io/myonlinebook/| for example,my book link is: 
https://sakurachaojun.github.io/PSYO3505/notebooks.html

This is a template book. You need to know more details about Jupter book. like add group, change title or even add pages. Unlike Gitbook, all action based on command line. I will not elaborate on them in here because of space limitations. For more details, I recommend your read the documents.

Cheers!

## References and Documents:

[1][Gitbook document](https://docs.gitbook.com)<br>

[2][Books with Jupyter](https://jupyterbook.org/intro.html)<br>








