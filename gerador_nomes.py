import random

def gerar_nome():
    primeiros_nomes = [
    "Os Cabeludos de", "Os Amigos de", "Os Criadores de", "Os Enrolados de", 
    "Os Estourados de", "Os Lendários de", "Os Sabichões de", "Os Carregadores de", 
    "Os Fugitivos de", "Os Bizarros de", "Os Preguiçosos de", "Os Esticados de", 
    "Os Desajeitados de", "Os Caçadores de", "Os Briguentos de", "Os Engraçadinhos de", 
    "Os Mestres de", "Os Capengas de", "Os Super-Heróis de", "Os Fritadores de", 
    "Os Amantes de", "Os Devotos de", "Os Infiéis de", "Os Dançarinos de", 
    "Os Resmungões de", "Os Pescadores de", "Os Apavorados de", "Os Espiões de", 
    "Os Distraídos de", "Os Topetudos de"
]

    segundos_nomes = [
    "Pipoca", "Foguete", "Papelão", "Peido", "Coxinha", "Macarrão", "Espaguete", 
    "Biscoito", "Lata", "Xixi", "Torta", "Pneu", "Pantufa", "Feijão", "Galocha", 
    "Bunda", "Geladeira", "Salsicha", "Meia", "Almofada", "Chaveiro", "Copo", "Ventilador", 
    "Escova", "Pirulito", "Cabeludo", "Bolacha", "Lombriga", "Tetra", "Pirata", "Sundae"
]
    nome_gerado = random.choice(primeiros_nomes) + ' ' + random.choice(segundos_nomes)
    return nome_gerado

def macaco_gerar():
    nomes_macacos = [
    "Cabeludo", "Chaveirinho", "Banano", "Peludo", "Chimpanzito", "Rabudo", 
    "Mico", "Macacão", "Gorilão", "Fruta", "Marmota", "Coxinha", "Biscoito", 
    "Dengo", "Loro", "Arapuca", "Fumaça", "Bate-Palmas", "Marmelada", "Pelé", 
    "Sombra", "Fofucho", "Pipoca", "Goloso", "Bigode", "Bambú", "Gargalhada", 
    "Mãozinha", "Caramelo", "Tico", "Zé Macaco", "Mangueira", "Banguela", 
    "Pirueta", "Quicó", "Maracujá", "Anzol", "Mandioca", "Açaí", "Xingado", 
    "Tigre", "Tuca", "Bola", "Palmeira", "Coco", "Pinga", "Avião", "Pele de Onça", 
    "Vagabundo", "Teimoso", "Ratinho", "Coquinho"
]
    sobrenomes_macacos = [
    "da Selva", "do Bananal", "da Rampa", "do Galho", "do Mato", "da Árvore", 
    "do Pulo", "da Perna Longa", "do Pulo Alto", "do Rio", "da Liana", "do Bambu", 
    "do Pé de Manga", "da Fruta Podre", "do Cacau", "da Caverna", "da Floresta", 
    "do Coco", "do Tucuruí", "do Balanco", "do Pé de Feijão", "da Cachoeira", 
    "da Escada", "do Pântano", "do Buraco", "da Fumaça", "da Ponte", "do Topo", 
    "da Curva", "da Caçamba", "do Bigode", "do Lodo", "da Caverna", "do Tomate", 
    "da Lixeira", "da Poeira", "do Mico Leão", "do Espelho", "do Pote", "do Toco", 
    "da Foca", "do Pipi", "da Bagunça", "do Relâmpago", "do Tacho", "da Tenda", 
    "do Deserto", "do Galo", "da Pousada", "da Manhã"
]
    macaco_nome = random.choice(nomes_macacos) + ' ' + random.choice(sobrenomes_macacos)
    return macaco_nome