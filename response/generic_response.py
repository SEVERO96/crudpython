"""Generic Responses"""
import json

class Responses():
    """class for make generic responses"""
    @staticmethod
    def index_response(data):
        """response for index operation"""
        response = {
            "statusCode": 200,
            "status": "Success",
            "text": "Index have been made Successfully",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)
    @staticmethod
    def create_response(data):
        """response for create operation"""
        response = {
            "statusCode":201,
            "status": "Created",
            "text": "Resource have created successfull",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)
    @staticmethod
    def show_response(data):
        """response for show operation"""
        response = {
            "statusCode": 200,
            "status": "Success",
            "text": "Success show of resource",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)
    @staticmethod
    def update_response(data):
        """response for update operation"""
        response = {
            "statusCode": 200,
            "status": "Success",
            "text": "Success update resource",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)
    @staticmethod
    def not_found_response(data):
        """error response for not found resource"""
        response = {
            "statusCode": 404,
            "status": "Not found",
            "text": "No resource found according to the given data",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)
    @staticmethod
    def logical_delete(data):
        """response for logical delete of a resource"""
        response = {
            "statusCode": 200,
            "status": "Deleted",
            "text": "resource has been successfully deleted",
            "data": data
        }
        return json.dumps(response, ensure_ascii=False)
    @staticmethod
    def destroy_resource():
        """response for a resoruce destroy"""
        response = {
            "statusCode": 204,
            "status": "Destroyed",
            "text": "Resource has been permanently deleted"
        }
        return json.dumps(response, ensure_ascii=False)
