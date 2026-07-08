"""ActivityLog model — audit trail entries recording user actions."""

from datetime import datetime

from task_management.extensions import db


class ActivityLog(db.Model):
    """Represents a single audit-log entry for a user action."""

    __tablename__ = "activity_logs"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    action: str = db.Column(db.String(100), nullable=False)
    target_type: str | None = db.Column(db.String(50), nullable=True)
    target_id: int | None = db.Column(db.Integer, nullable=True)
    details: str | None = db.Column(db.Text, nullable=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", back_populates="activity_logs")

    def __repr__(self) -> str:
        return f"<ActivityLog id={self.id} action={self.action!r}>"
