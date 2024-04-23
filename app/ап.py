def counting_duplicates(text: str) -> int:
    w = []
    for i in text.lower():
        x = text.lower().count(i)
        if i  not in w:
            if x >= 2 :
                w.append(i)
    q = len(w)

    print( q)
counting_duplicates("aabbcde")