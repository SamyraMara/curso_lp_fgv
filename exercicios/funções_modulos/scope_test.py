def scope_test():
    spam = "test spam"
    def do_local():
        spam = "local spam"
        
    def do_global():
        global spam
        spam = "global spam"
        
    do_local()
    print("After local assignment:", spam)
    
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)