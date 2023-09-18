import pyspark

file = sc.textFile("work/README.md")
words = file.flatMap(lambda linha: linha.slpit(" "))
word_count = words.countByValue()

for words, itens in word_count.items():
    print(f'palavra: {words} aparece {itens} vez(es)')