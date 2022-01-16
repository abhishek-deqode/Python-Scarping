import requests
import re

def readFromURL(logs_url):
    # get the request from the url
    res = requests.get(logs_url)

    # return as a text
    return res.text


def writeIntoFile(logs_data, log_file_name):
    # open a file for writting & create it
    f = open(log_file_name, "w+")

    # write some lines of data to the file
    f.write(logs_data)

    # close the file when done
    f.close()

def uniqueIPs(log_file_name):
    # decleaing the regex patter for IP addresses
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    # initializing the list object
    unique_IPs = []

    # open and read lines from file
    with open(log_file_name) as current_file:
        lines = current_file.readlines()
        if not lines:
            print('File is empty!')
        else:
            for line in lines:
                unique_IPs.append(pattern.search(line)[0])

    # remove the duplicate the IPs
    unique_IPs = set(unique_IPs)

    # return the total number of unique IPs
    total_unque_IPs = len(unique_IPs)

    # return
    print('Total Unique IPs:', total_unque_IPs)
    return total_unque_IPs

def getMaxPostReq(log_file_name):
    # decleaing the regex patter for POST
    post = 'POST'

    # initialize the list object
    post_req = []

    # open and read lines from file
    with open(log_file_name) as current_file:
        lines = current_file.readlines()
        if not lines:
            print('File is empty!')
        else:
            for line in lines:
                if post in line:
                    post_req.append(line)
    

    # return 
    print('Total Post Request:', len(post_req))
    return len(post_req)


if __name__ == '__main__':
    logs_url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/apache_logs/apache_logs'
    log_file_name = 'logs.txt'
    
    # retrieve data from url
    logs_data = readFromURL(logs_url)

    # write into a file
    writeIntoFile(logs_data, log_file_name)

    # search maximum post requests
    uniqueIPs(log_file_name)

    # find the max post req
    getMaxPostReq(log_file_name)