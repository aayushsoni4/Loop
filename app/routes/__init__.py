from flask import Blueprint

get_report_bp = Blueprint("get_report", __name__)
trigger_report_bp = Blueprint("trigger_report", __name__)

from . import get_report, trigger_report
