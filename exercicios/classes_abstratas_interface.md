Exercícios práticos sobre métodos abstratos e `ABC`

1. **Animal falando**
   Crie uma classe abstrata `Animal` com um método abstrato `falar()`.
   Depois crie as classes `Cachorro` e `Gato` que implementam esse método.
   Teste chamando `falar()` em objetos das subclasses.

---

2. **Formas geométricas**
   Crie uma classe abstrata `FormaGeometrica` com os métodos abstratos `area()` e `perimetro()`.
   Implemente as classes `Retangulo` e `Circulo` herdando dela.
   Teste os cálculos de área e perímetro.

---

3. **Proibindo instância direta**
   Tente instanciar diretamente a classe `FormaGeometrica` e verifique o erro que o Python retorna.
   Explique por que isso acontece.

---

4. **Funcionários e salários**
   Crie uma classe abstrata `Funcionario` com:

   * atributo `nome`
   * método abstrato `calcular_salario()`
   * método concreto `exibir_informacoes()` que imprime o nome.
     Implemente duas subclasses:
   * `FuncionarioCLT` que calcula salário fixo mensal
   * `FuncionarioPJ` que calcula salário por hora * horas trabalhadas.

---

5. **Veículos**
   Crie uma classe abstrata `Veiculo` com métodos abstratos `acelerar()` e `frear()`.
   Implemente `Carro` e `Bicicleta`.
   Simule o uso de cada um chamando os métodos.

---

6. **Instrumentos musicais**
   Crie uma classe abstrata `Instrumento` com método abstrato `tocar()`.
   Depois crie `Violao`, `Bateria` e `Piano`.
   Crie uma lista de instrumentos e percorra chamando `tocar()` em cada um.

---

7. **Sistema de pagamentos**
   Crie uma classe abstrata `Pagamento` com o método abstrato `processar(valor)`.
   Implemente `PagamentoCartao` e `PagamentoBoleto`.
   Crie uma função `efetuar_pagamento(p: Pagamento, valor)` que chama `processar`.

---

8. **Mensagens**
   Crie uma classe abstrata `Mensagem` com método abstrato `enviar(destinatario: str)`.
   Implemente `MensagemEmail` e `MensagemSMS`.
   Crie uma lista de mensagens e percorra chamando `enviar()`.
