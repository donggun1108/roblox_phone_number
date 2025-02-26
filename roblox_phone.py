import requests

url = "https://accountinformation.roblox.com/v1/phone"
verify_url = "https://accountinformation.roblox.com/v1/phone/verify"
Session = requests.session()

나라 = input("나라 입력좀 :") # KR
국번 = input("ex) 한국이면 82: ") # 82
전화번호 = input("전화번호 입력좀: ") # 01012345678

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Host" : "accountinformation.roblox.com",
    "Origin" : "https://www.roblox.com",
    "Referer" : "https://www.roblox.com/",
    "Cookie" : "" # 쿠키
}

csrf_request = Session.post(url, headers=headers)
csrf_token = csrf_request.headers.get("X-CSRF-TOKEN", "")
headers["X-CSRF-TOKEN"] = csrf_token

pay_load = {
    "countryCode": 나라,
    "prefix": 국번,
    "phone": 전화번호
}

response = requests.post(url, headers=headers, data=pay_load)

try:
    json = response.json()
    print("응답 :", response.status_code)
    print("전번 전송 여부:", json)
except requests.exceptions.JSONDecodeError:
    print("운지함, 응답: ",response.text)

인증번호 = input("인증번호 입력: ").strip()

verify_payload = {"code": 인증번호}

verify_response = Session.post(verify_url, headers=headers, json=verify_payload)

if verify_response.status_code == 200:
    print("인증성공!")
    print("응답:", verify_response.json())
else:
    print("인증실패:", verify_response.text)
