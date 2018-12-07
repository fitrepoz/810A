def arg_cnt(args, expect):
    if len(args) != expect:
        print("expected {} but found {}".format(expect, len(args)))
    else: 
        print("ok")

arg_cnt(['hello'],1)