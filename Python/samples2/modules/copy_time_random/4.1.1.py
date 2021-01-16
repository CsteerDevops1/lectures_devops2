# -*- encoding: utf-8 -*-
"""
Поверхностное и глубокое копирование
"""
import copy

listOne = [{"name": "Willie", "city": "Providence, RI"}, 1, "tomato", 3.0]

listTwo = listOne[:]                   
listTwo=copy.copy(listOne)
listThree = copy.deepcopy(listOne)

listOne.append("kid")
listOne[0]["city"] = "San Francisco, CA" 

print listOne
print listTwo
print listThree