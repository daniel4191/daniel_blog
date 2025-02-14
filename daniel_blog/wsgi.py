# wsgi.py

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

# 가상환경 경로 설정 (로컬 환경에서 설정하는 부분)
# activate_this = "/path/to/your/virtualenv/bin/activate_this.py"
# with open(activate_this) as file_:
#     exec(file_.read(), dict(__file__=activate_this))

# 프로젝트 경로 설정 (로컬 환경에서 설정하는 부분)
# project_root = "/path/to/your/project"
# if project_root not in sys.path:
#     sys.path.append(project_root)

# Django 설정 모듈 설정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings.production")

# WSGI 애플리케이션 반환
application = StaticFilesHandler(get_wsgi_application())
