# jenkins-job-action

This action can be used to trigger Jenkins job and follow up on build results, bringing back the log in case it fails. Can be used to introduce any sort of check validation before allowing merges, for example.

[Read more actions here, in the official Github documentation.](https://help.github.com/en/actions/automating-your-workflow-with-github-actions)

## Inputs

### `jenkins_url`

Description: Jenkins domain URL.

### `jenkins_user`

Description: Jenkins username that will be impersonated to run the jobs.

### `jenkins_token`

Description: Jenkins token generated by user.

### `job_name`

Description: Jenkins job that will be triggered and followed up.

### `jenkins_params` (**not required**)

Description: Jenkins build parameters to use in job.


### `console_log_regex` (**not required**)

Description: Base64 encoded jenkins console log regex to filter out unecessary output text. This regex search runs using re.DOTALL.

### `console_log_regex_group` (**not required**)

Description: Jenkins console log regex group number to collect specific match from regex grouping.

### `job_timeout` (**not required**)

Description: Jenkins timeout period for called functions. Default to 150 seconds.


## Example usage

Create a `.yml` file inside yout project in the path `.github/workflows/example.yml`. 

```yml
name: Run Jenkins Job with Build Result
on: [push] # Can be any Github event
jobs:
  build:
    name: Display name on Github
    runs-on: ubuntu-latest
    steps:
    - name: Display step name on Github
      uses: Gympass/jenkins-job-action@0.0.5
      with:
        jenkins_url: "{JENKINS_URL}"
        jenkins_user: "{JENKINS_USER}"
        jenkins_token: "${{ secrets.jenkins_token }}" # Consider declaring this as a Github secret, for security purposes.
        job_name: "{JOB_NAME}"
        jenkins_params: '{"any_build_param_or_none": "value", "branch": "${GITHUB_SHA}"}' # Optional.
        console_log_regex: "KGVuY29kZWQpIChyZWdleCBydWxlKSAod2l0aCAzIHNlYXJjaCBncm91cHMp" # Optional. This is base64 encoded.
        console_log_regex_group: "2" # Optional.
        job_timeout: "150" # Optional.
```
