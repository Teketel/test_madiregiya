import gcm as core_gcm
from time import gmtime, strftime

SENDER_ID = "YOUR_SENDER_ID"
API_KEY = "YOUR_API_KEY"
reg_id = "YOUR_REGI_ID"

gcm = core_gcm.GCM(API_KEY) 
data = {"message": 'Hello user, Izihi [' + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + '] new', "message2" : "hello"}
# Plaintext request reg_id = '12345' 
res = gcm.plaintext_request(registration_id=reg_id, data=data) 

#Error handling 

# Plaintext request

try:
    canonical_id = gcm.plaintext_request(registration_id=reg_id, data=data)
    if canonical_id:
        # Repace reg_id with canonical_id in your database
        entry = entity.filter(registration_id=reg_id)
        entry.registration_id = canonical_id
        entry.save()
except GCMNotRegisteredException:
    # Remove this reg_id from database
    print "E: NotRegisteredException raised, So registration id will be deleted."
    entity.filter(registration_id=reg_id).delete()
except GCMUnavailableException:
    # Resent the message
    print "E: Error sending message, please Resent the message"
