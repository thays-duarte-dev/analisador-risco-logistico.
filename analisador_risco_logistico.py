# =========================================================================
# PROJETO: MONITOR DE RISCO OPERACIONAL
# DESENVOLVEDORA: Thays - Logística & Tecnologia
# OBJETIVO: Automatizar a triagem de segurança das cargas
# =========================================================================

# Aqui eu crio a lista que vai segurar os dados até o final do processo
triagem_final = []

print(">>> SISTEMA INICIADO: Módulo de Segurança Operacional")
print("-" * 50)

# Vou processar 3 mercadorias por vez para manter o fluxo rápido
for i in range(3):
    print(f"Lançamento da Carga #{i+1}")
    
    # Input dos dados (com tratamento para não dar erro com vírgula)
    item = input("Descrição do Produto: ")
    valor_texto = input(f"Valor de {item}: R$ ")
    valor = float(valor_texto.replace(',', '.'))
    
    # Minha lógica de decisão baseada no valor da carga
    if valor > 12000:
        analise = "⚠️ CRÍTICO: Requer escolta armada"
    elif valor >= 6000:
        analise = "🟡 ALERTA: Rastreamento via isca eletrônica"
    else:
        analise = "✅ NORMAL: Liberação via rota padrão"
        
    # Organizando os dados para o meu relatório
    linha_relatorio = f"PRODUTO: {item.upper()} | VALOR: R$ {valor:,.2f} | DECISÃO: {analise}"
    
    # Adicionando na lista para não perder nada (o famoso append)
    triagem_final.append(linha_relatorio)
    print("Processamento concluído.\n")

# --- PARTE FINAL: EXIBIÇÃO DO TRABALHO ---
print("-" * 50)
print("RELATÓRIO DE TRIAGEM PARA O GESTOR")
print("-" * 50)

# O loop que lê minha lista e imprime linha por linha
for linha in triagem_final:
    print(linha)

print("\n[Fim do Processo - Sistema em Standby]")