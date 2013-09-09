notes
=====

Repository for notes taken from Queen's University.

##How-to:
Edit the source .rst files with rst + mathjax syntax

generate the html pages with
```bash
sphinx-build -b html ./ ./gh-pages
```

this will generate all the html in `gh-pages/` submodule. 

then, commit stuff.
```
cd gh-pages
git add --all ./
git commit -m "Added a note about blah"
git push
cd ..
git add gh-pages *.rst
git commit -m "Added a note about blah"
git push
```

##Todo:
automate the above git stuff with a pre
