# py-selenium
python-selenium

# environment
- mac Catalina 10.15.6
- Python 3.7.6
- chrome 90.0.4430

# batch register
crontab -e
// 분(0-59) 시간(0-23) 일(1-31) 월(1-12) 주(일요일=0-6)
10 00 * * * /{dir}/start_capture.sh
