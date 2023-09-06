# generate_assessment_report.py
import datetime
import json

def generate_security_assessment_report(template_name, template_version, template_description, checks_results):
    assessment_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    assessment_report = {
        "AssessmentDate": assessment_date,
        "TemplateName": template_name,
        "TemplateVersion": template_version,
        "TemplateDescription": template_description,
        "SecurityChecks": checks_results,
        "OverallAssessment": "Pass" if all(result["Passed"] for result in checks_results) else "Fail"
    }
    assessment_report_json = json.dumps(assessment_report, indent=4)
    return assessment_report_json
