from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

uid = ""
name = ""
perc_10 = ""
school_name = ""
board = ""
pass_year_10 = ""
perc_12 = ""
stream_12 = ""
pass_year_12 = ""
grad_course = "B.E."
cgpa = ''
grad_uni = ""
grad_location = ""
grad_spec = ""
grad_year = ""
post_grad = ""
backlogs = ""
address = ""
pin_code = ""
curr_city = ""
college_id = ""
personal_id = ""
contact_no = ""
alt_contact_no = ""
skype_id = ""
resume_link = ""

options = webdriver.ChromeOptions()
userdatadir = 'C:/Users/{userName}/AppData/Local/Google/Chrome/User Data'
options.add_argument(f"--user-data-dir={userdatadir}")

url = ""
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(4)

# Enter UID
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(uid)
time.sleep(2)
# Enter Name
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)
time.sleep(2)
# Choose College
driver.find_element(By.XPATH, '//*[@id="i19"]/div[3]/div').click()
# Enter Course
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_course)
# Enter Stream
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_spec)
# Choose Gender
driver.find_element(By.XPATH, '//*[@id="i39"]/div[3]/div').click()
# Enter 10th %
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(perc_10)
time.sleep(2)
# Enter 10th School Name
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(school_name)
time.sleep(2)
# Enter 10th Board Name
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(board)
time.sleep(2)
# Enter 10th passing year
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(pass_year_10)
time.sleep(2)
# Enter 12th percentage
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(perc_12)
time.sleep(2)
# Enter 12th stream
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(stream_12)
time.sleep(2)
# Enter 12th board name
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(board)
time.sleep(2)
# Enter 12th school name
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(school_name)
time.sleep(2)
# Enter 12th passing year
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[16]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(pass_year_12)
time.sleep(2)
# Enter grad course
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[18]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_course)
time.sleep(2)
# Enter grad campus
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[19]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_uni)
time.sleep(2)
# Enter grad uni
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[20]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_uni)
time.sleep(2)
# Enter grad location
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[21]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_location)
time.sleep(2)
# Enter grad spec
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[22]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(grad_spec)
time.sleep(2)
# Enter grad gpa
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[23]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(cgpa)
time.sleep(2)
# Enter comm address
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[27]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)
time.sleep(2)
# Enter Pin Code
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[28]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(pin_code)
time.sleep(2)
# Enter Current City
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[29]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(curr_city)
time.sleep(2)
# Enter perm address
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[30]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address)
time.sleep(2)
# Enter College Email Id
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[31]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(college_id)
time.sleep(2)
# Enter Personal Email
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[32]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(personal_id)
time.sleep(2)
# Enter Contact No
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[33]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(contact_no)
time.sleep(2)
# Enter Alt No
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[34]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(alt_contact_no)
time.sleep(100)
