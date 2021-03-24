# cooltone-warmtone
사람 얼굴 이미지를 보고 피부의 쿨톤과 웜톤의 정도를 퍼센테이지로 알려주는 AI입니다. Google teachable machine을 사용하여 구현하였습니다.

### Google teachable machine
- https://teachablemachine.withgoogle.com/

### Crawling
google_images_download 모둘을 사용해 학습에 필요한 이미지를 수집하였습니다.  
- 모듈 관련 공식 문서 : https://google-images-download.readthedocs.io/en/latest/index.html
- 설치 및 사용방법 : https://otugi.tistory.com/137

### 학습 데이터
쿨톤과 웜톤으로 대표되는 연예인들의 사진을 학습 데이터로 사용하였습니다.
- 쿨톤 : 이영애, 태연, 손예진, 홍빈, 차은우
- 웜톤 : 최강창민, 박보검, 이효리, 박보영, 박신혜
