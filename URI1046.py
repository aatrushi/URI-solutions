time = input().split()

start = int(time[0])
end = int(time[1])

if start == end:
    print('O JOGO DUROU 24 HORA(S)')

else:
    x = end - start
    if x < 0:
        x += 24
    print('O JOGO DUROU %d HORA(S)' %x)