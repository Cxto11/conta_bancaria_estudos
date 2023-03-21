SCRIPT: 
from conta_bancaria_OO import conta
conta1 = conta()  

    Titular: Renan --->(Definir o nome do titular pelo input)
success>>>Conta criada com sucesso! ID(<conta_bancaria_OO.conta object at 0x000001E74F107E90>)
          saldo 0.0

conta1.deposito(100)
success>>

conta1.extrato()
success>>O titular Renan,possui 100.0 de saldo disponivel.

conta1.credito
success>>100.0

conta.credito = 200
success>>

conta.credito
success>>200
############################################################################################
Aprendizado arquivo(conta_bancaria_bascia):
    -Dicionário
    -Funções
    -Encapsulamento de código
Aprendizado arquivo(conta_bancaria_OO):
    -Classes
    -Objetos
    -Função construtora
    -Endereço e referência de objetos
    -Atributos de classe
    -Acesso aos atributos através do objeto
    -Métodos, que definem o comportamento de uma classe
    -Criação de métodos
    -Como chamar métodos através do objeto
    -Acesso aos atributos através do self
    -Garbage Collector
    -O tipo None
    -Atributos privados
    -Encapsulamento de código
    -Encapsulamento da manipulação dos atributos nos métodos
    -Coesão do código
    -Métodos de leitura dos atributos, os getters
    -Métodos de modifição dos atributos, os setters
    -Propriedades
