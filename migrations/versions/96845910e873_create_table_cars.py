"""create table cars

Revision ID: 96845910e873
Revises:
Create Date: 2025-03-19 04:55:39.821102

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "96845910e873"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cars",
        sa.Column("brand", sa.String(length=60), nullable=False),
        sa.Column("model", sa.String(length=60), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("price", sa.Float(precision=2), nullable=False),
        sa.Column("percentage", sa.Float(precision=2), nullable=False),
        sa.Column("broker_fee", sa.Float(precision=2), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(op.f("ix_cars_uuid"), "cars", ["uuid"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_cars_uuid"), table_name="cars")
    op.drop_table("cars")
    # ### end Alembic commands ###
