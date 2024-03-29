from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging
from lib.db import db # pool, query_wrap_array
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    with tracer.start_as_current_span("home-activities-mock-data"):
      #logger.info("HomeAcivities")
      now = datetime.now(timezone.utc).astimezone()

      #sql = query_wrap_array("""
      sql = db.template('activities/home')
      results = db.query_array_json(sql)

      # with pool.connection() as conn:
      #   with conn.cursor() as cur:
      #     cur.execute(sql)
      #     # this will return a tuple
      #     # the first field being the data
      #     json = cur.fetchone()
      # print("========",flush=True)  
      # print(json[0],flush=True)    
      # return json[0]

      return results

                                                          # results = [{
                                                          #   'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                                                          #   'handle':  'Andrew Brown',
                                                          #   'message': 'Cloud is very fun!',
                                                          #   'created_at': (now - timedelta(days=2)).isoformat(),
                                                          #   'expires_at': (now + timedelta(days=5)).isoformat(),
                                                          #   'likes_count': 5,
                                                          #   'replies_count': 1,
                                                          #   'reposts_count': 0,
                                                          #   'replies': [{
                                                          #     'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                                                          #     'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                                                          #     'handle':  'Worf',
                                                          #     'message': 'This post has no honor!',
                                                          #     'likes_count': 0,
                                                          #     'replies_count': 0,
                                                          #     'reposts_count': 0,
                                                          #     'created_at': (now - timedelta(days=2)).isoformat()
                                                          #   }],
                                                          # },
                                                          # {
                                                          #   'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                                                          #   'handle':  'Worf',
                                                          #   'message': 'I am out of prune juice',
                                                          #   'created_at': (now - timedelta(days=7)).isoformat(),
                                                          #   'expires_at': (now + timedelta(days=9)).isoformat(),
                                                          #   'likes': 0,
                                                          #   'replies': []
                                                          # },
                                                          # {
                                                          #   'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                                                          #   'handle':  'Garek',
                                                          #   'message': 'My dear doctor, I am just simple tailor',
                                                          #   'created_at': (now - timedelta(hours=1)).isoformat(),
                                                          #   'expires_at': (now + timedelta(hours=12)).isoformat(),
                                                          #   'likes': 0,
                                                          #   'replies': []
                                                          #   }     
                                                          # ]
                                                          # if cognito_user_id != None:
                                                          #   extra_crud =  {
                                                          #   'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                                                          #   'handle':  'Lore',
                                                          #   'message': 'My dear brother, it\'s the humans that are the problem',
                                                          #   'created_at': (now - timedelta(hours=1)).isoformat(),
                                                          #   'expires_at': (now + timedelta(hours=12)).isoformat(),
                                                          #   'likes': 0,
                                                          #   'replies': []
                                                          #   }
                                                          #   results.insert(0, extra_crud)
     
