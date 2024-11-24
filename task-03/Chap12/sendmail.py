from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def send_email(email, message):
   
    driver = webdriver.Chrome()  
    driver.get("https://accounts.google.com/")  

   
    username = driver.find_element("name", "identifier")
    username.send_keys("prarthana.desai@gmail.com")  
    username.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)
    password = driver.find_element("name", "password")
    password.send_keys("Prarthana2345")  
    password.send_keys(Keys.RETURN)

    driver.implicitly_wait(10)
  
    driver.get("https://mail.google.com/mail/#inbox?compose=new")
    driver.implicitly_wait(10)

    to = driver.find_element("name", "to")
    to.send_keys(email)
    subject = driver.find_element("name", "subjectbox")
    subject.send_keys("Automated Message")
    body = driver.find_element("css selector", "div[aria-label='Message Body']")
    body.send_keys(message)
    body.send_keys(Keys.CONTROL, Keys.RETURN) 

    driver.quit()

if __name__ == "__main__":

    if len(sys.argv) == 3:
        email_address = sys.argv[1]
        email_message = sys.argv[2]
        send_email(email_address, email_message)
    else:
        print("Usage: python emailer.py <email_address> <message>")