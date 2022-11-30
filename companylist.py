import requests
import pprint
import parsel
import csv

f = open('企业名录.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['企业名称', '类型', '区域', '主营'])
csv_writer.writeheader()

for page in range(0, 1, 1):
    url = f'http://www.idacn.org/companys/search.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    companys = selector.css('.companyItem')
    for company in companys:
        title = company.css('h2 a::text').get()   # get()输出形式是 字符串
        companyInfo = company.css('.row p::text').getall()
        companyType = companyInfo[0].replace('类型：','')
        companyArea = companyInfo[1].replace('区域：','').replace('>','')
        companyBusiness = companyInfo[2]
        dit = {
            '企业名称': title,
            '类型': companyType,
            '区域': companyArea,
            '主营': companyBusiness,
        }
        pprint.pprint(dit)
        csv_writer.writerow(dit) 
