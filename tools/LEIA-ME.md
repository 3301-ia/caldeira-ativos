# Robo do acervo

O arquivo `arquivar.py` roda no GitHub Actions a cada 4 horas e tambem pelo botao
"Run workflow". Ele le as fichas com imagem pendente no sistema, baixa a imagem,
grava em `acervo/` e devolve o link definitivo para a ficha.

Nao depende do computador de ninguem e nao consome credito de mensagem do agente.
O unico ponto que depende do sistema e a leitura da lista e a devolutiva do link.

Se a porta de entrada estiver fora do ar, o robo avisa e encerra sem erro.
