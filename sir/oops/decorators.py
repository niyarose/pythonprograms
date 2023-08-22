def dec_name(fn):
    def inner_fn(n1,n2): #fn=sub(10,20)
        (n1,n2)=(n2,n1) #10>20
        return fn(n1,n2) #
    return inner_fn

@dec_name
def sub(n1,n2):
    return n1-n2
@dec_name
def div(n1,n2):
    return n1/n2

print(div(10,20))
print(sub(10,20))