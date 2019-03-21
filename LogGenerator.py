import logging
import os, tempfile, sys
import time


def generate_log_file():	

	old_work_dir = os.getcwd()
	tmp_file_path = old_work_dir + '/tmp'

	# tmp_file_path = '/tmp'

	if os.path.exists(tmp_file_path):
	    #os.remove(tmp_file_path)
	    print("Found path %s" % tmp_file_path)
	else:
	    print("Sorry, file %s does not exist." % tmp_file_path)

	os.chdir(tmp_file_path)
	cdir = os.getcwd()

	print(cdir)


	timestr = time.strftime("%Y%m%d_%H%M%S")
	filename = 'log_' + timestr + '.log'

	with open(filename, "w") as f:   # Opens file and casts as f 
		f.close()

	root = logging.getLogger()
	if root.handlers:
	    for handler in root.handlers:
	        root.removeHandler(handler)
	logging.basicConfig(filename= filename, filemode = 'w', format='%(asctime)s %(levelname)s %(name)s %(message)s',level=logging.INFO)
	logger = logging.getLogger()

	return(logger,filename)




def append_logs_s3(logger,filename,s3client):
	with open(filename, 'rb') as f:
		s3client.upload_fileobj(f, 'S3', 'Key/{0}'.format(filename))

