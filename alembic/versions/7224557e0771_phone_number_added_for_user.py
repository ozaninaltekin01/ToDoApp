"""phone number added for user

Revision ID: 7224557e0771
Revises: 
Create Date: 2025-06-19 22:34:43.796225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7224557e0771'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('phone_number', sa.String(), nullable=True)
    )


def downgrade() -> None:
    pass
