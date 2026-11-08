# -*- coding: utf-8 -*-
import csv

P = "CG"
familias = {
    ("01", "Salgados"): {
        "01": "Pães de queijo e biscoitos",
        "02": "Assados enrolados",
        "03": "Empadas",
        "04": "Esfirras e tortas",
        "05": "Quibes",
    },
    ("02", "Sanduíches"): {
        "01": "Hambúrgueres",
        "02": "Quentes",
        "03": "Frios",
    },
    ("03", "Espetos"): {
        "01": "Carnes",
        "02": "Aves",
        "03": "Queijos",
    },
    ("04", "Porções"): {
        "01": "Carnes",
        "02": "Aves",
        "03": "Peixes",
        "04": "Fritas e acompanhamentos",
        "05": "Caldos",
        "06": "Pastéis",
        "07": "Ovos",
    },
    ("05", "Bebidas"): {
        "01": "Águas",
        "02": "Refrigerantes",
        "03": "Energéticos e isotônicos",
        "04": "Sucos",
        "05": "Achocolatados",
    },
    ("06", "Cervejas"): {
        "01": "Lata 473 ml",
        "02": "Lata 350 ml e longneck",
        "03": "Garrafa 600 ml",
    },
    ("07", "Drinks e doses"): {
        "01": "Drinks",
        "02": "Doses",
    },
    ("08", "Vinhos e espumantes"): {
        "01": "Espumantes",
        "02": "Tintos",
        "03": "Brancos",
        "04": "Rosés",
    },
}

mapa = {}
for (cod, nome), subs in familias.items():
    mapa[cod] = (nome, subs)

itens = [
    # (familia, subfamilia, nome, preco, unidade, observacao)
    ("01","01","Pão de queijo",5.00,"un",""),
    ("01","01","Pão de queijo recheado",8.00,"un",""),
    ("01","01","Biscoito de queijo",5.00,"un",""),
    ("01","02","Enrolado de salsicha assado",8.00,"un",""),
    ("01","02","Enrolado de presunto e queijo assado",8.00,"un",""),
    ("01","03","Empada de frango",8.50,"un",""),
    ("01","03","Empada de carne seca",8.60,"un",""),
    ("01","03","Empada de alho poró",8.60,"un",""),
    ("01","04","Esfirra de carne",10.00,"un",""),
    ("01","04","Torta de frango com requeijão",10.00,"un",""),
    ("01","05","Kibe",10.00,"un",""),

    ("02","01","X-Burguer",18.50,"un","hambúrguer bovino 120g, queijo, alface, tomate"),
    ("02","01","X-Egg Bacon",24.00,"un","hambúrguer bovino 120g, bacon, ovo, queijo"),
    ("02","01","Burguer Artesanal",38.00,"un","Angus 180g, cheddar, bacon, batata frita"),
    ("02","02","Misto quente",8.60,"un",""),
    ("02","02","Misto quente especial",10.60,"un",""),
    ("02","02","Queijo quente",9.00,"un",""),
    ("02","03","Sanduíche natural",17.30,"un",""),

    ("03","01","Espeto de alcatra",15.80,"un",""),
    ("03","02","Espeto de frango",15.80,"un",""),
    ("03","02","Espeto de coração",15.80,"un",""),
    ("03","02","Espeto de salsichão",15.80,"un","insumo CG.11.03.002"),
    ("03","02","Espeto de medalhão de frango",15.80,"un",""),
    ("03","03","Espeto de queijo coalho",15.80,"un",""),
    ("03","01","Espeto de mignon",19.50,"un",""),

    ("04","01","Filé mignon 400g com fritas",96.50,"porção",""),
    ("04","01","Filé mignon 400g",75.80,"porção",""),
    ("04","03","Peixe à doré 400g com fritas",74.00,"porção",""),
    ("04","03","Peixe à doré 400g",53.00,"porção",""),
    ("04","04","Fritas com queijo e bacon 400g",35.00,"porção",""),
    ("04","05","Caldos diversos",25.90,"porção",""),
    ("04","02","Cubos de frango empanados 400g",43.50,"porção",""),
    ("04","02","Cubos de frango empanados 400g com fritas",54.00,"porção",""),
    ("04","02","Peito de frango à palito grelhado 400g",43.50,"porção",""),
    ("04","02","Peito de frango à palito grelhado 400g com fritas",54.00,"porção",""),
    ("04","04","Fritas 400g",24.00,"porção",""),
    ("04","04","Torresmo 400g",30.00,"porção",""),
    ("04","06","Pastel de queijo ou carne, 15 mini",16.80,"porção","mini pastéis, caixa fechada"),
    ("04","07","Omelete de presunto, queijo e tomate",24.00,"porção",""),

    ("05","01","Água com gás",6.00,"un",""),
    ("05","01","Água sem gás",6.00,"un",""),
    ("05","01","Água de coco",13.00,"un",""),
    ("05","02","Pepsi Black",7.00,"un",""),
    ("05","02","Pepsi",7.00,"un",""),
    ("05","02","Guaraná",7.00,"un",""),
    ("05","02","Guaraná zero",7.00,"un",""),
    ("05","02","Soda",7.00,"un",""),
    ("05","02","Soda zero",7.00,"un",""),
    ("05","02","Sukita laranja",7.00,"un","a confirmar no PDV"),
    ("05","02","Sukita uva",7.00,"un","a confirmar no PDV"),
    ("05","02","Tônica",7.00,"un",""),
    ("05","02","Tônica zero",7.00,"un",""),
    ("05","02","H2O",9.20,"un",""),
    ("05","02","Limoneto",9.20,"un",""),
    ("05","03","Red Bull",15.50,"un",""),
    ("05","03","Gatorade",9.30,"un",""),
    ("05","04","Suco Tial",9.30,"un",""),
    ("05","04","Suco natural",11.00,"un",""),
    ("05","05","Toddynho ou Nescau",6.00,"un",""),

    ("06","01","Stella 473 ml",12.50,"un","centavos a confirmar"),
    ("06","01","Stella Pure Gold 473 ml",13.60,"un","centavos a confirmar"),
    ("06","01","Original 473 ml",12.50,"un","centavos a confirmar"),
    ("06","01","Spaten 473 ml",12.50,"un","centavos a confirmar"),
    ("06","01","Corona Extra 473 ml",13.60,"un","centavos a confirmar"),
    ("06","01","Budweiser Zero 473 ml",15.00,"un","centavos a confirmar"),
    ("06","02","Stella 350 ml",11.50,"un",""),
    ("06","02","Spaten 350 ml",11.50,"un",""),
    ("06","02","Corona Extra longneck",13.50,"un",""),
    ("06","02","Corona Cero 350 ml",13.00,"un",""),
    ("06","02","Stella Pure Gold longneck",13.50,"un","a conferir inversão com a lata"),
    ("06","03","Stella 600 ml",19.20,"un",""),
    ("06","03","Stella Pure Gold 600 ml",22.00,"un",""),
    ("06","03","Original 600 ml",17.20,"un",""),
    ("06","03","Spaten 600 ml",19.20,"un",""),
    ("06","03","Serramalte 600 ml",17.60,"un",""),

    ("07","01","Caipirinha",25.00,"dose",""),
    ("07","01","Caipifruta Smirnoff",30.60,"dose",""),
    ("07","01","Caipifruta Absolut",33.50,"dose",""),
    ("07","01","Gin tônica",30.60,"dose",""),
    ("07","01","Mojito",29.50,"dose",""),
    ("07","01","Soda italiana",25.00,"dose",""),
    ("07","02","Dose Smirnoff",16.00,"dose",""),
    ("07","02","Dose Absolut",22.00,"dose",""),
    ("07","02","Dose Campari",11.00,"dose",""),
    ("07","02","Dose Boazinha",10.00,"dose",""),
    ("07","02","Dose Seleta",11.00,"dose",""),
    ("07","02","Dose Salinas",9.30,"dose",""),
    ("07","02","Dose Vale Verde",14.00,"dose",""),
    ("07","02","Dose de whisky",25.00,"dose",""),

    ("08","01","Espumante Seival Brut branco",130.00,"garrafa",""),
    ("08","01","Espumante Seival Brut rosé",130.00,"garrafa",""),
    ("08","02","Sol Sul Malbec",145.00,"garrafa",""),
    ("08","02","Bodegas Centenário",150.00,"garrafa",""),
    ("08","02","Miolo Blend",130.00,"garrafa",""),
    ("08","02","Miolo Cabernet Sauvignon e Merlot",130.00,"garrafa",""),
    ("08","02","Don Luciano Tinto",130.00,"garrafa",""),
    ("08","02","Seival Tempranillo",130.00,"garrafa",""),
    ("08","03","Miolo Seleção Chardonnay e Viognier",150.00,"garrafa",""),
    ("08","03","Seival Blanc",150.00,"garrafa",""),
    ("08","04","Seival Rosé",150.00,"garrafa",""),
]

# sequencial dentro de cada familia+subfamilia
contador = {}
linhas = []
for fam, sub, nome, preco, un, obs in itens:
    chave = (fam, sub)
    contador[chave] = contador.get(chave, 0) + 1
    codigo = f"{P}.{fam}.{sub}.{contador[chave]:03d}"
    compacto = f"{P}{fam}{sub}{contador[chave]:03d}"
    linhas.append({
        "codigo": codigo,
        "codigo_sistema": compacto,
        "familia": f"{fam} {mapa[fam][0]}",
        "subfamilia": f"{fam}.{sub} {mapa[fam][1][sub]}",
        "item": nome,
        "preco": f"{preco:.2f}".replace(".", ","),
        "unidade": un,
        "observacao": obs,
    })

with open("cardapio_codigos.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["codigo","codigo_sistema","familia","subfamilia","item","preco","unidade","observacao"])
    w.writeheader(); w.writerows(linhas)

# documento de leitura
with open("cardapio_codigos.md", "w", encoding="utf-8") as f:
    f.write("# Cardápio Caldeira Gourmet · tabela de códigos\n\n")
    f.write("Prefixo do restaurante: **CG** (Caldeira Gourmet).\n")
    f.write("Formato: `CG.família.subfamília.sequencial`, seis dígitos no núcleo, prefixo separado por ponto.\n")
    f.write("Forma compacta para o sistema: `CG` seguido dos seis dígitos, sem pontos.\n\n")
    f.write(f"Total de itens: **{len(linhas)}**.\n\n")
    fam_atual = None
    for l in linhas:
        if l["familia"] != fam_atual:
            fam_atual = l["familia"]
            f.write(f"\n## {fam_atual}\n\n")
            f.write("| Código | Item | Preço |\n|---|---|---|\n")
        f.write(f"| `{l['codigo']}` | {l['item']} | {l['preco']} |\n")
    f.write("\n## Regras do código\n\n")
    f.write("1. O código nunca muda. Preço muda, nome muda, código não.\n")
    f.write("2. Item novo entra no fim da subfamília, com o próximo sequencial.\n")
    f.write("3. Item descontinuado não é apagado: fica inativo e o código não é reaproveitado.\n")
    f.write("4. O prefixo CG permite juntar bases de projetos diferentes sem colisão. A plataforma de personagens usará outro.\n")
    f.write("5. Nada de código por ordem alfabética. Código é posição, não nome.\n")

print("itens:", len(linhas))
por_fam = {}
for l in linhas: por_fam[l["familia"]] = por_fam.get(l["familia"],0)+1
for k,v in por_fam.items(): print(" ", k, v)
