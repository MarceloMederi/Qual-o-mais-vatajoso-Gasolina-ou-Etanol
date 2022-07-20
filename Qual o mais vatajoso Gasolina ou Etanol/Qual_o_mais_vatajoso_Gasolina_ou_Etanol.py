print("------------------")
print("GASOLINA OU ETANOL")
print("------------------")

print("Vamos calcular se é mais vantajoso abastecer o seu veiculo com GASOLINA ou ETANOL")

print("------------------------------------------------------------------------------------")
Gasolina = float (input("Informe o preço da Gasolina:\n"))
Etanol = float (input("Informe o preço do Etanol:\n"))
Media = float (Etanol / Gasolina)
print("O resultado deu: {:.2f}".format(Media))
if Media > 0.7:
    print("O mais indicado seria abastecer com Gasolina")
else:
    print("O mais indicado seria abastecer com Etanol")