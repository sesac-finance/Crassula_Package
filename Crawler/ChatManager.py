# 필요한 라이브러리 및 클래스 불러오기(Import)
import json

# ----------------------------------------------------------------------------------------------------

def chat_id_manager(chat_id, result):
    """
    채팅방 ID(chat_id)와 검색 결과(result)를 입력 받아 json 파일로 저장해 주는 함수입니다.
    """

    # chat_id를 json 파일에 저장 및 result 변수 초기화
    with open("./Chat_Room/ChatID.json", "r") as openfile:
        chat_rooms = json.load(openfile)
        chat_rooms[str(chat_id)] = result
        with open("./Chat_Room/ChatID.json", "w") as savefile:
            json.dump(chat_rooms, savefile)

    return print(f"채팅방 ID({chat_id})가 기록되었습니다.")

# ----------------------------------------------------------------------------------------------------

def result_exist(chat_id):
    """
    채팅방 ID(chat_id)의 검색 결과(result)가 존재하는지 여부를 판단해, 결과를 반환해 주는 함수입니다.
    """

    # json 파일을 열어 딕셔너리로 가져오기
    with open("./Chat_Room/ChatID.json", "r") as openfile:
        chat_rooms = json.load(openfile)

        # 해당 채팅방의 검색 결과가 존재하지 않는 경우 False 값 반환
        if chat_rooms[str(chat_id)] == [] or chat_rooms[str(chat_id)] == ["error"]:
            return False

        # 해당 채팅방의 검색 결과가 존재하는 경우 결과 반환
        else:
            result = chat_rooms[str(chat_id)]
            return result