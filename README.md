# Zomato-Indian-restaurant-Scraper
I implemented a scraper on Zomato to scrape the data of the different type of restaurant. I find the restaurant rating, locality, etc. I used selenium, Beautiful-soup in this project.

## How to install Chrome driver 
```
sudo apt-get update
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

## selenium
```
wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
unzip testng-6.8.7.jar.zip
xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar
chromedriver --url-base=/wd/hub
pip install urllib3==1.23
pip install requests
```
 
