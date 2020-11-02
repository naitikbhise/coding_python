# Execute this file using python to simulate what our own test script will do
# Example: `python tester.py`
# This script should then output some data indicating if your solution functioned as expected.
# Keep in mind that our script will test more test cases than just this example.
# This script will also warn you if your python version is lower than the python versions we may test with (3.6+).

import json
import sys

if sys.version_info[0] < 3:
    print('warning, your python version may not adequately represent the environment that your code will be tested in')
elif sys.version_info[0] == 3 and sys.version_info[1] < 6:
    print('warning, your python version may not adequately represent the environment that your code will be tested in')

def output_print(hosts_dict):
    print(json.dumps(hosts_dict, sort_keys=True, indent=4))

if __name__=='__main__':


    from coding_assignment import convert_mapping

    #example input
    ips_to_hosts={
        '142.250.72.238': 'google.com',
        '1.0.0.1': 'one.one.one.one',
        '13.91.40.166': 'logmein.com'}
    known_hosts={
        'one.one.one.one': ['1.1.1.1', '1.0.0.1'],
        'logmein.com': ['52.178.114.226', '40.71.199.117','142.250.72.238']}
    #known_hosts = None
    #example call
    convert_mapping(ips_to_hosts, known_hosts)
    #example output
    expected_known_hosts={
        'one.one.one.one': ['1.1.1.1', '1.0.0.1'],
        'logmein.com': ['52.178.114.226', '40.71.199.117', '13.91.40.166'],
        'google.com': ['142.250.72.238']}
    print('output is:')
    output_print(known_hosts)
    print('expected output is:')
    output_print(expected_known_hosts)
    if known_hosts == expected_known_hosts:
        print('Congratulations, your code worked in this test case!\nFeel free to add more cases to this file that you would like to test your code against.')
    else:
        print('Unfortunately, your result did not match the expected result.')