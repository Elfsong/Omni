# coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 24


import json
import requests

class Searcher(object):
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        
    def query(query_str):
        raise NotImplementedError("Don't call the base class directly.")
    

class JinaReader(Searcher):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        
    def query(self, url):
        url = f"https://r.jina.ai/{url}"
        payload = {}
        headers = {'Authorization': 'Bearer jina_d6030ac7fbcc4b2485d5ae318de840b00YR4ddgthDJBenCGuL5wB-cZf-2p'}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text
    
class JinaSearcher(Searcher):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        
    def query(self, url):
        url = f"https://s.jina.ai/{url}"
        payload = {}
        headers = {'Authorization': 'Bearer jina_d6030ac7fbcc4b2485d5ae318de840b00YR4ddgthDJBenCGuL5wB-cZf-2p', "X-Timeout": "3"}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.text
    
class MicrosoftSearcher(Searcher):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        
    def query(self, query):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        search_url = "https://api.bing.microsoft.com/v7.0/search"
        params = {"q": query, "textDecorations": True, "textFormat": "HTML"}
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()['webPages']
        return search_results
    
class CiscoSearcher(Searcher):
    def query(self, query_str, doc_num=10):

        url = "https://search.cisco.com/services/search"

        payload = json.dumps({
            "query": query_str,
            "startIndex": 0,
            "count": doc_num,
            "searchType": "CISCO",
            "tabName": "Cisco",
            "sortType": "RELEVANCY",
            "searchMode": "text",
            "callId": "MqgFtek84g",
            "requestId": 1676997244167,
            "taReqId": "1676996834071",
            "appName": "CDCSearchFE",
            "localeStr": "enUS",
        })
        headers = {
            'authority': 'search.cisco.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
            'content-type': 'application/json',
            'cookie': '_cs_c=0; UnicaNIODID=undefined; _gcl_au=1.1.148050418.1675083872; aam_uuid=81665194308821499492291952182538275165; _biz_uid=13b12fdc333d412fe5efb12a7b953edd; ORA_FPC=id=7d62ae1f-0d88-4df7-a70e-c842d822ac77; OptanonAlertBoxClosed=2023-01-30T13:05:06.219Z; _gscu_1403625542=75084248z3d7uo54; _mkto_trk=id:564-WHV-323&token:_mch-cisco.com-1675084440194-64906; Hm_lvt_a804d9548837e94caa5dc76086a8154f=1675084247,1675513224; ELOQUA=GUID=9B35670EC25E429A8513EF4E647ED7D2&FPCVISITED=1; _biz_flagsA=%7B%22Version%22%3A1%2C%22Ecid%22%3A%221075060619%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _ga_MB8Q5XRDJJ=GS1.1.1675514056.2.1.1675514116.0.0.0; AMCVS_B8D07FF4520E94C10A490D4C%40AdobeOrg=1; cdcUniqueKey=ce074507j31h7; check=true; _gid=GA1.2.1753824503.1676861527; anchorvalue=; _ga=GA1.2.1105767920.1675083873; _ga_KP8QEFW4ML=GS1.1.1676878464.6.1.1676880756.60.0.0; aam_uuid=81665194308821499492291952182538275165; _abck=ADC73596B4FFE05BE6EA60E4B6C9754B~0~YAAQLMvcF6elUWuGAQAA3vk1cQmtdkfTgkRxtZZ/AUHk7qKqDn7Bj2C+ThbiiJPcyhZcCzvTf0lMZDTOymozJq2Pm+nyJi47rn04SptLGoiomCVsdGDLT04AcXXkWNy+DSHGtu8ran8i6F92y8TLfgQeSWQ5tqecVTyVcsad+xqjP9STNUHGSSO4nBpcFKjcsFJLQxdjygOUYFWZuPsY6re++Khd0tKRitcxZ/0C7BFAWuDbKvGIVFntlWZsu5OwtFy6bn0v8w4UeaOyTXosgQPJHLaR23G9YWLBOEa8/kJf11RBFdZi0qPYN6RC3tKnHEqXNg/Vi0jLTqboSbZtZjR5HIdnLIzOkMtC9NGSYe0D98tt+ZreJ8ZrqiXorDfuM2YpU+maTbJfgSD48RiTvew0bB2lP0c=~-1~||-1||~-1; _cs_cvars=%7B%222%22%3A%5B%22Template%20Name%22%2C%22supporthomepage_20%22%5D%2C%223%22%3A%5B%22Title%22%2C%22support%20-%20cisco%20support%20and%20downloads%20%E2%80%93%20documentation%2C%20tools%2C%20cases%22%5D%2C%224%22%3A%5B%22Page%20Channel%22%2C%22technical%20support%22%5D%2C%225%22%3A%5B%22Page%20Name%22%2C%22cisco.com%2Fc%2Fen%2Fus%2Fsupport%2Findex.html%22%5D%2C%226%22%3A%5B%22Content%20Type%22%2C%22postsales%22%5D%7D; CP_GUTC=23.50.232.106.272801676952870990; ADRUM=s=1676979479889&r=https%3A%2F%2Fwww.cisco.com%2Fc%2Fen%2Fus%2Fsupport%2Fsecurity%2Findex.html; _uetsid=90094b60b0c911ed821e79548e95a7d9; _uetvid=a5ce3df059b311edbc8ad9e12a380133; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Feb+21+2023+23%3A39%3A58+GMT%2B0800+(Singapore+Standard+Time)&version=6.39.0&isIABGlobal=false&hosts=&consentId=8ee11340-fdbe-4a2f-bd3e-d896a41df0c1&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&AwaitingReconsent=false&geolocation=SG%3B; _biz_nA=238; s_cc=true; WTPERSIST=cisco.gutcid=23.50.232.106.272801676952870990&ora.eloqua=9b35670ec25e429a8513ef4e647ed7d2&cisco.mid=87068195414001827161607572055450456284&cisco.aam_uuid=81665194308821499492291952182538275165&cisco._ga=GA1.2.1105767920.1675083873&cisco.account_or_company_id=sav_203808807; _biz_pendingA=%5B%5D; _cs_id=f58923c4-2645-a49e-d3a8-10741cef96ed.1667531444.17.1676971098.1676971098.1589297132.1701695444411; gpv_v9=search.cisco.com%2Fsearch; mbox=session#bfc535eace8b46b387e986a52c3bf62b#1676998695; AMCV_B8D07FF4520E94C10A490D4C%40AdobeOrg=281789898%7CMCIDTS%7C19409%7CMCMID%7C87068195414001827161607572055450456284%7CMCAAMLH-1677601640%7C3%7CMCAAMB-1677601640%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1677004040s%7CNONE%7CMCAID%7CNONE%7CMCCIDH%7C479621989%7CvVersion%7C4.1.0; utag_main=v_id:018602c76a780080cca57be0f2a005075006006d00e50$_sn:9$_ss:0$_st:1676998650559$vapi_domain:cisco.com$_se:143$unique_visitor:true$ses_id:1676996138834%3Bexp-session$_pn:1%3Bexp-session$ctm_ss:true%3Bexp-session; s_sq=%5B%5BB%5D%5D; JSESSIONID=06D2B5574DFD5902CADF798416FB7872; s_ptc=0%5E%5E0%5E%5E0%5E%5E0%5E%5E76%5E%5E1%5E%5E1061%5E%5E15%5E%5E1164; s_ppvl=cisco.com%2Fc%2Fen%2Fus%2Fsupport%2Fall-products.html%2C95%2C95%2C1408%2C2560%2C1329%2C2560%2C1440%2C1%2CP; s_ppv=search.cisco.com%2Fsearch%2C9%2C9%2C1329%2C1479%2C1329%2C2560%2C1440%2C1%2CP; ADRUM_BT1=R:249|i:574697|t:1721821075650; ADRUM_BTa=R:249|g:c39faf3d-fa2a-46bb-84da-0542194febdc|n:cisco1_d5ce4a50-0e7c-4e42-a5a5-4c7d1bcfcd74; ADRUM_BTs=R:249|s:f; JSESSIONID=D8DAE55FE82728809B04EDB5CC70C575; SameSite=None',
            'origin': 'https://search.cisco.com',
            'referer': 'https://search.cisco.com/search?locale=enUS&query=500%20Series%20WPAN%20Industrial%20Routers%20Configuration&bizcontext=&mode=text&clktyp=button&autosuggest=false&categoryvalue=Cisco%20500%20Series%20WPAN%20Industrial%20Routers&tareqid=1676996834071',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()["items"]
    