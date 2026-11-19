---
title: "A guide to the API integration process"
url: "https://www.merge.dev/blog/api-integration-process"
fetched_at: 2026-11-19T10:03:57.719105+00:00
source: "Merge Blog"
tags: [blog, raw]
---

# A guide to the API integration process

Source: https://www.merge.dev/blog/api-integration-process

Application programming interfaces (APIs) act as the foundation of communication between applications. They establish the channels and formats in which applications can exchange information.
In this article, you'll learn all about the process of
integrating APIs
and how to perform it without third-party tools.
What is API integration?
API integration is the systematic process of connecting different software applications using their APIs, allowing them to exchange data and functionalities. This isn't merely about establishing a connection; it's about ensuring that data is transferred in a secure, efficient, and accurate way. The goal is to create a seamless flow of data between systems that enhance their functionality and the user experience.
An API integration process typically involves the following components:
The
client application
is the application that initiates the API request. For instance, if you're building a mobile application that needs to process payments, the mobile application is considered the client application.
The
server application
is the application that receives the API request and processes it. In the previous mobile application example, the server application would be the payment gateway.
API middleware
acts as a translator, ensuring that data is correctly formatted and understood by both sides. Positioned within the client application, it enables communication with a third-party application. Once the server application handles the request, the middleware guarantees that the resulting response is conveyed back to your application in a format the client application understands.
Note: It's generally advised to have a dedicated API middleware component in client applications as it helps maintain the
separation of concerns
. However, for simpler applications, the API middleware operations of request and response translations, as well as communication with the server application, can be performed inline. This means that sometimes you may see the middleware code inlined with the business logic of the application rather than as a separate component.
Related:
How API access controls work
How to integrate APIs without using a third-party tool
Now that you know what an API integration process looks like, it's time to learn how to integrate with common remote API formats. To keep the demonstrations succinct, you'll find that the API middleware is inlined in the application rather than placed in a separate module. However, when dealing with complex applications, it's important to create a separate module for API middleware code.
Integrate a remote API
Remote APIs, also referred to as remote services, are primarily web-based interfaces offered by server-side applications. Classic examples of remote services are the
Firebase Realtime Database
and
Stripe Payment Gateway
. The services expose specific endpoints, which are essentially URLs, and request and response data objects (aka data contracts) that developers can interact with to retrieve or send data. The endpoints and data contracts form the remote APIs are made available for integration by the remote services.
Here are the steps you would take to integrate a remote API into your development process:
1. Start by thoroughly reading the API documentation to identify the endpoints you need to integrate. The documentation provides critical information about each endpoint's functionality, the expected request format, and possible responses. Documentation is the blueprint for understanding how to communicate effectively with the API.
2. Most APIs require authentication to guarantee security, which means you need to obtain the necessary credentials for the remote API. This typically entails creating an account with the API provider and generating API keys or OAuth tokens. These credentials ensure that only authorized entities can access the API.
3. Next, in your code, you need to write network calls that correspond to the type of remote API you're using.
In the following sections, you'll look at a few examples of network calls for different types of remote APIs using .NET. Before you do, use your preferred IDE and terminal to generate a client application using the following command:
```bash
mkdir ApiClient && cd ApiClient
dotnet new console --framework net7.0
```
Related:
How to build API integrations (5 steps)
REST APIs
REST APIs are a popular type of remote API that uses HTTP requests to retrieve or send data. For instance, the following GET request returns a list of users from an API:
GET https://api.example.com/users
In your client application, you can use the HttpClient class to make HTTP requests to the API. The following code snippet demonstrates how to make a GET request to the popular comic
XKCD's REST API endpoint
to retrieve the latest comic:
using System.Net.Http;
var httpClient = new HttpClient();
var restApiresponse = await httpClient.GetStringAsync("https://xkcd.com/info.0.json");
Console.WriteLine($"{restApiresponse}\n");
The following screenshot shows the response object formatted as a string returned by the API:
Related:
A guide to API integration management
GraphQL APIs
GraphQL is a query language for APIs that provides a more flexible alternative to REST. GraphQL APIs expose a single POST endpoint that accepts queries and returns data in JSON format.
For instance, the following query returns the ID and name of all users: {  users {    id    name  }}
The .NET GraphQL client library,
GraphQL
, provides a convenient way to make GraphQL requests. The library abstracts the request and response transformation and manages the communication per GraphQL standards, freeing developers from the hassle of writing boilerplate GraphQL API integration code. Add the library
NuGet
package to your project using the following command:
dotnet add package GraphQL
dotnet add package GraphQL.Client
dotnet add package GraphQL.Client.Serializer.SystemTextJson
The following snippet shows you how to make a GraphQL request to the
Star Wars API
to retrieve a list of all the films and their creation dates:
using GraphQL;
using GraphQL.Client.Http;
using GraphQL.Client.Serializer.SystemTextJson;

using var graphQlClient = new GraphQLHttpClient(new GraphQLHttpClientOptions
{
  EndPoint = new Uri("https://swapi-graphql.netlify.app/.netlify/functions/index")
}, new SystemTextJsonSerializer());

var request = new GraphQLRequest
{
  Query = @"query MovieQuery {
  allFilms {
    films {
      title
      created
    }
  }
}"
};

var response = await graphQlClient.SendQueryAsync
(request);
Console.WriteLine(response.Data.ToString());
This screenshot shows the string representation of the response object returned by the API:
Related:
What is multiple API integration? Here's what you need to know
SOAP APIs
Simple Object Access Protocol (SOAP) APIs are a type of remote API that uses SOAP to exchange data. SOAP APIs expose a single endpoint that accepts XML requests and returns XML responses.
The .NET SOAP client library
System.ServiceModel.Http
provides a convenient way to make SOAP requests. Working with SOAP requires a fair bit of XML parsing, but the library simplifies this process by offering types that facilitate the exchange of SOAP messages using HTTP. Add the library package to your project using the following command: <code class="blog_inline-code">dotnet add package System.ServiceModel.Http</code>
Now that you've added the System.ServiceModel.Http library, walk through the steps to make a SOAP request to the
DataFlex Web Service
to retrieve the currency of a country based on its
International Organization for Standardization (ISO) code
.
Before making the request, you need to add a service reference to the API endpoint using the dotnet-svcutil tool. This tool retrieves metadata from a web service on a network location or from a WSDL file and generates a WCF class containing client proxy methods that access the web service operations. To learn more about the tool, you can check out the
Microsoft Learn guide
.
To install the dotnet-svcutil tool, navigate to your project directory in the shell and execute the following commands:
dotnet tool install --global dotnet-svcutil
dotnet-svcutil http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso
This tool generates a ServiceReference1 folder containing the Reference.cs file. Add the Reference.cs file to your project by adding the following text to the .csproj file in the <Project> element like this:
<ItemGroup>
<Content Include="ServiceReference\Reference.cs" />
</ItemGroup>
Run the following code snippet to make a SOAP request to the API to retrieve the currency of Australia:
using ServiceReference;
var client = new CountryInfoServiceSoapTypeClient(CountryInfoServiceSoapTypeClient.EndpointConfiguration.CountryInfoServiceSoap);

var response = await client.CountryCurrencyAsync("AU");

Console.WriteLine(response.Body.CountryCurrencyResult.sName);
The following screenshot shows the response returned by the API:
gRPC APIs
gRPC is a high-performance, open source framework for building remote procedure call (RPC) APIs. It was developed by Google and is now part of the
Cloud Native Computing Foundation (CNCF)
.
gRPC uses
Protocol Buffers
as its default serialization format, which is a language-agnostic binary format that is more compact and faster to serialize and deserialize than JSON or XML. gRPC also supports streaming and bidirectional communication, making it well-suited for real-time applications.
One of the main benefits of using gRPC is its performance. Because it uses binary serialization and supports streaming, gRPC can be significantly faster and more efficient than traditional REST APIs. Additionally, gRPC's support for bidirectional communication makes it well-suited for real-time applications, such as chat applications or online games.
To integrate with a gRPC API, you need to install the following NuGet packages to your project:
```bash
dotnet add package Grpc.Net.Client
dotnet add package Google.Protobuf
dotnet add package Grpc.Tools
```
Once you've successfully installed the NuGet packages, it's time to learn how to make a gRPC request to the gRPC bin service's Hello API to retrieve a greeting message. To do so, download the
Hello API's proto file
and add it to your project.
Then add an item group in the project file .csproj with a <Protobuf> element in the <Project> element that refers to the hello.proto file:
```xml
<ItemGroup>
  <Protobuf Include="hello.proto" GrpcServices="Client" />
</ItemGroup>
```
Build the project to enable the gRPC tool to generate the client classes. Use the following code to make a gRPC request to the API to retrieve a greeting message:
```csharp
using Grpc.Net.Client;
using Hello;

using var channel = GrpcChannel.ForAddress("http://grpcb.in:9000");
var client = new HelloService.HelloServiceClient(channel);
var reply = await client.SayHelloAsync(new HelloRequest { Greeting = "visitor" });
Console.WriteLine("Greeting: " + reply.Reply);
```
This screenshot shows the response returned by the API:
And now you've completed the process of incorporating a .NET client application with various remote APIs. However, there are certain factors you need to take into account if you're integrating with remote APIs without using a software development kit (SDK), which you'll learn more about next.
Related:
Examples of building API integrations
Pros and cons of integrating with a remote API directly
There are several benefits to integrating directly with a remote API:
Direct integration can ensure that the behavior of your application is consistent across all platforms, providing users with a uniform experience. This means that whether you are building an Android or an iOS application, you can be confident that the API will respond in the same way.
Direct integration helps developers avoid adding extra in-app dependencies, which preserves the application's binary size and potentially improves performance. Maintaining a lean codebase also makes it easier to debug and maintain the application.
However, there are certain drawbacks to integrating directly with a remote API as well:
Direct integration setup can be complicated and time-consuming. Developers need to have a thorough understanding of the API's architecture and documentation to ensure that the integration is secure and reliable. This may result in a longer implementation time and higher development costs.
Developers may experience a slowdown in the development process due to the lack of integrated IDE support for documentation. This may cause them to frequently refer to external API docs. Additionally, the available guidance may not always be consistent across APIs and may not be up-to-date, leading to confusion.
Manual work on data objects can lead to errors and requires careful attention to maintain data integrity. This is particularly challenging when dealing with APIs that return complex data objects that need to be parsed and validated.
Integrating an API using an SDK
Now that you've not only walked through the process of direct integration with APIs but also considered their pros and cons, take a look at another type of
API integration using SDKs
.
What Does an SDK Look Like?
SDKs are comprehensive packages containing tools, libraries, and documentation to facilitate specific software integrations. SDKs, like the
Firebase SDK
or
Stripe SDK
, abstract the complexities of direct API calls, providing a more straightforward integration pathway. They typically provide a set of classes, modules, and functions that developers can use to interact with the API in a more intuitive manner. SDKs are language-specific, providing support for popular languages such as C#, Java, Python, and JavaScript.
This diagram illustrates the communication flow between a client application and a remote API using an SDK. The SDK acts as a middleware, abstracting the complexities of the API and managing the communication protocol and data format conversions between the client application and the API.
Related:
How to use SDKs (3 tips)
Integrate an SDK Into Your Application
The following is a brief overview of the steps you need to follow to integrate an SDK into your application:
1. Read the SDK docs and identify the classes/modules/functions to integrate.
Before diving into integration, it's essential to understand the SDK's architecture. This involves studying its classes, modules, and functions, which are typically well-documented. This helps you identify the specific classes/modules/functions you need to integrate. For instance, if you're integrating the Firebase SDK, you might need to use the FirebaseApp class to initialize the SDK and the FirebaseDatabase class to interact with the Realtime Database.
2. Acquire any necessary credentials.
Similar to direct API integration, SDKs often require specific credentials for authentication. This might involve generating unique keys or tokens specific to the SDK.
‍
3. Initialize the SDK
and use the relevant programming constructs to integrate with the remote API.
To demonstrate the process of integrating an SDK, integrate the
Stripe SDK
into your .NET client application.
Add the necessary NuGet packages to your client application using the following command: <code class="blog_inline-code">dotnet add package Stripe.net</code>
Then use the Stripe SDK to create a customer with the email customer@example.com:
using Stripe;

StripeConfiguration.ApiKey = "
";
var options = new CustomerCreateOptions
{
  Email = "customer@example.com"
};

var service = new CustomerService();
Customer customer = service.Create(options);
Console.WriteLine(customer.Email);
This screenshot shows you the customer email that was returned by the API:
The SDK operation is equivalent to the following direct API call:
curl https://api.stripe.com/v1/customers \
  -u
\
  --data-urlencode email="customer@example.com"
As you can see, the SDK provides a more intuitive way to interact with the API, abstracting the complexities of the API call, such as authentication and data formatting. Additionally, the SDK provided a typed response object, which is easier to work with than the raw JSON response.
Pros and cons of integrating with the SDK
There are some key considerations to keep in mind while integrating with an SDK. For instance, the following are some of the benefits of integrating with an SDK:
SDKs often simplify the integration process, abstracting many of the complexities associated with direct API calls.
Integrated documentation in some IDEs can significantly speed up the development process, providing instant access to essential references. This can help developers avoid frequent context switching, improving productivity.
SDKs typically handle request and response objects gracefully, reducing the need for manual data handling and potential errors. This can help developers avoid common pitfalls, such as data type mismatches and null pointer exceptions.
There are also a few drawbacks you should consider:
While SDKs simplify integration, they might not always expose the full functionality of the underlying API, potentially limiting some advanced features. Generally, SDKs are updated less frequently than the underlying API, which means that they may not always support the latest API features.
Incorporating SDKs can increase the application's binary size due to the added dependencies, which may impact performance, especially on resource-constrained devices. Additionally, SDKs might not always be available for all platforms, which can limit the application's cross-platform compatibility.
Final thoughts
Integrating APIs is an essential aspect of modern software development. It guarantees that applications can work together seamlessly within a broader ecosystem.
That said, the process of implementing API integrations is, clearly, complex and extensive. This is especially true in the context of
product integrations
; your clients and prospects will need and want you to build and maintain an ever-growing number of integrations between their applications and your product.
You can help your developers avoid following many of the steps outlined in this article and still implement the integrations your prospects and clients need with Merge, the leading
unified API solution
. Simply build to Merge’s Unified API to start offering dozens, or even hundreds, of product integrations across key software categories, from CRM to HRIS to ATS to file storage.
Learn more about Merge by
scheduling a demo with one of our integration experts
.
API integration FAQ
In case you have any more questions on API integrations, we’ve addressed several common questions below.
What’s the difference between API integration and API management?
They’re fundamentally different concepts.
API integrations refer to the process of connecting disparate applications to exchange data and functionality; while API management involves handling any aspect in an API's lifecycle, whether that's creating, deploying, governing, and/or monitoring endpoints.
You’ll likely need to both integrate and manage APIs, but the tooling and teams involved in each area will probably differ. For example, to integrate with customers’ 3rd-party systems, your product team can use a unified API solution like Merge; but to manage your APIs, your engineers will need a solution like Kong.
What are the typical costs involved in building and maintaining API integrations?
It largely depends on the API endpoints you’re building to and the use case you’re trying to support.
That said, we typically see a single integration build consume 150 engineering hours and 300 hours per year to maintain. Many API providers also charge an annual partnership fee to access their endpoints, which is often $10,000 per year (if not more).
Assuming your engineers earn an annual salary of $150,000 (or $72.10 per hour), this can amount to $32,400 in engineering costs for building and maintaining a single integration in a given year. With the partnership costs, this figure can balloon to $42,400.
If you’re building product integrations, the costs are even higher. Your customer success teams will also need to support customers who adopt the integrations, which can consume hundreds of hours of their time every year.
Learn more about the costs associated with API integrations in
this guide
.
When should I build integrations in-house versus using an integration platform (and vice versa)?
The “build vs buy” dilemma can be influenced by several factors.
If your integrations need to be extremely customized to your business or product and you know that you only need to support a handful of integrations over time, it can make sense to keep the integrations in house.
However, if your integrations aren’t extremely customized to your business or product and you know there’s a long tail of integrations that you need to support, it makes sense to outsource them.
In many cases, you should adopt a hybrid approach: You can build and maintain your core, heavily-customized integrations in-house and use a
3rd-party integration platform
to handle the rest of them.
To help you navigate this decision for product integrations, here’s how Eran Dover, the VP of Product at Snappy (a corporate gifting platform), thinks you should approach the decision:
VIDEO
How do API integrations help automate workflows and reduce manual work?
Since API integrations allow applications to retrieve or create/update data, they can automate processes that involve copying and pasting data between applications.
For example, if a candidate is marked as hired in your ATS, an integration can trigger a POST /candidates request to your HRIS. This can lead to the new hire’s profile getting created and populated automatically.
As this example shows, API integrations can save your team a meaningful amount of time and prevent human errors, especially as these processes scale.
How can I ensure my API integrations remain secure and compliant?
Securing API integrations requires implementing OAuth 2.0 or similar authentication protocols, encrypting data in transit using TLS/SSL, storing credentials securely (never hardcoded), and maintaining audit logs for compliance.
Implementing these security measures (let alone maintaining them) can be incredibly time and resource consuming, which is another reason why 3rd-party integration platforms are an attractive option.
Solutions like Merge, for example, comply with HIPAA, are ISO 27001 certified, regularly pass SOC 2 Type II audits, and offer advanced security features (e.g., audit trails) to keep sensitive information secure.
