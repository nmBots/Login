import requests, json, random


def QRV2():
    apiKey = "NIGHT MASTER BOTS"
    headers = {
        "apiKey":apiKey, 
        "appName": "DESKTOPWIN\t6.0.3\tWindows\t10",
        "cert" : None, 
        "server": random.choice(["pool-1","pool-2"]), 
        "sysname": "NIGHT MASTER BOTS" 
        }
    main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
    print("")
    print("QR Link: " + main["result"]["qr_link"])
    if not headers["cert"]:
        print('')
        result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
        print("")
        print("Your Pincode: " + result["result"])
    result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
    if result["status"] != 200:
        print("[ Error ] "+ result["reason"])
    else:
        print("")
        print("Your Token: " + result["result"]["token"])
    
QRV2()
        
                               