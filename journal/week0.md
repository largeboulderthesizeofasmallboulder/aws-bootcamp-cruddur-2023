# Week 0 — Billing and Architecture
## Architectural Diagram
https://lucid.app/lucidchart/0ea19967-d39d-4a0c-8e45-0afa5bce9f66/edit?viewport_loc=-732%2C-120%2C3126%2C1602%2C0_0&invitationId=inv_8341da2b-175f-4b5a-99fb-c9ef79d08854

![](/journal/images/Diagram.png)

## AWS EventBridge for Health Events
Created EventBridge rule for EC2 Health events to be delevired to email through sns topic
 by [this guidance](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
 ![](/journal/images/EventBridgeRule.png)