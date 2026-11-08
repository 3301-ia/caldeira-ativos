# Árvore de códigos do Caldeira

Como um item vendável chama os códigos que estão dentro dele, e como o código da nota do fornecedor entra nessa história sem virar bagunça.

## Três origens de código, três donos diferentes

1. **Código do item vendável** — o que aparece no cardápio e no PDV. Prefixo `CG`, famílias 01 a 08. Exemplo: `CG.04.01.001` filé mignon 400g com fritas.
2. **Código de insumo e de prep** — o que existe na cozinha, e que aparece em muitas fichas. Famílias 10 a 20. Exemplo: `CG.10.03.004` cebolinha, `CG.20.01.001` molho de tomate da casa.
3. **Código do fornecedor** — o que vem impresso na nota, no hortifruti, no atacado. Nunca é a identidade do item. É o apelido externo, que aponta para o código interno.

Juntar as três coisas em um número só é o erro clássico: no dia em que o hortifruti troca o código dele, a ficha do filé quebra.

## Famílias de insumo e prep

| Família | Conteúdo |
|---|---|
| 10 | Hortifruti (frutas, verduras, legumes, temperos frescos) |
| 11 | Carnes, aves e pescados |
| 12 | Frios, laticínios e ovos |
| 13 | Mercearia seca, óleos, condimentos, farinhas |
| 14 | Congelados e panificação |
| 15 | Bebidas de compra e descartáveis |
| 20 | Preps da casa: bases, molhos, caldos, guarnições preparadas |

Exemplo de código de insumo: `CG.10.03.004` cebolinha, unidade kg.
Exemplo de código de prep: `CG.20.02.003` molho de tomate rústico, rendimento 2 L.

## Como o item puxa o resto

O item vendável guarda a lista de componentes, cada um com o seu código e a quantidade.

`CG.04.01.001` filé mignon 400g com fritas

- `CG.11.01.002` filé mignon limpo — 0,300 kg
- `CG.10.08.001` batata pré-frita — 0,300 kg
- `CG.13.04.002` óleo de fritura — 0,060 L
- `CG.10.03.004` cebolinha — 0,005 kg
- `CG.10.03.001` salsinha — 0,005 kg

Ao pedir `CG.04.01.001`, o sistema devolve todos os filhos, com quantidade, custo e a que fornecedor cada um pertence. É o que você descreveu como chamar o número e sair tudo.

## O código da nota

A nota do hortifruti chega com o código dele. O sistema não cria item novo para isso. Ele consulta a tabela de apelidos.

| Código do fornecedor | Fornecedor | Vira | Confiança |
|---|---|---|---|
| 4512 | Hortifruti Central | `CG.10.03.004` cebolinha | alta |
| 4471 | Hortifruti Central | `CG.10.03.001` salsinha | alta |
| 7788 | Atacado MG | `CG.11.01.002` filé mignon | média |

Regra de ouro: código desconhecido na nota não vira item novo na surdina. Ele entra como pendência de apelido, para alguém confirmar. Sem isso, a mesma cebolinha ganha três códigos em três meses e o custo vira ficção.

## Por que o apelido tem camada de confiança

- **alta**: alguém já conferiu e o de-para está certo. Baixa automático.
- **média**: o sistema sugeriu por nome parecido. Baixa, mas sinaliza para conferência no fechamento.
- **baixa**: ambíguo, mais de um candidato. Não baixa sozinho, exige escolha humana.

Isso resolve o caso do nome igual: "tomate" pode ser tomate italiano, salada ou cereja, e são três códigos diferentes.

## O preps entram na mesma árvore

O prep é filho de um item e pai de outros insumos. Exemplo: o molho de tomate da casa (`CG.20.02.003`) entra na porção de fritas com queijo? Não entra. Mas entra na pizza, no escondidinho e no caldo. Ele tem ficha própria, custo próprio e rendimento próprio.

Duas consequências práticas:

1. Prep tem código e ficha, igual a item vendável. A diferença é que ele não tem preço de venda, tem custo por litro ou por quilo.
2. Quando o tomate sobe, quem sente é o prep, e o prep avisa todos os itens que dependem dele. É o que faz o CMV reagir no mesmo dia, não no fechamento do mês.

## Regra final

O código do item é a porta. O código do insumo é a chave. O código do fornecedor é o apelido. Quem confunde os três acaba com um sistema que ninguém confia.
