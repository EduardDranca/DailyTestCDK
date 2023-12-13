import constructs
from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    Duration,
    aws_events_targets,
    aws_events as events,
    aws_iam as iam,
    aws_s3,

)
from constructs import Construct


class DailymailStackTest(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        scheduled_lambda = lambda_.Function(self, "MyDailyMailTest",
                                            handler='lambda_function.lambda_handler',
                                            runtime=lambda_.Runtime.PYTHON_3_8,
                                            code=lambda_.Code.from_asset('lambda'),
                                            )

        scheduled_lambda.add_to_role_policy(iam.PolicyStatement(effect=iam.Effect.ALLOW,
                                                                resources=[
                                                                    "arn:aws:ses:region-id:identity/example@domain.com"],
                                                                actions=["ses:SendEmail", "ses:SendRawEmail",
                                                                         "ses:SendTemplatedEmail"]
                                                                ))

        principal = iam.ServicePrincipal("events.amazonaws.com")
        scheduled_lambda.grant_invoke(principal)

        rule = events.Rule(self, "Rule", schedule=events.Schedule.rate(Duration.hours(24)))

        rule.add_target(aws_events_targets.LambdaFunction(scheduled_lambda, event=events.RuleTargetInput.from_object(
            {"content": "Your daily CDK", "address": "example@domain.com"}), retry_attempts=1))

        bucket = aws_s3.Bucket(self, "TestBucket", bucket_name="testbucketcdk12412162234155")



