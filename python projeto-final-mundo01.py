# Cores ANSI
azul = '\033[34m'
verde = '\033[32m'
amarelo = '\033[33m'
vermelho = '\033[31m'
reset = '\033[m'

# Estilos
bold = '\033[1m'
underline = '\033[4m'
negative = '\033[7m'

print('-=-' * 25)
print(f'{bold}{azul}SISTEMA DE PRIORIZAÇÃO DE PROJETOS{reset}')
print('-=-' * 25)

print('''
Este sistema visa apoiar a tomada de decisão utilizando
um modelo de priorização baseado em critérios de negócio.

Estamos considerando uma matriz de impacto, esforço, custo e risco,
permitindo, dessa forma, uma avaliação orientada a dados!
''')

print('-=-' * 25)

# Nome do projeto
nome_projeto = str(input(
    'Antes de começar, informe o nome do projeto que deseja avaliar: '
)).strip()

print('-=-' * 25)
print(f'''
Agora que sabemos qual projeto está sendo avaliado,
vamos dar início à nossa análise de priorização.

Projeto: {underline}{amarelo}{nome_projeto}{reset}

Para cada critério, atribua uma nota de 1 a 5,
sendo 1 baixo/pouco e 5 alto/muito.
''')

print('-=-' * 25)

# IMPACTO
print(f'{bold}{azul}1 - IMPACTO NO NEGÓCIO{reset}')
print('''
Avalie quanto o projeto pode gerar valor para o negócio.

1 - Impacto baixo: melhoria pontual ou pouco relevante
3 - Impacto moderado: melhora processos ou resultados existentes
5 - Impacto alto: impacto estratégico ou crítico para a empresa
''')
impacto = int(input(
    'Para esse projeto, qual o nível de impacto para o negócio? (1 a 5): '
))

print('-=-' * 25)

# ESFORÇO
print(f'{bold}{azul}2 - ESFORÇO NECESSÁRIO{reset}')
print('''
Avalie a complexidade e o esforço necessário para executar o projeto.

1 - Execução simples, poucas dependências (quick win)
3 - Complexidade média, exige coordenação entre áreas
5 - Execução complexa, alto esforço ou longo prazo
''')
esforco = int(input(
    'Para esse projeto, qual é o nível de esforço para sua execução? (1 a 5): '
))

print('-=-' * 25)

# CUSTO
print(f'{bold}{azul}3 - CUSTO ESTIMADO{reset}')
print('''
Avalie o investimento financeiro necessário.

1 - Baixo custo, facilmente absorvido pelo orçamento
3 - Custo moderado, exige planejamento
5 - Alto custo ou investimento significativo
''')
custo = int(input(
    'Para este projeto, qual o nível de custo esperado? (1 a 5): '
))

print('-=-' * 25)

# RISCO
print(f'{bold}{azul}4 - RISCO ENVOLVIDO{reset}')
print('''
Avalie o nível de incerteza e exposição a problemas ao longo do projeto.

1 - Baixo risco, cenário previsível
3 - Risco moderado, algumas incertezas
5 - Alto risco, muitas variáveis desconhecidas
''')
risco = int(input(
    'Para este projeto, qual o nível de risco esperado? (1 a 5): '
))

print('-=-' * 25)

# CÁLCULO DO SCORE
score = (impacto * 3) - esforco - custo - risco

print(f'Análise concluída para o projeto: {bold}{nome_projeto}{reset}')
print('-=-' * 25)

# DECISÃO E EXPLICAÇÃO
if score >= 6:
    print(f'{bold}{verde}PRIORIDADE ALTA{reset}')
    print('''
Este projeto apresenta alto potencial de impacto,
com esforço, custo e risco em níveis aceitáveis.

Recomendação: priorizar a execução.
''')
elif score >= 2:
    print(f'{bold}{amarelo}PRIORIDADE MÉDIA{reset}')
    print('''
Este projeto gera valor, mas envolve trade-offs
que exigem uma análise mais cuidadosa.

Recomendação: avaliar cenários ou ajustar escopo.
''')
else:
    print(f'{bold}{vermelho}PRIORIDADE BAIXA{reset}')
    print('''
Neste momento, o esforço, custo ou o risco
superam os benefícios esperados.

Recomendação: reavaliar ou postergar o projeto.
''')

print('-=-' * 25)
print(
    f'Processo de priorização do projeto: '
    f'{bold}{nome_projeto}{reset} foi finalizado :)'
)
