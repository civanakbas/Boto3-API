from flask import request, jsonify, make_response, render_template
from boto_functions import instantiate_client, list_instance_ids


def configure_routes(app):
    @app.route("/ec2/list", methods=["GET"])

    # For listing instances with query parameters
    def list_instances_query():
        access_key_id = request.args.get("aws_access_key_id")
        secret_key_id = request.args.get("aws_secret_access_key")
        region = request.args.get("region_name")

        try:
            client = instantiate_client(access_key_id, secret_key_id, region)
            return make_response(jsonify(list_instance_ids(client)), 200)
        except Exception:
            message = {
                "message": "Error when instantiating client. Please make sure you entered the correct credentials"
            }
            return make_response(jsonify(message), 400)

    # For listing instances with url parameters
    @app.route(
        "/ec2/list/<access_key_id>/<aws_secret_access_key>/<region_name>",
        methods=["GET"],
    )
    def list_instances_url(access_key_id, aws_secret_access_key, region_name):

        try:
            client = instantiate_client(
                access_key_id, aws_secret_access_key, region_name
            )
            return make_response(jsonify(list_instance_ids(client)), 200)
        except Exception:
            message = {
                "message": "Error when instantiating client. Please make sure you entered the correct credentials"
            }
            return make_response(jsonify(message), 400)

    # For listing instances with json body
    @app.route("/ec2/list/json", methods=["GET"])
    def list_instances_json():
        json_data = request.json

        try:
            client = instantiate_client(
                json_data["access_key_id"],
                json_data["aws_secret_access_key"],
                json_data["region_name"],
            )
            return make_response(jsonify(list_instance_ids(client)), 200)
        except Exception:
            message = {
                "message": "Error when instantiating client. Please make sure you entered the correct credentials"
            }
            return make_response(jsonify(message), 400)

    # Starting an instance with query parameters
    @app.route("/ec2/start", methods=["POST"])
    def start_instance_query():
        access_key_id = request.args.get("aws_access_key_id")
        secret_key_id = request.args.get("aws_secret_access_key")
        region = request.args.get("region_name")
        instance_id = request.args.get("InstanceId")

        try:
            client = instantiate_client(access_key_id, secret_key_id, region)
            response = client.start_instances(InstanceIds=[instance_id])
            return make_response(jsonify(response), 200)
        except Exception:
            message = {
                "message": "Error when starting the instance. Please make sure you entered a valid InstanceId and credentials"
            }
            return make_response(jsonify(message), 400)

    # Starting an instance with url parameters
    @app.route(
        "/ec2/start/<access_key_id>/<aws_secret_access_key>/<region_name>/<InstanceId>",
        methods=["POST"],
    )
    def start_instance_url(
        access_key_id, aws_secret_access_key, region_name, InstanceId
    ):
        try:
            client = instantiate_client(
                access_key_id, aws_secret_access_key, region_name
            )
            response = client.start_instances(InstanceIds=[InstanceId])

            return make_response(jsonify(response), 200)
        except Exception:
            message = {
                "message": "Error when starting the instance. Please make sure you entered a valid InstanceId and credentials"
            }
            return make_response(jsonify(message), 400)

    # Starting an instance with json body
    @app.route("/ec2/start/json", methods=["POST"])
    def start_instance_json():
        json_data = request.json

        try:
            client = instantiate_client(
                json_data["access_key_id"],
                json_data["aws_secret_access_key"],
                json_data["region_name"],
            )
            response = client.start_instances(InstanceIds=[json_data["InstanceId"]])

            return make_response(jsonify(response), 200)
        except Exception:
            message = {
                "message": "Error when starting the instance. Please make sure you entered a valid InstanceId and credentials"
            }
            return make_response(jsonify(message), 400)

    # Stopping an instance with query parameters
    @app.route("/ec2/stop", methods=["POST"])
    def stop_instance_query():
        access_key_id = request.args.get("aws_access_key_id")
        secret_key_id = request.args.get("aws_secret_access_key")
        region = request.args.get("region_name")
        instance_id = request.args.get("InstanceId")

        try:
            client = instantiate_client(access_key_id, secret_key_id, region)
            response = client.stop_instances(InstanceIds=[instance_id])

            return make_response(jsonify(response), 200)
        except Exception:
            message = {
                "message": "Error stopping the instance. Please make sure you entered a valid InstanceId and credentials"
            }
            return make_response(jsonify(message), 400)

    # Stopping an instance with url parameters
    @app.route(
        "/ec2/stop/<access_key_id>/<aws_secret_access_key>/<region_name>/<InstanceId>",
        methods=["POST"],
    )
    def stop_instance_url(
        access_key_id, aws_secret_access_key, region_name, InstanceId
    ):
        try:
            client = instantiate_client(
                access_key_id, aws_secret_access_key, region_name
            )
            response = client.stop_instances(InstanceIds=[InstanceId])

            return make_response(jsonify(response), 200)
        except Exception:
            message = {
                "message": "Error stopping the instance. Please make sure you entered a valid InstanceId and credentials"
            }
            return make_response(jsonify(message), 400)

    @app.route("/ec2/stop/json", methods=["POST"])
    def stop_instance_json():
        json_data = request.json

        try:
            client = instantiate_client(
                json_data["access_key_id"],
                json_data["aws_secret_access_key"],
                json_data["region_name"],
            )
            response = client.stop_instances(InstanceIds=[json_data["InstanceId"]])

            return make_response(jsonify(response), 200)
        except Exception:
            message = {
                "message": "Error stopping the instance. Please make sure you entered a valid InstanceId and credentials"
            }
            return make_response(jsonify(message), 400)

    @app.route("/", methods=["GET"])
    def start_page():
        return render_template("index.html")
