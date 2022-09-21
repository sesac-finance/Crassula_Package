# 필요한 라이브러리 및 클래스 불러오기(Import)
from ChatLogManager import *
from DiningCodeCrawler import *
from TextMessageMaker import *
import time

# ----------------------------------------------------------------------------------------------------

def start(update, context):
    """
    봇 최초 실행 시 텔레그램 명령어의 목록과 사용 방법을 설명하고, 채팅방 ID를 저장하는 함수입니다.
    """

    # 크롤링한 결과를 담을 result 리스트 초기화
    result =[]

    # help() 함수를 호출해 실행
    help(update, context)

    # 현재 대화 중인 채팅방 ID를 찾아 chat_id 변수에 할당
    chat_id = update.effective_chat.id

    # chat_id_manager() 함수를 호출해 실행
    chat_id_manager(chat_id, result)

# ----------------------------------------------------------------------------------------------------

def search(update, context):
    """
    크롤링 함수를 실행해 검색 결과를 메시지로 전송하는 함수입니다.
    """
    
    # 매개변수로 받아온 값을 area, page 변수에 할당하고 안내 문구 출력
    area = context.args[0]
    page = context.args[1]
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"[ {area} ] 검색 결과 [ {page} ] 페이지를 출력합니다.")

    # 현재 대화 중인 채팅방 ID를 찾아 chat_id 변수에 할당
    chat_id = update.effective_chat.id

    # 크롤링 함수 실행 후 결과 값 result 변수에 할당
    result = dc_crawler(area, page)

   # 크롤링한 결과를 받아올 시간 동안 딜레이
    time.sleep(1)

    # 6페이지 이상을 입력하거나 크롤링 결과가 존재하지 않는 경우 안내 문구 출력
    if int(page) > 5 or result == []:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "검색 결과가 존재하지 않습니다.")

   # 서버 요청 과정에 오류가 발생한 경우 안내 문구 출력
    elif result == ["error"]:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "서버 요청 과정에 오류가 발생했습니다.")

    else:
        # search_message 함수를 호출해 response_text 문자열에 할당
        response_text = search_message(page, result)

        # response_text 문자열 문구를 출력
        context.bot.send_message(chat_id = update.effective_chat.id, text = response_text)

    # chat_id_manager() 함수를 호출해 실행
    chat_id_manager(chat_id, result)

# ----------------------------------------------------------------------------------------------------

def info(update, context):
    """
    검색 결과 중에서 입력한 순위의 식당 상세 정보를 메시지로 전송하는 함수입니다.
    """

    # 현재 대화 중인 채팅방 ID를 찾아 chat_id 변수에 할당
    chat_id = update.effective_chat.id

    # chat_id의 검색 결과가 존재하는지 확인하는 result_exist 함수 호출해 결과 값을 result 변수에 할당
    result = result_exist(chat_id)

    # 크롤링 결과가 존재하지 않는 경우 안내 문구 출력
    if not result:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "기존에 검색한 결과가 존재하지 않습니다. 검색부터 실행해 주세요.")

    else:
        # 매개변수로 받아온 값을 ranking 변수에 할당하고 info_message 함수를 호출
        ranking = context.args[0]

        # info_message 함수를 호출해 response_text 문자열에 할당
        response_text = info_message(ranking, result)

        # response_text 문자열 문구를 출력
        context.bot.send_message(chat_id = update.effective_chat.id, text = response_text, parse_mode = "Markdown")

# ----------------------------------------------------------------------------------------------------

def help(update, context):
    """
    텔레그램 명령어의 목록과 사용 방법을 설명하는 함수입니다.
    """

    # help_message 함수를 호출해 response_text 문자열에 할당
    response_text = help_message()
    context.bot.send_message(chat_id = update.effective_chat.id, text = response_text)

# ----------------------------------------------------------------------------------------------------

def feedme(update, context):
    """
    밥봇아, 밥 먹여 줘!
    """

    # 지정된 이미지 출력
    context.bot.send_document(chat_id = update.effective_chat.id, document = open("./Thumbnail/FeedMe.gif", "rb"), caption = "입 벌리세요.")