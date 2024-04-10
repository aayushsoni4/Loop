from . import get_report_bp


@get_report_bp.route("/get_report")
def get_report():
    """
    Get report status or CSV file.
    """
    return "Get report"
