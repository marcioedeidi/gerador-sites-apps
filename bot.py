#!/usr/bin/env python3
"""
Gerador de sites estáticos prontos para hospedar.
Uso:
  python bot.py --nome "Studio Pulse" --nicho "estúdio criativo" --cta "Quero um site"
Gera a pasta ./site com index.html pronto para GitHub Pages / Netlify / Vercel.
"""
from __future__ import annotations

import argparse
import html
from pathlib import Path


TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;600&display=swap" rel="stylesheet" />
  <style>
    :root {{ --bg:#07080c; --text:#f4f1ea; --muted:#9aa0ae; --gold:#e8c47a; --line:rgba(255,255,255,.08); }}
    * {{ box-sizing:border-box; margin:0; padding:0; }}
    body {{ font-family:Outfit,system-ui,sans-serif; background:var(--bg); color:var(--text); }}
    .wrap {{ max-width:960px; margin:0 auto; padding:48px 20px 80px; }}
    h1 {{ font-family:"Instrument Serif",serif; font-size:clamp(40px,8vw,76px); line-height:.95; font-weight:400; }}
    h1 em {{ color:var(--gold); font-style:italic; }}
    p.lead {{ margin-top:20px; color:var(--muted); max-width:46ch; font-size:18px; }}
    a.btn {{ display:inline-block; margin-top:28px; background:var(--gold); color:#111; text-decoration:none; padding:14px 18px; border-radius:999px; font-weight:600; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin-top:56px; }}
    .card {{ border:1px solid var(--line); border-radius:18px; padding:18px; background:#10131a; }}
    .card h3 {{ margin-bottom:8px; }}
    .card p {{ color:var(--muted); font-size:14px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>{heading}</h1>
    <p class="lead">{lead}</p>
    <a class="btn" href="{cta_url}">{cta}</a>
    <section class="grid">
      <article class="card"><h3>Rápido</h3><p>Página gerada automaticamente e pronta para publicar.</p></article>
      <article class="card"><h3>No ar</h3><p>Hospede em GitHub Pages, Netlify ou Vercel em minutos.</p></article>
      <article class="card"><h3>Seu nicho</h3><p>{nicho}</p></article>
    </section>
  </div>
</body>
</html>
"""


def generate(nome: str, nicho: str, cta: str, cta_url: str, out_dir: Path) -> Path:
    title = html.escape(nome)
    heading = f"{html.escape(nome)} <em>já no ar.</em>"
    lead = html.escape(
        f"Landing page criada para {nicho}. Conteúdo inicial pronto para você personalizar e publicar."
    )
    page = TEMPLATE.format(
        title=title,
        heading=heading,
        lead=lead,
        cta=html.escape(cta),
        cta_url=html.escape(cta_url, quote=True),
        nicho=html.escape(nicho),
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "index.html"
    dest.write_text(page, encoding="utf-8")
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera um site estático pronto para hospedar.")
    parser.add_argument("--nome", required=True, help="Nome da marca ou do projeto")
    parser.add_argument("--nicho", required=True, help="Nicho ou descrição curta")
    parser.add_argument("--cta", default="Falar agora", help="Texto do botão")
    parser.add_argument("--cta-url", default="#contato", help="Link do botão")
    parser.add_argument("--out", default="site", help="Pasta de saída")
    args = parser.parse_args()
    path = generate(args.nome, args.nicho, args.cta, args.cta_url, Path(args.out))
    print(f"Site gerado em {path.resolve()}")
    print("Publique a pasta 'site' no GitHub Pages, Netlify ou Vercel para entregar o link funcionando.")


if __name__ == "__main__":
    main()
