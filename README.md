# Lista de exercícios para consolidar o conceito de Tipos Abstratos de Dados em Python 
### Exercício 01 
A startup **NeoBank**, um banco 100% digital, está em fase inicial de desenvolvimento de sua plataforma financeira. Como a empresa ainda não possui um sistema bancário completo, 
a equipe de engenharia decidiu começar pela modelagem do componente mais essencial do sistema: a conta digital dos clientes.

Seu time foi contratado para desenvolver a primeira versão dessa estrutura. Essa classe será usada futuramente por diversos módulos do sistema, como aplicativo mobile, internet 
banking e APIs externas. Portanto, ela deve ser bem projetada, segura e organizada.

O objetivo é criar um **Tipo Abstrato de Dado (TAD)** que represente uma conta bancária digital e permita executar operações financeiras básicas com segurança e rastreabilidade.

**Atributos**  
titular  
numero  
saldo  

**Métodos obrigatórios**  
depositar(valor)  
sacar(valor)  
transferir(valor, conta_destino)  
str()  

**Regras**  
Não permitir saque se saldo insuficiente  

### Exercício 02 
A startup **ShopNext**, uma plataforma de e-commerce em crescimento acelerado, está desenvolvendo seu novo sistema de compras online. A empresa já possui catálogo de 
produtos, sistema de login e processamento de pagamentos, mas percebeu que falta um componente essencial para permitir que clientes realizem compras: o carrinho de compras.

O time de engenharia definiu que o carrinho deve ser implementado como um módulo independente, pois futuramente ele será reutilizado em:
* aplicativo mobile
* versão web
* API para parceiros

Você foi contratado como desenvolvedor para implementar a estrutura responsável por representar o carrinho e suas operações. Essa estrutura deve ser bem organizada, 
confiável e capaz de manipular itens de forma segura.

O carrinho deve armazenar uma coleção de itens. Cada item deve possuir:
* nome
* preço
* quantidade

A estrutura interna fica a seu critério (lista, dicionário, etc.), desde que funcione corretamente.  

A classe deve implementar:
* **adicionar_item(nome, preco, quantidade)**: adiciona um produto ao carrinho. **Regra**: Se o item já existir → apenas soma a quantidade.
* **remover_item(nome)**: remove completamente um item do carrinho.
* **atualizar_quantidade(nome, quantidade)**: altera a quantidade de um item. **Regra**: Se quantidade = 0 → remover item.
* **total()**: retorna o valor total da compra.
* **listar_itens()**: mostra todos os itens presentes no carrinho.
