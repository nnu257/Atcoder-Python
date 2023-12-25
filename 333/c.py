n,k=map(int, input().split())
ass=list(map(int, input().split()))

sockses = [i for i in range(1, n+1)] + [i for i in range(1, n+1) if i not in ass]
sockses.sort()
print(sockses)