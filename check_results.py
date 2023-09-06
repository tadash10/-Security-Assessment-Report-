# check_results.py
def validate_security_check_results(checks_results):
    return all(result.get("Passed", False) for result in checks_results)
