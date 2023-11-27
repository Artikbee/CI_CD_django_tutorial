#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    import coverage

    cov = coverage.Coverage()
    cov.start()
    failures = test_runner.run_tests(["product"])
    cov.stop()
    # result = cov.report(include="*/views.py")
    # print('result is', result)
    sys.exit(bool(failures))
