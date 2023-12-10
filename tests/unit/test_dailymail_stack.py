import aws_cdk as core
import aws_cdk.assertions as assertions

from dailymail.dailymail_stack import DailymailStack

# example tests. To run these tests, uncomment this file along with the example
# resource in dailymail/dailymail_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DailymailStack(app, "dailymail")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
