"""Task model — a unit of work that can be assigned to employees."""

from datetime import date, datetime

from task_management.extensions import db


class Task(db.Model):
    """Represents a task created by a user (typically an admin)."""

    __tablename__ = "tasks"

    id: int = db.Column(db.Integer, primary_key=True)
    title: str = db.Column(db.String(150), nullable=False)
    description: str | None = db.Column(db.Text, nullable=True)
    status: str = db.Column(db.String(20), nullable=False, default="pending")
    priority: str = db.Column(db.String(10), nullable=False, default="medium")
    due_date: date | None = db.Column(db.Date, nullable=True)
    created_by: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    creator = db.relationship("User", foreign_keys=[created_by])
    assignments = db.relationship(
        "TaskAssignment", back_populates="task", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Task id={self.id} title={self.title!r} status={self.status!r}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "created_by": self.created_by,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
