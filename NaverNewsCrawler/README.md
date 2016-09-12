### 네이버뉴스크롤러
####Guideline
* 실제로 많은 사람들에게 영향을 미칠 production 제품이기 때문에 제품이 **정상적으로 작동 되는지**가 중요합니다.
* 추후 다른 사람들과 협업하게 될 production 제품 이라고 가정하고 문서화, testing을 진행(가능할 시)해주세요.
* 프로젝트에 대한 전체 설명을 담은 문서파일을 작성(가능할 시)해주세요.
   * 예: 사용한 프레임워크 및 라이브러리, 설계, 향후 개선사항 
* 프로젝트의 기능을 개선하기 위한 새로운 제안사항이 있으면 이를 적용하셔도 무방합니다.

####기능요구사항
네이버 뉴스를 1시간마다 확인 하여 새로운 뉴스가 확인 될 경우 메세지플랫폼(**Jandi,Slack**)에 알림을 보내는 크롤러를 제작하려 합니다.
* 수집
    * [여기](http://news.naver.com/main/history/mainnews/index.nhn?date=2016-08-30&time=02:00)에서 뉴스 수집을 진행합니다.
    * 수집되는 시간은 매 한시간마다 작동됩니다.
    * 처음 작동을 시작하였을때 뉴스의 정보들을 가지고 있다가 1시간 뒤에 확인을 하고 달라진 부분을 확인할 수 있어야 합니다.
    * 변경을 확인해야하는 부분은 뉴스의 기사 제목들을 기준으로 합니다.
* 전송
    * 메세지 전송은 Jandi, Slack 중에서 *선택*하여 진행합니다.
    * Slack 의 메세지 전송은 [https://api.slack.com/](https://api.slack.com/) 공식 사이트를, Jandi 의 메세지 전송은 [http://goo.gl/a0geJ1](http://goo.gl/a0geJ1) 공식 사이트를 참조하시기 바랍니다.

####알림 화면 예시
\* Jandi
>naver_news

>폐쇄 7개월 개성공단 가보니…원자재 그대로 >http://news.naver.com/main/read.nhn?oid=055&sid1=100&aid=0000451166&mid=shm&mode=LSD&nh=20160908223409

>'위생 불량' 중국집, 바퀴벌레에 유통기한도 '훌쩍' >http://news.naver.com/main/read.nhn?oid=214&sid1=102&aid=0000669009&mid=shm&mode=LSD&nh=20160908204619 
> ...

### Manual
#### 실습 환경
* Python 3.5.2
* Beautiful Soup 4.5.1
* Windows 10 (Intel PC)

#### 실행 방법
> python NaverNewsCrawler.py

