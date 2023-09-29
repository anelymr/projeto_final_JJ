from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#Defina aqui os dados que serão utilizado para cadastro / login
email = "digite-email"
senha = "digite-senha"
senha_conf = "digite-senha"

@given("que a pessoa esta acessando o site pela primeira vez")
def go_to_page(context):
    context.browser.get("https://projetofinal.jogajuntoinstituto.org")
    sleep(1.5)

@when("ela clicar em registrar-se o site deverá redirecioná-la para a tela de cadastro")
def register_user(context):
   registro = context.browser.find_element(By.XPATH, "/html/body/div/main/form/div[6]/span[2]/a")
   registro.click()
   sleep(1.5)

@when("deverá preencher os dados necessários para criar o usuario")
def register_data(context):
    context.browser.find_element(By.NAME, "email").send_keys(email)
    context.browser.find_element(By.NAME, "password").send_keys(senha)
    context.browser.find_element(By.NAME, "confirmPassword").send_keys(senha_conf)

@when("clicar em criar conta")
def confirm_register(context):
    criar_conta = context.browser.find_element(By.XPATH, "/html/body/div/div/form/button")
    criar_conta.click()

@when("o usuário será redirecionado para fazer login")
def verify_login_text(context):
    try:
        WebDriverWait(context.browser, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//label"), "Faça login")
        )
    except Exception as e:
        assert False, f"Usuário não criado, não foi possível redirecioná-lo para a tela de login {e}"

@then("irá preencher os dados para efetuar o login")
def fill_login_data(context):
    context.browser.find_element(By.NAME, "email").send_keys(email)
    context.browser.find_element(By.NAME, "password").send_keys(senha)
    iniciar_sessao = context.browser.find_element(By.XPATH, "/html/body/div/main/form/button")
    iniciar_sessao.click()
    sleep(10)