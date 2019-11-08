# dev_onsight(for AlmondChocorate Project in RockPlace)

본 레포지터리들은 Google GKE 상에서 구축하였던 rockcube 라는 빌링시스템의 자동화 모니터링을 구축하기 위한 파이선 코드들로서 
기본 구성은 Restfult API로 GET 방식으로 호출 후 status code 가 200일 경우에는 별도의 알람을 발생시키지 않으며 
200이 아닌경우에는 슬랙으로 알람을 발송해주는 내용을 코딩 후 Jenkins에 적용하여 새로운 소스코드 수정이 발생 후 배포시마다 
체크하여 어플리케이션의 상태를 모니터링하는 코드들로 구성되어 있습니다.


1. https://github.com/dhdiagram4011/dev_onsight/blob/master/pod-status-check-cpprod.py<br>
운영 GKE kubernetes pod의 상태를 체크하기 위한 코드



2. https://github.com/dhdiagram4011/dev_onsight/blob/master/pod-status-check.py<br>
kubernets 의 evited pod를 체크하기 위한 코드
evicted pod가 발생하면 슬랙 팀 체널로 알람을 보내주는 코드



3. https://github.com/dhdiagram4011/dev_onsight/blob/master/rockcube-app-error-logger.py<br>
구글의 pub/sub 서비스를 이용하여 어플리케이션의 로그를 게더링 하기 위한 파이선 코드
수집된 에러 로그들을 슬랙의 팀 채널로 보내주는 코드



4. https://github.com/dhdiagram4011/dev_onsight/blob/master/rockcube_GET.py<br>
고객사별 프로젝트 리스트를 API를 이용하여 업데이트하는 파이선 코드로서 프로젝트리스트에 대한 업데이트 결과를 알려주고 결과내용을 이메일로 자동
발송하도록 해주는 파이선 코드


5.https://github.com/dhdiagram4011/dev_onsight/blob/master/view/login_check.py<br>
rockcube는 고객사별로 아이디를 제공하여 고객사가 아이디/패스워드로 로그인 하여 서비르를 이용하는 개념의 어플리케이션으로서
수정배포시마다 로그인이 정상적으로 되는지의 여부를 체크하기 위하여 만든 파이선 코드로서 체크 결과를 슬랙으로 발송합니다.
로그인이 되지 않을 시에는 롤백을 하도록 코드를 구성하였지만 실질적으로 롤백은 수행하지 않았습니다.

