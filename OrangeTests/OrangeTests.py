import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select # This one helps with dropdowns


from selenium.webdriver.common.keys import Keys

class TestingBot(webdriver.Chrome):
    def __init__(self):
        #Initialize Chrome driver
        super().__init__()
        self.implicitly_wait(10)
        self.maximize_window()


    def __enter__(self):
        # Perform any setup actions here
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Perform any cleanup actions here
        self.quit()

    def land_first_page(self):
        url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.get(url)

    def login(self):
        login_username = self.find_element(By.NAME, "username")
        login_username.clear()
        login_username.send_keys("Admin")

        login_password = self.find_element(By.NAME, "password")
        login_password.clear()
        login_password.send_keys("admin123")

        login_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("Successfully logged in")

        time.sleep(2)

    def pim_details(self):
        pim_button = self.find_element(By.CSS_SELECTOR, "span.oxd-text.oxd-text--span.oxd-main-menu-item--name"
                                       ).find_element(By.XPATH, "//span[text()='PIM']")
        pim_button.click()
        print("PIM button located!")

    def add_employee(self):
        #Find the add employee button
        global employee_id_button
        wait = WebDriverWait(self, 20)

        another_employee  = self.find_element(By.XPATH, "//a[contains(text(), 'Add Employee')]")
        print("Found the Add employee button!")
        another_employee.click()

        firstname_button = self.find_element(By.NAME, 'firstName')
        firstname_button.send_keys('DARK')

        middlename_button = self.find_element(By.NAME, 'middleName')
        middlename_button.send_keys('VADER')

        lastname_button = self.find_element(By.NAME, 'lastName')
        lastname_button.send_keys('JUNIOR')

        save_details_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_details_button.click()
        print("Successfully added an employee!")
        time.sleep(10)

    def assign_leave(self):
        wait = WebDriverWait(self, 20)
        # leave_button = wait.until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "span.oxd-text oxd-text--span oxd-main-menu-item--name"
        #                                ).find_element(By.XPATH, "//span[text()='Leave']")))
        # leave_button.click()

        # Wait until the element is visible using CSS_SELECTOR
        leave_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.oxd-text.oxd-text--span.oxd-main-menu-item--name"))
        )

        # Find the specific element using XPATH
        leave_button = leave_button.find_element(By.XPATH, "//span[text()='Leave']")

        # Click the button
        leave_button.click()


        assign_leave_button = self.find_element(By.LINK_TEXT, "Assign Leave")
        assign_leave_button.click()

        employee_name_hint = self.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']")
        employee_name_hint.click()
        employee_name_hint.send_keys('DARK VADER JUNIOR')
        employee_name_hint.send_keys(Keys.TAB)

        #click on dropdown element
        leave_type_button = self.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        leave_type_button.click()
        #click on the type of leave
        leave_type = self.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[3]")
        leave_type.click()

        # # Click on dropdown dropdown arrow element
        # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]").click()
        # # Click on ESS element
        # driver.find_element(By.XPATH, "(//div[@role='listbox']//child::div)[3]").click()

        # Find the first date input (start date)
        start_date_input = self.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])")
        start_date_input.clear()
        start_date_input.send_keys('2024-10-10')

        # Find the second date input (end date)
        end_date_input = self.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
        end_date_input.clear()
        end_date_input.send_keys('2024-15-10')

        save_changes_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_changes_button.click()
        print("Assigned leave for employee!")






