# 27/08/24 - pinging_the_cloud (#18)
This is a Amazon Lambda function that keeps track of how many times [this api](https://7zv6l6as52.execute-api.ap-southeast-2.amazonaws.com/default/hourly_ping)
has been invoked. There is also an additional invokation once per hour using Amazon EventBridge. The number of times is stored using amazon's DynamoDB.

This is my first time using a cloud service (AWS). There are so many AWS services and I am very overwhelmed! I've spent 10+ hours these past two days researching about AWS services and just cloud stuff in general. Even just setting up basic instances of these services takes a lot of effort. Now that I have used some of these services (I also played around with CLoudWatch, ECS, S3), I have a better idea of what I can make in a reasonable amount of time with future AWS miniprojects.

I think cloud computing and backend architecture in general can be quite an interesting endeavour but I am not yet at the knowledge level to where I am super excited to code or learn about this topic in depth. Initially I also disliked frontend development. It only began to become fun for me when I had mostly worked out the basics and I was mainly thinking about the higher level concepts (like visualising the component tree) while coding instead spending most of the time debugging trivial errors. Maybe backend will be the same for me.
