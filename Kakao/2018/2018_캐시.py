def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cache = []
    answer = 0
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1

        else:
            cache.append(c)
            cache = cache[-cacheSize: ]
            answer += 5
            
    return answer