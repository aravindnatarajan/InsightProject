import os
files = [file[:-1] for file in open("list")]
for file in files: 
  comm = "python reanalyze.py " + "analysis/"+file+" > "+"reanalysis/re"+file
  os.system(comm)
