def max( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max( x, max( y, z ) )
print(max_of_three(20, 40, -5))