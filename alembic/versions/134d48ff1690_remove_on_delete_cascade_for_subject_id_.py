"""Remove on delete cascade for subject_id column in GradeSubjects table

Revision ID: 134d48ff1690
Revises: 0a772cbe53e4
Create Date: 2022-04-20 00:52:52.413731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '134d48ff1690'
down_revision = '0a772cbe53e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('gradesubjects_subject_id_fkey', 'gradesubjects', type_='foreignkey')
    op.create_foreign_key(None, 'gradesubjects', 'subjects', ['subject_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gradesubjects', type_='foreignkey')
    op.create_foreign_key('gradesubjects_subject_id_fkey', 'gradesubjects', 'subjects', ['subject_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
