import datetime
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define a function to generate the assessment report
def generate_security_assessment_report(template_name, template_version, template_description, checks_results, recipient_email=None):
    # Get the current date and time
    assessment_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Create a dictionary to store assessment information
    assessment_report = {
        "AssessmentDate": assessment_date,
        "TemplateName": template_name,
        "TemplateVersion": template_version,
        "TemplateDescription": template_description,
        "SecurityChecks": checks_results,
        "OverallAssessment": "Pass" if all(result["Passed"] for result in checks_results) else "Fail"
    }

    # Convert the assessment report to JSON format
    assessment_report_json = json.dumps(assessment_report, indent=4)

    # Save the report to a local file
    with open("security_assessment_report.json", "w") as report_file:
        report_file.write(assessment_report_json)

    # Send the report via email if recipient email is provided
    if recipient_email:
        send_report_email(assessment_report_json, recipient_email)

# Define a function to send the report via email
def send_report_email(report_json, recipient_email):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "CloudFormation Security Assessment Report"

    # Attach the assessment report as a JSON attachment
    message.attach(MIMEText(report_json, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

if __name__ == "__main__":
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

    # Optionally, provide a recipient email address
    recipient_email = "recipient@example.com"

    # Generate the security assessment report
    generate_security_assessment_report(template_name, template_version, template_description, checks_results, recipient_email)
