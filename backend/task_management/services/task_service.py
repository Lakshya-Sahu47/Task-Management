"""Task business logic."""

from __future__ import annotations

from datetime import date
from typing import List, Optional

from task_management.extensions import db
from task_management.models.task import Task
from task_management.models.user import User
from task_management.services import log_activity

VALID_STATUSES = {"pending", "in_progress", "completed", "cancelled"}
VALID_PRIORITIES = {"low", "medium", "high", "urgent"}


class TaskError(Exception):
    """Raised for any task business-rule violation."""


def create_task(
    *,
    created_by: int,
    title: str,
    description: Optional[str] = None,
    priority: str = "medium",
    due_date: Optional[date] = None,
) -> Task:
    """Create a new task owned by the given user.

    Raises TaskError if the creating user doesn't exist or the priority
    is not one of the recognized values.
    """
    if User.query.get(created_by) is None:
        raise TaskError(f"No user found with id={created_by}.")
    if priority not in VALID_PRIORITIES:
        raise TaskError(f"Invalid priority '{priority}'. Must be one of {sorted(VALID_PRIORITIES)}.")

    task = Task(
        title=title,
        description=description,
        status="pending",
        priority=priority,
        due_date=due_date,
        created_by=created_by,
    )
    db.session.add(task)
    db.session.flush()

    log_activity(user_id=created_by, action="task_created", target_type="Task", target_id=task.id)
    db.session.commit()
    return task


def get_task(task_id: int) -> Task:
    """Fetch a task by primary key, raising TaskError if not found."""
    task: Optional[Task] = Task.query.get(task_id)
    if task is None:
        raise TaskError(f"No task found with id={task_id}.")
    return task


def update_task(
    *,
    acting_user_id: int,
    task_id: int,
    title: Optional[str] = None,
    description: Optional[str] = None,
    status: Optional[str] = None,
    priority: Optional[str] = None,
    due_date: Optional[date] = None,
) -> Task:
    """Update mutable fields on a task. Only provided fields change."""
    task = get_task(task_id)

    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if status is not None:
        if status not in VALID_STATUSES:
            raise TaskError(f"Invalid status '{status}'. Must be one of {sorted(VALID_STATUSES)}.")
        task.status = status
    if priority is not None:
        if priority not in VALID_PRIORITIES:
            raise TaskError(f"Invalid priority '{priority}'. Must be one of {sorted(VALID_PRIORITIES)}.")
        task.priority = priority
    if due_date is not None:
        task.due_date = due_date

    log_activity(
        user_id=acting_user_id, action="task_updated", target_type="Task", target_id=task.id
    )
    db.session.commit()
    return task


def delete_task(*, acting_user_id: int, task_id: int) -> None:
    """Delete a task and its assignments (cascade is handled at the DB/model level)."""
    task = get_task(task_id)
    db.session.delete(task)
    log_activity(user_id=acting_user_id, action="task_deleted", target_type="Task", target_id=task_id)
    db.session.commit()


def list_tasks(*, status: Optional[str] = None, created_by: Optional[int] = None) -> List[Task]:
    """Return tasks, optionally filtered by status and/or creator."""
    query = Task.query
    if status is not None:
        if status not in VALID_STATUSES:
            raise TaskError(f"Invalid status '{status}'. Must be one of {sorted(VALID_STATUSES)}.")
        query = query.filter_by(status=status)
    if created_by is not None:
        query = query.filter_by(created_by=created_by)
    return query.all()
