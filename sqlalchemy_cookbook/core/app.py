#!coding:utf-8
"""
app.py
"""
from db import dal
from sqlalchemy.sql import select
from datetime import datetime as dt

def get_orders_by_customer(cust_name, shipped=None, details=False):
	columns = [dal.chaoses.c.id, dal.chaoses.c.name, dal.chaoses.c.fractal]

	sel = select(columns)
	sql = sel.where(dal.chaoses.c.modifyed_at < dt.now())

	return dal.connection.execute(sql).fetchall()

def get_chaos_all():
	sel = select([dal.chaoses]) # tableの列全てを指定
	return dal.connection.execute(sel).fetchall()

def get_chaos_all_count():
	sel = select([dal.chaoses]) # tableの列全てを指定
	result = dal.connection.execute(sel).fetchall()
	return len(result)

def get_chaos_order_by_fractal():
	sel = select([dal.chaoses])
	sel = sel.order_by(dal.chaoses.c.fractal)

	return dal.connection.execute(sel).fetchall()

def get_sum_fractal():
	from sqlalchemy.sql import func
	sel = select([func.sum(dal.chaoses.c.fractal)])
	return dal.connection.execute(sel).scalar()

# ============================================
# Samples
# ============================================
# s = select([dal.chaoses.c.name, dal.chaoses.c.fractal])
# s = s.order_by(dal.chaoses.c.created_at)
# s = s.limit(2)
# results = dal.connection.execute(s)

