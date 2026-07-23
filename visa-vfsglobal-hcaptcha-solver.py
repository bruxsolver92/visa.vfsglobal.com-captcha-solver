import requests
API_URL = "https://bruxsolver.io/solve"
API_KEY = "YOUR BRUX SOLVER API KEY GET IT FROM bruxsolver.io"
PROXY = "user:pass@ip:port"
response = requests.post(
            API_URL,
            headers={
                "x-api-key": API_KEY,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json={
            "proxy": PROXY,
        "website_host": "visa.vfsglobal.com",
        "sitekey": "9278ebd4-da60-402a-ac8a-e604bc4ac524",
        "href": "https://visa.vfsglobal.com/tur/tr/fra/login",
        "rqdata_required": False,
        "pow_type": "hsj"
        }
)

if response.json()['success'] ==  True:
    token = response.json()['token']
    print(f'Captcha solved successfully, {str(token[:60])} ')
else:
    print('Failed to solve captcha please try again or contact the administrator @brux92 on telegram.')
