import csv
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


# read the file "device_file" and create a dictionary
def get_device_details():
    with open("devices_details") as f:
        content = csv.reader(f)
        dict_from_csv = {rows[0]: rows[1:6] for rows in content}
    return dict_from_csv


# get the switch details and connect to it
def connect_to_sw(switch_details):
    try:
        if switch_details['secret'] != 'none':  # if the device has enable-password, insert the value of the secret key
            ssh_handler = ConnectHandler(**switch_details)
            ssh_handler.enable()
            return ssh_handler
        else:
            ssh_handler = ConnectHandler(**switch_details)
            return ssh_handler
    except AuthenticationException:
        print('Authentication failure: ' + switch_details["ip"])
    except NetMikoTimeoutException:
        print('Timeout to device: ' + switch_details["ip"])
    except EOFError:
        print('End of file while attempting device ' + switch_details["ip"])
    except SSHException:
        print('SSH Issue. Are you sure SSH is enabled? ' + switch_details["ip"])
    except BaseException as unknown_error:
        print('Some other error: ' + str(unknown_error))
    return None


# depending on the vendor, issue the relevant command to show the device configuration
def get_configuration(ssh_handler, switch_details):
    vendor = switch_details['device_type']
    vendor_list = ['cisco_ios', 'cisco_ios_telnet', 'dell_os6', 'dell_dnos6', 'arista_eos']
    if vendor in vendor_list:
        switch_config = ssh_handler.send_command("show run")
    elif vendor == "checkpoint_gaia":
        switch_config = ssh_handler.send_command("clish -c \"show configuration\"")
    else:
        switch_config = ssh_handler.send_command("display current-configuration", read_timeout=30)
    return switch_config


# save to device configuration to a file named after the device IP address
def save_to_file(switch_configuration, switch_details):
    path = "/lib/jenkins/Switch_BackUp/"
    try:
        with open(f"{path}{switch_details['ip']}.bak", "w") as back_up_file:
            back_up_file.write(switch_configuration)
    except FileNotFoundError as e:
        print(f"file not found {e.args}")
    except PermissionError as e:
        print(e.args)


# call all functions and loop through the different devices to connect all of them
def main():
    switch_dict = get_device_details()
    for key, value in switch_dict.items():  # insert the values of each key in the dictionary to a new dictionary
        switch_details = {
            'device_type': value[1],
            'ip': value[0],
            'username': value[2],
            'password': value[3],
            'secret': value[4]
        }
        print(f"connecting to switch {value[0]}...")
        ssh_handler = connect_to_sw(switch_details)
        if ssh_handler is None:
            continue
        switch_configuration = get_configuration(ssh_handler, switch_details)
        print(f"saving configuration to switch {value[0]}...")
        save_to_file(switch_configuration, switch_details)
    print("done")


main()
