
files = [
"analysis/analysis_AliceWonderland.dat",
"analysis/analysis_heidi.dat",
"analysis/analysis_pinocchio.dat",
"analysis/analysis_BlackBeauty.dat",
"analysis/analysis_hiawatha.dat",
"analysis/analysis_rainbow_rose.dat",
"analysis/analysis_anne_green_gables.dat",
"analysis/analysis_jack_jill.dat",
"analysis/analysis_secret_garden.dat",
"analysis/analysis_arabian_nights.dat",
"analysis/analysis_jungle_book.dat",
"analysis/analysis_snow_flakes.dat",
"analysis/analysis_book_dragons.dat",
"analysis/analysis_magic_city.dat",
"analysis/analysis_stories_of_birds.dat",
"analysis/analysis_chronicles_avonlea.dat",
"analysis/analysis_malory_towers.dat",
"analysis/analysis_treasure_island.dat",
"analysis/analysis_flower_fables.dat",
"analysis/analysis_mother_goose.dat",
"analysis/analysis_wizard_of_oz.dat",
"analysis/analysis_footprints_sea_shore.dat",
"analysis/analysis_my_native_land.dat",
"analysis/analysis_gift_magi.dat",
"analysis/analysis_peter_pan.dat"
]

allWords = []
for i in range(0,len(files)):
  for w in [(word.split())[0] for word in open(files[i])]:
    allWords.append(w)
 
allWordsSet = [word for word in set(allWords)]

frequencies = []
 
for theWord in allWordsSet:  
  sumFreq = 0
  for whichFile in range(0,len(files)):
    words = [(word.split())[0] for word in open(files[whichFile])]
    freq  = [int((word.split())[1]) for word in open(files[whichFile])]
 
    for i in range(0,len(words)):
      if theWord == words[i]:
        sumFreq += freq[i]
  frequencies.append(sumFreq)

for i in range(0,len(allWordsSet)):
  print allWordsSet[i], frequencies[i]
