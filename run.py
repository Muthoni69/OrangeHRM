from selenium.webdriver.ie.webdriver import WebDriver
from OrangeTests.OrangeTests import TestingBot



with TestingBot() as bot:
    bot.land_first_page()
    bot.login()
    bot.pim_details()
    bot.add_employee()
    bot.assign_leave()
