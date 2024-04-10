from . import trigger_report_bp


@trigger_report_bp.route("/trigger_report")
def trigger_report():
    """
    Trigger report generation.
    """
    return "Trigger Report"
