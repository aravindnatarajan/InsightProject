
files = [
"analysis_gift_magi.dat",
"analysis_anne_green_gables.dat",
"analysis_AliceWonderland.dat",
"analysis_BlackBeauty.dat",
"analysis_jungle_book.dat",
"analysis_wizard_of_oz.dat",
"analysis_peter_pan.dat",
"analysis_jack_jill.dat",
"analysis_hiawatha.dat",
"analysis_arabian_nights.dat",
"analysis_heidi.dat"]

myFile = files[0]
words = [(word.split())[0] for word in open(myFile)]
theWord = words[0]

i = 1
otherWords = [(word.split())[0] for word in open(files[i])]
otherCount = [int((word.split())[1]) for word in open(files[i])]

for i in range(0,len(otherWords)):
  if otherWords[i] == theWord:
    print otherWords[i]
