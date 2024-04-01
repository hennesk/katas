# Implement an algorithm to determine if a string has all unique characters.
# what if you can't use additional data structures?

def all_unique(string):
    seen = set(string)
    return len(string) == len(seen)

def all_unique_optimized(string):
    seen = set()
    for c in string:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True

# If you can't use additional space, use additional compute
def all_unique_no_other_ds(string):
    for i, c in enumerate(string):
        for j in range(i+1,len(string)):
            if string[j] == c:
                return False
    return True

if __name__ == '__main__':
    non_uniq = "steve"
    uniq = "abcde"
    assert all_unique(uniq)
    assert not all_unique(non_uniq)

    assert all_unique_optimized(uniq)
    assert not all_unique_optimized(non_uniq)

    assert all_unique_no_other_ds(uniq)
    assert not all_unique_no_other_ds(non_uniq)
    print("All passed")
