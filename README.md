Otimização do Agendamento de Chamados Técnicos com Pesquisa Operacional e Lógica de Programação Aplicada


Descrição do Projeto

Este projeto é o Trabalho de Conclusão de Curso (TCC) do curso de Data Science da USP/ESALQ, que tem como objetivo desenvolver uma solução para otimizar o agendamento de chamados técnicos utilizando técnicas de Pesquisa Operacional e Lógica de Programação.

A metodologia envolve processamento de dados, limpeza, organização e alocação inteligente dos chamados técnicos para melhorar a eficiência operacional.


Estrutura do Repositório

TCC-Data-Science-Operational-Research/
│
├── README.md
├── requirements.txt
└── alocacao_de_chamados/
    ├── 01_gerar_chamados.ipynb
    ├── 02_organizar_chamados.ipynb
    ├── 03_limpar_chamados.ipynb
    ├── 04_criar_tabela_liberacao.ipynb
    ├── 05_criar_agenda.ipynb
    ├── 06_main_alocar_chamados.ipynb
    ├── agenda.xlsx
    ├── chamados.xlsx
    ├── chamados_nao_agendados.xlsx
    ├── chamados_verificacao.xlsx
    ├── dados.xlsx
    ├── liberacao_tecnicos_clientes.xlsx
    └── tecnicos.xlsx


Descrição dos Códigos

01_gerar_chamados.ipynb
Geração dos chamados técnicos a partir critérios estabelecidos no código.

02_organizar_chamados.ipynb
Organização dos chamados conforme critérios de prioridade / urgência de atendimento.

03_limpar_chamados.ipynb
Exclui todos os chamados das planilhas: chamados.xlsx e chamados_nao_agendados.xlsx

04_criar_tabela_liberacao.ipynb
Criação da tabela que representa a disponibilidade e restrições de técnicos e clientes.

05_criar_agenda.ipynb
Gera uma agenda conforme critérios estabelecidos na planilha dados.xlsx

06_main_alocar_chamados.ipynb
Script principal que executa a alocação dos chamados técnicos, aplicando a lógica de programação e otimização da data de agendamento com pesquisa operacional.


Descrição das Planilhas

agenda.xlsx
Agenda onde serão alocados os chamados para cada técnico, conforme datas e horários disponíveis.

chamados.xlsx
Lista de chamados pendentes de agendamento.

chamados_nao_agendados.xlsx
Chamados que não foram alocados na agenda final, obedecendo as restrições de alocação.

chamados_verificacao.xlsx
Planilha usada para verificação e validação dos chamados após o processamento.

dados.xlsx
Conjunto de dados pré-estabelecidos para a representação de chamados e agendas.

liberacao_tecnicos_clientes.xlsx
Representação da disponibilidade e restrições entre técnicos e clientes para agendamento.

tecnicos.xlsx
Dados dos técnicos disponíveis.


Requisitos (requirements.txt)

Para executar os notebooks e scripts, é necessário instalar as dependências listadas em requirements.txt. Para isso, utilize:

pip install -r requirements.txt


Como Executar

1. Clone o repositório:

git clone https://github.com/caio-duarte-dev/TCC-Data-Science-Operational-Research.git

2. Instale as dependências:

pip install -r requirements.txt

3. Execute 01_gerar_chamados, por padrão serão gerados 200 chamados, mas a quantidade pode ser alterada no código confome necessidade.

4. Execute 02_organizar_chamados e os chamados serão classificados conforme ordem de prioridade de atendimento.

5. Execute 06_main_alocar_chamados, e os chamados em chamados.xlsx serão alocados em agenda.xlsx respeitando a ordem de prioridade, 
as restrições de alocação, como por exemplo, a tabela de liberação dos técnicos nos clientes (liberacao_tecnicos_clientes.xlsx),
além dos possíveis agendamentos que já possam ter sido inseridos manualmente na agenda.xlsx.

6. Caso haja necessidade de realizar outras simulações, basta executar limpar_chamados, e reiniciar o processo, gerando outros chamados e alterando os parâmetros em 01_gerar_chamados.

