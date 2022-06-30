class IO:
    supportedSrcs = ["console", "file"]

    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        
        else:
            print("Read from {}".format(src))

print("IO.supportedSrcs : {}".format(IO.supportedSrcs))
IO.read("file")
IO.read("internet")