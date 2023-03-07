from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
from opentelemetry import trace
import logging


tracer = trace.get_tracer("user.activities")
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
LOGGER.addHandler(console_handler)

class UserActivities:
    def run(user_handle):
        with tracer.start_as_current_span('user-activities') as current_span:
            try:
                model = {
                    'errors': None,
                    'data': None
                }

                now = datetime.now(timezone.utc).astimezone()
                LOGGER.info("user_handle")
                LOGGER.info(user_handle)
                if user_handle == None or len(user_handle) < 1:
                    model['errors'] = ['blank_user_handle']
                else:
                    now = datetime.now()
                    if user_handle == 'Andrew Brown':
                      results = [{
                          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                          'handle':  'Andrew Brown',
                          'message': 'Cloud is fun!',
                          'created_at': (now - timedelta(days=1)).isoformat(),
                          'expires_at': (now + timedelta(days=31)).isoformat()
                      }]
                    else:
                      results = [{
                            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                            'handle':  'Worf',
                            'message': 'looking for magic!',
                            'created_at': (now - timedelta(days=1)).isoformat(),
                            'expires_at': (now + timedelta(days=31)).isoformat()
                        },
                        {
                            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                            'handle':  'Worf',
                            'message': 'looking for friends',
                            'created_at': (now - timedelta(days=1)).isoformat(),
                            'expires_at': (now + timedelta(days=31)).isoformat()
                        }]   
                    model['data'] = results
                    current_span.set_attribute("userName", user_handle)
                    current_span.set_attribute("userNumberMessages", len(results))
                # xray ---
                subsegment = xray_recorder.begin_subsegment(
                    'mock-data-for-user-activities')
                dict = {
                    "now": now.isoformat(),
                    "results-size": len(model['data'])
                }
                subsegment.put_metadata('key', dict, 'namespace')
            finally:
                xray_recorder.end_subsegment()
            return model
