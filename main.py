# main.py
from generate_assessment_report import generate_security_assessment_report
from send_email import send_report_email
from file_operations import save_report_to_file, read_recipient_email
from check_results import validate_security_check_results
import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def main():
    # Replace these with actual values obtained from your existing script
    template_name = "MyCloudFormationTemplate"
    template_version = "1.0"
    template_description = "This is a sample CloudFormation template."
    checks_results = [
        {
            "CheckName": "Check1",
            "Passed": True,
            "Details": "Passed without issues."
        },
        {
            "CheckName": "Check2",
            "Passed": False,
            "Details": "Failed due to misconfiguration in resource X."
        }
        # Add more check results as needed
    ]

    recipient_email = read_recipient_email()
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    if validate_security_check_results(checks_results):
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

        save_report_to_file(assessment_report_json)
        
        if recipient_email:
            send_report_email(assessment_report_json, sender_email, sender_password, recipient_email)
        
        print("Security assessment completed.")
    else:
        print("Security assessment failed. Please review the results.")

if __name__ == "__main__":
    main()
