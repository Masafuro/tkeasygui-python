from selenium import webdriver


driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

try:
    # Googleのページを開く
    driver.get("https://www.google.com")

    # 検索ボックスを見つける
    search_box = driver.find_element(By.NAME, "q")

    # 検索ボックスに「Python」と入力
    search_box.send_keys("Python")

    # Enterキーを送信して検索を実行
    search_box.send_keys(Keys.RETURN)

    # 結果が表示されるのを待つ（実際のコードでは適切な待機を設定することが重要です）
    driver.implicitly_wait(10)  # 秒単位で指定

finally:
    # ブラウザを閉じる
    driver.quit()
