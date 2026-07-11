"""
Employee endpoints.

Wraps `task_management.services.employee_service`. Mutating actions
(create/update/delete) are restricted to admin/manager roles; reads
are open to any authenticated user.

Routes (mounted at /api/employees):
    POST   /                              -- create an employee profile
    GET    /<int:employee_id>              -- fetch a single employee
    PUT    /<int:employee_id>               -- update an employee
    DELETE /<int:employee_id>                -- delete an employee
    GET    /department/<int:department_id>    -- list employees in a department
"""

from __future__ import annotations

from flask import Blueprint, jsonify, request

from task_management.routes import login_required, roles_required
from task_management.services.employee_service import (
    EmployeeError,
    create_employee,
    delete_employee,
    get_employee,
    list_employees_by_department,
    update_employee,
)

employee_bp = Blueprint("employee", __name__)


@employee_bp.post("")
@login_required
@roles_required("admin", "manager")
def create(current_user):
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    department_id = data.get("department_id")
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    if not user_id or not department_id or not first_name or not last_name:
        return (
            jsonify(
                {"error": "user_id, department_id, first_name, and last_name are required."}
            ),
            400,
        )

    try:
        employee = create_employee(
            acting_user_id=current_user.id,
            user_id=user_id,
            department_id=department_id,
            first_name=first_name,
            last_name=last_name,
            position=data.get("position") or data.get("job_title"),
        )
    except EmployeeError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(employee.to_dict()), 201


@employee_bp.get("/<int:employee_id>")
@login_required
def get(employee_id: int, current_user):
    try:
        employee = get_employee(employee_id)
    except EmployeeError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify(employee.to_dict()), 200


@employee_bp.put("/<int:employee_id>")
@login_required
@roles_required("admin", "manager")
def update(employee_id: int, current_user):
    data = request.get_json(silent=True) or {}

    try:
        employee = update_employee(
            acting_user_id=current_user.id,
            employee_id=employee_id,
            **data,
        )
    except EmployeeError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(employee.to_dict()), 200


@employee_bp.delete("/<int:employee_id>")
@login_required
@roles_required("admin", "manager")
def delete(employee_id: int, current_user):
    try:
        delete_employee(acting_user_id=current_user.id, employee_id=employee_id)
    except EmployeeError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify({"message": "Employee deleted."}), 200


@employee_bp.get("/department/<int:department_id>")
@login_required
def by_department(department_id: int, current_user):
    try:
        employees = list_employees_by_department(department_id)
    except EmployeeError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify([employee.to_dict() for employee in employees]), 200
