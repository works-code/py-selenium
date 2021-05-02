from selenium import webdriver
import time

# headless 모드(background)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome("/Users/hongyoolee/document/study/capture/chromedriver", options=options)
try:
	driver.get("https://co-de.tistory.com/")
	# 스크린샷 전에 시간 두기(로딩이 느릴수도 있으니)
	time.sleep(3)
	# 창 최대화
	driver.maximize_window()
	# 스크린샷 찍기
	driver.save_screenshot("/Users/hongyoolee/document/study/capture/capture.png")
	# 종료 (모든 탭 종료)
	driver.quit()
	print("### capture complete")
except Exception as e:
	print('### error msg :: ', e)
	driver.quit()
