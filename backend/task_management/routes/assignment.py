"""
Task-assignment endpoints.

Wraps `task_management.services.assignment_service`, covering the
Task <-> Employee join (`TaskAssignment`).

Routes (mounted at /api/assignments):
    POST   /                                   -- assign a task to an employee
    PUT    /<int:assignment_id>/status          -- update an assignment's status
    DELETE /<int:assignment_id>                  -- remove an assignment
    GET    /employee/<int:employee_id>            -- list assignments for an employee
    GET    /task/<int:task_id>                      -- list assignments for a task
"""

from __future__ import annotations

from flask import Blueprint, jsonify, request

from task_management.routes import login_required
from task_management.services.assignment_service import (
    AssignmentError,
    assign_task_to_employee,
    list_assignments_for_employee,
    list_assignments_for_task,
    remove_assignment,
    update_assignment_status,
)

assignment_bp = Blueprint("assignment", __name__)


@assignment_bp.post("")
@login_required
def assign(current_user):
    data = request.get_json(silent=True) or {}
    task_id = data.get("task_id")
    employee_id = data.get("employee_id")

    if not task_id or not employee_id:
        return jsonify({"error": "task_id and employee_id are required."}), 400

    try:
        assignment = assign_task_to_employee(task_id=task_id, employee_id=employee_id)
    except AssignmentError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(assignment.to_dict()), 201


@assignment_bp.put("/<int:assignment_id>/status")
@login_required
def update_status(assignment_id: int, current_user):
    data = request.get_json(silent=True) or {}
    status = data.get("status")

    if not status:
        return jsonify({"error": "status is required."}), 400

    try:
        assignment = update_assignment_status(assignment_id, status=status)
    except AssignmentError as exc:
        return jsonify({"error": str(exc)}), 400

    return jsonify(assignment.to_dict()), 200


@assignment_bp.delete("/<int:assignment_id>")
@login_required
def remove(assignment_id: int, current_user):
    try:
        remove_assignment(assignment_id)
    except AssignmentError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify({"message": "Assignment removed."}), 200


@assignment_bp.get("/employee/<int:employee_id>")
@login_required
def by_employee(employee_id: int, current_user):
    try:
        assignments = list_assignments_for_employee(employee_id)
    except AssignmentError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify([a.to_dict() for a in assignments]), 200


@assignment_bp.get("/task/<int:task_id>")
@login_required
def by_task(task_id: int, current_user):
    try:
        assignments = list_assignments_for_task(task_id)
    except AssignmentError as exc:
        return jsonify({"error": str(exc)}), 404

    return jsonify([a.to_dict() for a in assignments]), 200
