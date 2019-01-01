import requests
import json
from rasa_core_sdk import Action


class ActionJoke(Action):
  def name(self):
    return "action_joke"

  def run(self, dispatcher, tracker, domain):
    request = requests.get('http://api.icndb.com/jokes/random').json() #make an api call
    joke = request['value']['joke'] #extract a joke from returned json response
    dispatcher.utter_message(joke) #send the message back to the user
    return []

class ActionEmpName(Action):
  def name(self):
    return "action_empName"

  def run(self, dispatcher, tracker, domain):
    #print("before calling API: ", req)
    req = requests.get('http://10.140.28.202:5051/employees/155108').json() #make an api call
    emps = req['data'][0]['name'] #extract employee ids from json response
    dispatcher.utter_message(emps) #send the message back to the user
    return []

class ActionTotalLeaves(Action):
  def name(self):
    return "action_totalLeaves"

  def run(self, dispatcher, tracker, domain):
    #print("before calling API: ", req)
    req = requests.get('http://10.140.28.202:5051/totalLeaves/155108').json() #make an api call
    emps = req['data'][0]['leaves_total'] #extract employee ids from json response
    dispatcher.utter_message(str(emps)) #send the message back to the user
    return []

class ActionAppliedLeaves(Action):
  def name(self):
    return "action_appliedLeaves"

  def run(self, dispatcher, tracker, domain):
    #print("before calling API: ", req)
    req = requests.get('http://10.140.28.202:5051/appliedLeaves/155108').json() #make an api call
    emps = req['data'][0]['leaves_applied'] #extract employee ids from json response
    dispatcher.utter_message(str(emps)) #send the message back to the user
    return []

class ActionBalanceLeaves(Action):
  def name(self):
    return "action_balanceLeaves"

  def run(self, dispatcher, tracker, domain):
    #print("before calling API: ", req)
    req = requests.get('http://10.140.28.202:5051/balanceLeaves/155108').json() #make an api call
    emps = req['data'][0]['leaves_balance'] #extract employee ids from json response
    dispatcher.utter_message(str(emps)) #send the message back to the user
    return []

