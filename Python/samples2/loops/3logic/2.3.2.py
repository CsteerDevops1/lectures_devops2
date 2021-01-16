# -*- encoding: utf-8 -*-
"""
Логическое ИЛИ
"""

print 'a' or 'b'                                         

print '' or 'b'                                          

print '' or [] or {}                                     

def sidefx(): 
     print "in sidefx()" 
     return 1 
'a' or sidefx()                       
