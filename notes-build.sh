#!/bin/bash
sphinx-build -b html $1 $1/gh-pages
touch $1/gh-pages/index.html