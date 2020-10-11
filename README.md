# kanban-board
 a REST API for a Kanban board on Python using Serverless
Framework with a simple react front end

# Prerequisites

Setting up an AWS account and creating a python REST API app on  https://app.serverless
Creating a postgreSQL database on AWS and setting up the credentials in rds_config.py
 
# Deployement

To deploy the app simply cd into the kanban-board folder and do
``serverless deploy``

To deploy the react app first cd into the front-end then do `npm install` afterwards do `npm run build` and finally open a second terminal and do `npm run live` to start the live server

The URL can be found in `src/index.js` in the `base_url` variable and should be changed to the endpoint received from serverless

# Unit tests

Tests can be found in the `test_handler.py` file 

#  Documentation

The documentation uses https://github.com/Ajaxy/tinyspec which should be installed first to generate them

# Demo

A demo version of the documentation can be found here https://kanban-board-dev-serverlessdeploymentbucket-hwq2wjlunz9o.s3.amazonaws.com/documentation/index.html

A demo version of the front end app can be found here https://kanban-board-dev-serverlessdeploymentbucket-hwq2wjlunz9o.s3.amazonaws.com/front-end/index.html

A demo version of the REST API can be found here https://jx2ubbcvfi.execute-api.us-east-1.amazonaws.com/dev/