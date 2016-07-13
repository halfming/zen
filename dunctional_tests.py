from selenium import webdriver
bowser = webdriver.Firefox()
bowser.get('http://localhost:8000')
assert 'Django' in bowser.title
bowser.quit()