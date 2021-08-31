"""This module contains all actions and interactions for the Home Page."""

from selenium.webdriver.common.by import By


class HomePage:

    # * Locators

    @classmethod
    def contact_us_a(cls):
        return (By.ID, 'contact-link')

    def __init__(self, driver):
        self.driver = driver

    # * Actions

    def click_contact_us_link(self):
        contact_us_link = self.driver.find_element(*self.contact_us_a())
        contact_us_link.click()