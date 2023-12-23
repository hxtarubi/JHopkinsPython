#Jude Yang
#7/26/21

report_card = "%s %s  Report Card"
s = " " * 8
print(report_card % (s, s))
#Title of the report card

labels = "%s Course Name %s Course Grade"
print(labels % (s, s))
#The labels of the report card

print("-" * 51)
print(" ")
#Border to organize the report card

python = "%s Python %s %s"
p1 = " " * 8
p2 = " " * 18
p3 = 96
print(python % (p1, p2, p3))
#Listed the python course grade

(" ")

java = "%s Java %s %s"
j1 = " " * 8
j2 = " " * 20
j3 = 91
print(java % (j1, j2, j3))
#Listed the java course grade

math = "%s Math %s %s"
m1 = " " * 8
m2 = " " * 20
m3 = 98
print(math % (m1, m2, m3))
#Listed the math course grade

print(" ")
print("=" * 51)

total = "%s Total %s %s"
t1 = " " * 8
t2 = " " * 19
t3 = p3 + j3 + m3
print(total % (t1, t2, t3))
#The sum of the grades for pytho, java, and math are labelled the total.

average = "%s Average %s %s"
a1 = " " * 8
a2 = " " * 17
a3 = t3 / 3
print(average % (a1, a2, a3))
#The average grade would be the sum of all grades divided by 3, hence,
#the average is 95.


