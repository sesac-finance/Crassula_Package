# 필요한 라이브러리 및 클래스 불러오기(Import)
from telegram.ext import Updater
from telegram.ext import CommandHandler
from DiningCodeCrawler import *
from TextMessage import *
from ChatManager import *
import time

# config 파일의 내용을 담을 딕셔너리 초기화
telegram_config = {}

# config 파일 읽어와 configs 변수에 할당
with open("./telegram_config", "r") as f:
    configs = f.readlines()

    # 1. for 반복문을 통해 한 줄씩 확인하며 줄바꿈 기호 제거, " = "으로 문자열을 분리
    # 2. 이후 키(Key), 값(Value)으로 언패킹한 다음 딕셔너리에 키와 값을 추가
    for config in configs:
        key, value = config.rstrip().split(" = ")
        telegram_config[key] = value

# config 파일에서 읽어온 값을 각 변수에 할당
token = telegram_config["token"]
my_chat_id = telegram_config["chat_id"]
group_id = telegram_config["group_id"]

# token 변수로 봇을 생성하고 신규 메시지를 감시하는 Updater 객체를 생성
updater = Updater(token = token, use_context = True)

# Updater 객체가 큐에 담은 신규 메시지를 꺼내오는 Dispatcher 객체를 생성
dispatcher = updater.dispatcher

# 크롤링한 결과를 담을 result 리스트 초기화
result =[]

# ----------------------------------------------------------------------------------------------------

def start(update, context):
    """
    봇 최초 실행 시 텔레그램 명령어의 목록과 사용 방법을 설명하고, 채팅방 ID를 저장하는 함수입니다.
    """

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
    context.bot.send_document(chat_id = update.effective_chat.id, document = open("./FeedMe.gif", "rb"), caption = "입 벌리세요.")

# ----------------------------------------------------------------------------------------------------

# 각 이벤트에 대한 CommandHandler 객체 생성
start_handler = CommandHandler("start", start)
search_handler = CommandHandler("search", search)
info_handler = CommandHandler("info", info)
help_handler = CommandHandler("help", help)
feedme_handler = CommandHandler("feedme", feedme)

# 각 CommandHandler 객체를 Dispatcher 객체에 추가
dispatcher.add_handler(start_handler)
dispatcher.add_handler(search_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(feedme_handler)

# Updater 객체가 메시지를 계속 감시
updater.start_polling()

# 새로운 메시지가 수신될 때까지 차단하고 업데이트를 중지
updater.idle()