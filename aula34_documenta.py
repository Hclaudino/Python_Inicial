"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool = objetos, tendo ações que podem ser realizadas
"""
#tipos imutaveis não é possivel serem substituidos
string = 'henrique Claudino'
out_s = f'{string[:3]}ABC{string[4:]}' #fatiamento para mostrar somente de 0 a 3, porém na criação de uma variavél eu posso mudar.
print(out_s)
print(string.capitalize())
print(string.upper())