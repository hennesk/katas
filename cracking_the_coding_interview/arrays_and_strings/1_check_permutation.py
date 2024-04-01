# Given two strings, write a method to decide if one is a permutation of the other
def permutation(string1, string2):
    st1_dict = dict()
    for c in string1:
        st1_dict[c] = st1_dict.get(c, 0) + 1

    for c in string2:
        if not st1_dict.get(c, None):
            return False
        st1_dict[c] -= 1
        if st1_dict[c] < 0:
            return False
    
    for v in st1_dict.values():
        if v != 0:
            return False
    return True

if __name__ == '__main__':
    orig = "chupacabra"
    rev =  "arbacapuch"
    wro =  "arbcpuh"
    wro1 =  "chupacabraz"
    assert permutation(orig, rev)
    assert not permutation(orig, wro)
    assert not permutation(orig, wro1)