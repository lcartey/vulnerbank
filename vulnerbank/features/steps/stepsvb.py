from behave import *
import requests


@given(u'an attacker')
def step_impl(context):
    headers = {"Content-Type" : "application/x-www-form-urlencoded" }
    r = requests.post('http://vulnerbank2-postgresjavi.7e14.starter-us-west-2.openshiftapps.com/login',
                      data='form-username=javi&form-password=12345', headers=headers)

@when(u'I try to access to an unauthorised account')
def step_impl(context):
    r = requests.get('http://vulnerbank2-postgresjavi.7e14.starter-us-west-2.openshiftapps.com/accounts&user=user1')
    context.body = r.content

@then(u'I should have no access to that account')
def step_impl(context):
    assert ('98381867' not in str(context.body)), "An attacker can access an unauthorised account"
