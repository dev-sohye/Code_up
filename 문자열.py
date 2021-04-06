# a = '''
# 요미는
# 귀여움
# '''
# print (a)

yomi = "yomi is so Cute"

print (yomi.lower())
print (yomi.upper())
print (yomi[0].isupper())
print (yomi[0].islower())
print (len(yomi))
print (yomi.replace("yomi", "yomyomi"))
index = yomi.index("i")
print (index)
index = yomi.index("i", index + 1)
print (index)

print (yomi.find("dog"))
# print (yomi.index("dog"))
print (yomi.count("i"))
