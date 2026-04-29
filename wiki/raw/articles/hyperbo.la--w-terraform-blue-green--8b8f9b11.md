---
title: "Blue-Green Deployments With Autoscaling Groups and Terraform"
url: "https://hyperbo.la/w/terraform-blue-green/"
fetched_at: 2026-04-29T07:02:15.861205+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Blue-Green Deployments With Autoscaling Groups and Terraform

Source: https://hyperbo.la/w/terraform-blue-green/

Blue-green deployments make deploys less risky by running old and new code
simultaneously on identical stacks. If there is a problem with the deploy, you
can quickly fail back to the previous version.
One way you can perform a blue-green deployment with an AWS autoscaling group
(ASG) involves mutating the ASG configuration and state.
Create a new launch configuration that points to your new pre-baked AMI.
Change the launch configuration for your ASG
.
Gradually cycle your ASG by terminating instances running the old AMI.
If all goes well, your new code is fully rolled out.
To rollback a bad deploy:
Change the launch configuration on the ASG back to the old AMI.
Terminate instances running the new AMI.
This achieves a gradual rollout, but it requires manually terminating hosts. We
can do better with terraform.
Rather than creating blue and green launch configurations, we can create blue
and green ASGs and roll between them. To achieve this with terraform, we
configure our launch configuration and ASG with
create_before_destroy = true
and
make the name of the ASG depend on the launch configuration’s generated
name. Your terraform config should look something like this:
resource
"aws_launch_configuration"
"backend"
{
name_prefix
=
"app-backend-"
image_id
=
"
${
data
.
aws_ami
.
backend
.
id
}
"
instance_type
=
"c5.xlarge"
security_groups
=
[
"
${
aws_security_group
.
backend
.
id
}
"
]
iam_instance_profile
=
"
${
var
.
iam_instance_profile
}
"
lifecycle
{
create_before_destroy
=
true
}
}
resource
"aws_autoscaling_group"
"backend"
{
name
=
"
${
aws_launch_configuration
.
backend
.
name
}
"
launch_configuration
=
"
${
aws_launch_configuration
.
backend
.
name
}
"
desired_capacity
=
"
${
var
.
size
}
"
min_size
=
"
${
var
.
size
}
"
max_size
=
"
${
2
*
var
.
size
+
1
}
"
wait_for_elb_capacity
=
"
${
var
.
size
}
"
availability_zones
=
[
"
${
data
.
aws_subnet
.
private
.*.
availability_zone
}
"
]
vpc_zone_identifier
=
[
"
${
data
.
aws_subnet
.
private
.*.
id
}
"
]
target_group_arns
=
[
"
${
aws_alb_target_group
.
backend
.
arn
}
"
]
lifecycle
{
create_before_destroy
=
true
}
}
Writing the config like this forces terraform to create a new ASG every time the
we update the launch configuration. A new ASG forces new instances to spin up,
which quickly rolls the infra to the latest AMI.
If we pin the
backend
AMI to a specific tag, a
terraform apply
will roll our
infrastructure to a new AMI. If the deploy is bad, we can revert by reverting
the AMI version bump in code and running
terraform apply
again.
We are slightly cheating here because we don’t maintain two copies of the app
and it is more costly to rollback. For my blog, ease-of-use wins over
availability concerns. Your trade-off space may be different.
