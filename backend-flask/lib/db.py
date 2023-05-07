from psycopg_pool import ConnectionPool
import os
import re
import sys
from flask import current_app as app

# connection_url = os.getenv("CONNECTION_URL")
# pool = ConnectionPool(connection_url)

class Db:
  def __init__(self):
    self.init_pool()

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def query_commit(self, sql, params={}):
    self.print_sql('commit with or without returning',sql,params)
    pattern = r"\bRETURNING\b"
    is_returning_id = re.search(pattern, sql)

    try:
      with self.pool.connection() as conn:
        cur = conn.cursor()
        cur.execute(sql,params)
        if is_returning_id:
          returning_id = cur.fetchone()[0]
        conn.commit()
        if is_returning_id:
          return returning_id
    except Exception as err:
      self.print_sql_err(err)
      #conn.rollback()

  
  def query_object_json(self, sql, params={}):
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql, params)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
        return json[0]

  def query_array_json(self, sql, params={}):
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql, params)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchone()
        return json[0]

  # when we want to return a a single value
  def query_value(self,sql,params={}):
    self.print_sql('value',sql,params)

    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql,params)
        json = cur.fetchone()
        return json[0]


  def print_sql_err(self, err):
      # get details about the exception
      err_type, err_obj, traceback = sys.exc_info()

      # get the line number when exception occured
      line_num = traceback.tb_lineno

      # print the connect() error
      print ("\npsycopg2 ERROR:", err, "on line number:", line_num)
      print ("psycopg2 traceback:", traceback, "-- type:", err_type)

      # psycopg2 extensions.Diagnostics object attribute
      #print ("\nextensions.Diagnostics:", err.diag)

      # print the pgcode and pgerror exceptions
      print ("pgerror:", err.pgerror)
      print ("pgcode:", err.pgcode, "\n")

  
  def query_wrap_object(self, template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self, template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

#  def template(self,*args):
#     pathing = list((app.root_path,'db','sql',) + args)
#     pathing[-1] = pathing[-1] + ".sql"

#     template_path = os.path.join(*pathing)
  def template(self,name):
    template_path = os.path.join(app.root_path,'db','sql',name + '.sql')

    with open(template_path, 'r') as f:
      template_content = f.read()
      return template_content 

  def print_sql(self,title,sql,params={}):
    cyan = '\033[96m'
    no_color = '\033[0m'    
    print(f'{cyan}SQL----------------[{title}]----{no_color}', flush=True)
    print(sql, params)

db = Db()