from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


class WhatsBlaster:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--force-device-scale-factor=1")
        self.driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        self.driver.get("https://web.whatsapp.com")
        print "Login, and wait for app to load."
        raw_input("Then, hit enter to continue. ")

    def close(self):
        self.driver.close()
    
    def send_message(self, contact_name, message, timeout=10):
        driver = self.driver
        # Find contact
        search = driver.find_element_by_css_selector(".input.input-search")
        search.send_keys(contact_name)
        try:
            element = WebDriverWait(driver, 10).until(
                    lambda driver: driver.find_element_by_css_selector(
                        "span[title='{}']".format(contact_name)
                        ))
        except:
            return "Failure: could not find contact {}.".format(contact_name)
        # Load chat
        driver.find_element_by_css_selector(
                "span[title='{}']".format(contact_name)
                ).click()
        try:
            element = WebDriverWait(driver, 10).until(
                    lambda driver: driver.find_element_by_css_selector(
                        ".pane-chat span[title='{}']".format(contact_name)
                        ))
        except:
            return "Failure: could not load chat with contact {}.".format(contact_name)
        # Send message
        input_element = driver.find_element_by_css_selector("div.input")
        input_element.send_keys(message)
        input_element.send_keys(Keys.ENTER)
        # Wait until successful
        messages_0 = driver.find_elements_by_css_selector(".message-list .msg")
        for t in range(timeout):
            messages_1 = driver.find_elements_by_css_selector(".message-list .msg")
            if len(messages_0) != len(messages_1):
                return "Success: sent to {}.".format(contact_name)
            time.sleep(1)
        return "Message to {} may not have been sent.".format(contact_name)


if __name__ == '__main__':
    W = WhatsBlaster()
    print W.send_message("Mickey Mouse", "Hello!")
    W.close()
