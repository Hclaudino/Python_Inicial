for c in range(8):
    if c == 2:
        print("Seu c é 2, pulando....")
        continue
    if c == 8:
        print("c é 8, seu else não executara")
        break
    for j in range(1,3):
        print(c,j)
else:
    print("For completo com sucesso")