from behave import *
from main import *
import utils
import pdb


@given(u'the scenario precedente')
def step_impl(context):
    prova = 1
    print(f'grazie di cuore la prova vale {prova}')

@when(u'copy')
def step_impl(context):
    prova = 2
    print(f'grazie di cuore la prova vale {prova}')


@then(u'check')
def step_impl(context):
    prova = 3
    print(f'grazie di cuore la prova vale {prova}')

@given(u'set the stringa {default}')
def step_impl(context, default):
    context.default = default


@when(u'copy stringa')
def step_impl(context):
   print(context.default)

@then(u'check the stringa {created}')
def step_impl(context, created):
#    print(created)
    context.x = x
#    print(f"la x sarà quello che voglio {x}")
    assert context.default == "default"
    

@then(u'initial json checkPosition')
def step_impl(context):
 #   print(context.config.userdata.get("global_configuration"))
    
    payload = context.text or ""
 #   payload = utils.replace_global_variables(payload, context)

    print(payload)
    

@given(u'the {name} scenario executed successfully')
def step_impl(context, name):
  #  pdb.set_trace()
    phase = ([phase for phase in context.feature.scenarios if name in phase.name] or [None])[0]
    text_step = ''.join([step.keyword + " " + step.name + "\n\"\"\"\n" + (step.text or '') + "\n\"\"\"\n" for step in phase.steps])
    context.execute_steps(text_step)
    print("123")


