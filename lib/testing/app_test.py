#!/usr/bin/env python3

import io
import runpy
import sys
from os import path

class TestAppPy:
    '''
    app.py 
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert path.exists("lib/app.py")

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(self):
        '''
        prints 'Hello World! Hello sun! Hello sky!.\n'
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Hello World! Hello sun! Hello sky!."