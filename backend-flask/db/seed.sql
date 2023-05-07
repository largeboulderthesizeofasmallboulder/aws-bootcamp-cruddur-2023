INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  --('Andrew Brown','andrew@exampro.co', 'andrewbrown' ,'MOCK'),
  ('First User','mock@mock.co', 'FirstUser' ,'MOCK'),
  ('Andrew Bayko', 'bayko@exampro.co', 'bayko' ,'MOCK'),
  ('Funny Guy', 'fguy@exampro.co', 'FunnyGuy' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'FirstUser' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )