### For Loop - Lesson 9 - Trial

animals=['cat','dog','mouse','cow','wabbit','bird']
###for animal in animals:
###print animal
horizontal = "cat dog mouse cow wabbit bird"
horizontal = " "
for animal in animals:
    horizontal = horizontal + " " + animal
print horizontal

print "\n".join([" ".join(animals[i:i+5]) for i in xrange(0,len(animals),5)])



###Total ages? Vamos a calcular el total de las edades
ages=[18, 21, 14, 7, 90, 12]
total_age=0
for age in ages:
    total_age += age
print 'Total Age', total_age
print "Average Age", total_age/len(ages)
print "len:  ", len(ages)
