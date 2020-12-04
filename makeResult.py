import csv

q1 = 0 #온도(뜨,차,암)
q2 = 1 #맵기(맵,안맵,암)
q3 = 0 #종류(밥,면,빵,암)
q4 = 1 #국물(있,없,암)
q5 = 0 #고기(육,해,암)
q6 = 3 #나라(한,중,일,남,암)
q7 = 1 #칼로리(낮,중,높,암)
q8 = 1 #가격(낮,중,높,암)
q9 = 1 #알러지
l = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp = 0

f = open('food_dataset.csv','r',encoding='utf-8')
rd = csv.reader(f)

for idx,val in enumerate(rd):
    if(q1 == 0) : a = 'hot'
    elif(q1 == 1): a = 'cold'
    else: a = ''
    if(a in val[2]): l[idx] +=1

    if(q2 == 1):
        if not('spicy' in val[2]): l[idx] += 1
    else:
        if(q2 == 0) : a = 'spicy'
        else: a= ''
        if (a in val[2]): l[idx] += 1

    if (q3 == 0): a = 'rice'
    elif (q3 == 1): a = 'noodle'
    elif (q3 == 2): a = 'bread'
    else: a = ''
    if (a in val[2]): l[idx] += 1

    if (q4 == 0): a = 'soup'
    elif (q4 == 2): a = ''
    if (q4 == 1):
        if not ('soup' in val[2]): l[idx] += 1
    else:
        if (a in val[2]): l[idx] += 1

    if (q5 == 0): a = 'meat'
    elif (q5 == 1): a = 'fish'
    else: a = ''
    if (a in val[2]): l[idx] += 1

    if (q6 == 0): a = 'korea'
    elif (q6 == 1): a = 'china'
    elif (q6 == 2): a = 'japan'
    else: a = ''
    if (a in val[5]): l[idx] += 1

    if (q7 == 0): a = 'high'
    elif (q7 == 1): a = 'med'
    elif (q7 == 2): a = 'low'
    else: a = ''
    if (a in val[3]): l[idx] += 1

    if (q8 == 0): a = 'high'
    elif (q8 == 1): a = 'med'
    elif (q8 == 2): a = 'low'
    else: a = ''
    if (a in val[6]): l[idx] += 1

print(l)

best = max(l)
best_index = l.index(best)
print(best_index)

f.close()