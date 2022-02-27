t = int(input())

for _ in range(t):
    voice = list(input().split())
    result = []
    crawl_set = set()
    while True:
        animal = input()
        if animal == "what does the fox say?":
            break
        animal = animal.split()
        crawl_set.add(animal[2])
    for i in range(len(voice)):
        if voice[i] not in crawl_set:
            result.append(voice[i])
    print(*result)