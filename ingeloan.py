import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
from faker import Faker

""" 'pl_PL' jest niezbędne aby skorzystać z generowania danych do testów wykorzystujących np. polski numer nip"""
fake = Faker(['en_US', 'pl_PL'])

valid_first_name = fake.first_name()
valid_last_name = fake.last_name()
valid_password = fake.password(length=5)
valid_email = fake.free_email()
invalid_date = str(fake.date_between(start_date='-123y', end_date='-123y'))


class INGLoan(unittest.TestCase):
    """
    Scenariusz testowy: Pożyczka dla firm
    """

    def setUp(self):
        """
        Warunki wstępne:
        Przeglądarka otwarta na ing
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://forms.ing.pl/DETeWniosekWormsExt/wizardwfb.aspx?path=T5_E-EndUserWormsExt-S5-CREDIT_SBF&url_channel=vortal&FROM=https%3a%2f%2fwww.ing.pl%2fmale-firmy%2fkredyty-i-pozyczki%2fpozyczka-dla-malych-firm&bankId=6&profileId=4&c=1")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """ Sprzątanie po teście """
        self.driver.quit()

    def test_invalid_date_of_birth(self):
        """
        Wnioskowanie o pożyczkę używająć
        używając nieakceptowalnego roku urodzenia - dane niepoprawne
        (data urodzenia wcześniejsza niż rok 1900)
        """
        driver = self.driver
        # KROKI:

        """
        Wyłączam komunikat o ciasteczkach - "zasłania" on dolne pola formularza, przez co Selenium ich
        "nie widzi"

        Sposób bez użycia javascript:
        driver.find_element_by_xpath('//*[@id="ctl00_MCP_CUW___CustomNav0_StepNextButton"]').send_keys(Keys.ENTER)
        """
        # sleep(100)
        # Wyłączam komunikat o ciasteczkach z użyciem javascript

        # accept_cookies = driver.find_element(By.XPATH, '// *[ @ id = "qc-cmp2-ui"] / div[2] / div / button[2] / span')
        # driver.execute_script("arguments[0].click();", accept_cookies)



        # 1. Kliknij Dalej




        dwanascie_mies_button = driver.find_element(By.XPATH, '// *[ @ id = "icheckFullID_ctl00_CPH_Content_companyPeriodOfActivity__RB__0"]')
        dwanascie_mies_button.click()

        szesc_mies_button = driver.find_element(By.XPATH, '//*[@id="icheckFullID_ctl00_CPH_Content_companyPeriodOfBusinessBankAccount__RB__0"]')
        szesc_mies_button.click()

        klauzula_button = driver.find_element(By.ID, 'icheckHelperID_ctl00_CPH_UI_KlauzulaBIKVortal')
        klauzula_button.click()

        # rodzaj_dzialalnosci = driver.find_element(By.ID, 'ctl00_CPH_SelectedOptionID_DropDown3_companyBusinessActivityType')
        # drop = Select(rodzaj_dzialalnosci)
        # drop.select_by_visible_text('Kancelarie notarialne')

        # rodzaj_dzialalnosci = driver.find_element(By.XPATH, '// *[ @ id = "ctl00_CPH_SelectedOptionID_DropDown3_companyBusinessActivityType"]')
        # rodzaj_dzialalnosci.click()

        # driver.send_keys(Keys.DOWN)


        # inna = driver.find_element(By.ID, 'ctl00_CPH_SelectedOptionID_DropDown3_companyBusinessActivityType')
        # inna.select_by_visible_text('Inna')


        # rodzaj_dzialalnosci = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "ctl00_CPH_SelectedOptionID_DropDown3_companyBusinessActivityType"]')))
        # rodzaj_dzialalnosci.send_keys(Keys.DOWN)
        #
        # inna = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_CPH_SelectedOptionID_DropDown3_companyBusinessActivityType"]')))
        # inna.click()

        # . Kliknij Dalej
        # dalej_button = driver.find_element(By.XPATH, '// *[ @ id = "ctl00_CPH_nav_START_Button1_Start_goNextAction"]')
        # dalej_button.click()

        # dalej_button = driver.find_element(By.ID, 'ctl00_CPH_nav_START_Button1_Start_goNextAction')
        # dalej_button.click()


        sleep(5)


        # Wizualnie oceniam test"
        sleep(10)

        """
        Test: sprawdzam oczekiwany rezultat
        """

        # Wyszukuję wszystkie błędy
        error_notices = driver.find_elements(By.XPATH,
            '//*[@id="ctl00_MCP_CUW_CreateUserStepContainer_RangeValidator1"]')
        # Zapisuję widoczne błędy do listy visible_error_notices
        # Tworzę pustą listę
        visible_error_notices = []
        for error in error_notices:
            # Jesli błąd jest widoczny, dodaj go do listy
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy jest widoczny tylko jeden błąd
        assert len(visible_error_notices) == 1
        # Sprawdzam treść widocznego błędu
        error_text = visible_error_notices[0].get_attribute("innerText")
        assert error_text == "* Niepoprawny rok urodzenia"


if __name__ == '__main__':
    unittest.main(verbosity=2)
