def verificar_suficiencia(competidores, quantidade_papel, quantidade_folhas):
    total_folhas_necessarias = competidores * quantidade_folhas
    
    if quantidade_papel >= total_folhas_necessarias:
        return "Suficiente"
    else:
        return "Insuficiente"

competidores, quantidade_papel, quantidade_folhas = map(int, input().split(','))

print(verificar_suficiencia(competidores, quantidade_papel, quantidade_folhas))
