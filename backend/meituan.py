import time

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

idList = []


def getDetail(id):
    headers = {
        "Host": "ihotel.meituan.com",
        "Referer": "https://servicewechat.com/wxde8ac0a21135c07d/1244/page-frame.html",
        "Content-Type": "application/json",
        "openId": "oJVP50Ct47PMuZGv_06o1B9iIyqs",
        "openIdCipher": "AwQAAABJAgAAAAEAAAAyAAAAPLgC95WH3MyqngAoyM/hf1hEoKrGdo0pJ5DI44e1wGF9AT3PH7Wes03actC2n/GVnwfURonD78PewMUppAAAADhRFbUASCnZVDdapFM6KtsqVwhu6skbGOYzN7kJ6xbT4yKSYWwjNGLUJCkDz84N9jUeKAyjcdmBaw==",
        "M-APPKEY": "wxmp_mt-weapp",
        "token": "AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.5(0x13080510)XWEB/1100",
        "mtgsig": '{"a1":"1.2","a2":1702455502837,"a3":"7y5zu7827y75543vz3zx63x8034z64w781x4x45582v97978u3w4w30u","a4":"882c171a1cdc42f11a172c88f142dc1cef706dea1e32b1f6","a5":"BT57xq5zFymjcnKMpYdzZfzLjRGxu2VbNtwst9owG8D3DCZs5uYKVl4eAYsFPY1Z5emMGiFpZ9vWiv6kAioitV3g4apg883f6O7kvsxGajPpxQcQn2ot7jlId+10qiwHtKJa7soKBZRGw7s+WCsjUxBsPC4YF9sFNsXTNi2goeXkNI6SoKWBWsV3kCh94fGUUo/SnUgjcPH0JIWXhu0jGc==","a6":"w1.3UsjKuZegZQtaPab/h2xxBtg5EzcQtupCOL+ToYMbIsYOdRHjnyFyOaf/nBAS/2ap7+f2TJQDppuHC/uHtuiHFSuFHtma0RzH2VRBWLNPUDOV/w5dQxJpDQ3MD+b5UVLACyYxRsM2N401z8keHQkjVcEYwjXVYsfPCTu0emWWO+p+q3WQr7CIlRDtK9mGwWuEgLSoHERwDRntvpKfVkmBfreEzawsHN5bZBjFHfU8eqgVG6mSInqEILimeY/MDdkTXjJtk8xa5r6sEJzARfphRvDAe5RTaqv3DEC1MnIsJLhIW9tRPEdMK5MexrXkoD4+eAj6v+7x/zHWqb5P/RZnlNWBNKZZ6nTDyMeC4qFxvBCO4jWBKIwxdR152CAeCCnKbkPl92H9lM8pA673xlNiiBCfMIsLYyE6w6cjRCrzfFJHyrfn0zv/fchglJ9ycitPIXOSDprj5XeELJtXVLCtAg95L8GUTCYHUgh9S8lI6blP03VIJEDLLkF5c8tUmkzn","a7":"wxde8ac0a21135c07d","x0":3,"d1":"8fe288ac5d2ae6ad806e41841d77c056"}',
    }
    # 获取详情时，每次url都会变化
    url = "https://ihotel.meituan.com/group/v1/poi/{0}?openId=oJVP50Ct47PMuZGv_06o1B9iIyqs&antiRepPlatform=Mac&programName=mt&utm_medium=WEIXINPROGRAM&riskLevel=71&optimusCode=10&openIdCipher=AwQAAABJAgAAAAEAAAAyAAAAPLgC95WH3MyqngAoyM%2Fhf1hEoKrGdo0pJ5DI44e1wGF9AT3PH7Wes03actC2n%2FGVnwfURonD78PewMUppAAAADhRFbUASCnZVDdapFM6KtsqVwhu6skbGOYzN7kJ6xbT4yKSYWwjNGLUJCkDz84N9jUeKAyjcdmBaw%3D%3D&utm_campaign=entry%253DMTLive_scene%253D1074&token=AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn&usertoken=AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn&userToken=AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn&userId=219058143&userid=219058143&uuid=18c5c543b4cc8-1d8d9225cee627-0-0-18c5c543b4cc8&locateCityId=59&locatecityid=59&lat=30.542962718901638&lng=104.06076241446382&appletShieldScene=null&poiId={0}&mypos=30.542962718901638%2C104.06076241446382&cityId=59&subtype=0&type=1&recType=0&isRecommend=0&propagateData=%25257B%252522content%252522%25253A%252522CYksnts4RuHwqJNWe0pdnBfdXO%25252Foey9L4QN2MsyRADklHANn3qWcwE%25252FLQ%25252FGfsB7SPXkJbktw9wPuKNIxumvskhN5zJChagHVFvDXQ4h3qrWZvRGKjAArozng7N47WjRVwoww6FoBb6aR%25252FvFsrpE9OUYd%25252FZzNjkbJClA4k5UnvzkBA4n6ZETeKa5zIrhwuLtA6ggoRO%25252Bs0aiGZedumZXI5Z1VA6jTwm2iJe4ZqM2STxVyvTu%25252BtzQSVD8mVZ4rxBbKNsgEJmU5dehF%25252FRzpSEJioLfLLe7cZmnGWhQcPLrMnk2psuyLwz2sQL6GNW36Hza5n6DUrhytfNKfI2NaPMCNJF8OL7fDDTWrq6%25252BP0W0MT5yStn2zo5SvQcLqrRX6ZXFAOJhdi2i%25252Fa%25252BeJ6%25252FCsi7m3s3kNWDOvQThEPSx%25252F7A%25252Fro5qQSrd9wrOZMQ2uK0XHZrgYASGtkLeS9SDqM%25252Brd8CBAG68leaSJfoHvYcgKAwu%25252FMSEklZp3WHsRa5IRyLpCkhwCf9DbjkzbMuzKW%25252Bp5g0KVROfq8dHCRnUXQrJKuGP6BbNZjDFQZuKXb9wmZquw5j2bqd3Zl0F0%25252FwZMs7xVSeRkTNPDxNs8oBA7qr2dvSldI8%25252B3ZFEYS10242Jr%25252B9rRNvsNSVkbqC23bbAWgx%25252BMctbugdKawl0lGy%25252FsIuxShPB9OUuhO%25252BbKcsCPjOhHbPaZpdQPd1ifUCrQqOmK546zDw%25252FC0t5a2wB3pyjlQvnUiEmCCzL4JELOfpvo%25252FpcGdzRZO2H5ovh2h7vcZu4jkY2iWj9SfpGYqYE8bG19zh2I7IABPw3HAUKxxtCvxcaIgGGXVKep%25252BTN0rWLUZ6Wv5k8JrhBNkHZGQgF04z0XZNYbNjSwcI8Xr9Se8pLH5fhJrq7Lma4CO7ccWf4QRDVIxydFw69WS8Ohh8Uo36Z7hApbhER%25252B5KHmNNqvxThUWObLjJ9Gk0hJm52HGRzILMmgqp84eFespcvvIbJs3ZHM2vuf%25252FB1Kb8OeKAPkeY4lO%25252B3ddcDElHm5jjRjp9pmHmx5h%25252F53Xg%25252FpBOfl7Eq76m4u2rbAAOiEGD2b1bxQtObOcv9P%25252BAO5YYJqkTLTzAdDuyYSavNg8W8nTWxYkoaHm%25252B24Cd1DBq2pnyLLGPioU3%25252FF6ubSWZdeYFc3CJyk1H769%25252BACWeVAVx0ZZtLGW4ralbMXo27da4CbpH2HEGFMOUNrwACaZUpFoSOHoMvym65elnvsCd7wKH9Pn6sNL9BRE7wcCyLwHSCCfcuD1zRy5li61slQZzlSL1PkQ9MpSOCIroDwLrryRcdMyraAiXV9vCSJA5h7ZVLxFl5P5zR5OwiIOZAm2BGMxbm3%252522%25252C%252522contentTransparent%252522%25253A%252522A1k14jdZvFfvvbI4tFBVU5Zr9mOsuXV3TAnaqke1CS2QU5GgupDZ%25252FQ2iRa8HmZN3vcG%25252F6XUEWwHhweNjxJbp8Ta0JgzPhGQFfXA571Y%25252FEhANM%25252Bz%25252FLUu3P84jdjUHLRB5%25252BGqKgqaAGmBHDj3bc2h8AsidZAPfIYV30gMgqAps2yvA0f1qsHQd8n8I0rwMlnpN1Rgd8VV46KV21XvqqvCMYbSQan7J2wBHuvAGjlldlS4dbbzix7XI0R1o2ekLWb9oKwgrxEglKMjj0qy9ABpyO%25252FR%25252FDNnU8rhHStg4ZFYksHaKeU9xgq24qRhEdemOj0qPLkM3aTKwG%25252F9g7KUkAKzS2LjxO3XztCr2jUAq82uGQ78BU64zYRGIMNGLVKZlgzMPAcAaOA%25252Bvdsjfa1BI%25252FR4TQq52zS%25252BQWsKHYZZmNgQ7ET0Q5M2lW82EQ0hoU0wa0HMh%252522%25252C%252522poiType%252522%25253A%2525221%252522%25257D&isLocal=1&entryType=2&fields=phone%2CmarkNumbers%2CcityId%2Caddr%2Clng%2ChasGroup%2CsubwayStationId%2Ccates%2CfrontImg%2CchooseSitting%2Cwifi%2CavgPrice%2Cstyle%2CfeatureMenus%2CavgScore%2Cname%2CparkingInfo%2Clat%2Cintroduction%2CshowType%2CareaId%2Cpreferent%2ClowestPrice%2CcateName%2CareaName%2CsourceType%2Cgeo%2CfodderInfo%2CscoreSource%2CbrandId&city_id=59&locate_city_id=59&gps_cityid=59&client=iphone&client_type=&utm_term=8.7.0&version_name=8.7.0&utm_content=&utm_source=&showComment=true&isInfoReqOver=false&isShowMoreHour=false&start=1702425600000&end=1702512000000&utm_fp=MINI_PROGRAM&wechatVersion=3.8.5&SDKVersion=3.0.2".format(
        id)

    t = requests.get(url=url, headers=headers)
    print(url)
    print(t.text)
    res = t.json()
    print(res["data"]["name"])


def getList(page):
    headers = {
        "Host": "ihotel.meituan.com",
        "Referer": "https://servicewechat.com/wxde8ac0a21135c07d/1244/page-frame.html",
        "Content-Type": "application/json",
        "openId": "oJVP50Ct47PMuZGv_06o1B9iIyqs",
        "openIdCipher": "AwQAAABJAgAAAAEAAAAyAAAAPLgC95WH3MyqngAoyM/hf1hEoKrGdo0pJ5DI44e1wGF9AT3PH7Wes03actC2n/GVnwfURonD78PewMUppAAAADhRFbUASCnZVDdapFM6KtsqVwhu6skbGOYzN7kJ6xbT4yKSYWwjNGLUJCkDz84N9jUeKAyjcdmBaw==",
        "M-APPKEY": "wxmp_mt-weapp",
        "token": "AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/6.8.0(0x16080000) NetType/WIFI MiniProgramEnv/Mac MacWechat/WMPF MacWechat/3.8.5(0x13080510)XWEB/1100",
        "mtgsig": '{"a1":"1.2","a2":1702450926792,"a3":"7y5zu7827y75543vz3zx63x8034z64w781x4x45582v97978u3w4w30u","a4":"97d24dcfea4a39f6cf4dd297f6394aea07d929f6f1e0631c","a5":"5XI55PeaY24YXE/H/HV1zq6vrt7yuPUYqXSsnNYgvpD0fjh2x8QsUaOVLTCTB7oTpmPi/LN4Q7cGHrRVIyKkB3fkzsXr0CWjXFLGK3lQa82q1CR0Ix4jo/Rw622aXZieymcDrWcauwY0gHUu25w9fL17Ays6NG0kO80zsWyoE/cszInbjBQXusSV8k1cQi9kfDcFt8+2oWv7slC11amw","a6":"w1.3EjMPi+COREn91TXG5bze8/WU5f91khU4rxVrPtO02jUeqJoKG8+TdcCjXETHE+Dgeafp+7jsnsLgHIDWN83B0rrpwAL9gda6BmuDuVf4D6s3QwovQPdWd5oXF7Udks9/ff046u6lU8BM+0r3NCLcnOr2HnW8ZyKhpECFKhQ4a2OJMY7h4QisCxaUxa3zYe09SgpyIJxQj0pzkU4Dmg6Io8dQL9XHY9/gJCBU/5i8vZe5Qa2PHUx7bSou58F6+uUkcEJIG8X0yVzYLPwO79nxBk7wuidXMspFXt2954Z1yPi5SUdeWzgD77WDpyLWmK5C9QTS7iGwA1rOebUwYgzXANeQWM1g7Ti1lqPmCJtyRMIZEzd8gy8txJCwMSYcm0Nd5Y8zZ1G4HM60TTDrNos/Iu8w3UAuAC8DNI5h3N4vBrXm8LSmZgkwMnIkNZeiMNLb/Z1ejQEfiAHcpluM72HYafCqGcDXGF6mvC678GFHBW3SyE4/NQwMhxikyYSzXb80","a7":"wxde8ac0a21135c07d","x0":3,"d1":"33ae1bdea631f305ae165730e73d0eae"}',

    }
    url = "https://ihotel.meituan.com/coresearch/HotelSearch?openId=oJVP50Ct47PMuZGv_06o1B9iIyqs&antiRepPlatform=Mac&programName=mt&utm_medium=WEIXINPROGRAM&riskLevel=71&optimusCode=10&openIdCipher=AwQAAABJAgAAAAEAAAAyAAAAPLgC95WH3MyqngAoyM%2Fhf1hEoKrGdo0pJ5DI44e1wGF9AT3PH7Wes03actC2n%2FGVnwfURonD78PewMUppAAAADhRFbUASCnZVDdapFM6KtsqVwhu6skbGOYzN7kJ6xbT4yKSYWwjNGLUJCkDz84N9jUeKAyjcdmBaw%3D%3D&utm_campaign=entry%253DMTLive_scene%253D1074&token=AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn&usertoken=AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn&userToken=AgG_IIKcaRXmmLUfu7RyULjJjJ0C6SBAHDhk4ZYlzLuuRQ20LHuCv26MejkRgwlrEZ5c-YjQxQkaQAAAAACJHAAAniRt5DWrMYXLkHPzgtwxQetWcE2EMbJhNDJzi1RvxOLtLeFA4EsRPwVmzZp2Aezn&userId=219058143&userid=219058143&uuid=18c5c543b4cc8-1d8d9225cee627-0-0-18c5c543b4cc8&locateCityId=59&locatecityid=59&lat=30.542962718901638&lng=104.06076241446382&appletShieldScene=null&limit=12&hotelStar=&price=&cityId=59&ci=59&gps_cityid=59&antiRepCityId=59&antiRepLocateCityId=59&category=5&client=android&cateId=20&cate=20&attr_28=129&version_name=9.14.800&mypos=30.542962718901638%2C104.06076241446382&sourceType=hotelSearch&wechatVersion=3.8.5&sdkVersion=3.0.2&startDay=20231213&endDay=20231213&query=&_setResultTimeStamp_=1702450926719&q=&offset={0}&hotelCustomGpsStatus=1&utm_fp=MINI_PROGRAM&SDKVersion=3.0.2".format(
        (page - 1) * 12)
    t = requests.get(url=url, headers=headers)
    res = t.json()
    list = res["data"]["searchresult"]
    for i in list:
        # 插入商品id
        print(i)
        # idList.append(i["shopId"])
        getDetail(i["shopId"])
        time.sleep(2)


def print_hi(name):
    getList(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
