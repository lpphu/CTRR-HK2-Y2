# 52100988 Lữ Phúc Phú

def extended_euclidean(a, b):
    if a == 0:
        return (0, 1, b)
    else:
        x, y, gcd = extended_euclidean(b%a, a)
        return (y - (b//a) * x, x, gcd)
    
def inverse_modulo(a, b):
    x, y, gcd = extended_euclidean(a, b)
    if gcd == 1:
        return x%b
    else:
        return None
    
print("inverse_modulo(26,15) =",inverse_modulo(26,15))
print("inverse_modulo(3,15) =",inverse_modulo(3,15))
print("inverse_modulo(19,15) =",inverse_modulo(29,15))
print("inverse_modulo(22,1) =",inverse_modulo(22,1))
print("inverse_modulo(22,0) =",inverse_modulo(22,0))