import time

from selenium import webdriver






driver = webdriver.Chrome(executable_path="C:\\Users\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\chromedriver.exe")
zoomvenues_url = "https://zoomvenues.info/"
vendor_signin_url = "http://vendor.zoomvenues.info/login"


def venues_signIn():
    driver.implicitly_wait(20)
    parent_page = driver.current_window_handle
    venues_signup = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/a").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            compy_nm = driver.find_element_by_css_selector("body > div:nth-child(19) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(4) > div:nth-child(1) > input:nth-child(2)")
            compy_nm.send_keys("skillteck")
            time.sleep(2)
            address = driver.find_element_by_xpath("//form[@id='formVendorSignup']//input[@id='busiaddress']")
            address.send_keys("Abu Dhabi")
            time.sleep(2)
            f_name = driver.find_element_by_xpath("//form[@id='formVendorSignup']//input[@id='firstname']")
            f_name.send_keys("om")
            time.sleep(2)
            l_name = driver.find_element_by_xpath("//form[@id='formVendorSignup']//input[@id='lastname']")
            l_name.send_keys("chavhan")
            time.sleep(2)
            mail_id = driver.find_element_by_xpath("//form[@id='formVendorSignup']//input[@id='emailid']")
            mail_id.send_keys("ombhagyeshchavhan@gmail.com")
            time.sleep(2)
            click_pin_code = driver.find_element_by_xpath("//form[@id='formVendorSignup']//div[@class='iti__selected-dial-code'][normalize-space()='+971']").click()
            time.sleep(2)
            pin_code_india = driver.find_element_by_xpath("(//span[@class='iti__country-name'][contains(text(),'India (भारत)')])[1]").click()
            contact = driver.find_element_by_xpath("//input[@class='form-control contact_number']")
            contact.send_keys("9158333486")
            time.sleep(2)
            password = driver.find_element_by_xpath("//form[@id='formVendorSignup']//input[@id='pswd']")
            password.send_keys("omworld01")
            time.sleep(2)
            comf_password = driver.find_element_by_xpath("//form[@id='formVendorSignup']//input[@id='confirmpwd']")
            comf_password.send_keys("omworld01")
            time.sleep(2)
            i_agree_checkbx = driver.find_element_by_css_selector("body > div:nth-child(19) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(8) > label:nth-child(1) > input:nth-child(1)").click()
            time.sleep(2)
            submit = driver.find_element_by_xpath("//form[@id='formVendorSignup']//button[@type='submit'][normalize-space()='Submit']").click()
    # driver.switch_to.window(parent_page)


def vendor_logIn_to_mail_link():
    driver.implicitly_wait(20)
    mail_id = driver.find_element_by_css_selector("input[placeholder='Email']")
    mail_id.send_keys("ombhagyeshchavhan@gmail.com")
    time.sleep(2)
    password = driver.find_element_by_css_selector("input[placeholder='Password']")
    password.send_keys("omworld01@")
    time.sleep(2)
    remember_me = driver.find_element_by_css_selector("label[for='remember']").click()
    time.sleep(2)
    signin = driver.find_element_by_css_selector("button[type='submit']").click()
    time.sleep(2)
    # -------- term and condition accept then sunbmit ------------
    # accept_contact = driver.find_element_by_css_selector("label[for='checkme']").click()
    # time.sleep(2)
    # submit = driver.find_element_by_xpath("//*[@id='send_approv']").click()
    submit = driver.find_element_by_css_selector("button[type='submit']").click()


def vendor_logIn():
    driver.implicitly_wait(20)
    parent_page = driver.current_window_handle
    venues_signup = driver.find_element_by_xpath("//*[@id='main']/header/div[2]/a").click()
    child_page = driver.window_handles
    for handle in child_page:
        if handle != parent_page:
            driver.switch_to.window(handle)
            close_screen = driver.find_element_by_xpath("//a[@href='#close-modal']").click()
            mail_id = driver.find_element_by_css_selector("#user")
            mail_id.send_keys("ombhagyeshchavhan@gmail.com")
            time.sleep(2)
            password = driver.find_element_by_css_selector("#password")
            password.send_keys("omworld01@")
            time.sleep(2)
            login = driver.find_element_by_css_selector("#form-submit").click()



def business_hubs():
    driver.implicitly_wait(20)
    driver.execute_script("window.scrollTo(0,2700)")
    # business_hub = driver.find_element_by_xpath("//input[@id='name']")
    # business_hub.send_keys(" skillteck")
    # time.sleep(2)
    description = driver.find_element_by_xpath("//p[@class='ck-placeholder']")
    description.send_keys(" We work in partnership with clients of various sizes – from mid-market to Fortune 100 – while helping them strengthen their IT foundation, manage risk and compliance, and enhance their competitive position.")
    time.sleep(2)
    job_title = driver.find_element_by_xpath("//input[@id='job_title']")
    job_title.send_keys("tester")
    time.sleep(2)
    choose_file1 = driver.find_element_by_css_selector(".hubFile")
    choose_file1.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
    time.sleep(2)
    submit = driver.find_element_by_css_selector("button[type='submit']").click()


def update_profile():
    driver.implicitly_wait(20)
    profile = driver.find_element_by_xpath("//a[@href='http://vendor.zoomvenues.info/admin/users/profile' and @class='d-block']").click()
    time.sleep(2)
    f_name = driver.find_element_by_css_selector("#first_name")
    f_name.clear()
    time.sleep(2)
    f_name.send_keys("ombhagyesh")
    time.sleep(2)
    l_name = driver.find_element_by_css_selector("#last_name")
    l_name.clear()
    time.sleep(2)
    l_name.send_keys("chavhan")
    time.sleep(2)
    contact = driver.find_element_by_css_selector("#contact_number")
    contact.clear()
    time.sleep(2)
    contact.send_keys("9258333486")
    time.sleep(2)
    upload_photo = driver.find_element_by_css_selector(".userFile")
    upload_photo.send_keys("C:\\Users\\GiTESH SONAR\\PycharmProjects\\GoogleAuto\\ZoomVenues\\imgs\\marten-bjork-n_IKQDCyrG0-unsplash.jpg")
    time.sleep(2)
    submit = driver.find_element_by_css_selector("form[id='profileForm'] button[value='submit']").click()



def change_password():
    driver.implicitly_wait(20)
    profile = driver.find_element_by_xpath("//a[@href='http://vendor.zoomvenues.info/admin/users/profile' and @class='d-block']").click()
    time.sleep(2)
    change_pass = driver.find_element_by_css_selector("#custom-tabs-passoword-tab").click()
    time.sleep(2)
    submit = driver.find_element_by_css_selector("body > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > button:nth-child(1)").click()

def click_zoomvenues_logo():
    driver.implicitly_wait(20)
    profile = driver.find_element_by_xpath("//a[@href='http://vendor.zoomvenues.info/admin/users/profile' and @class='d-block']").click()
    time.sleep(2)
    logo_zoomvenues = driver.find_element_by_css_selector(".img-responsive").click()

def test_vendor_page():
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(zoomvenues_url)
    # venues_signIn()
    # vendor_logIn_to_mail_link()
    vendor_logIn()

    time.sleep(3)
    # business_hubs()
    # update_profile()
    # change_password()
    # click_zoomvenues_logo()

    time.sleep(6)
    driver.quit()