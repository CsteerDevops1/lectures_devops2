# -*- encoding: utf-8 -*-
"""
Закрытие файла
"""

# Open files consume system resources, and depending on the file mode, 
# other programs may not be able to access them. 

# It's important to close files as soon as you're finished with them, as shown in 
# 

f = open("/music/_singles/kairo.mp3", "rb")        

print f.closed                                     

f.close()                                          
print f 

print f.closed                      
