#KOSIS API 크롤링
import requests
import json
import pandas as pd

def get_kosis_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

# KOSIS API URL
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=개인API키&itmId=T1+&objL1=ALL&objL2=ALL&objL3=ALL&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&startPrdDe=2014&endPrdDe=2016&orgId=101&tblId=DT_2UNS0233"

# 데이터 가져오기
data = get_kosis_data(url)

if data:
    # JSON 파일로 저장
    with open('kosis_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    # 데이터프레임으로 변환
    df = pd.DataFrame(data)
    
    # CSV 파일로 저장
    df.to_csv(r'C:\Users\m\data\api\kosis_data.csv', index=False, encoding='utf-8-sig')
    
    print("데이터 저장 성공")
else:
    print("데이터 저장 실패ㅠㅠ 코드를 다시 확인하세요")
