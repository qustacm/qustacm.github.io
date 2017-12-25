#coding=utf-8
import requests
import os
from bs4 import BeautifulSoup
import re

# add more id and name
ids = ["98K1","TravelingFish","lvzh","zigx"]
names = ["恒尉","星宇","zigx"]
acs = []
# nyist.net

my_id = "hanxukun"
my_name = "k"
url = "http://59.69.128.203/JudgeOnline/profile.php?userid=" + my_id
wbdata = requests.get(url).text
soup = BeautifulSoup(wbdata,'lxml')
x = soup.select("th")
m = str(x[0])
my_ac = str(re.sub("\D", "", m))


for id in ids:
    url = "http://59.69.128.203/JudgeOnline/profile.php?userid=" + id
    wbdata = requests.get(url).text
    soup = BeautifulSoup(wbdata,'lxml')
    x = soup.select("th")
    m = str(x[0])
    acs.append(str(re.sub("\D", "", m)))


# write
a_text = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>QUST-ACM-新生Rank</title><script type="text/javascript" src="jQuery.js"></script><script type="text/javascript" src="jqplot.js"></script></head><body><div style="text-align:center;clear:both;"><script src="/gg_bd_ad_720x90.js" type="text/javascript"></script><script src="/follow.js" type="text/javascript"></script></div><div id="chart2"></div><script type="text/javascript">var data = [['

b_text = my_ac
for ac in acs:
    b_text =b_text + ',' + ac

c_text = ']];var data_max = 100; var line_title = ["nyist题数"]; var y_label = "AC题数"; var x_label = "给大佬们递AC"; var x = ['

d_text = '"' + my_name + '"'
for name in names:
    d_text = d_text + ',' + '"' + name + '"'

e_text = ']; var title = "A题使我快乐";j.jqplot.diagram.base("chart2", data, line_title, "A题使我快乐", x, x_label, y_label, data_max, 2);</script></body></html>'
all_the_text = a_text + b_text + c_text + d_text + e_text
file_object = open('index.html', 'w')
file_object.write(all_the_text)
file_object.close()
