reply = input()

difficult = ""
if "," in reply:
    difficult = "сложное "

res = ""
if "!" in reply and "?" in reply:
    res = "вопросительно-восклицательное"
elif "!" in reply:
    res = "восклицательное"
elif "?" in reply:
    res = "вопросительное"
else:
    res = "повествовательное"

print(difficult + res)