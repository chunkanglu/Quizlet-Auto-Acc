from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from time import sleep

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

DRIVER_PATH = 'C:/Users/Kang/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
TEXTBOOK = "https://quizlet.com/explanations/textbook-solutions/linear-algebra-with-applications-7th-edition-9781259066405?__cf_chl_tk=K1euKWI97OM_Z5kzSHe.ISrI3s111tPl4seZBcYgpck-1643038242-0-gaNycGzNC5E"


driver.get(TEXTBOOK)

driver.find_element(by=By.XPATH, value='//*[@id="TopNavigationReactTarget"]/header/div/div[2]/button').click()

month = driver.find_element(by=By.XPATH, value='/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div[1]/select')
month_op = random.choice(month.find_elements(by=By.TAG_NAME, value='option')[1:]).click()

day = driver.find_element(by=By.XPATH, value='/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div[2]/select')
day_op = random.choice(day.find_elements(by=By.TAG_NAME, value='option')[1:]).click()

year = driver.find_element(by=By.XPATH, value='/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div[3]/select')
year_op = random.choice(year.find_elements(by=By.TAG_NAME, value='option')[1:]).click()

email = ''.join(random.choices(string.ascii_letters, k=10)) + "@gmail.com"
user = ''.join(random.choices(string.ascii_letters, k=10))
password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

email_in = driver.find_element(by=By.ID, value='email')
email_in.send_keys(email)

user_in = driver.find_element(by=By.ID, value='username')
user_in.send_keys(user)

pass_in = driver.find_element(by=By.ID, value='password1')
pass_in.send_keys(password)
sleep(2)

driver.find_elements(by=By.CLASS_NAME, value="UICheckbox-input")[-1].click()
driver.find_element(by=By.XPATH, value='/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/button').click()

sleep(2)

driver.get(TEXTBOOK)


