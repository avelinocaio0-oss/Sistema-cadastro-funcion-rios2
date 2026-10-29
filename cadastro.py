print('#SISTEMA DE CADASTRO DOS FUNCIONARIOS')

funcionario=input('nome completo:')
departamento=input('departamento:')
email=input('email corporativo:')

mais=funcionario.title()
mais2=departamento.upper()
mais3=email.lower()
carac=len(mais)

print('===RELATORIO FINAL===')

print('AGUARDE...')

print('nome do funcionario:',mais)
print('departamento:',mais2)
print('email corporativo:',mais3)
print('numero de caracteres:',carac)

print('#CADASTRO REALIZADO COM SUCESSO!')