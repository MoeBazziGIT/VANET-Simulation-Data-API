from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Simulation
from Eavesdropper.models import Eavesdropper
from Message.models import Message
from django.core import serializers
import json

@api_view(['POST'])
def add_simulation(request, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        start_time, dev_name, privacy_scheme, eavesdroppers = data["start_time"], data["dev_name"], data["privacy_scheme"], data["eavesdroppers"]
        new_sim = Simulation(start_time=start_time, dev_name=dev_name, privacy_scheme=privacy_scheme)
        new_sim.save()

        # add all eavesdroppers to this Simulation
        for evs in eavesdroppers:
            new_evs = Eavesdropper(index=evs["index"], simulation=new_sim)
            new_evs.save()
            # collect all messages and add them to this eavesdropper
            for msg in evs["messages"]:
                # if this message hasnt been encountered already, then we will create a new Message object, otherwise just fetch the previously created Message
                new_msg = Message(msg["sender_address"], msg["sender_psynm"], msg["sender_psynm"], msg["sender_vel_x"], msg["sender_vel_y"], msg["sender_pos_x"], msg["sender_pos_y"], msg["sender_angle"], msg["simTime_eavesdropped"], msg["is_encrypted"])
                new_msg.save()
                # add message to this eavesdropper
                new_evs.eavesdropped_messages.add(new_msg)
            new_evs.save()
            # add this eavesdropper to this sumulation
            # new_sim.eavesdropper_set.add(new_evs)

        new_sim.save()
        # new_sim = serializers.serialize("json", new_sim)
        response = {'Success': 'Added simulation!'}
        _status = status.HTTP_200_OK

    else:
        _status = status.HTTP_403_FORBIDDEN
        response = {'Error': "Request was NOT an http POST request"}
    return Response(response, status=_status)
