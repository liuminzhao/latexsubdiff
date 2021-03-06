#! /usr/bin/env python

__author__ = 'liuminzhao'

import os, os.path, subprocess, tempfile, glob, re, sys

def flatten(infile, outfile):
    f = open(infile, 'r')
    f_text = f.read()
    sub_files = re.findall("subfile\\{(.*)}", f_text)
    b = open(outfile, 'w')
    f.seek(0)
    i = 0
    for row in f.readlines():
        row = row.strip()
        if not row.startswith('\\subfile'):
            b.writelines(row + '\n')
        else:
            f2 = open(sub_files[i]+'.tex', 'r')
            for line in f2.readlines():
                if not line.startswith('\\documentclass') and not line.startswith('\\begin{document}') and \
                    not line.startswith('\\end{document') and not line.startswith('%'):
                    b.writelines(line + '\n')
            i += 1
            f2.close()
    f.close()
    b.close()

def CheckoutFlatten(commit, filedir, fileloc, output):
    owd = os.getcwd()
    os.system('git clone . ' + filedir)
    os.chdir(filedir)
    os.system('git checkout ' + commit)
    flatten(fileloc, output)
    os.chdir(owd)

def CopyFlatten(filedir, fileloc, output):
    owd = os.getcwd()
    os.system('cp -R * ' + filedir)
    os.chdir(filedir)
    flatten(fileloc, output)
    os.chdir(owd)

def cleanAllNonePDF():
  ''' Delete all diff files that are not a .pdf file '''
  for filename in glob.glob('diff*') :
    if not "pdf" in filename and not "tex" in filename:
      os.remove(filename)

if len(sys.argv) == 4:
    old_commit, new_commit, fileloc = sys.argv[1:]
elif len(sys.argv) == 3:
    old_commit, fileloc = sys.argv[1:]
elif len(sys.argv) == 2:
    old_commit = 'HEAD'
    fileloc = sys.argv[1]
else:
    sys.exit('No file to be compared!')

old_dir = tempfile.mkdtemp()
new_dir = tempfile.mkdtemp()
CheckoutFlatten(old_commit, old_dir, fileloc, 'old.tex')
if len(sys.argv) == 4:
    CheckoutFlatten(new_commit, new_dir, fileloc, 'new.tex')
else:
    CopyFlatten(new_dir, fileloc, 'new.tex')
os.system('latexdiff --flatten ' + old_dir+ '/old.tex ' +  new_dir +'/new.tex > diff.tex')
os.system('pdflatex --nonestopmode diff.tex')
os.system('bibtex diff.aux')
os.system('pdflatex --nonestopmode diff.tex')
os.system('pdflatex --nonestopmode diff.tex')
os.system('open diff.pdf')
cleanAllNonePDF()
