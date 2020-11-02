# Implement a function that converts a mapping of IPs to hostnames into a mapping of hostnames to IPs.
# You may assume all IPs are singular IPv4 IPs, not IP ranges.
# You may assume that the IPs and Hostnames are all strings.
# Results should be output as a python dictionary with string keys and list values.
# If an input dictionary of hostnames to IPs is provided to an optional named variable "existing_hosts", then the results should be merged with the dictionary.
# If there is a conflict (existing host name), the new list should be concatenated to the end of the existing list, excluding any repeated IPs.
# Include a proper docstring

# Also include a list of test cases for your function in separate file "test_cases.txt". The test cases should cover any edge cases you identity. You need not code the test cases.

# Your code should be able to be imported. We will import your python module and test the convert_mapping function against tests of our own.
# Make sure your code doesn't have syntax errors.
# We will be using python 3.6+

# Expected solution time limit: 1hrs. Please try to turn your solution in before then.
# Keep in mind that there is no singular correct solution.
# This assignment is designed is to gauge your skills and give us an idea of how you approach tasks relevant to the Software Developer role.  
# We encourage you to move forward with your assumptions and add the necessary context for us as comments to let us understand those assumptions.
# If your solution is not functional due to syntax errors, please take some time to fix those before submitting.
# We will not consider answers that python 3.6+ will not load.

# To aid you in testing, we have provided another file, tester.py
# Execute that file using python to simulate what our own test script will do
# Example: `python tester.py`
# That script should then output some data indicating if your solution functioned as expected.
# Keep in mind that our script will test more test cases than just the example provided in that file
# That script will also warn you if your python version is lower than the python versions we may test with (3.6+).

# This is your chance to impress us. Send your best code forward. All the best!

#Template
def convert_mapping(ips_to_hosts, existing_hosts=None): #NOTE: "existing_hosts" should be modified to be an optional variable
    """
    Write a docstring for your function here
    """
    if existing_hosts==None:
        existing_hosts={}
        if len(ips_to_hosts)==0:
            return None
        keyer = list(ips_to_hosts.keys())
        existing_hosts[ips_to_hosts[keyer[0]]] = [keyer[0]]
    if len(ips_to_hosts) == 0:
        return existing_hosts
    for ip in ips_to_hosts.keys():
        ip_list = []
        for i in (existing_hosts.values()):
            ip_list += i
        if ip not in ip_list:
            if ips_to_hosts[ip] in existing_hosts.keys():
                existing_hosts[ips_to_hosts[ip]].append(ip)
            else:
                existing_hosts[ips_to_hosts[ip]] = [ip]
        else:
            lister = list(existing_hosts.keys())
            i = 0
            while i<len(lister):
                host_name = lister[i]
                if ip in existing_hosts[host_name]:
                    print(ip,host_name)
                    if host_name!=ips_to_hosts[ip]:
                        existing_hosts[host_name].remove(ip)
                        if ips_to_hosts[ip] in existing_hosts.keys():
                            existing_hosts[ips_to_hosts[ip]].append(ip)
                        else:
                            existing_hosts[ips_to_hosts[ip]] = [ip]
                        break
                i += 1
    #implement your solution here
    print(existing_hosts)
    return existing_hosts

#For example inputs and outputs check accompanying tester.py