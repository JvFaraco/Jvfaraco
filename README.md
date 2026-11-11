<a href="https://jvfaraco.github.io/jvfaraco-portifolio/">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/profile-banner.png" />
    <img src="assets/profile-banner.gif" alt="Banner de João Victor Faraco, Analista de Sistemas em São José, SC: Python, automação e integrações. Ao lado, um terminal ilustrativo mostra a pré-validação de uma O.S.: regras conferidas, sugestão da IA e decisão humana. Leva ao portfólio." width="100%" />
  </picture>
</a>

### Oi, eu sou o João 👋
**Analista de Sistemas na Orsegups · MBA em Inteligência Artificial · São José, SC**

Construo **soluções com IA aplicada, Python e automação** para problemas reais da operação: um validador de O.S. com IA em uso diário, integrações de sistemas, dashboards e mapas. Na IA, combino regras verificáveis, saída estruturada e conferência humana — o modelo ajuda a decidir, mas cada resultado precisa ser conferível. Comecei no suporte e passei por testes de hardware, por isso olho para o código e também para quem vai usar a ferramenta.

[**Conheça meu portfólio ↗**](https://jvfaraco.github.io/jvfaraco-portifolio/) · [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-victor-faraco-01066423a/) · [E-mail](mailto:joaovictorfaraco@gmail.com)

### Alguns projetos para explorar
<table><tr>
<td width="50%" valign="top"><a href="https://github.com/JvFaraco/os-validator-demo"><img src="assets/preview-os-validator.png" alt="Terminal com a análise de uma O.S. fictícia: pacote sanitizado com nome e telefone mascarados, regras sem pendência, IA escolhendo entre 3 opções do catálogo com as conferências aprovadas, e decisão pronta para validação, com aprovação final humana." width="100%" /></a></td>
<td width="50%" valign="top"><b>🤖 Validador de O.S. com IA</b><br>Versão pública, com dados fictícios, do validador que mantenho em produção. As regras determinísticas vêm primeiro. A IA lê a nota do técnico e escolhe de um catálogo fechado, com saída em JSON Schema. Dado pessoal não sai da máquina, e a aprovação final é sempre de uma pessoa.<br><br>A avaliação usa um gabarito rotulado à mão: o Claude Haiku acertou as 38 decisões do conjunto fictício, numa rodada de menos de 1 centavo de dólar.<br><code>Python</code> <code>LLM</code> <code>JSON Schema</code> <code>pytest</code> · <a href="https://github.com/JvFaraco/os-validator-demo">Código</a></td>
</tr><tr>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/mapaderotas/"><img src="assets/preview-route-coverage.png" alt="Captura da demo do Route Coverage Map: à esquerda, o total de áreas cobertas, de onde veio cada contorno e os filtros por região; à direita, áreas coloridas por rota sobre um mapa escuro, com as aproximadas hachuradas e a dica de uma delas aberta. Dados fictícios." width="100%" /></a><br><b>🗺️ Route Coverage Map</b><br>De uma planilha de rotas a um mapa navegável: geocodificação, limites do IBGE e tratamento das áreas de cobertura.<br><code>Python</code> <code>Leaflet</code> <code>GIS</code> · <a href="https://jvfaraco.github.io/mapaderotas/">Demo</a> · <a href="https://github.com/JvFaraco/mapaderotas">Código</a></td>
<td width="50%" valign="top"><a href="https://github.com/JvFaraco/quick-replies"><picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/preview-quick-replies.png" /><img src="assets/preview-quick-replies.gif" alt="Demonstração da extensão: o atendente digita barra no campo de mensagem, escolhe uma resposta pronta e ela é inserida no campo, com saudação e nome fictícios." width="100%" /></picture></a><br><b>💬 Extensão de respostas rápidas</b><br>Extensão Chrome para quem atende em chat web: digite / no campo, escolha a resposta e insira com Tab. Biblioteca da equipe sincronizada por planilha; quem envia é sempre o atendente.<br><code>JavaScript</code> <code>Chrome MV3</code> <code>Playwright</code> · <a href="https://github.com/JvFaraco/quick-replies">Código</a> · <a href="https://github.com/JvFaraco/quick-replies/releases/latest">Baixar</a></td>
</tr><tr>
<td width="50%" valign="top"><a href="https://github.com/JvFaraco/bot-telegram"><img src="assets/preview-bot-alertas.png" alt="Ilustração de duas mensagens do bot no Telegram, com produto, preço, desconto, loja, cupom e link. Oferta e loja fictícias." width="100%" /></a><br><b>📬 Bot de alertas no Telegram</b><br>Monitoramento de ofertas com filtros de preço, desconto e palavras-chave. Envia alertas sem repetir notificações e roda pelo GitHub Actions.<br><code>Python</code> <code>Scraping</code> <code>Telegram API</code> · <a href="https://github.com/JvFaraco/bot-telegram">Código</a></td>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/jvfaraco-portifolio/#certificados"><img src="assets/preview-certificados.png" alt="Seção de certificados do portfólio: MBA em Inteligência Artificial, diploma de Tecnólogo em Gestão da TI, certificações intermediárias da Estácio e curso de Python da Udemy." width="100%" /></a><br><b>🎓 Formação e certificados</b><br>MBA em Inteligência Artificial, diploma de Tecnólogo em Gestão da TI e cursos, com os documentos abertos no portfólio (dados pessoais cobertos).<br><a href="https://jvfaraco.github.io/jvfaraco-portifolio/#certificados">Ver certificados</a></td>
</tr></table>

<sub>O validador é a saída real do terminal, com uma O.S. fictícia. O mapa e a extensão são capturas das demos, com dados fictícios. O bot é uma ilustração no formato real das mensagens, com oferta fictícia.</sub>

### O trabalho que acontece nos bastidores
Também desenvolvo ferramentas internas para a operação: integrações de OS com CRM, relatórios, auditorias e pré-validação de atendimentos. Os estudos estão no [portfólio](https://jvfaraco.github.io/jvfaraco-portifolio/).

<details>
<summary><strong>Ver sistemas internos e decisões técnicas</strong></summary>

| Sistema | O que resolve |
|---|---|
| **Integração de OS com CRM** | Sincroniza contratos, anexos e timeline; considera mudanças, deduplicação e falhas de comunicação. |
| **Ferramentas de campo e agenda** | Relatórios de comissão/equipamentos, auditoria de rotas, reagendamento e recomendação de agenda. |
| **Validador de OS com IA** | Combina coleta, OCR local e regras com classificação assistida por IA; a decisão final continua humana. |

Dois fluxos simplificados, sem nomes de sistemas nem dados: a sincronização de OS com o CRM e a pré-validação de atendimentos.

```mermaid
flowchart LR
  A[OS na origem] --> B{Já existe no CRM?}
  B -- não --> C[Cria]
  B -- sim --> D[Atualiza só o que mudou]
  C & D --> E[Registro para conferência]
  C & D -. falha .-> F[Nova tentativa e reconciliação]
```

```mermaid
flowchart LR
  A[Atendimento coletado] --> B[OCR local e regras] --> C[Classificação assistida por IA] --> D[Decisão humana]
```

Cuido também do que acontece quando a API falha: simulação, reconciliação e conferência das alterações. Os repositórios são privados; os estudos não expõem credenciais nem dados operacionais. Uma versão pública do validador, escrita do zero com dados fictícios, está em [os-validator-demo](https://github.com/JvFaraco/os-validator-demo).

A suíte local do validador registrou **2.222 testes passando em 09/11/2026**. É uma medição desse projeto, não uma taxa de acerto da IA. O assistente de agenda está em validação: bloqueios e duração dos atendimentos ainda precisam de conferência operacional.

</details>

### Competências
- **IA aplicada:** LLMs com saída estruturada (JSON Schema) e catálogo fechado, Copilot Studio, Power Automate, OCR e servidores MCP, sempre com regras e decisão final humana. <sub>Validador de OS com IA e assistente operacional.</sub>
- **Python e automação de processos:** scripts, rotinas agendadas, planilhas e scraping. <sub>Bot de alertas, Route Coverage Map e ferramentas internas.</sub>
- **Integração de sistemas e APIs REST:** consumo de APIs e sincronização com deduplicação, nova tentativa e reconciliação. <sub>Integração de OS com CRM e bot de alertas.</sub>
- **Dados:** SQL/SQLite, pipelines (ETL) e dados geográficos. <sub>Route Coverage Map e relatórios internos.</sub>
- **Backend e web:** FastAPI e JavaScript.
- **Qualidade e entrega:** Git, GitHub Actions (CI/CD) e pytest. <sub>CI do Route Coverage Map e suíte do validador de OS.</sub>
- **Privacidade de dados e documentação:** minimização de PII e documentação de arquitetura e operação. <sub>Varredura de PII no CI do mapa e sanitização no validador.</sub>

### De onde venho e o que estou estudando
**Orsegups — Analista de Sistemas** · desde março/2025<br>
Automação, integrações e ferramentas para operação, suporte e backoffice.

**MBA em Inteligência Artificial** · Estácio de Sá · concluído em 2026

<details>
<summary>Formação, trajetória anterior e cursos</summary>

- **Gestão da Tecnologia da Informação** · Estácio de Sá · concluída em 2025. [Certificados e diploma no portfólio](https://jvfaraco.github.io/jvfaraco-portifolio/#certificados).
- **Orsegups:** Especialista em Testes de Hardware · set/2024–mar/2025. Dashboards de equipamentos, testes e RMA.
- **Figueirense Futebol Clube:** Estagiário de TI · fev–set/2024. Suporte e manutenção de infraestrutura.
- **Instituto São José:** Estagiário de TI · out/2022–out/2023. Suporte e administração de sistemas.
- Programação Python do Zero ao Avançado — Udemy, jul/2022.
- Aplicação da Melhoria Contínua e Implantação de Governança de TI — jun/2024.
- Gestão de Projetos e de Informação — mar/2024.
- Programação para Internet — ago/2023.

</details>

### Vamos conversar?
Aberto a oportunidades em **IA aplicada, desenvolvimento Python e automação de sistemas**.

**[joaovictorfaraco@gmail.com](mailto:joaovictorfaraco@gmail.com)** · [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-victor-faraco-01066423a/) · [Portfólio](https://jvfaraco.github.io/jvfaraco-portifolio/)
