import os
import pytest
from requests import post  # Import post function directly

failed_tests = []
total_tests = 0  # To count the total number of tests executed


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        global total_tests
        total_tests += 1  # Increment total test count for every test
        if result.failed:
            failed_tests.append((item.nodeid, str(call.excinfo.value)))


def send_to_discord(message):
    webhook_url = "https://discord.com/api/webhooks/1249636655506391140/IIEYN3oLd7iUkBirCAuyEmi5RMmev94HJmSLXdJWFSRnK9aj18RA4xqvLuzSmTcb43bK"
    data = {"content": message}
    post(webhook_url, json=data)  # Use post function directly


def pytest_sessionfinish(session, exitstatus):
    global total_tests
    failed_count = len(failed_tests)
    passed_count = total_tests - failed_count

    # Get the test script or directory pattern executed from the command line arguments
    args = session.config.args
    if len(args) == 1 and os.path.isdir(args[0]):
        test_suite_name = args[0]
    else:
        test_suite_name = os.path.dirname(args[0])

    if total_tests == 0:
        message = f"{'=' * 70}\n"
        message += f"**Test Case: `{test_suite_name}` was not executed**\n"
        message += "=" * 70
        message += "CC: <@1077483182942863470> <@771451525331025941>\n"
    else:
        message = f"{'=' * 70}\n"
        message += f"**Test Suite Name: Android - `{test_suite_name}`**\n"
        message += "Test Suites Summary:\n"
        message += f"Total: {total_tests}\n"
        message += f"Passed: {passed_count}\n"
        message += f"Failed: {failed_count}\n"

        if failed_count != 0:
            message += "**List Of Failed Test Cases**\n"

            for test, error_message in failed_tests:
                script_name = test.split("::")[0]  # Extract script name
                test_name = test.split("::")[-1]  # Extract test name
                if len(error_message) > 100:
                    error_message = error_message[:100] + "..."

                # Removing New Line for better readability
                error_message = error_message.replace("\n", " ")

                message += f"- [FAILED] {test_name} in {script_name}\n"
                message += f"  - {error_message}\n"
            message += "CC: <@1077483182942863470> <@771451525331025941>\n"

    send_to_discord(message)
