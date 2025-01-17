from jenkins_helper.jenkins_functions import *
import sys
import re
import os


DOMAIN_REGEX = "^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)"

jenkins_url = os.environ["INPUT_JENKINS_URL"]
jenkins_user = os.environ["INPUT_JENKINS_USER"]
jenkins_token = os.environ["INPUT_JENKINS_TOKEN"]
job_name = os.environ["INPUT_JOB_NAME"]
jenkins_params = os.environ.get("INPUT_JENKINS_PARAMS")
console_log_regex = os.environ.get("INPUT_CONSOLE_LOG_REGEX")
console_log_regex_group = int(os.environ.get("INPUT_CONSOLE_LOG_REGEX_GROUP"))
job_timeout = int(int(os.environ["INPUT_JOB_TIMEOUT"])/INTERVAL_SECONDS) if os.environ.get("INPUT_JOB_TIMEOUT") else 30
jenkins_use_post_request = os.environ.get("INPUT_JENKINS_USE_POST_REQUEST") if os.environ.get("INPUT_JENKINS_USE_POST_REQUEST") else False
do_not_wait = os.environ.get("INPUT_DO_NOT_WAIT") if os.environ.get("INPUT_DO_NOT_WAIT") else False


def main():
    crumb = get_crumb(jenkins_url, jenkins_user, jenkins_token)
    queue_item_location = queue_job(crumb, jenkins_url, job_name, jenkins_params, jenkins_user, jenkins_token, jenkins_use_post_request)
    if do_not_wait is None:
        job_run_url = get_job_run_url(queue_item_location, jenkins_user, jenkins_token, job_timeout)
        print(f"Job run URL: {job_run_url}")
        job_run_url_api_domain = re.sub(DOMAIN_REGEX, jenkins_url, job_run_url)
        job_progress(job_run_url_api_domain, jenkins_user, jenkins_token, job_timeout, console_log_regex, console_log_regex_group)
    sys.exit(0)


if __name__ == "__main__":
    main()
