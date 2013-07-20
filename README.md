latexsubdiff
============

Git LaTeX Diff allowing Subfiles

Basically borrowed related idea from <https://bitbucket.org/paulhiemstra/scm-latexdiff>

Also there is a nice post about latexdiff in git : <http://tex.stackexchange.com/questions/1325/using-latexdiff-with-git/64387#64387>

# Usage #

	./latexsubdiff.py oldcommit newcommit texfile

Can compare un-committed file too:

	./latexsubdiff.py oldcommit texfile

with HEAD:

	./latexsubdiff.py texfile

# Bibtex #

Please copy the `bib` file to project root directory.

# Claim #

This is an unclean work by a Python beginner. So please help to improve it.

# TODO #

- [ ] use `subprogress` instead of `os`
- [ ] clean output from `os`
- [ ] use `argsparse` instead of `sys.argv`
