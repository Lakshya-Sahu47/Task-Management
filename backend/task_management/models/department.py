"""Department model — organizational grouping for employees."""

from task_management.extensions import db


class Department(db.Model):
    """Represents a company department (e.g. Engineering, HR, Sales)."""

    __tablename__ = "departments"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), unique=True, nullable=False)
    description: str | None = db.Column(db.String(255), nullable=True)

    employees = db.relationship("Employee", back_populates="department")

    def __repr__(self) -> str:
        return f"<Department id={self.id} name={self.name!r}>"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
