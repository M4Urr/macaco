from gerador_nomes import gerar_nome
from gerador_nomes import macaco_gerar
import random

# Classe Facções
class Fac:
    def __init__(self, nome, id):
        self.id = id
        self.nome = nome
        self.macacos = []  # A lista de macacos da facção

    def adicionar_macaco(self, macaco):
        self.macacos.append(macaco)

# Classe Macaco
class Macaco:
    def __init__(self, id, nome, forc, vel, inte, fac):
        self.id = id
        self.nome = nome
        self.forc = forc
        self.vel = vel
        self.inte = inte
        self.fac = fac  # A facção a qual o macaco pertence

# Gerar as facções
facs = [Fac(gerar_nome(), i+1) for i in range(10)]

# (Função) Criar e distribuir macacos
def criar_macacos():
    macacos = []
    for i in range(50):
        nome = macaco_gerar()
        forc = random.randint(1, 10)  # Força do macaco
        vel = random.randint(1, 10)   # Velocidade do macaco
        intel = random.randint(1, 10)   # Inteligência do macaco
        fac = facs[i % 10]            # Distribui os macacos entre as 10 facções
        macaco = Macaco(i+1, nome, forc, vel, intel, fac)
        fac.adicionar_macaco(macaco)
        macacos.append(macaco)
    return macacos

# Criar
macacos = criar_macacos()

def macaco_id(macacosArr,idm):
    for macaco in macacosArr:
        if macaco.id == idm:
          return macaco
    return None

def fac_id(facsArr, idf):
    for fac in facsArr:
        if fac.id == idf:
            return fac
    return None

def fac_name(facsArr, nmf):
    for fac in facsArr:
        if fac.nome == nmf:
            return fac
    return None

def macaco_name(macacoArr, nmc):
    for macaco in macacoArr:
        if macaco.nome == nmc:
            return macaco
    return None

rodando = True

while rodando:
    e = input("Quer fechar?: ").upper()

    if e == 'SIM':
        rodando = False
        break

    ed = input("Procurar Fac ou Macaco: ").upper()

    if ed == 'MACACO':
        esc = input("Quer procurar macaco por ID ou NOME?").upper()
        if esc == 'ID':
            prid = int(input("Digite o ID:"))
            alvo = macaco_id(macacos, prid)

            if alvo:
                print(f"Macaco encontrado! {alvo.nome} faz parte da facção {alvo.fac.nome}")
            else:
                print('Macaco não foi encontrado!')
                continue
        elif esc == 'NOME':
            prid = input("Digite o NOME:")
            alvo = macaco_name(macacos, prid)

            if alvo:
                print(f"Macaco encontrado! {alvo.nome} faz parte da facção {alvo.fac.nome}")
            else:
                print('Macaco não foi encontrado!')
                continue
    if ed == 'FAC':
        esc = input("Quer procurar facção por ID ou NOME?").upper()
        if esc == 'ID':
            prid = int(input("Digite o ID:"))
            alvo = fac_id(facs, prid)

            if alvo:
                print(f"Facção encontrada! {alvo.nome} e tem {len(alvo.macacos)} membros.")
            else:
                print('Facção não foi encontrado!')
                continue
        elif esc == 'NOME':
            prid = input("Digite o NOME:")
            alvo = fac_name(facs, prid)

            if alvo:
                print(f"Facção encontrada! {alvo.nome} e tem {alvo.macacos} membros, quais são {macaco.nome for macaco}")
            else:
                print('Facção não foi encontrado!')
                continue
            
    
    
