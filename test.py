from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.by import By

class test_cases:
    def cases_1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        login = driver.find_element(By.ID,"login-button")
        login.click()

        error_Message = driver.find_element(By.XPATH, "//*'[@id='login_button_container']'/div/form/div[3]/h3")
        test_Result = error_Message.text =="Epic sadface: Username is required"
        print(f"Yapılan 1. testin sonucu: {test_Result}")

    def cases_2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")

        usserInput = driver.find_element(By.ID,"user-name")
        usserInput.send_keys("1")

        login =driver.find_element(By.ID,"login-button")
        login.click()

        error_Message = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        test_Result = error_Message.text == "Epic sadface: Password is required"
        print(f"Yapılan 2. testin sonucu: {test_Result}")

    
    
    def cases_3(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.get()

        usserInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")

        usserInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")

        login = driver.find_element(By.ID, "login-button")
        login.click()

        error_Message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_Result = error_Message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Yapılan 3. testin sonucu: {test_Result}")
        

    def cases_4(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        login = driver.find_element(By.ID, "login-button")
        login.click()

        user_name_icon =driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        user_name_icon_enb = user_name_icon.is_enabled()
        print(f"Kullanıcı hata ikonu var mi: {user_name_icon_enb}")

        passwordIcon = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        passwordIconEnb = passwordIcon.is_enabled()
        print(f"Sifre hata ikonu var mi: {passwordIconEnb}")


        error_Message_Button = driver.find_element(By.CLASS_NAME, "error-button")
        var = error_Message_Button.is_enabled()
        print(f"Hata mesajını kapatmak için buton var mı? {var}")
        error_Message_Button.click()
        
    def cases_5(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        
        email_input = driver.find_element(By.ID, "user-name")
        password_Input = driver.find_element(By.ID, "password")

        email_input.send_keys("standart_user")
        password_Input.send_keys("secret_sauce")
        login = driver.find_element(By.ID, "login-button")
        login.click()
        print("Inventoy'e geçiş yapıldı.")
    
    def cases_6(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        
        email_input = driver.find_element(By.ID, "user-name")
        password_Input = driver.find_element(By.ID, "password")

        email_input.send_keys("standart_user")
        password_Input.send_keys("secret_sauce")
        login = driver.find_element(By.ID, "login-button")
        login.click()
        print("Inventoy'e geçiş yapıldı.")

        list1 = driver.find_element(By.CLASS_NAME, "inventory_item")
        print(f"{len(list1)} adet kadar ürün sayısı var.")

    
class_test = test_cases()

# class_test.cases_1()
# class_test.cases_2()
# class_test.cases_3()
# class_test.cases_4()
# class_test.cases_5()
# class_test.cases_6()

