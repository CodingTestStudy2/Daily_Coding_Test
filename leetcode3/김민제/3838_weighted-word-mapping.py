def mapWordWeights(words, weights):
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
           'r','s','t','u','v','w','x','y','z']
    arr2 = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j',
           'i','h','g','f','e','d','c','b','a']
    ret = ""

    for word in words:
        weight = 0
        for n in range(len(word)):
            weight += weights[arr.index(word[n])]
        ret+=arr2[weight % 26]

    return ret


words = ["abcd","def","xyz"]
weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]

print(mapWordWeights(words,weights))
