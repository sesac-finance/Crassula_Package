# 필요한 라이브러리 및 클래스 불러오기(Import)
import json

# ----------------------------------------------------------------------------------------------------

def chat_id_manager(chat_id, result, page):
    """
    채팅방 ID(chat_id)와 검색 결과(result), 페이지(page)를 입력 받아 json 파일로 저장해 주는 함수입니다.
    """

    # chat_id를 json 파일에 저장 및 result 변수 초기화
    temp = {}
    temp["ID"] = chat_id
    temp["Log"] = result
    temp["Page"] = page

    with open(f"./ChatLog/{chat_id}.json", "w", encoding = "utf-8") as savefile:
        json.dump(temp, savefile)

    return print(f"채팅방 ID({chat_id})가 기록되었습니다.")

# ----------------------------------------------------------------------------------------------------

def result_exist(chat_id):
    """
    채팅방 ID(chat_id)의 검색 결과(result)가 존재하는지 여부를 판단해, 결과와 페이지를 반환해 주는 함수입니다.
    """

    # json 파일을 열어 딕셔너리로 가져오기
    with open(f"./ChatLog/{chat_id}.json", "r") as openfile:
        chat_logs = json.load(openfile)

        # 해당 채팅방의 검색 결과가 존재하지 않는 경우 False 값 반환
        if chat_logs["Log"] == [] or chat_logs["Log"] == ["error"]:
            return False, False

        # 해당 채팅방의 검색 결과가 존재하는 경우 결과 반환
        else:
            result = chat_logs["Log"]
            page = chat_logs["Page"]
            return result, page