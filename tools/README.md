# Banner do perfil

`render_banner.py` gera um GIF de terminal e um PNG estático. Ambos usam azul/amarelo para acompanhar o portfólio. O nome e a especialidade permanecem visíveis desde o primeiro frame; o terminal é uma ilustração, sem execução de comandos reais.

O GIF toca uma única vez por carregamento, por menos de cinco segundos, e termina com todas as linhas visíveis. Não depende de serviço remoto de animação ou de JavaScript no README.

Para regenerar, instale Pillow no ambiente de desenvolvimento e execute:

```sh
python tools/render_banner.py
```

Usa DM Sans e Fira Code, as mesmas fontes do portfólio, versionadas em `tools/fonts/` sob a SIL Open Font License (textos da licença na mesma pasta), então o resultado é igual em qualquer sistema. `assets/profile-banner.png` é a versão estática, usada no README para quem ativou movimento reduzido.

## Previews dos projetos

`render_previews.py` gera `assets/preview-bot-alertas.png`, uma ilustração no formato das mensagens do bot, com oferta e loja fictícias:

```sh
python tools/render_previews.py
```

`record_route_preview.py` grava `assets/preview-route-coverage.gif` a partir da demo publicada do mapaderotas (dados fictícios): um cursor desenhado passa sobre uma área, seleciona a rota, aproxima o mapa, abre uma área aproximada e troca para o tema claro. É stop-motion (uma captura por passo do cursor; o que a página anima sozinha é gravado em tempo real), em loop, com cerca de 13 s, abaixo de 1 MB e na mesma proporção do GIF da extensão. `assets/preview-route-coverage.png` é um quadro da mesma gravação, usado para quem ativou movimento reduzido. Precisa de Playwright (Chromium), Pillow e internet:

```sh
python tools/record_route_preview.py
```

Os outros dois previews não são gerados por script:

- `assets/preview-quick-replies.gif` é o `docs/demo.gif` do repositório quick-replies (dados fictícios); `assets/preview-quick-replies.png` é o último quadro, usado para quem ativou movimento reduzido.
- `assets/preview-certificados.png` é uma captura da seção de certificados do portfólio, reduzida para 800 px de largura. Os dados pessoais dos documentos já aparecem cobertos no portfólio.
