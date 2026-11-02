text = input("Введите текст: ")

words = text.split()
quantity_w = len(words)

repetitions = {}
for word in words:
    if word in repetitions:
        repetitions[word] += 1
    else:
        repetitions[word] = 1

max_count = 0
max_word = ""

for word in repetitions:
    if repetitions[word] > max_count:
        max_count = repetitions[word]
        max_word = word

max_len_word = words[0]
min_len_word = words[0]

for word in words:
    if len(word) > len(max_len_word):
        max_len_word = word
    if len(word) < len(min_len_word):
        min_len_word = word

print("Первый анализ:")
print("Количество слов:", quantity_w)
print("Самое частое слово:", max_word, "- встречается", max_count, "раз")
print("Самое длинное слово:", max_len_word)
print("Самое короткое слово:", min_len_word)


new_text = []
for word in words:
    if len(word) >= 3:
        new_text.append(word)

print("Слова после выбрасывания коротких слов:", new_text)

quantity_w2 = len(new_text)

repetitions2 = {}
for word in new_text:
    if word in repetitions2:
        repetitions2[word] += 1
    else:
        repetitions2[word] = 1

max_count2 = 0
max_word2 = ""

for word in repetitions2:
    if repetitions2[word] > max_count2:
        max_count2 = repetitions2[word]
        max_word2 = word

if len(new_text) > 0:
    max_len_word2 = new_text[0]
    min_len_word2 = new_text[0]

    for word in new_text:
        if len(word) > len(max_len_word2):
            max_len_word2 = word
        if len(word) < len(min_len_word2):
            min_len_word2 = word
else:
    max_len_word2 = "Нет слов"
    min_len_word2 = "Нет слов"

print("Второй анализ:")
print("Количество слов:", quantity_w2)
print("Самое частое слово:", max_word2, "- встречается", max_count2, "раз")
print("Самое длинное слово:", max_len_word2)
print("Самое короткое слово:", min_len_word2)