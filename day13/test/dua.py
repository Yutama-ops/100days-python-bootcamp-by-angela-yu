def findLowestPrice(products, discounts):
    # Write your code here
    pass

products = [['10','sale', 'january-sale'], ['200', 'sale', 'EMPTY']]

discounts =[['sale', '0', '10'], ['january-sale', '1', '10']]
type0 = 10 #fixedprice
type1= 10%2 #discount%- price
type2 = 10-5 #discout-price



products = [['10','d0', 'd1'], ['15', 'EMPTY', 'EMPTY'], ['20', 'd1', 'EMPTY']]

discounts =[['d0', '1', '27'], ['d1', '2', '5']]
total_prod = len(products)
low_dis_1 = 0
low_dis_2 = 0
low_dis_3 = 0
dis1 = []
dis2 = []
dis3 = []
for dis in discounts:
    print(dis)
    for prod in products:
        print(prod)
        if prod[1] != 'EMPTY':
            if prod[1] == dis[0]:
                if dis[1] == '0':
                    low_dis_1 = dis[2]
                    dis1.append(low_dis_1)
                if dis[1] == '1':
                    low_dis_2 = round(int(prod[0])-int(prod[0])*int(dis[2])/100)
                    dis2.append(low_dis_2)
                if dis[1] == '2':
                    low_dis_3 = int(prod[0])-int(dis[2])
                    dis3.append(low_dis_3)
        if prod[2] != 'EMPTY':
            if prod[2] == dis[0]:
                if dis[1] == '0':
                    if low_dis_1 < int(dis[2]):
                        low_dis_1 = dis[2]
                        dis1[low_dis_1] = low_dis_1
                if dis[1] == '1':
                    new_dis = round(int(prod[0])-int(prod[0])*int(dis[2])/100)
                    if new_dis < low_dis_2:
                        low_dis_2 = new_dis
                        dis2[low_dis_2] = low_dis_2
                if dis[1] == '2':
                    new_dis = int(prod[0])-int(dis[2])
                    if new_dis < low_dis_3:
                        low_dis_3 = new_dis
                        dis3[low_dis_3] = low_dis_3

total = int(low_dis_1)+int(low_dis_2)+int(low_dis_3)

print(dis1)
print(dis2)
print(dis3)


print(low_dis_2)
print(low_dis_1)
print(low_dis_3)
print(total)