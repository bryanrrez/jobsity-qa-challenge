"""This module contains all the test cases for the Contact Form Section."""

import pytest

from src.pages.home import HomePage
from src.pages.contact_form_section import ContactFormSection


URL = 'http://automationpractice.com/'
# This decorator parametrize the test, so we can indicate which browsers we want to use for the test case.
# In this case I'm only using chrome as the browser where the test will be execute,
# but in case I want to execute it on more than one I just have to a string item to the list, i.e. 'firefox'
@pytest.mark.parametrize('browser', ['chrome'])
def test_verify_subject_heading(driver):

    SUBJECT_HEADING = 'Customer service'

    driver.get(URL)

    home_page = HomePage(driver)
    home_page.click_contact_us_link()

    contact_form_section = ContactFormSection(driver)
    contact_form_section.select_subject_heading(SUBJECT_HEADING)
    contact_form_section.click_send_button()

    # Verify that the message is not sent
    assert contact_form_section.error_alert_is_displayed() == True

@pytest.mark.parametrize('browser', ['chrome'])
def test_verify_email_address(driver):

    EMAIL_ADDRESS = 'khart@yopmail.com'

    driver.get(URL)

    home_page = HomePage(driver)
    home_page.click_contact_us_link()

    contact_form_section = ContactFormSection(driver)
    contact_form_section.type_email_address(EMAIL_ADDRESS)
    contact_form_section.click_send_button()

    # Verify that the message is not sent
    assert contact_form_section.error_alert_is_displayed() == True

@pytest.mark.parametrize('browser', ['chrome'])
def test_verify_order_reference(driver):

    ORDER_REFERENCE = 'A01'

    driver.get(URL)

    home_page = HomePage(driver)
    home_page.click_contact_us_link()

    contact_form_section = ContactFormSection(driver)
    contact_form_section.type_order_reference(ORDER_REFERENCE)
    contact_form_section.click_send_button()

    # Verify that the message is not sent
    assert contact_form_section.error_alert_is_displayed() == True

@pytest.mark.parametrize('browser', ['chrome'])
def test_verify_message(driver):

    MESSAGE = 'This is a test'

    driver.get(URL)

    home_page = HomePage(driver)
    home_page.click_contact_us_link()

    contact_form_section = ContactFormSection(driver)
    contact_form_section.type_mesage(MESSAGE)
    contact_form_section.click_send_button()

    # Verify that the message is not sent
    assert contact_form_section.error_alert_is_displayed() == True