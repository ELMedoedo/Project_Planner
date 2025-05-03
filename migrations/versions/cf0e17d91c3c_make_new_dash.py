"""make new dash

Revision ID: cf0e17d91c3c
Revises: 449b1de11690
Create Date: 2025-05-03 01:58:19.180813

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = 'cf0e17d91c3c'
down_revision = '449b1de11690'
branch_labels = None
depends_on = None

def upgrade():
    # 1. Добавляем колонку с временным разрешением NULL
    with op.batch_alter_table('dashboards', schema=None) as batch_op:
        batch_op.add_column(sa.Column(
            'created_at', 
            sa.DateTime(), 
            nullable=True,
            server_default=sa.text('NOW()')
        ))

    # 2. Обновляем существующие записи
    conn = op.get_bind()
    conn.execute(text("UPDATE dashboards SET created_at = NOW()"))

    # 3. Меняем на NOT NULL
    with op.batch_alter_table('dashboards', schema=None) as batch_op:
        batch_op.alter_column(
            'created_at',
            existing_type=sa.DateTime(),
            nullable=False,
            existing_server_default=sa.text('NOW()')
        )

def downgrade():
    with op.batch_alter_table('dashboards', schema=None) as batch_op:
        batch_op.drop_column('created_at')