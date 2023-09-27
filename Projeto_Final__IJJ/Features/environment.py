from selenium.webdriver import Firefox

def before_scenario(context, scenario):
    context.browser = Firefox()

def after_scenario(context, scenario):
    context.browser.quit()
