from flask import Blueprint, jsonify, url_for
from postnews.models import User
from postnews.core.utils import ApiResult, ApiException

bp = Blueprint("core_api", __name__, url_prefix="/core")

@bp.route("/")
def core_main():
    return ApiResult({"_links": {"users": url_for("core_api.users")}})

@bp.route("/users")
def users():
    return ApiResult({"users": []})
