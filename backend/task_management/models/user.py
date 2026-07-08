"""User model — authentication credentials and role information."""

from datetime import datetime

from task_management.extensions import db


class User(db.Model):
    """Represents a login account (admin or employee) with hashed credentials."""

    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash: str = db.Column(db.String(255), nullable=False)
    role: str = db.Column(db.String(20), nullable=False, default="employee")
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # One-to-one: not every user (e.g. an admin) necessarily has an employee profile.
    employee = db.relationship(
        "Employee",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )
    activity_logs = db.relationship(
        "ActivityLog", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username!r} role={self.role!r}>"
