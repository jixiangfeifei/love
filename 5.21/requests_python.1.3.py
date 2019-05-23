
import requests

r = requests.get("https://www.amazon.cn/dp/B00H6X6EJU/ref=cngwdyfloorv2_recs_0?pf_rd_p=01374bfc-6b07-4245-85bc-343e152d609c&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=B5S8PK3JE50XQQ6NMTF2&pf_rd_r=B5S8PK3JE50XQQ6NMTF2&pf_rd_p=01374bfc-6b07-4245-85bc-343e152d609c")
print (r.status_code)
print (r.headers)


#======================

kv = {'wd':'python'}

m = requests.get("http://www.baidu.com/s",params = kv)

print (m.status_code)
print (m.request.url)
print (len(m.text))

#============
#爬取网络图片

import os
