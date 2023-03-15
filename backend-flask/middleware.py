import time
import os
from flask import Flask, jsonify
from flask_http_middleware import MiddlewareManager, BaseHTTPMiddleware
from lib.cognito_jwt_token import CognitoJwtToken, extract_access_token, TokenVerifyError



cognito_jwt_token = CognitoJwtToken(
  user_pool_id = os.getenv("AWS_COGNITO_USER_POOL_ID"), 
  user_pool_client_id = os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"), 
  region = os.getenv("AWS_DEFAULT_REGION")
  )


class AccessMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__()
        self._app = app

    def dispatch(self, request, call_next):
        app.logger.info('request.headers')  
        app.logger.info(request.headers)  
        access_token = extract_access_token(request.headers)
       # app.logger.info(access_token)  
        # authenticated request
        claims = cognito_jwt_token.verify(access_token)
        # app.logger.info('authenticated')  
        # app.logger.info(claims)  
        # app.logger.info(claims['username'])
        


        return call_next(request)
     
