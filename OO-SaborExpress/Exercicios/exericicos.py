
class Restaurante:
    nome=''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
'''restaurante_praca.nome = 'Mama Mia' '''
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

nome_do_restaurante = restaurante_praca.nome

print(nome_do_restaurante)

if restaurante_praca.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')

categoria = Restaurante.categoria

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')
    
if restaurante_pizza.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')
print(f'Nome: {restaurante_pizza.nome}, Categoria: {restaurante_pizza.categoria}')
