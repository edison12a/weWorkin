from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields

from utils import *

app = Flask(__name__)
CORS(app)
api = Api(app, version="1.0", title="API Title", description="A simple API")

ns = api.namespace("API", description="API Routes")


# Define the model for your project data
json_model = api.model(
    "project",
    {},
)


@ns.route("/")
class HelloWorld(Resource):
    def get(self):
        """Returns 'Hello, World!'"""
        return {"hello": "world"}


@ns.route("/projects")
class Projects(Resource):

    def get(self):
        projects = fileReader("data/projects.json")
        return projects

    @api.expect(json_model)
    def post(self):
        content = request.get_data(as_text=True)
        project = json.loads(content)
        fileWriter("data/projects.json", project)
        return {"status": "success"}


@ns.route("/projects/<int:id>")
class ProjectById(Resource):
    def get(self, id):
        """Returns a single project by its ID"""
        projects = fileReader("data/projects.json")
        project = next((proj for proj in projects if proj["id"] == id), None)
        if project:
            return project
        else:
            api.abort(404, f"Project {id} not found")


@ns.route("/apply")
class Apply(Resource):
    def post(self):
        project_id = request.json.get("<int:id>")
        projects = fileReader("data/projects.json")
        project = next((proj for proj in projects if proj["id"] == project_id), None)
        if project:
            fileWriter("data/myprojects.json", project)
        else:
            api.abort(404, f"Project {id} not found")


# @ns.route("/login")
# class Login(Resource):
#     def get(self):
#         """Redirects to the Auth0 login page"""
#         auth0 = oauth.create_client("auth0")
#         return auth0.authorize_redirect(redirect_uri="http://localhost:5000/callback")

#     def post(self):
#         """Returns 'Hello, World!'"""
#         return {"hello": "world"}
