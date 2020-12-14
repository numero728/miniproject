수신 양호

# 연동 확인 김채정

# 미니프로젝트 관련 환경
- 배포 후 클라이언트측 화면 확인 위해 임시적으로 강사님이 제공한 fabfile.py 사용
- 가상머신 이름: miniproject
- key pair 이름: miniproject_key
- DNS 이름: Configure
- IP: 40.76.38.92



# 서버 최초 배포 후 apache2 default page 설정
# ssh 접속 후
1) /etc/apache2/sites_available 디렉토리로 이동
2) sudo a2dissite 000-default.conf
3) sudo systemctl reload apache2

