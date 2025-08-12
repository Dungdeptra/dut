from flask import Flask, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "105240338"
PASSWORD = "Dung123"
LOGIN_URL = "https://sv.dut.udn.vn/PageDangNhap.aspx"
RESULT_URL = "https://sv.dut.udn.vn/PageKQRL.aspx"

app = Flask(__name__)

@app.route("/")
def xem_diem():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(LOGIN_URL)
    driver.find_element(By.NAME, "_ctl0:MainContent:DN_txtAcc").send_keys(USERNAME)
    driver.find_element(By.NAME, "_ctl0:MainContent:DN_txtPass").send_keys(PASSWORD)
    driver.find_element(By.NAME, "_ctl0:MainContent:DN_txtPass").send_keys(Keys.RETURN)

    time.sleep(1)

    driver.get(RESULT_URL)
    time.sleep(1)

    html_content = driver.page_source
    driver.quit()

    return Response(html_content, mimetype="text/html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
