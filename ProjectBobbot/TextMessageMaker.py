def search_message(page, result):
    """
    페이지 수(page)와 크롤링한 결과(result)를 입력받아 봇이 보낼 메시지를 반환하는 함수입니다.
    """

    # 결과로 출력할 response_text 문자열 초기화
    response_text = ""

    # for 반복문과 enumerate() 함수를 통해 식당 상호, 분류, 순위를 만들어 문자열에 추가
    for index, restaurant in enumerate(result):
        ranking = index + int(page) * 20 - 19
        name = restaurant["상호"]
        category = restaurant["분류"]
        response_text += f"{ranking}위. 【 {name} 】  //  {category}\n"

    # 결과 값 반환
    return response_text

# ----------------------------------------------------------------------------------------------------

def info_message(ranking, result):
    """
    순위(ranking)와 크롤링한 결과(result)를 입력받아 봇이 보낼 메시지를 반환하는 함수입니다.
    """
    
    # 메시지로 출력할 결과가 담긴 인덱스를 index 변수에 할당
    index = int(ranking) % 20 - 1

    # 필요한 정보를 추출해 각 변수로 할당
    name = result[index]["상호"]
    address = result[index]["주소"]
    category = result[index]["분류"]
    phone = result[index]["연락처"]
    score = result[index]["점수"]
    hyperlink = result[index]["링크"]

    # 결과로 출력할 response_text 문자열 설정
    response_text = f"{ranking}위. 【 {name} 】  //  {category}\n    - 점수: {score}\n    - 연락처: {phone}\n    - 주소 : {address}\n    - 다이닝코드에서 더 보기: [링크]({hyperlink})"

    # 결과 값 반환
    return response_text

# ----------------------------------------------------------------------------------------------------

def help_message():
    """
    봇이 보낼 명령어 안내 메시지를 반환하는 함수입니다.
    """

    # 결과로 출력할 response_text 문자열 설정
    response_text = """밥봇의 명령어는 다음과 같습니다.
    
※ /start : 봇과의 대화 새로 시작, 기존 검색 결과 초기화
※ /help : 명령어 전체 목록 출력
※ /search [지역] [페이지] : 다이닝 코드의 검색 결과 출력
    (예) /search 문래동 1
※ /info [식당 순위] : 검색 결과에서 특정 순위 식당의 상세 정보 확인
    (예) /info 9
※ /feedme : 밥봇에게 밥 먹여달라고 하기"""

    # 결과 값 반환
    return response_text