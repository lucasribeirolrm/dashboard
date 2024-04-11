import time

def test_home_page(browser):
    browser.get('http://127.0.0.1:8080')
    time.sleep(5)
    assert browser.title == 'Dash'
    print("Teste da página inicial concluído com sucesso.")
