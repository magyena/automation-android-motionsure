import os
import pytest
from requests import post

failed_tests = []


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        failed_tests.append((item.nodeid, str(call.excinfo.value)))
        test_name = item.nodeid.split("::")[-1]  # Extract test name
        error_message = str(call.excinfo.value)  # Get the error message


def send_to_discord(message):
    webhook_url = "https://discord.com/api/webhooks/1248465866132029473/5p-uFE-P_Ei7s0HdUPAeg0dHvjHD6BDP8flB8okmLB8jijOqwZz-zI63jC2F82HAoowM"
    data = {"content": message}
    post(webhook_url, json=data)


def pytest_sessionfinish(session, exitstatus):
    total_tests = session.testscollected
    failed_count = len(failed_tests)
    passed_count = total_tests - failed_count

    args = session.config.args
    if len(args) == 1 and os.path.isdir(args[0]):
        test_suite_name = args[0]
    else:
        test_suite_name = os.path.dirname(args[0])

    if total_tests == 0:
        message = f"{'=' * 70}\n"
        message += f"**Test Case: `{test_suite_name}` was not executed**\n"
        message += "=" * 70
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
                if len(error_message) > 50:
                    error_message = error_message[:50] + "..."
                message += f"- [FAILED]{script_name} in {test_name} with error: {error_message}\n"

        # message += "CC: <@1077483182942863470> <@1161584629011197972>\n"

    send_to_discord(message)
