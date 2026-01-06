import os
os.system("cls")

set1={"Artel","Alif","Yandex", "Google", "Meta"} 
set2={"Google", "Apple", "Amazon", "Meta"}
set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

set4=set1.intersection(set2,set3)

set5=set1.difference(set2,set3)

print("Umumiy elementlar:",end=" ")
print(set4)
print("Faqat birinchi elementda mavjud:", end=" ")
print(set5)