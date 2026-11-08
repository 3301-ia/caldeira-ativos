#!/usr/bin/env python3
"""Robo do acervo Caldeira.

Le as fichas com imagem fora do acervo, baixa cada imagem, grava em acervo/
e devolve o link definitivo para o sistema. Roda no GitHub Actions: nao depende
do computador de ninguem, nem de mensagem do agente.
"""
import json, os, re, sys, unicodedata, urllib.parse, urllib.request

API = os.environ.get("API", "https://romerito-agente-9f88b64a.base44.app/functions/caldeiraReceber")
TOKEN = os.environ.get("TOKEN", "cg-perchance-2026")
RAW = "https://raw.githubusercontent.com/3301-ia/caldeira-ativos/main/"
LIMITE = 7_000_000


def slug(texto):
    t = unicodedata.normalize("NFD", str(texto))
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:48] or "receita"


def buscar(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read()


def pendentes():
    with urllib.request.urlopen(API + "?pendentes=1", timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def devolver(ficha_id, link):
    corpo = json.dumps({"token": TOKEN, "atualizar_id": ficha_id, "foto_arquivada": link}).encode()
    req = urllib.request.Request(API, data=corpo, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    try:
        dados = pendentes()
    except Exception as e:
        print("Porta de entrada indisponivel agora:", str(e)[:160])
        print("Nada a fazer nesta rodada.")
        return 0

    fichas = dados.get("fichas", [])
    print("Pendentes:", len(fichas))
    feitas = 0

    for f in fichas:
        nome, origem, fid = f.get("nome", ""), f.get("foto_url", ""), f.get("id", "")
        try:
            req = urllib.request.Request(origem, headers={"User-Agent": "CaldeiraBot/1.0"})
            with urllib.request.urlopen(req, timeout=45) as r:
                tipo = r.headers.get("Content-Type", "image/jpeg")
                if not tipo.startswith("image/"):
                    print("ignorado, nao e imagem:", origem[:60]); continue
                dados_img = r.read()
            if len(dados_img) > LIMITE:
                print("ignorado, acima de 7MB:", nome); continue
            ext = "png" if "png" in tipo else "webp" if "webp" in tipo else "jpg"
            destino = "acervo/%s-%s.%s" % (slug(nome), fid[:6], ext)
            os.makedirs("acervo", exist_ok=True)
            with open(destino, "wb") as arq:
                arq.write(dados_img)
            link = urllib.parse.urljoin(RAW, destino)
            devolver(fid, link)
            print("arquivada:", nome, "->", link)
            feitas += 1
        except Exception as e:
            print("falhou em", nome, ":", str(e)[:120])

    print("Total arquivado nesta rodada:", feitas)
    return 0


if __name__ == "__main__":
    sys.exit(main())
