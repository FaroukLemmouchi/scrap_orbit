from selenium import webdriver
import time, datetime

browser = webdriver.Chrome('/home/farouk/Downloads/chromedriver')
browser.get('https://evdc.esa.int/orbit/')
browser.implicitly_wait(5)

# s5p data avaliable since (30 avril 2018)
# resolution refined 5.5 x 3.5 km (6 Aout 2019)
year0 = 2019
month0 = 8
day0 = 7
deltadays = 13 #13 days maximum TLE incertainty

print(f'Initial date : {year0}-{month0}-{day0} yyyy-mm-dd')


#Instruments selection : checkboxes
browser.find_element_by_id('instrument-36').click() # s5p
browser.find_element_by_id('sat-29108').click() # calipso


browser.find_element_by_name('query_start_time').send_keys('1200PM')
browser.find_element_by_name('query_end_time').send_keys('300PM')

#date setup
date0 = datetime.datetime(year0,month0,day0)
date1 = date0

while date1 < datetime.datetime.now() :
  browser.find_element_by_name('query_start_date').send_keys(date0.strftime('%m%d%Y'))

  date1 = date0 +  datetime.timedelta(days = deltadays)
  browser.find_element_by_name('query_end_date').send_keys(date1.strftime('%m%d%Y'))

  print(f'from {date0.strftime("%Y%m%d")} to {date1.strftime("%Y%m%d")}')
  browser.find_element_by_id('temporal_search').click()

  time.sleep(4)
  #download results
  browser.find_element_by_xpath("//button[@class='btn btn-primary temporal-button'][last()]").click()
  browser.find_element_by_xpath('//button[@data-bb-handler="downloadCSV"]').click()

  time.sleep(30) # must be >= 30

  date0 = date1

