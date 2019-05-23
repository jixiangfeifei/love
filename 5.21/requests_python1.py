import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()             #如果 r.status_code 不是200，将产生异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url ="https://item.jd.com/7115861.html?extension_id=eyJhZCI6IjQ2IiwiY2giOiIyIiwic2t1IjoiNzExNTg2MSIsInRzIjoiMTU1ODQyODg2MyIsInVuaXFpZCI6IntcImNsaWNrX2lkXCI6XCIyNTllYWYwZS1jMjVlLTRjZGEtYmU2Yy04NjU1ZGRhOTI0OTVcIixcIm1hdGVyaWFsX2lkXCI6XCI4Njg1OTM1MzA5Njc0MzkxNjYzXCIsXCJwb3NfaWRcIjpcIjQ2XCIsXCJzaWRcIjpcIjgyZGUwNzc5LTQwY2ItNGE2Mi1iYmUzLWIzODdlZDg2NDIyOFwifSJ9&jd_pop=259eaf0e-c25e-4cda-be6c-8655dda92495&abt=0"
    print(getHTMLText(url))
