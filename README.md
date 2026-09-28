# Gerador de sites e apps (já hospedado)

Bot simples em Python que gera uma landing page pronta.

## Site de demonstração

Quando o GitHub Pages estiver ativo neste repositório:

https://marcioedeidi.github.io/gerador-sites-apps/

Se o link ainda não abrir, ative uma vez em:
**Settings → Pages → Source: GitHub Actions**

## Como gerar um site novo

```bash
python3 bot.py --nome "Minha Marca" --nicho "consultoria" --cta "Quero orçamento"
```

Isso cria `site/index.html`.

## Como entregar já funcionando

1. Copie o HTML gerado para a pasta `site/` deste repositório.
2. Faça commit e push para `main`.
3. O workflow de GitHub Pages publica o site.
4. Você entrega o link público.
