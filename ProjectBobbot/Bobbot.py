# 필요한 라이브러리 및 클래스 불러오기(Import)
from telegram.ext import Updater, CommandHandler
from CommandDefiner import *

# 해당 파일을 메인으로만 실행
if __name__ == "__main__":

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

    # config 파일에서 읽어온 값을 변수에 할당
    token = telegram_config["token"]

    # token 변수로 봇을 생성하고 신규 메시지를 감시하는 Updater 객체를 생성
    updater = Updater(token = token, use_context = True)

    # Updater 객체가 큐에 담은 신규 메시지를 꺼내오는 Dispatcher 객체를 생성
    dispatcher = updater.dispatcher

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