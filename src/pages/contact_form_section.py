"""This module contains all actions and interactions with the Contact Form Section."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactFormSection:

    # * Locators

    @classmethod
    def subject_heading_select(cls):
        return (By.ID, 'id_contact')

    @classmethod
    def send_button(cls):
        return (By.ID, 'submitMessage')

    @classmethod
    def email_address_input(cls):
        return (By.ID, 'email')

    @classmethod
    def order_reference_input(cls):
        return (By.ID, 'id_order')

    @classmethod
    def attach_file_input(cls):
        return (By.ID, 'fileUpload')

    @classmethod
    def error_alert(cls):
        return (By.CLASS_NAME, 'alert-danger')

    @classmethod
    def message_textarea(cls):
        return (By.ID, 'message')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120) # Explicit wait, waits until 120 seconds (2 minutes)

    # * Actions

    def select_subject_heading(self, subject_heading):
        """
        Selects a Subject Heading by visible text from the dropdown.

        Arguments
        ---------
        subject_heading : (str)
            Subject Heading to select.
        """
        subject_heading_dropdown = Select(self.driver.find_element(*self.subject_heading_select()))
        subject_heading_dropdown.select_by_visible_text(subject_heading)

    def click_send_button(self):
        send_button = self.driver.find_element(*self.send_button())
        send_button.click()

    def type_email_address(self, email_address):
        """
        Type an email address.

        Arguments
        ---------
        email_address : (str)
            Email address to type.
        """
        email_address_input = self.driver.find_element(*self.email_address_input())
        email_address_input.send_keys(email_address)

    def type_order_reference(self, order_reference):
        """
        Type an order reference.

        Arguments
        ---------
        order_reference : (str)
            Order reference to type.
        """
        order_reference_input = self.driver.find_element(*self.order_reference_input())
        order_reference_input.send_keys(order_reference)

    def error_alert_is_displayed(self):
        """
        Determine if the error alert is presented.

        Returns
        -------
        bool
            Returns True if error alert is presented.
        """
        error_alert = self.wait.until(EC.visibility_of_element_located(self.error_alert()))

        if error_alert.is_displayed():
            return True

        return False

    def type_mesage(self, message):
        """
        Type a message.

        Arguments
        ---------
        message : (str)
            Message to type.
        """
        message_textarea = self.driver.find_element(*self.message_textarea())
        message_textarea.send_keys(message)