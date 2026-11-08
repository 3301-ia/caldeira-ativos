# Salada de fruta · do improviso ao sistema

Hoje a salada é feita com o que tem. Isso funciona no balcão e não funciona no sistema, porque sem composição definida não existe baixa, não existe custo e não existe previsão.
O objetivo aqui é transformar a salada em item de fluxo, igual a uma porção.

## Item de cardápio

- Código: `CG.09.01.001`
- Família: 09 Frutas e naturais
- Unidade de venda: pote
- Preço: a definir

## O modelo que resolve

Uma salada de composição variável não permite baixa automática. Então a saída não é fixar para sempre, é fixar em lotes.

**Base fixa** — as frutas que existem sempre, e que respondem pela maior parte do peso.
**Rotação** — duas ou três frutas que mudam conforme a estação e o que a praça de acesso entrega.

A ficha registra a base fixa e uma regra de rotação: o peso total por pote é sempre o mesmo, a composição pode mudar.

Exemplo de regra: 300 g por pote, sendo 60% da base fixa, 40% de rotação.

## O que cada fruta precisa ter

Cada fruta da salada é um insumo da família 10, com quatro números medidos uma vez:

1. **Peso bruto** — como chega.
2. **Peso limpo** — depois de casca, caroço e talo. A diferença é o fator de correção.
3. **Rendimento por pote** — quantos gramas limpos vão no pote.
4. **Perda por tempo** — quanto se perde entre o corte e a venda, por oxidação e por validade.

A fruta é o único insumo do Caldeira em que o tempo destrói valor mesmo sem ninguém tocar. O custo dela tem prazo.

## A produção

Um lote por dia, de manhã, com quantidade planejada.

Planejado = venda média do mesmo dia da semana nas últimas quatro semanas, com ajuste para cima em fim de semana e para baixo em feriado.

Produção maior que a venda vira sobra de salada, que é perda conhecida. Produção menor vira falta, que é venda perdida e não aparece em número nenhum, a não ser como reclamação.

Regra: o lote resta no máximo 15 minutos de produção além do planejado. Sobra com registro vale mais que falta sem registro.

## O fluxo de pedido no PDV

O item vendido é um só: salada de fruta, pote.

O que acontece por trás da venda:

1. Cliente pede no balcão, caixa ou totem. O PDV imprime a comanda com o código `CG.09.01.001`.
2. A praça monta o pote conforme a ficha do dia, que já indica a rotação vigente.
3. A entrega confirma. A confirmação fecha o pedido com hora de saída.
4. A baixa dos insumos é automática, pela ficha: o sistema desconta o peso limpo de cada fruta do pote vendido.
5. A sobra do dia é contada no fechamento e registrada como perda, com causa e responsável.

Isso é o que hoje não existe: o pedido não puxa o insumo, então a baixa é feita no olho ou não é feita.

## O que muda para quem opera

- A praça deixa de decidir a composição na hora e passa a seguir a ficha do dia. Menos dúvida, mais velocidade.
- A quantidade produzida passa a vir do histórico, não do palpite.
- A sobra passa a ser um número, e não um incômodo.

## Decisões que faltam

1. Peso do pote. É o número que ancora custo, preço e baixa.
2. Quais frutas compõem a base fixa.
3. Qual a rotação aceitável por estação.
4. Preço de venda.
5. Onde a salada é montada: na praça, em lote fechado, ou na frente do cliente.

## Custo por pote, depois de tudo medido

Custo do pote = soma de (peso limpo da fruta × custo do grama limpo) + embalagem + rateio da perda.

O custo do grama limpo é o preço da compra dividido pelo peso limpo, não pelo peso bruto. É aí que a maioria erra e o custo sai 20% abaixo do real.
