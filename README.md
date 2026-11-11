<a href="https://jvfaraco.github.io/jvfaraco-portifolio/">
  <picture>
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/profile-banner.png" />
    <img src="assets/profile-banner.gif" alt="Banner de João Victor Faraco, Analista de Sistemas em São José, SC: Python, automação e integrações. Ao lado, um terminal ilustrativo mostra a pré-validação de uma O.S.: regras conferidas, sugestão da IA e decisão humana. Leva ao portfólio." width="100%" />
  </picture>
</a>

### Oi, eu sou o João 👋
**Analista de Sistemas na Orsegups · MBA em Inteligência Artificial · São José, SC**

Construo ferramentas com **IA aplicada, Python e automação** para problemas reais da operação. A principal é um validador de O.S. com IA, em uso todos os dias, que já conferiu mais de 2.300 ordens de serviço. Nos meus projetos, a IA trabalha junto com regras verificáveis e saída estruturada, e a decisão final é sempre de uma pessoa. Comecei no suporte e passei por testes de hardware, por isso penso no código e também em quem vai usar a ferramenta.

[**Conheça meu portfólio ↗**](https://jvfaraco.github.io/jvfaraco-portifolio/) · [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-victor-faraco-01066423a/) · [E-mail](mailto:joaovictorfaraco@gmail.com)

### Projetos para explorar
Cada um tem uma demo aberta no navegador, sem instalar nada.

<table><tr>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/os-validator-demo/"><picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/preview-os-validator.png" /><img src="assets/preview-os-validator.gif" alt="Demo interativa do validador, com O.S. fictícias: o cursor abre uma O.S. cuja nota tenta dar ordem ao sistema, que vai para revisão humana na guarda de comando sem chamar a IA; depois uma O.S. com sensor trocado sem devolução, que volta ao técnico nas regras; e uma O.S. com nome e telefone na nota, que viram marcadores antes de sair da máquina." width="100%" /></picture></a><br><b>🤖 Validador de O.S. com IA</b><br>Versão pública do validador que mantenho em produção. As regras em Python vêm primeiro, a IA só lê a nota do técnico e escolhe dentro de um catálogo fechado (JSON Schema), e a aprovação é sempre humana. Na demo, você segue cada O.S. etapa por etapa.<br><br>No gabarito rotulado à mão, o Claude Haiku acertou <b>38 de 38</b> decisões, numa rodada de menos de 1 centavo de dólar.<br><code>Python</code> <code>LLM</code> <code>JSON Schema</code> <code>pytest</code> · <a href="https://jvfaraco.github.io/os-validator-demo/">Demo</a> · <a href="https://github.com/JvFaraco/os-validator-demo">Código</a></td>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/binance-daytrade/?modo=pro"><picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/preview-binance-daytrade.png" /><img src="assets/preview-binance-daytrade.gif" alt="Painel do binance-daytrade com dados públicos ao vivo: uma esfera de 10 mil fios gira, cada fio é um replay da sessão, verde quando terminou no lucro e vermelho no prejuízo; o cursor troca o alvo e o stop do plano e a esfera é refeita." width="100%" /></picture></a><br><b>📈 Day trade na Binance, com pesquisa honesta</b><br>Skill do Claude para day trade spot: scanner de rompimento, 10.000 replays da sessão, backtest com treino e teste, e ordem só depois do seu sim (testnet por padrão). Testada com taxas e walk-forward, a regra não deu lucro: <b>0 de 88</b> combinações positivas fora da amostra. O painel mostra isso, sem esconder o resultado.<br><code>Python</code> <code>TypeScript</code> <code>Backtest</code> <code>Claude Skills</code> · <a href="https://jvfaraco.github.io/binance-daytrade/">Painel</a> · <a href="https://github.com/JvFaraco/binance-daytrade">Código</a></td>
</tr><tr>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/mapaderotas/"><picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/preview-route-coverage.png" /><img src="assets/preview-route-coverage.gif" alt="Demonstração da demo do Route Coverage Map, com dados fictícios: o cursor passa sobre uma área e aparece o nome dela; o clique acende a rota e abre a ficha; o mapa aproxima a rota, uma área hachurada explica por que é aproximada, e a tela passa para o tema claro." width="100%" /></picture></a><br><b>🗺️ Route Coverage Map</b><br>De uma planilha de rotas a um mapa de cobertura navegável: geocodificação em cascata, limites do IBGE e, onde não há limite oficial, área aproximada por Voronoi e marcada como aproximada.<br><code>Python</code> <code>Leaflet</code> <code>GIS</code> <code>GitHub Actions</code> · <a href="https://jvfaraco.github.io/mapaderotas/">Demo</a> · <a href="https://github.com/JvFaraco/mapaderotas">Código</a></td>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/quick-replies/"><picture><source media="(prefers-reduced-motion: reduce)" srcset="assets/preview-quick-replies.png" /><img src="assets/preview-quick-replies.gif" alt="Demonstração da extensão: o atendente digita barra no campo de mensagem, escolhe uma resposta pronta e ela é inserida no campo, com saudação e nome fictícios." width="100%" /></picture></a><br><b>💬 Extensão de respostas rápidas</b><br>Extensão Chrome para quem atende em chat web: digite / no campo, escolha a resposta e insira com Tab. A biblioteca da equipe é sincronizada por planilha, e quem envia é sempre o atendente.<br><code>JavaScript</code> <code>Chrome MV3</code> <code>Playwright</code> · <a href="https://jvfaraco.github.io/quick-replies/">Demo</a> · <a href="https://github.com/JvFaraco/quick-replies">Código</a> · <a href="https://github.com/JvFaraco/quick-replies/releases/latest">Baixar</a></td>
</tr><tr>
<td width="50%" valign="top"><a href="https://jvfaraco.github.io/mapa-antenas-anatel/"><img src="assets/preview-mapa-antenas.png" alt="Mapa de Antenas Anatel em tema escuro: milhares de pontos coloridos por operadora sobre o Sul do Brasil, com a busca por endereço e o lote de pontos no painel à esquerda." width="100%" /></a><br><b>📡 Mapa de Antenas Anatel</b><br>Todas as antenas de celular licenciadas na Anatel num HTML único que funciona offline. Cole uma coordenada e veja a antena mais próxima de cada operadora e a tecnologia (2G a 5G). A base pública, com 3,3 milhões de linhas consolidadas, é atualizada toda semana. Evolução de um mapa de Cliver Guisolphi.<br><code>JavaScript</code> <code>Python</code> <code>Dados abertos</code> · <a href="https://jvfaraco.github.io/mapa-antenas-anatel/">Mapa</a> · <a href="https://github.com/JvFaraco/mapa-antenas-anatel">Código</a></td>
<td width="50%" valign="top"><a href="https://github.com/JvFaraco/bot-telegram"><img src="assets/preview-bot-alertas.png" alt="Ilustração de duas mensagens do bot no Telegram, com produto, preço, desconto, loja, cupom e link. Oferta e loja fictícias." width="100%" /></a><br><b>📬 Bot de alertas no Telegram</b><br>Monitora ofertas com filtros de preço, desconto e palavras-chave, e avisa no Telegram sem repetir notificação. Roda agendado no GitHub Actions.<br><code>Python</code> <code>Scraping</code> <code>Telegram API</code> · <a href="https://github.com/JvFaraco/bot-telegram">Código</a></td>
</tr></table>

<sub>As prévias são gravações das demos publicadas, com dados fictícios ou públicos. O painel da Binance usa só dados públicos de mercado e não envia ordens. O bot é uma ilustração no formato real das mensagens, com oferta fictícia.</sub>

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
- **IA aplicada:** LLMs com saída estruturada (JSON Schema) e catálogo fechado, avaliação contra gabarito, skills do Claude e servidores MCP, Copilot Studio, Power Automate e OCR, sempre com regras e decisão final humana. <sub>Validador de OS com IA, binance-daytrade e assistente operacional.</sub>
- **Python e automação de processos:** scripts, rotinas agendadas, planilhas e scraping. <sub>Bot de alertas, Route Coverage Map e ferramentas internas.</sub>
- **Integração de sistemas e APIs REST:** consumo de APIs e sincronização com deduplicação, nova tentativa e reconciliação. <sub>Integração de OS com CRM e bot de alertas.</sub>
- **Dados:** SQL/SQLite, pipelines (ETL), dados abertos e geográficos, backtest com walk-forward. <sub>Route Coverage Map, Mapa de Antenas, binance-daytrade e relatórios internos.</sub>
- **Backend e web:** FastAPI, JavaScript e TypeScript, extensões Chrome e páginas estáticas no GitHub Pages.
- **Qualidade e entrega:** Git, GitHub Actions (CI/CD), pytest e Playwright. <sub>CI do Route Coverage Map e da extensão, suíte do validador de OS.</sub>
- **Privacidade de dados e documentação:** minimização de PII e documentação de arquitetura e operação. <sub>Varredura de PII no CI do mapa e sanitização no validador.</sub>

### De onde venho e o que estou estudando
**Orsegups — Analista de Sistemas** · desde março/2025<br>
Automação, integrações e ferramentas para operação, suporte e backoffice.

**MBA em Inteligência Artificial** · Estácio de Sá · concluído em 2026 · [certificados e diploma](https://jvfaraco.github.io/jvfaraco-portifolio/#certificados)

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
