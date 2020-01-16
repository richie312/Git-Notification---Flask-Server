#### Changes Required in Database
 * Include the ranking column in `skillz.result_sphere_engine` by typing the following code in MySql Editor,
	- `ALTER TABLE skillz.result_sphere_engine add column ranking varchar(200);`

#### Database Change request has been sent to it@capitalnumbers.com . The new database schema will be skillz.

#### New Database schema name **skillz** has been configured on the RDS database server. Please gitpull to incorporate the changes.

#### The code will be deployed on 10.0.8.34 and the live url will be shared soon.

#### The flask server is live for testing purpose and for internal users. Here is the live base url `http://111.93.164.108:5000/`

#### API Documentation is updated.

#### Cors is applied on the flask server.

#### New database is online on `cndb3mysql.cnifsz8x7lk0.us-east-1.rds.amazonaws.com`. Details are shared in database_auth.json file in git repo of `aritra_skillz` branch.

#### Git Webhook for auto notification is in progress...
	* Update 1 : Local Batch file is sheduled with windows task scheduler. Thus, during the office time if script detect any changes in file size of main.py, changes_required and mail.py; then it will send mail to the concerned stakeholders of this repository.

	* Direct git webhook auto notification is in progress. There is some dependency on IT team of capital numbers. IT will be updated soon.

#### Git Webhook for auto notification deployed on 10.0.8.34
	
	* Direct git webhook auto notification is deployed on linux server and is functional. Local checks from windows machine is disabled.

#### Next Step of Actions:
	* Code Optimization
	* Addition of difficult problems
	* Exposing check file with testcases api.
	* Decide on how to rank
	* Deployment on AWS Lambda

#### Url Added to the testing server `10.0.8.34`
	* `http://127.0.0.1:5000/get_testcases`
	* Documentation for the above api has been updated.
	* The Api is tested with POSTMAN.


#### Check File Status Route

	* check file status route has been added to the  testing server `http://111.93.164.108:5000/check_file_status`

#### Skillsz API Document Route 

	* Skillsz API documentation route has been added to the  testing server `http://111.93.164.108:5000/skillsz_api_docs`

#### /get_problems
	* New parameter **all** has been added to the /get_problems api in order to fetch all the details regardless of the levels. It is also live on the testing server `http://111.93.164.108:5000/get_problems?level=all`
	





