import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest_driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest_driver.get('http://petfriends.skillfactory.ru/login')


    yield pytest_driver

    pytest_driver.quit()


def test_show_my_pets(testing):
    pytest_driver = testing
    # Вводим email
    pytest_driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    # Вводим пароль
    pytest_driver.find_element(By.ID, 'pass').send_keys('12345')
    # Нажимаем на кнопку входа в аккаунт
    pytest_driver.implicitly_wait(10)
    pytest_driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest_driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(5)
    # Нажимаем на кнопку мои питомцы
    pytest_driver.find_element(By.XPATH,'//[contains(test(), "Мои питомцы")]').click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))

    All_my_pets = pytest_driver.find_element(By.CSS_SELECTOR, '#all_my_pets table tbody tr')
    All_my_pets_number = pytest_driver.find_element(By.XPATH,'//[contains(@class, ".col-sm-4 left")]/text()[2]')





