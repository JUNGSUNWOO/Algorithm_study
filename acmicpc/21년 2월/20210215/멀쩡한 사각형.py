def solution(w,h):
    gcd = Euclidean_algorithm(w,h)
    w_hat = w / gcd
    h_hat = h / gcd
    if w_hat == h_hat :
        return w * h - (w_hat * gcd)
    elif w_hat != h_hat :
        return w * h - ((w_hat + h_hat - 1) * gcd)


def Euclidean_algorithm(a, b):
    if b ==0:
        return a
    else :
        return Euclidean_algorithm(b, a%b)

