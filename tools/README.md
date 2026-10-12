# Banner do perfil

`render_banner.py` gera um GIF de terminal e um PNG estático. Ambos usam azul/amarelo para acompanhar o portfólio. O nome e a especialidade permanecem visíveis desde o primeiro frame; o terminal é uma ilustração, sem execução de comandos reais.

O GIF toca uma única vez por carregamento, por menos de cinco segundos, e termina com todas as linhas visíveis. Não depende de serviço remoto de animação ou de JavaScript no README.

Para regenerar, instale Pillow no ambiente de desenvolvimento e execute:

```sh
python tools/render_banner.py
```

No Windows, usa Segoe UI e Consolas já instaladas. `--font-dir` permite escolher a pasta; em outros sistemas usa DejaVu Sans/Mono como alternativa. As fontes não são redistribuídas. `assets/profile-banner.png` é a versão estática.
