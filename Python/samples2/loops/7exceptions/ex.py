try:
    print 1/float(raw_input("\nEnter a number: "))
except(ValueError):
    print "ValueError"
except(KeyboardInterrupt):
    print "KeyboardInt"
except(ZeroDivisionError):
    print "0"
   print "1"
