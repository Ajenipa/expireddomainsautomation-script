from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\AJENIPA JAMIU\\chromedriver.exe")#  the downloded chrome driver your file path
driver.get('https://www.expireddomains.net/')
driver.find_element_by_link_text("Login").click()
driver.find_element_by_id("inputLogin").send_keys("enter your expireddomains.net username here")
driver.find_element_by_id("inputPassword").send_keys('enter your expireddomains.net password here')
driver.find_element_by_css_selector("div.container:nth-child(3) div.row div.col-md-6.col-sm-12:nth-child(1) div.box div.box-content form.form-horizontal div.form-group:nth-child(4) div.col-sm-12 > button.btn.btn-default").click()
driver.find_element_by_css_selector('div.container-fluid:nth-child(3) div.row:nth-child(2) div.col-md-12 div.tab-content div.tab-pane.active:nth-child(1) ul.navlist.l_tinynav1 li.subbutton.dropdown:nth-child(2) > a.sublink.dropdown-toggle').click()
driver.find_element_by_css_selector('div.container-fluid:nth-child(3) div.row:nth-child(2) div.col-md-12 div.tab-content div.tab-pane.active:nth-child(1) ul.navlist.l_tinynav1 li.subbutton.dropdown.open:nth-child(2) ul.dropdown-menu li:nth-child(1) > a:nth-child(1)').click()
driver.find_element_by_link_text('Show Filter').click()
driver.find_element_by_css_selector('#fwordcountmax').send_keys('2')
driver.find_element_by_link_text('Additional').click()
driver.find_element_by_css_selector('#fstatusnetnot').click()
driver.find_element_by_css_selector('div.container-fluid:nth-child(3) div.expiredcom div.filter:nth-child(1) form:nth-child(1) div.row:nth-child(9) div.col-xs-12 > input.btn.btn-primary').click()
driver.save_screenshot("C:/Users/AJENIPA JAMIU/Desktop/exp.png") #for saving the screenshot test result to my desktop
driver.quit()