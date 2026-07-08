"""TaskAssignment model — links a Task to the Employee(s) assigned to it."""

from datetime import datetime

from task_management.extensions import db


class TaskAssignment(db.Model):
    """Represents the assignment of one task to one employee."""

    __tablename__ = "task_assignments"

    id: int = db.Column(db.Integer, primary_key=True)
    task_id: int = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    employee_id: int = db.Column(
        db.Integer, db.ForeignKey("employees.id"), nullable=False
    )
    status: str = db.Column(db.String(20), nullable=False, default="assigned")
    assigned_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed_at: datetime | None = db.Column(db.DateTime, nullable=True)

    task = db.relationship("Task", back_populates="assignments")
    employee = db.relationship("Employee", back_populates="task_assignments")

    __table_args__ = (
        db.UniqueConstraint("task_id", "employee_id", name="uq_task_employee"),
    )

    def __repr__(self) -> str:
        return (
            f"<TaskAssignment task_id={self.task_id} "
            f"employee_id={self.employee_id} status={self.status!r}>"
        )
