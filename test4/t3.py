origin = 0

def factory(pos) :
    def go(step) :
        nonlocal pos
        new_post = pos + step
        pos = new_post
        return new_post
    return go

tourist = factory(origin)

print(tourist(2))
print(tourist(3))
print(tourist(5))
        