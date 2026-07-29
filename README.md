<!-- Header animado -->
<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&duration=2800&pause=400&color=FFC72C&background=FFFFFF00&random=false&width=760&height=70&lines=Ol%C3%A1%2C+eu+sou+Jo%C3%A3o+Victor+Faraco+%F0%9F%91%8B;Analista+de+Sistemas+%7C+MBA+em+Intelig%C3%AAncia+Artificial;Construindo+IA+aplicada+em+opera%C3%A7%C3%B5es+reais;Python+%7C+FastAPI+%7C+pandas+%7C+Leaflet+%7C+Azure+OpenAI)](https://git.io/typing-svg)

</div>

---

## 🧠 Sobre Mim

Analista de Sistemas com foco em **IA aplicada a processos operacionais**. Atuo na Orsegups desenvolvendo projetos que combinam automação, inteligência de dados e agentes de IA em operações reais — do campo ao dashboard.

Na prática, isso significa ir da ponta à ponta: **backend em Python** (FastAPI, pandas, integração com APIs), **frontend e visualização** (JavaScript, Chart.js, Leaflet) e o **deploy** que coloca aquilo na mão de quem precisa. Trato **privacidade e LGPD como requisito de arquitetura**, não como checklist do fim — minimização de PII, allowlist no payload e retenção só do que é agregado.

Atualmente cursando **MBA em Inteligência Artificial** na Estácio de Sá, com formação em Gestão da Tecnologia da Informação.

> *"Não basta implementar IA. Precisa resolver o problema certo."*

---

## 🚀 O que estou construindo

**Públicos — com demo ao vivo**

| Projeto | Descrição | Stack |
|--------|-----------|-------|
| 🗺️ **[Route Coverage Map](https://github.com/JvFaraco/mapaderotas)** · [demo](https://jvfaraco.github.io/mapaderotas/) | Pipeline geoespacial que transforma planilhas de rotas (só nomes, sem coordenadas) em um mapa autocontido: geocodificação progressiva, malha oficial do IBGE, fallback por Voronoi e corte de sobreposição entre áreas. CI com lint, tipos e piso de 80% de cobertura | Python · Leaflet · IBGE |
| 📊 **[Operations Dashboard Platform](https://github.com/JvFaraco/operational-dashboard-platform)** · [demo](https://jvfaraco.github.io/operational-dashboard-platform/) | Plataforma que transforma planilhas operacionais dispersas em cinco módulos navegáveis: controle de O.S, agendadas, não agendadas, risco contratual e mapa de cobertura | Flask · pandas · Chart.js |

**Internos — em produção na operação**

| Projeto | Descrição | Stack |
|--------|-----------|-------|
| 🔍 **Validação de O.S com IA** | Coleta autenticada das O.S, monta o pacote completo (telemetria da central, equipamentos, fotos) e aplica uma régua determinística de checagens antes de qualquer IA. Anexa o contrato assinado convertendo o PDF em imagens, com rotação de token e minimização de PII em duas camadas de payload | Python · LLMs · APIs |
| 🛡️ **Portal Operacional A365** | Portal interno que reúne as ferramentas da operação atrás de um único login: dashboard de O.S atualizado a cada 60s, mapa de rotas e área administrativa. Senha em argon2id, sessão em cookie httpOnly, deploy em VPS com systemd atrás de HTTPS | FastAPI · SQLite · JavaScript |
| ↔️ **Vazão do Dia** | Responde "estamos zerando ou acumulando chamado?" — O.S abertas × fechadas no dia, com saldo e quebras por supervisor, regional e tipo. Janela tratada no fuso de São Paulo, histórico só agregado por decisão de LGPD e paleta validada para daltonismo | Python · Playwright |
| 🤖 **Agente de Classificação de O.S** | Agente de IA que classifica Ordens de Serviço dos especialistas de campo usando a taxonomia padronizada TIPO / MOTIVO / PROBLEMA / SOLUÇÃO, reduzindo erro de classificação e retrabalho | Copilot Studio · Azure OpenAI |

---

## 🛠️ Tecnologias & Ferramentas

**IA & Dados**

![Python](https://img.shields.io/badge/Python-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white)
![Azure OpenAI](https://img.shields.io/badge/Azure%20OpenAI-%230078D4.svg?&style=for-the-badge&logo=microsoftazure&logoColor=white)
![Copilot Studio](https://img.shields.io/badge/Copilot%20Studio-%23742774.svg?&style=for-the-badge&logo=microsoft&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?&style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-%23F2C811.svg?&style=for-the-badge&logo=powerbi&logoColor=black)

**Backend**

![FastAPI](https://img.shields.io/badge/FastAPI-%23009688.svg?&style=for-the-badge&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-%2307405E.svg?&style=for-the-badge&logo=sqlite&logoColor=white)

**Frontend & Visualização**

![HTML5](https://img.shields.io/badge/HTML5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black)
![Chart.js](https://img.shields.io/badge/Chart.js-%23FF6384.svg?&style=for-the-badge&logo=chartdotjs&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-%23199900.svg?&style=for-the-badge&logo=leaflet&logoColor=white)

**Infra & Qualidade**

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-%232671E5.svg?&style=for-the-badge&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-%23FCC624.svg?&style=for-the-badge&logo=linux&logoColor=black)
![pytest](https://img.shields.io/badge/pytest-%230A9EDC.svg?&style=for-the-badge&logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-%232EAD33.svg?&style=for-the-badge&logo=playwright&logoColor=white)

---

## 📚 Educação & Certificações

- 🎓 **MBA em Inteligência Artificial** — Estácio de Sá *(em andamento)*
- 🎓 **Gestão da Tecnologia da Informação** — Estácio de Sá *(2025)*

![Udemy](https://img.shields.io/badge/Udemy-%23A435F0.svg?&style=for-the-badge&logo=udemy&logoColor=white) **Python Completo do Zero ao Avançado + Projetos Reais** — *jul 2022*

![Estácio](https://img.shields.io/badge/Est%C3%A1cio-%230066CC.svg?&style=for-the-badge&logo=graduationcap&logoColor=white) **Aplicação da Melhoria Contínua** — *jun 2024*

![Estácio](https://img.shields.io/badge/Est%C3%A1cio-%230066CC.svg?&style=for-the-badge&logo=graduationcap&logoColor=white) **Implantação de Governança de T.I.** — *jun 2024*

![Estácio](https://img.shields.io/badge/Est%C3%A1cio-%230066CC.svg?&style=for-the-badge&logo=graduationcap&logoColor=white) **Gestão de Projetos e de Informação** — *mar 2024*

![Estácio](https://img.shields.io/badge/Est%C3%A1cio-%230066CC.svg?&style=for-the-badge&logo=graduationcap&logoColor=white) **Programação para Internet** — *ago 2023*

---

## 💼 Experiência Profissional

**Orsegups** · Analista de Sistemas · *03/2025 — Atual*
- Portal interno em FastAPI + SQLite reunindo as ferramentas da operação atrás de um único login, com deploy em VPS
- Backend de validação de O.S com IA: coleta autenticada, régua determinística de checagens e anexo automático do contrato assinado
- Coletores que substituíram a extração manual de planilhas, alimentando dashboards que atualizam sozinhos
- Dashboards de O.S, produtividade e vazão do dia usados por supervisores em 22 regionais
- Cobertura geográfica das rotas de campo com pipeline geoespacial (geocodificação em cascata, IBGE e Voronoi)
- Privacidade por design em todos os projetos: minimização de PII, allowlist de payload e retenção só de dado agregado
- Padronização dos fluxos e da taxonomia de dados de campo usada pela Operação, NAC e BackOffice

**Orsegups** · Especialista em Testes de Hardware · *09/2024 — 03/2025*
- Dashboards para monitoramento do ciclo de vida de equipamentos (RMA, novos, testados e em campo)
- Reestruturei o sistema de testes da fábrica separando o fluxo NOVOS vs. RMA, eliminando input manual que gerava erro de classificação

**Figueirense Futebol Clube** · Estágio TI · *02/2024 — 09/2024*

**Instituto São José** · Estágio TI · *10/2022 — 10/2023*

---

## 📫 Conecte-se Comigo

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joão-victor-faraco-01066423a)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/jvfaraco/)
[![Portfolio](https://img.shields.io/badge/Portfolio-%231E3A8A.svg?&style=for-the-badge&logo=githubpages&logoColor=white)](https://jvfaraco.github.io/jvfaraco-portifolio/)
[![Email](https://img.shields.io/badge/Email-%23EA4335.svg?&style=for-the-badge&logo=gmail&logoColor=white)](mailto:joaovictorfaraco@gmail.com)

</div>

---

<div align="center">
  <img src="https://komarev.com/ghpvc/?username=JvFaraco&color=1E3A8A&style=flat-square&label=Visualizações+do+perfil" alt="profile views" />
</div>
