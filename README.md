latexsubdiff
============

Git LaTeX Diff allowing Subfiles

Basically borrowed related idea from <https://bitbucket.org/paulhiemstra/scm-latexdiff>

Also there is a nice post about latexdiff in git : <http://tex.stackexchange.com/questions/1325/using-latexdiff-with-git/64387#64387>

# Usage #

	./latexsubdiff oldcommit newcommit texfile

Can compare un-committed file too:

	./latexsubdiff oldcommit texfile

with HEAD:

	./latexsubdiff texfile
