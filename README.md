- [x] Usuários devem ser capazes de inserir empréstimos e seus respectivos pagamentos
- [x] Usuários devem ser capazes de visualizar seus empréstimos e pagamentos
- [ ] Usuários devem ser capazes de visualizar o saldo devedor de cada um dos seus empréstimos
    Você pode decidir onde e como mostrar a informação
    O saldo devedor nada mais é do que o quanto o cliente ainda deve para o banco
    O saldo devedor deve considerar a taxa de juros do empréstimo e descontar o que já foi pago
- [x] Usuários não podem ver ou editar empréstimos ou pagamentos de outros usuários
- [x] A autenticação da API deve ser feita via token
    Não é necessário desenvolver endpoints para criação/gerenciamento de usuários
- [x] Os empréstimos devem conter no mínimo as informações abaixo:
    Identificador - um identificador aleatório gerado automaticamente
    Valor nominal - o valor emprestado pelo banco
    Taxa de juros - a taxa de juros mensal do empréstimo
    Endereço de IP - endereço de IP que cadastrou o empréstimo
    Data de solicitação - a data em que o empréstimo foi solicitado
    Banco - informações do banco que emprestou o dinheiro (pode ser um simples campo de texto)
    Cliente - informações do cliente que pegou o empréstimo (pode ser um simples campo de texto)
- [x] Os pagamentos devem conter no mínimo as informações abaixo:
    Identificador do empréstimo
    Data do pagamento
    Valor do pagamento
- [ ] Testes
    As funcionalidade principais devem estar com testes escritos
    Você pode decidir quais os testes que mais agregam valor ao projeto
