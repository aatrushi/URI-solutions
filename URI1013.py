a, b, c = input().split()

MaiorAB = (int(a) + int(b) + abs(int(a) - int(b))) / 2
MaiorABC = (MaiorAB + int(c) + abs(MaiorAB - int(c))) / 2

print('{} eh o maior'.format(int(MaiorABC)))