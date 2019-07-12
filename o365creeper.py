#!/usr/bin/python

# Created by Korey McKinley, Senior Security Consulant at LMG Security
# https://lmgsecurity.com

# July 12, 2019

# This tool will query the Microsoft Office 365 web server to determine
# if an email account is valid or not. It does not need a password and
# should not show up in the logs of a client's O365 tenant.

# Note: Microsoft has implemented some throttling on this service, so
# quick, repeated attempts to validate the same username over and over
# may produce false positives. This tool is best ran after you've gathered
# as many email addresses as possible through OSINT in a list with the
# -f argument.

import requests as req
import argparse
import re
import time

parser = argparse.ArgumentParser(description='Enumerates valid email addresses from Office 365 without submitting login attempts.')
parser.add_argument('-e', '--email', help='Single email address to validate.')
parser.add_argument('-f', '--file', help='List of email addresses to validate, one per line.')
parser.add_argument('-o', '--output', help='Output valid email addresses to the specified file.')
args = parser.parse_args()

url = 'https://login.microsoftonline.com/common/GetCredentialType'

def main():

    if args.file is not None:
        with open(args.file) as file:
            for line in file:
                s = req.session()
                line = line.split()
                email = ' '.join(line)
                body = '{"Username":"%s"}' % email
                request = req.post(url, data=body)
                response = request.text
                valid = re.search('"IfExistsResult":0,', response)
                invalid = re.search('"IfExistsResult":1,', response)
                if invalid:
                    print '%s - INVALID' % email
                if valid and args.output is not None:
                    print '%s - VALID' % email
                    with open(args.output, 'a+') as output_file: 
                        output_file.write(email+'\n')
                else:
                    if valid:
                        print '%s - VALID' % email

    elif args.email is not None:
        email = args.email
        body = '{"Username":"%s"}' % email
        request = req.post(url, data=body)
        response = request.text
        valid = re.search('"IfExistsResult":0', response)
        invalid = re.search('"IfExistsResult":1', response)
        if invalid:
            print '%s - INVALID' % email
        if valid and args.output is not None:
            print '%s - VALID' % email
            with open(args.output, 'w') as output_file:
                output_file.write(email+'\n')
        else:
            if valid:
                print '%s - VALID' % email
if __name__ == "__main__":
    main()
