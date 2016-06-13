'''
    File name: api.py
    Author: Jiwei Zhang(Lucas)
    Email: jiweiz@cmu.edu
    Date created: 12/06/2016
    Python Version: 3.5
    Description: This is a simple python script to manage docker containers
    Reference: https://docker-py.readthedocs.io/en/stable/
'''

from docker import Client
import datetime
import sys

#refers to the protocol+hostname+port where the Docker server is hosted.
url='unix://var/run/docker.sock'
#the path to save the logs
path = '/home/ubuntu/'
#log file name
logname = 'logfile'
# indicate the logs will include stdout
stdout = True
# indicate the logs will include stderr
stderr = True
# indicate the logs will be streamed
stream = True
# show timestamp in the logs
timestamps = True
# out put all lines in the log
tail = "all"
# include the logs which start from
log_start_time = datetime.datetime.now() - datetime.timedelta(days=1*365)
# follow log output
follow = True


def create(imagename):
	"""Create a container from a image.
    Args:
        imagename: the image name.
    """
	try:
		cli = Client(base_url=url)
		cli.containers()
		container = cli.create_container(image=imagename, command='/bin/sleep 30')
		print(container["Id"][:11] + " has been created.")
	except Exception,e: print str(e)

def start(container_id):
	"""start a container.
    Args:
        container_id: the id of the cointainer to start.
    """
	try:
		cli = Client(base_url=url)
		response = cli.start(container_id)
		print(container_id + " has been started.")
	except Exception,e: print str(e)

def stop(container_id):
	"""Stop a container.
    Args:
        container_id: the id of the cointainer to stop.
    """
	try:
		cli = Client(base_url=url)
		response = cli.start(container_id)
		print(container_id + " has been stopped.")
	except Exception,e: print str(e)


def restart(container_id):
	"""Restart a container.
    Args:
        container_id: the id of the container to restart
    """
	try:
		cli = Client(base_url=url)
		response = cli.restart(container_id)
		print(container_id + " has been restarted.")
	except Exception,e: print str(e)

def containers():
	"""Get info of all containers.
    """
	try:
		cli = Client(base_url=url)
		response = cli.containers(True)
		print(response)
	except Exception,e: print str(e)

def logs(container_id):
	"""Save logs in the logfile and print all the current logs of the container.
    Args:
        container_id: the id of the container to get logs from
    """
	try:
		cli = Client(base_url=url)
		response = cli.logs(container_id, stdout, stderr, stream, timestamps, tail, log_start_time,follow)
		print(response)
		logfile = open(path + logname,'a+')
		logfile.write(str(response))
		logfile.close()
	except Exception,e: print str(e)

def printlogs(container_id):
	"""Print the log of a container.
    Args:
        container_id: the id of the container to get logs from.
    """
	try:
		logfile = open(path + logname,'r')
		for line in logfile:
			print line
	except Exception,e: print str(e)

def rm(container_id):
	"""Remove a container. It will remove the volumes associated with the container
		link (bool) and force the removal of a running container
    Args:
        container_id: the id of the container to remove
    """
	try:
		cli = Client(base_url=url)
		cli.remove_container(container_id, True, False, True)
		print(container_id + " has been removed.")
	except Exception,e: print str(e)

def cleanup():
	"""Remove all the running and non-running containers.
    """
	try: 
		cli = Client(base_url=url)
		items = cli.containers(True)
		for i in items:
			rm(i['Id'])
		print "cleanup has finished."
	except Exception,e: print str(e)

#Function chooser
func_arg = {"create": create, "start": start, "stop": stop, "restart": restart, "containers": containers, 
			"logs": logs, "printlogs": printlogs, "rm": rm, "cleanup": cleanup}


if __name__ == "__main__":

	if len(sys.argv) > 3 or len(sys.argv) < 2:
		print "The command format should be: docker_api.py + COMMMANDS + parameter(optional)"
	if (len(sys.argv) == 3):
		func_arg[sys.argv[1]](sys.argv[2])
	elif (len(sys.argv) == 2):
		func_arg[sys.argv[1]]()



	








