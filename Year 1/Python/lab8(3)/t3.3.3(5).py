import enum
import random


class Country(enum.Enum):
    China = 0
    Germany = 1
    USA = 2
    Japan = 3
    France = 4

class Product(enum.Enum):
    phone = 0
    car = 1
    petroleum_oil = 2
    automobile_parts = 3
    aircraft = 4

class Amount(enum.Enum):
    China = 46289
    Germany = 36247
    USA = 19563
    Japan = 229310
    France = 978

prodList = []
amountList = []

for i in Amount:
    j = 0
    while len(amountList) < len(Country):
        try:
            if i.name == Country(j).name:
                amountList.append(i.value)
                j+=1
                break
            else:
                j+=1
        except ValueError:
            j+=1
amountList.reverse()

for i in range(len(Product)):
    prodList.append(Product(i).name)

prodListSort = sorted(prodList)
prodIndex = []
j = 0
k = 0

while j in range(len(prodList)):
    if prodListSort[j] != prodList[k]:
        k+=1
    else:
        prodIndex.append(k)
        j+=1
        k=0

for i in range(len(prodIndex)):
    print(str(Product(prodIndex[i])) + ' ' + str(Country(prodIndex[i])), 'Amount.' + str(amountList[i]))