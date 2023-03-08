# Week 2 — Distributed Tracing

## Assignment: Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span

Added a new span to user_activities endpoint: 

![](/journal/images/customSpan1.png)



Added custom attributes to the span: userName and userNumberMessages

![](/journal/images/customSpan2.png)



Added mock data to provide data for different users with different number of messages:

![](/journal/images/userMockData.png)


Span and attributes are visible n the dataset:

![](/journal/images/trace.png) ![](/journal/images/traceAttributes.png)


## Assignment: Run custom queries in Honeycomb and save them later
Created custom query to check average number of messages for each user, could be used later to compare users  number of messages changes over time. Saved the query to a new UserBoard
![](/journal/images/customQuery.png)
