"""add healing column to spell table

Revision ID: 2cea16d7e311
Revises: 40ae25403ca6
Create Date: 2023-08-12 13:35:19.272680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2cea16d7e311'
down_revision: Union[str, None] = '40ae25403ca6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spell', sa.Column('healing', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spell', 'healing')
    # ### end Alembic commands ###
