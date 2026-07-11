"""Employee model — profile information linked to a User and Department."""

from datetime import date

from task_management.extensions import db


class Employee(db.Model):
    """Represents an employee profile tied one-to-one to a User account."""

    __tablename__ = "employees"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False
    )
    department_id: int | None = db.Column(
        db.Integer, db.ForeignKey("departments.id"), nullable=True
    )
    first_name: str = db.Column(db.String(50), nullable=False)
    last_name: str = db.Column(db.String(50), nullable=False)
    position: str | None = db.Column(db.String(100), nullable=True)
    hire_date: date | None = db.Column(db.Date, nullable=True)

    user = db.relationship("User", back_populates="employee")
    department = db.relationship("Department", back_populates="employees")
    task_assignments = db.relationship(
        "TaskAssignment", back_populates="employee", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Employee id={self.id} name={self.first_name!r} {self.last_name!r}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "department_id": self.department_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": f"{self.first_name} {self.last_name}",
            "position": self.position,
            "hire_date": self.hire_date.isoformat() if self.hire_date else None,
        }
