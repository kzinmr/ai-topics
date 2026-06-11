---
title: "Please, use a link!"
url: "https://idiallo.com/blog/use-a-link-please"
fetched_at: 2026-06-11T07:00:58.150596+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# Please, use a link!

Source: https://idiallo.com/blog/use-a-link-please

This is a rant. It didn't start today, but I think I've reached the end of the line. The straw that broke the camel's back, so to say. I used an internal tool for the first time. I logged in and navigated through the web app, making some updates here and there. All was well. But then I made the mistake of wanting to go back to the initial dashboard. I clicked the back button, and instead of returning to the previous page, I saw Chrome's default tab page staring right back at me.
How is it possible? I had navigated through at least a dozen pages, yet one back button click and the web app was completely gone. If you've ever experienced something similar, it's probably because you were using a single-page app. Nothing wrong with single-page apps, of course, but over the years I've concluded that people who only know how to build single-page apps don't know what a link is.
So let's start with examples of what a link isn't.
<div onclick="navigate('home')">Home</div>
Not a link. It's a div with an
onclick
event handler. You can style it all you want, but it's not a link.
<button onclick="navigate('home')">Home</button>
This may be a button, but it is not a link. With the advent of React, this has become so common. Because it's called a button, learners naturally gravitate toward it to link different pages. But there is worse.
<a onclick="navigate('home')">Home</a>
This almost feels intentional. As if the developer is teasing me. Why would you use an anchor tag but then omit its most important attribute? Here is what a link is supposed to look like:
<a href="/home">Home</a>
That's it. Simple. You don't have to add any configuration for the browser to support it. You don't even have to style it. All user agents have sensible default styling for the different states of a link: unvisited, visited, and active. It works well with browser history. On desktop, when you hover over it, you get a preview of the destination URL in the bottom-left corner of your screen. On mobile, you can press and hold to get several options on how to open it. You don't even have to worry about accessibility. It just works.
But when a developer is deep in their React app thinking about functionality, they might say, "When you click this button, go to the home page." They will naturally think of
onClick
as an event. And since it's a single-page app, they're thinking about state, not a page. They might write something like this:
import { navigate } from 'somewhere'; 
function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Home Page</h1>

      <button onClick={() => navigate('/about')}>
        Go to About Page
      </button>
      <div 
        onClick={() => navigate('/about')} 
        style={{ cursor: 'pointer', marginTop: '10px', color: 'blue' }}
      >
        Click this text to navigate
      </div>
    </div>
  );
}
export default Home;
This is already bad enough. But depending on how the
navigate
function is implemented, it can make or break the entire browser history. In the internal tool I was using,
navigate
was essentially replacing the current URL with the new one using
location.replace()
.
You can avoid all of these issues by just using an anchor tag. If you need it to play nicely with your React app, React Router has a
Link
component.
import { Link } from 'react-router-dom';
function Navbar() {
  return (
    <nav>
      <Link to="/home">Home</Link>
    </nav>
  );
}
Please, just use a native link and you won't have to worry about anything else.
