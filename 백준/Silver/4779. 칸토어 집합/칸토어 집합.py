while True:
    try:
        N = int(input())

        cantor = ['-' for _ in range(3 ** N)]


        def rule(s, e):
            if e - s <= 1:
                return
            m1 = (e - s + 1) // 3

            for i in range(s + m1, s + m1 * 2):
                cantor[i] = ' '

            rule(s, s + m1 - 1)
            rule(s + 2 * m1, e)


        rule(0, (3 ** N) - 1)
        ans = ''.join(cantor)
        print(ans)

    except EOFError:
        break

