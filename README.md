<p><img src = "./Thumbnail/Logo.png" width = "500"></p>
<p>&nbsp;</p>
<p style="font-family: 을유1945; font-size: 25px;">1. 프로젝트 개요</p>
<p  style="font-family: 을유1945; font-size: 17px;">&nbsp;&nbsp;&nbsp;&nbsp;사용자로부터 지역과 페이지 수를 입력받으면, 빅데이터 맛집 검색 서비스를 제공하는 '<a href = "https://www.diningcode.com/">다이닝코드</a>(DiningCode)' 홈페이지에서 검색한 결과를 크롤링(Crawling)을 통해 가져와 보여주는 '텔레그램(Telegram)' 봇(Bot)입니다.</p>
<p  style="font-family: 을유1945; font-size: 17px;">&nbsp;&nbsp;&nbsp;&nbsp;현재 텔레그램에서 <span style="color: #FFD700">@BobAutoBot</span>을 검색해 대화를 시작하면, 밥보-ㅅ을 체험해 볼 수 있습니다.</p>

---

<p style="font-family: 을유1945; font-size: 25px;">2. 의존성(Dependency) 정보</p>

![Python](https://img.shields.io/badge/Python-3.9.13-brightgreen)
![Telegram Android](https://img.shields.io/badge/Telegram_Android-Install-green)

---

<p style="font-family: 을유1945; font-size: 25px;">3. 설치 및 실행 방법</p>
<p  style="font-family: 을유1945; font-size: 17px;">① 전체 패키지를 다운로드 받습니다.</p>

```bash
git clone https://github.com/sesac-finance/Crassula_Package.git
```

<p  style="font-family: 을유1945; font-size: 17px;">② Crassula_Package 폴더로 이동합니다.</p>

```bash
cd Crassula_Package
```

<p  style="font-family: 을유1945; font-size: 17px;">③ requirements.txt를 이용해 필요한 라이브러리를 설치합니다.</p>


```bash
pip install -r requirements.txt
```

<p  style="font-family: 을유1945; font-size: 17px;">④ ProjectBobbot 폴더로 이동합니다.</p>


```bash
cd ProjectBobbot
```

<p  style="font-family: 을유1945; font-size: 17px;">⑤ telegram_config 파일을 만들고 첫째 줄에 "token = [텔레그램에서 발급 받은 봇 토큰]"을 입력 후 저장합니다.</p>
<p  style="font-family: 을유1945; font-size: 17px;">⑥ Bobbot.py 파일을 실행합니다.</p>


```bash
python Bobbot.py
```

---

<p style="font-family: 을유1945; font-size: 25px;">4. 패키지 구조</p>
<p><img src = "./Thumbnail/FileTree.png" width = "800"></p>