#!/bin/bash

python generate_login_tests.py
nosetests --processes=100
rm -rf login_user_*_test.py