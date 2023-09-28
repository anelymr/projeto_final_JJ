#language: pt

Funcionalidade: Cadastro de usuario

    @cadastro_usuario
    Cenário: Cadastrando um usuário para a loja Joga Junto

    Dado que a pessoa esta acessando o site pela primeira vez
    Quando ela clicar em registrar-se o site deverá redirecioná-la para a tela de cadastro
    E deverá preencher os dados necessários para criar o usuario
    E clicar em criar conta
    E o usuário será redirecionado para fazer login
    Então irá preencher os dados para efetuar o login
