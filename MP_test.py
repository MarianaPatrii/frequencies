import re

print("Enter the text: ")
text = input()
print("Enter N: ")
N = int(input())
def freq(text, N):
    top_freq = 10
    arr = []
    result = {}
    res = []
    new_text = re.sub("[\W\d_]", "", text).lower()
    def append(array):
        for element in arr:
            if element in result:
                result[element] += 1
            else:
                result[element] = 1
        return result
    if N == 1:
        arr = list(new_text)
        append(arr)
    else:
        for i in range(0, len(new_text)):
            if len(new_text[i:i+N]) == N:
                arr.append(new_text[i:i+N])
        append(arr)
    for key, value in result.items():
        elem = [key, value]
        res.append(elem)
        res = res[0:top_freq]
        res = sorted(res, key=lambda x: x[1], reverse = True)
    print("( freq", N,  " \"", text, "\")", " => ( ", res, " )")
freq(text, N)
