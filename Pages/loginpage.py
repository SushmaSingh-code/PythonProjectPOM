class loginpage():
    # locators for all the element
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_linkText = "welcome"
    link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element_by_xpath(self.textbox_username_id).click()
