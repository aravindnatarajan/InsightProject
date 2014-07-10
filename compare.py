
pp = [(word.split())[0] for word in open("peter_pan_analysis.dat")]
aw = [(word.split())[0] for word in open("alice_analysis.dat")]
wo = [(word.split())[0] for word in open("wizard_analysis.dat")]
jb = [(word.split())[0] for word in open("analysis_jungle_book.dat")]
ag = [(word.split())[0] for word in open("analysis_anne.dat")]
bb = [(word.split())[0] for word in open("analysis_BB.dat")]

npp = [(word.split())[1] for word in open("peter_pan_analysis.dat")]
naw = [(word.split())[1] for word in open("alice_analysis.dat")]
nwo = [(word.split())[1] for word in open("wizard_analysis.dat")]
njb = [(word.split())[1] for word in open("analysis_jungle_book.dat")]
nag = [(word.split())[1] for word in open("analysis_anne.dat")]
nbb = [(word.split())[1] for word in open("analysis_BB.dat")]

theWord = "horse"
for i in range(0,len(pp)):
  if pp[i] == theWord:
    print "Peter",pp[i], npp[i]

for i in range(0,len(aw)):
  if aw[i] == theWord:
    print "Alice",aw[i], naw[i]

for i in range(0,len(wo)):
  if wo[i] == theWord:
    print "Wizard",wo[i], nwo[i]

for i in range(0,len(jb)):
  if jb[i] == theWord:
    print "Jungle Book", jb[i], njb[i]

for i in range(0,len(ag)):
  if ag[i] == theWord:
    print "Anne", ag[i], nag[i]

for i in range(0,len(bb)):
  if bb[i] == theWord:
    print "Black Beauty", bb[i], nbb[i]
