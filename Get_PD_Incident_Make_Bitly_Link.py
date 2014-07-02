import json
from temboo.Library.PagerDuty.Incidents import GetIncident
from temboo.core.session import TembooSession
from temboo.Library.Bitly.Links import ShortenURL
from temboo.core.session import TembooSession


# Create a session with your Temboo account details
session = TembooSession('pagerduty-preview', 'myFirstApp', 'my_temboo_api_key')

# Instantiate the Choreo
getIncidentChoreo = GetIncident(session)

# Get an InputSet object for the Choreo
getIncidentInputs = getIncidentChoreo.new_input_set()

# Set the Choreo inputs
getIncidentInputs.set_IncidentID("870")
getIncidentInputs.set_APIKey("my_pagerduty_api_key")
getIncidentInputs.set_SubDomain("pdt-dank")

# Execute the Choreo
getIncidentResults = getIncidentChoreo.execute_with_results(getIncidentInputs)

# Print the Choreo outputs
#print("Response: " + getIncidentResults.get_Response())
dct = json.loads(getIncidentResults.get_Response())
res = dct['trigger_summary_data']['client_url']

# Create a session with your Temboo account details

from temboo.Library.Bitly.Links import ShortenURL
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession('pagerduty-preview', 'myFirstApp', 'my_temboo_api_key')

# Instantiate the Choreo
shortenURLChoreo = ShortenURL(session)

# Get an InputSet object for the Choreo
shortenURLInputs = shortenURLChoreo.new_input_set()

# Set the Choreo inputs
shortenURLInputs.set_AccessToken("my_bitly_auth_token")
shortenURLInputs.set_LongURL(res)

# Execute the Choreo
shortenURLResults = shortenURLChoreo.execute_with_results(shortenURLInputs)

# Print the Choreo outputs
print("Response: " + shortenURLResults.get_Response()),


