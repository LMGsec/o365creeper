## Description
    This is a simple Python script used to validate email accounts that belong to Office 365 tenants. 
    This script takes either a single email address or a list of email addresses as input, 
    sends a request to Office 365 without a password, and looksfor the the "IfExistsResult"
    parameter to be set to 0 for a valid account. Invalid accounts will return a 1.

## Usage
    This script depends on the Python "Requests" library. The script can take a single email address
    with the -e parameter or a list of email addresses, one per line, with the -f parameter. 
    Additionally, the script can output valid email addressesto a file with the -o parameter.
    
    Examples:
    o365creeper.py -e test@example.com
    o365creeper.py -f emails.txt
    o365creeper.py -f emails.txt -o validemails.txt

## NOTE
    Office 365 will flag these requests randomly after repeated, successive attempts to validate the 
    same email address which may generate false positives such as invalid email addresses showing as 
    valid. This is denoted by the "ThrottleStatus" parameter being set to 1 in the server's response. 
    This tool is best used with a list of unique email addresses.
    
    This tool is offered with no warranty and is to be used at your own risk and discretion.
