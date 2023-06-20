from mendeley import Mendeley

# These values should match the ones supplied when registering your application.
mendeley = Mendeley('15565', client_secret="83eGkxeG3I5COtC9")

auth = mendeley.start_client_credentials_flow()
session = auth.authenticate()

print session.profiles.me.display_name