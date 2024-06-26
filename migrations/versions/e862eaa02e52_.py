"""empty message

Revision ID: e862eaa02e52
Revises: a5cffa318ac2
Create Date: 2024-05-02 16:32:44.573227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e862eaa02e52'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('gravity', sa.String(length=20), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=20), nullable=True),
    sa.Column('terrain', sa.String(length=20), nullable=True),
    sa.Column('surface_water', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('classification', sa.String(length=250), nullable=True),
    sa.Column('designation', sa.String(length=250), nullable=True),
    sa.Column('average_height', sa.String(length=20), nullable=True),
    sa.Column('skin_colors', sa.String(length=250), nullable=True),
    sa.Column('hair_colors', sa.String(length=250), nullable=True),
    sa.Column('eye_colors', sa.String(length=250), nullable=True),
    sa.Column('average_lifespan', sa.String(length=20), nullable=True),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.Column('language', sa.String(length=250), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('manufacturer', sa.String(), nullable=True),
    sa.Column('cost_in_credits', sa.Integer(), nullable=True),
    sa.Column('length', sa.DECIMAL(precision=20, scale=1), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('max_atmosphering_speed', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('consumable', sa.String(length=20), nullable=True),
    sa.Column('films', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('pilots', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=20), nullable=True),
    sa.Column('skin_color', sa.String(length=20), nullable=True),
    sa.Column('eyes_color', sa.String(length=20), nullable=True),
    sa.Column('birth_year', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.Column('url', sa.String(length=250), nullable=True),
    sa.Column('species_id', sa.Integer(), nullable=True),
    sa.Column('starship_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('vehicle_ids', sa.ARRAY(sa.Integer()), nullable=True),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=100), nullable=False))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    op.drop_table('favorite')
    op.drop_table('character')
    op.drop_table('vehicle')
    op.drop_table('species')
    op.drop_table('planet')
    # ### end Alembic commands ###
