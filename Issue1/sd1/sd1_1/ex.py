# def f1_1(): print("this is f1_1")

def f1_1(): 
    from sd2.ex import f2
    # import Issue1.sd2.ex
    f2()

    # from sd2.sd2_1.ex import f2_1
    # f2_1()

if (__name__ == "__main__") :
    print("Issue1/sd1/sd1_1/ex.py as main")
    f1_1()