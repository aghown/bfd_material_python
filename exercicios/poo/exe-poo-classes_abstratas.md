# Atividade: POO - Classes abstratas

1. **Definição de classe abstrata**

   Crie uma classe abstrata chamada `Animal` que possua um método abstrato `falar()`. Em seguida, crie duas classes concretas (`Cachorro` e `Gato`) que implementem esse método. Mostre o uso criando objetos e chamando o método `falar()`.

2. **Proibição de instanciamento**

   Tente instanciar diretamente a classe `Animal` da questão anterior e explique o erro gerado pelo Python.

3. **Múltiplos métodos abstratos**

   Defina uma classe abstrata `FormaGeometrica` com dois métodos abstratos: `area()` e `perimetro()`. Crie uma classe concreta `Retangulo` que herde de `FormaGeometrica` e implemente os dois métodos. Teste criando um objeto e calculando sua área e perímetro.

4. **Herança parcial**

   Crie uma classe abstrata `Transporte` com dois métodos abstratos: `mover()` e `parar()`. Depois, crie uma subclasse `Carro` que implemente apenas o método `mover()`. O que acontece quando você tenta instanciar `Carro`? Corrija implementando o segundo método.


