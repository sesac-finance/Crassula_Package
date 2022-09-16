# requests, json 모듈 불러오기(Import) 및 실행
import requests
import json

# 크롤링을 진행할 백엔드 서버 URL을 BASE_URL 변수로 할당
BASE_URL = "https://im.diningcode.com/API/isearch/"

def diningcode_crawler(area, page):

    # 크롤링한 결과를 저장할 리스트 초기화
    result = []

    # BASE_URL에 HTTPS 요청을 보내고 응답 확인
    data = {
        "query": area,
        "order": "r_score",
        "rn_search_flag": "on",
        "search_type": "poi_search",
        "mode": "poi",
        "dc_flag": "1",
        "page": str(page),
        "size": "20"
    }
    res = requests.post(BASE_URL, data = data)
    if res.status_code == 200:
        print("서버가 요청한 " + str(page) + "페이지를 성공적으로 제공했습니다.")
    else:
        print("서버로부터 요청한 " + str(page) + "페이지를 받아오는 데 문제가 발생했습니다.")

    # 받아온 페이지의 json 파일을 딕셔너리로 변환하여 저장
    restaurant_list = json.loads(res.text)

    # for 반복문을 통해 rstaurant_list의 restaurant를 순회
    for restaurant in restaurant_list["result_data"]["poi_section"]["list"]:

        # 상호, 주소, 연락처, 분류, 점수를 추출해 딕셔너리로 임시 저장
        name = restaurant["nm"]
        address = restaurant["addr"]
        phone = restaurant["phone"]
        category = restaurant["category"]
        score = restaurant["score"]
        result_dict = {
            "상호": name,
            "주소": address,
            "연락처": phone,
            "분류": category,
            "점수": score
        }
    
        # 식당 수 이상의 페이지가 입력된 경우 중복을 막기 위해 크롤링 중단
        if int(page) > 1:
            print("더 이상의 식당이 존재하지 않습니다.")
            break

        # 딕셔너리로 임시 저장한 정보를 결과 리스트에 추가
        else:
            result.append(result_dict)

    # 페이지 크롤링 종료 후 안내 문구 출력
    print(page + "페이지의 검색 결과를 성공적으로 저장했습니다.")

    # 크롤링 모두 종료 후 안내 문구 출력
    print("크롤링을 마쳤습니다.")

    # 결과 값 반환
    return result