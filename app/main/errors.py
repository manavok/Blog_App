from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    pass
    # return render_templates('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    pass