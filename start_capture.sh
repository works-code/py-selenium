#!/bin/bash
# capture
/Users/hongyoolee/miniconda3/bin/python /Users/hongyoolee/document/study/capture/script/capture.py >> /Users/hongyoolee/document/study/capture/logs/capture.log 2>&1

# chrome browse kill
/Users/hongyoolee/miniconda3/bin/python /Users/hongyoolee/document/study/capture/script/kill_chrome.py >> /Users/hongyoolee/document/study/capture/logs/capture.log 2>&1
