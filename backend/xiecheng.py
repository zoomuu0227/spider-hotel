import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def print_hi(name):
    millis1 = int(round(time.time() * 1000))
    millis2 = int(round((time.time() + 1) * 1000))
    url = "https://m.tujia.com/bnbapp-node-h5/h5/search/v2/searchhouse/bnb"
    headers = {
        "Host": "m.tujia.com",
        "Origin": "https://m.tujia.com",
        "Referer": "https://m.tujia",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Cookie": format(
            "_fas_uuid=2269f0d8-b809-4b83-a1f6-8f194b4a530a-1702347265845; _fas_session_id=k0GSsn4TrHEasPkj4AMz9ZRwFxGb1702347265846; tj_channel_id=tujia; clientAgent=T_h5; personalRecommend=true; _fas_fe_log_info=%257B%2522lat%2522%253A%2522null%2522%252C%2522lng%2522%253A%2522null%2522%252C%2522cityId%2522%253A%2522null%2522%252C%2522positionErrorMsg%2522%253A%2522%25E7%2594%25A8%25E6%2588%25B748%25E5%25B0%258F%25E6%2597%25B6%25E5%2586%2585%25E6%258B%2592%25E7%25BB%259D%25E8%25BF%2587%25E4%25BD%25BF%25E7%2594%25A8%25E5%25AE%259A%25E4%25BD%258D%2522%257D; tujia.com_PortalContext_UserToken=40a97b4a-9c95-464f-98ff-6def812f19ae; tujia.com_PortalContext_UserId=368089572; tj_abtest=%255B%257B%2522key%2522%253A%2522waptujia005_mm_1169%2522%252C%2522value%2522%253A%2522C%2522%257D%255D; tujia.com_MobileContext_StartDate=2023-12-13; tujia.com_MobileContext_EndDate=2023-12-14; gr_flag=MC41NTk2MzY0ODgzNDAxOTIxXzBfY2hpcHNfYWhveQ==")
    }
    params = {
        "pid": "SaiG0as6a5SN7ehR3t1fJf5spB69",
        "refPid": "y2miNSRMN4j5ArNXf0DknCy8iccw",
        "act": "",
        "_apitsp": str(millis1),
        "_fasTraceId": str(millis1 + 2) + "0jh826BH_SaiG0as6a5SN7ehR3t1fJf5spB69"
    }
    data = {
        "pageIndex": 0, "pageSize": 10,
        "conditions": [{"type": 1, "value": "23"}, {"type": 7, "value": "100,200"}, {"type": 2, "value": "2023-12-13"},
                       {"type": 3, "value": "2023-12-14"}], "returnFilterConditions": "true",
        "returnGeoConditions": "true", "specialKeyType": 0, "returnNavigations": "true", "excludeUnitIdSet": [],
        "isGetFilterTips": "false", "urlCode": "null",
        "feLog": {
            "h5_base_log": "{\"checkInDate\":\"2023-12-13\",\"checkOutDate\":\"2023-12-14\",\"cityId\":\"null\",\"lat\":\"null\",\"lng\":\"null\",\"pname\":\"unitList\",\"refpname\":\"unitList\",\"pid\":\"KZshBCY4kPw6n6Zii2MJa11fADFQ\",\"refPid\":\"y2miNSRMN4j5ArNXf0DknCy8iccw\",\"positionErrorMsg\":\"用户48小时内拒绝过使用定位\"}"
        }
    }
    t = requests.post(url=url, params=params, headers=headers, data=data)
    print(t.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
