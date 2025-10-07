# Atividade: POO - Associação / Agregação / Composição

1. Crie duas classes: `Autor` e `Livro`.

* Um `Autor` tem nome.
* Um `Livro` tem título e um autor associado.
  Mostre que, mesmo apagando o objeto `Livro`, o `Autor` continua existindo.

2. Crie as classes `Aluno` e `Curso`.

* Um `Aluno` tem nome.
* Um `Curso` tem nome e recebe alunos associados (sem armazená-los permanentemente).
  Demonstre que um `Aluno` pode estar em vários cursos ao mesmo tempo.


3. Crie a classe `Departamento` que contém uma lista de `Funcionarios`.

* Um `Funcionario` tem nome.
* O `Departamento` agrega funcionários já criados.
  Mostre que um funcionário pode existir mesmo sem pertencer a um departamento.

4. Crie as classes `Time` e `Jogador`.

* Um `Jogador` tem nome e posição.
* Um `Time` agrega jogadores em uma lista.
  Mostre que o mesmo jogador pode ser agregado a outro time (transferência).


5. Crie a classe `Carro` que possui um `Motor`.

* O `Motor` deve ser criado dentro do `Carro`.
* Se o `Carro` deixar de existir, o `Motor` também deixa.
  Mostre isso criando e depois apagando o objeto.

6. Crie a classe `Casa` que é composta por vários `Comodo`s (sala, cozinha, quarto, etc.).

* Cada `Comodo` deve ser criado dentro da `Casa`.
* Mostre que, ao excluir a `Casa`, todos os `Comodo`s também deixam de existir.

