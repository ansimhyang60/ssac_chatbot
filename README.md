# ssac_chatbot
대화형 음악추천 챗봇

- 0330 챗봇 모델링
- 0331 챗봇 모델(seq2seq, transformer 비교) , Django mian.html 변경
- 0404 모델링 완성, ppt 작업, Django mian.html 변경(배경, 폰트, 크기)
- 0405 ppt완성 및 발표준비
- 0406 발표
- ------------------------------------------------------------------------------------------
1. 프로젝트 배경
아침 알람을 좋아하는 연예인의 목소리로 설정할 수 있는
서비스가 있었는데 해당 서비스의 수요층이 있음에 착안, 기분이 별로 좋지 않을 때, 자기가 좋아하는 사람(ex) 연예
인)의 목소리로 위로받을 수 있는 서비스의 수요층 또한
존재할 것이라고 생각하여 착안

2. 목적
사람을 위로하는 문구를 생성하는 챗봇을 제작하고 해당
문구를 TTS(Text to Speech)로 읽어주는 서비스 제작 및

3. AI hub에 웰니스 대화 스크립트, 감성 대화 말뭉치 등
테이터를 kobert, kogpt 등의 사전학습이 되어있는 모델
을 미세조정하여 문장을 입력했을 시 그에 상응하는 자연
스러운 답변을 생성하는 챗봇을 개발

Tacotron 모델 등의 TTS 모델을 활용하여 챗봇에서 생
성된 답변을 음성으로 읽어주는 기능을 개발
웹 페이지에 텔레그램, 카카오톡, 라인 등의 메신저와 같
은 대화형 UI를 구현하여 AWS를 통해 온라인에 배포


1주차(~5월4일) - 프로젝트 기획
2주차(5월 9일 ~ 13일)
- 데이터 전처리, 모델 학습, 챗봇 개발
3, 4주차(5월 16일 ~ 27일)
- 2주차 미비점 및 미완성 부분 보완
- 음성 녹음 및 음성 모델 합성
- 웹 페이지 구현 시작
- ![image](https://github.com/user-attachments/assets/9c99e041-ff90-4d07-b5f7-a309ee2c4349)
- ![image](https://github.com/user-attachments/assets/8ec02147-d48d-4829-aba8-f034f6e49c73)
- ![image](https://github.com/user-attachments/assets/0c79ba29-8b1f-47da-8c1a-a4a0aa7634f6)
- ![image](https://github.com/user-attachments/assets/c4b8b050-313a-45ef-8b28-eeea82e7a71e)


5주차(5월 30일 ~ 6월 2일)
- PPT 발표 준비 및 시연 준비
- 웹 페이지 구현 마무리

AWS for service 49.43 USD/month
- cpu 4cores, 8 GB ram storage

- 완성본
  ![image](https://github.com/user-attachments/assets/293bc820-a229-4359-8c7b-8e75732c37ed)
