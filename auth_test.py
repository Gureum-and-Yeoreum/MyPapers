from mendeley import Mendeley

# These values should match the ones supplied when registering your application.
mendeley = Mendeley(client_id, client_secret=client_secret, redirect_uri=redirect_uri)

auth = mendeley.start_authorization_code_flow()

# The user needs to visit this URL, and log in to Mendeley.
login_url = auth.get_login_url()

# After logging in, the user will be redirected to a URL, auth_response.
session = auth.authenticate(auth_response)