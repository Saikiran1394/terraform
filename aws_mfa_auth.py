#!/usr/bin/env python3

import argparse
import configparser
import boto3
from pathlib import Path


# defualt global values
MFA_DEVICE_SERIAL_ARN   = "arn:aws:iam::752150096662:mfa/scheruku@diwo.ai"

# default 36 hours
SESSION_DURATION        = 129600

# default aws credentials file
AWS_CREDS_FILE          = Path(Path.home() / ".aws/credentials")

# profile name
PROFILE_NAME            = "mfa"


def command_args():

    # arguments parser
    parser = argparse.ArgumentParser(description="AWS MFA Authentication tool")

    # read the token number
    parser.add_argument("TOKEN_CODE", help="MFA token number", nargs='?')

    # read session duration
    parser.add_argument("--duration", help="Session duration", nargs='?', type=int)

    # read credential file
    parser.add_argument("--credential-file", help="AWS credential file", nargs='?')

    # read credential file
    parser.add_argument("--mfa-device-arn", help="MFA device serial number or ARN", nargs='?')

    return parser.parse_args()


def update_credential_file(output, file):

    config = configparser.ConfigParser()
    config.read(file)

    if "mfa" not in config.sections():
        config.add_section(PROFILE_NAME)

    # update credentials file with mfa profile
    config["mfa"]["aws_access_key_id"] = output["Credentials"]["AccessKeyId"]
    config["mfa"]["aws_secret_access_key"] = output["Credentials"]["SecretAccessKey"]
    config["mfa"]["aws_session_token"] = output["Credentials"]["SessionToken"]

    with open(file, 'w') as configfile:
        config.write(configfile)


def main():

    global MFA_DEVICE_SERIAL_ARN, SESSION_DURATION, AWS_CREDS_FILE

    # read token number if none
    if not command_args().TOKEN_CODE:
        TOKEN_CODE = input("Enter MFA Token Code: ")


    # update MFA_ARN
    if command_args().mfa_device_arn:
        MFA_DEVICE_SERIAL_ARN = command_args().mfa_device_arn

    # update SESSION_DURATION
    if command_args().duration:
        SESSION_DURATION = command_args().duration

    # update AWS_CREDS_FILE
    if command_args().credential_file:
        AWS_CREDS_FILE = command_args().credential_file

    client = boto3.client('sts')
    tempCredentials = client.get_session_token(
        DurationSeconds=SESSION_DURATION,
        SerialNumber=MFA_DEVICE_SERIAL_ARN,
        TokenCode=TOKEN_CODE
    )


    update_credential_file(tempCredentials, AWS_CREDS_FILE)


if __name__ == '__main__':
    main()