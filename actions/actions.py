# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ValidateHealthForm(FormValidationAction):
    def name(self):
        return "validate_health_form"
    
@staticmethod
def required_slots(tracker):
    if tracker.get_slot("confirm_excercise") == True:
        return ["confirm_excercise", "sleep", "diet", "stress", "goal"]
    else:
        return ["confirm_excercise", "sleep", "diet", "stress", "goal"]

def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
) -> List[Dict]:
    return  []  

def slot_mappings(self) ->  Dict[Text, Union[Dict, List[Dict]]]:
    return{
        "confirm_excercise": [
            self.form_intent(intent="affirm", value=True),
            self.form_intent(intent="deny", value=True),
            self.form_intent(intent="inform", value=True),
        ],
        "sleep":[
            self.form_entity(entity="sleep"),
            self.form_intent(intent="deny", value="None")
        ],
        "diet": [
            self.form_text(intent="inform"),
            self.form_text(intent="affirm"),
            self.form_text(intent="deny"),
        ],
        "goal":[
            self.from_text(intent="inform"),
        ]

    }    








