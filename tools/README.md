# Banner do perfil

`render_banner.py` gera um GIF de terminal e um PNG estático. Ambos usam azul/amarelo para acompanhar o portfólio. O nome e a especialidade permanecem visíveis desde o primeiro frame; o terminal é uma ilustração, sem execução de comandos reais.

O GIF toca uma única vez por carregamento, por menos de cinco segundos, e termina com todas as linhas visíveis. Não depende de serviço remoto de animação ou de JavaScript no README.

Para regenerar, instale Pillow no ambiente de desenvolvimento e execute:

```sh
python tools/render_banner.py
```

Usa DM Sans e Fira Code, as mesmas fontes do portfólio, versionadas em `tools/fonts/` sob a SIL Open Font License (textos da licença na mesma pasta), então o resultado é igual em qualquer sistema. `assets/profile-banner.png` é a versão estática, usada no README para quem ativou movimento reduzido.

## Previews dos projetos

`render_previews.py` gera `assets/preview-bot-alertas.png`, uma ilustração no formato das mensagens do bot, com oferta e loja fictícias, e, se receber o caminho de `docs/assets/overview.png` do repositório mapaderotas, recorta a captura da demo (dados fictícios) em `assets/preview-route-coverage.png`:

```sh
python tools/render_previews.py ../mapaderotas/docs/assets/overview.png
```
